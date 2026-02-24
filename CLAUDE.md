# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal blog/portfolio for Victor Silva (victorfts.com), built with Jekyll and hosted on GitHub Pages.

## Development Commands

```bash
# Run local development server (http://localhost:4000)
make run
# Or equivalently:
cd docs/ && bundle exec jekyll serve

# Install dependencies (first-time setup)
cd docs/ && bundle install
```

## Architecture

All Jekyll source files live under `docs/` (the GitHub Pages root). The site uses the **Minima** theme (v2.5, dark skin) with minimal customization.

- `docs/_config.yml` — Jekyll configuration, theme settings, social links
- `docs/_layouts/` — Custom layouts: `base.html`, `home.html`, `post.html`, `page.html`
- `docs/_includes/footer.html` — Custom footer override
- `docs/_posts/` — Blog posts (format: `YYYY-MM-DD-slug.md`)
- `docs/_pages/` — Static pages (about, 404); included via `include: [_pages]` in config
- `docs/assets/main.scss` — Custom styles importing Minima theme
- `docs/assets/imgs/` — Images
- `docs/index.MD` — Custom homepage template listing posts

## Content Conventions

- Posts use front matter: `layout`, `title`, `permalink`, `date`, `categories`, `tags`
- Pages use `permalink` in front matter (e.g., `/about/`)
- Only GitHub Pages-compatible gems are used (no custom plugins)

## Deployment

Pushes to `main` automatically deploy via GitHub Pages. Custom domain: `victorfts.com` (configured via `docs/CNAME`).
