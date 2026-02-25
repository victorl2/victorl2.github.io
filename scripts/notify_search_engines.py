#!/usr/bin/env python3
"""Notify search engines about new or updated pages after deployment."""

import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error

SITE_URL = "https://victorfts.com"
FEED_URL = f"{SITE_URL}/feed.xml"
CONTENT_PATHS = ("docs/_posts/", "docs/_pages/")
GOOGLE_INDEXING_ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
WEBSUB_HUB = "https://pubsubhubbub.appspot.com/"


def get_changed_files():
    """Get content files changed in the latest push using git diff."""
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", "HEAD~1", "HEAD"],
        capture_output=True, text=True, check=True,
    )
    return [
        f for f in result.stdout.strip().splitlines()
        if any(f.startswith(p) for p in CONTENT_PATHS) and f.endswith(".md")
    ]


def extract_permalink(filepath):
    """Extract permalink from the front matter of a markdown file."""
    with open(filepath) as f:
        content = f.read()
    match = re.search(r"^permalink:\s*(.+)$", content, re.MULTILINE)
    if match:
        return match.group(1).strip().strip('"').strip("'")
    return None


def file_to_url(filepath):
    """Convert a content file path to its public URL."""
    permalink = extract_permalink(filepath)
    if permalink:
        return f"{SITE_URL}{permalink}"
    return None


def get_google_access_token(service_account_json):
    """Get an OAuth2 access token using a Google service account (no external deps)."""
    import base64
    import hashlib
    import hmac
    import time

    sa = json.loads(service_account_json)
    now = int(time.time())

    # JWT header and claims
    header = base64.urlsafe_b64encode(json.dumps(
        {"alg": "RS256", "typ": "JWT"}
    ).encode()).rstrip(b"=")

    claims = base64.urlsafe_b64encode(json.dumps({
        "iss": sa["client_email"],
        "scope": "https://www.googleapis.com/auth/indexing",
        "aud": "https://oauth2.googleapis.com/token",
        "iat": now,
        "exp": now + 3600,
    }).encode()).rstrip(b"=")

    signing_input = header + b"." + claims

    # Sign with RSA-SHA256 using the service account private key
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding

        private_key = serialization.load_pem_private_key(
            sa["private_key"].encode(), password=None
        )
        signature = private_key.sign(signing_input, padding.PKCS1v15(), hashes.SHA256())
    except ImportError:
        print("  [!] cryptography package not available, trying PyJWT...")
        try:
            import jwt as pyjwt
            token = pyjwt.encode(
                {
                    "iss": sa["client_email"],
                    "scope": "https://www.googleapis.com/auth/indexing",
                    "aud": "https://oauth2.googleapis.com/token",
                    "iat": now,
                    "exp": now + 3600,
                },
                sa["private_key"],
                algorithm="RS256",
            )
            # Skip signature step, use JWT directly
            jwt_token = token if isinstance(token, str) else token.decode()
            data = urllib.parse.urlencode({
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                "assertion": jwt_token,
            }).encode()
            req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read())["access_token"]
        except ImportError:
            print("  [!] Neither cryptography nor PyJWT available. Skipping Google API.")
            return None

    sig_encoded = base64.urlsafe_b64encode(signature).rstrip(b"=")
    jwt_token = (signing_input + b"." + sig_encoded).decode()

    import urllib.parse
    data = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt_token,
    }).encode()

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["access_token"]


def notify_google(urls, service_account_json):
    """Submit URLs to Google Indexing API."""
    print("\n[Google Indexing API]")
    access_token = get_google_access_token(service_account_json)
    if not access_token:
        return

    for url in urls:
        body = json.dumps({"url": url, "type": "URL_UPDATED"}).encode()
        req = urllib.request.Request(
            GOOGLE_INDEXING_ENDPOINT,
            data=body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}",
            },
        )
        try:
            with urllib.request.urlopen(req) as resp:
                print(f"  OK  {url} ({resp.status})")
        except urllib.error.HTTPError as e:
            print(f"  ERR {url} ({e.code}: {e.read().decode()[:200]})")


def notify_indexnow(urls, api_key):
    """Submit URLs to IndexNow (Bing, Yandex, Seznam, Naver)."""
    print("\n[IndexNow]")
    body = json.dumps({
        "host": "victorfts.com",
        "key": api_key,
        "urlList": urls,
    }).encode()

    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=body,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"  OK  Submitted {len(urls)} URL(s) ({resp.status})")
    except urllib.error.HTTPError as e:
        print(f"  ERR ({e.code}: {e.read().decode()[:200]})")


def ping_websub():
    """Ping WebSub/PubSubHubbub hub about RSS feed update."""
    print("\n[WebSub]")
    import urllib.parse
    data = urllib.parse.urlencode({
        "hub.mode": "publish",
        "hub.url": FEED_URL,
    }).encode()

    req = urllib.request.Request(WEBSUB_HUB, data=data)
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"  OK  Pinged hub for {FEED_URL} ({resp.status})")
    except urllib.error.HTTPError as e:
        print(f"  ERR ({e.code}: {e.read().decode()[:200]})")


def main():
    changed_files = get_changed_files()
    if not changed_files:
        print("No content files changed. Nothing to do.")
        return

    print(f"Changed content files ({len(changed_files)}):")
    urls = []
    for f in changed_files:
        url = file_to_url(f)
        if url:
            urls.append(url)
            print(f"  {f} -> {url}")
        else:
            print(f"  {f} -> [skipped, no permalink]")

    if not urls:
        print("No URLs to submit.")
        return

    # Google Indexing API
    sa_key = os.environ.get("GOOGLE_SERVICE_ACCOUNT_KEY")
    if sa_key:
        notify_google(urls, sa_key)
    else:
        print("\n[Google Indexing API] Skipped (GOOGLE_SERVICE_ACCOUNT_KEY not set)")

    # IndexNow (Bing, Yandex)
    indexnow_key = os.environ.get("INDEXNOW_KEY")
    if indexnow_key:
        notify_indexnow(urls, indexnow_key)
    else:
        print("\n[IndexNow] Skipped (INDEXNOW_KEY not set)")

    # WebSub ping (always runs — no credentials needed)
    ping_websub()


if __name__ == "__main__":
    main()
