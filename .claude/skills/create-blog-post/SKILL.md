---
name: create-blog-post
description: "Use when creating a new blog post, writing an article, or adding content to the blog. Guides the full process from topic through drafting, image sourcing, and review."
---

# Create Blog Post

Guide the creation of a new blog post for victorfts.com, from topic definition through writing, image sourcing, review, and publishing.

## Process

### 1. Gather Details

Ask the user one question at a time using multiple choice when possible:

- **Topic**: What is the post about?
- **Target audience**: Who is this for? (developers, general audience, etc.)
- **Writing style**: Informal (conversational, first person, casual), Semi-formal (clear and approachable but more structured), or Rigorous (precise, well-cited, academic-leaning)
- **Article size**: Short (500-800 words), Medium (800-1500 words), Long (1500-2500 words), or In-depth (2500+ words)
- **Key points**: What are the main things to cover?

### 2. Create the File

- **Filename**: `docs/_posts/YYYY-MM-DD-slug.md` using today's date
- **Slug**: lowercase, hyphen-separated, concise summary of the topic
- **Front matter**:
  ```yaml
  ---
  layout: post
  title: Post Title Here
  permalink: /slug/
  date: YYYY-MM-DD HH:MM:00 -0300
  categories: ["category1", "category2"]
  tags: ["tag1", "tag2"]
  ---
  ```

### 3. Write the Content

Follow these writing rules strictly:

- **Match the chosen writing style**:
  - *Informal*: Write like a real person talking, not a corporate blog or AI. Use first person, contractions, and casual language.
  - *Semi-formal*: Clear, approachable, and well-structured. First person is fine but keep the language more polished. Less slang, more precision.
  - *Rigorous*: Precise and well-cited. Use technical terminology correctly, reference sources explicitly, and maintain a structured argument. Can still use first person but the tone should be measured and deliberate.
- **No overuse of lists or bullet points**: Prefer flowing paragraphs. Use lists only when genuinely listing items (tools, steps in a sequence). Never use bullets just to organize prose.
- **No dashes as separators**: Avoid using " - " as a stylistic separator in prose.
- **Include reference links**: Link to official docs, tools, repos, and resources mentioned in the post. Use inline markdown links naturally within sentences.
- **Include contextual images**: Search for relevant free-to-use images online (Unsplash, official project logos, screenshots). Place images where they add context, not as decoration. Store in `docs/assets/imgs/` and reference as `![alt text](/assets/imgs/filename.ext)`.
- **Avoid AI writing patterns**: No "In this article, we will explore...", no "Let's dive in", no "In conclusion", no excessive transitional phrases. Just get to the point.
- **Paragraphs over structure**: Don't break everything into H2/H3 sections. Use headings only when there's a genuine topic shift. A post can have large sections of continuous prose.

### 4. Review with the User

Present the full draft to the user and ask for feedback. Iterate based on their input:

- Check tone (does it match the chosen writing style?)
- Check content (are the key points covered?)
- Check images and links (are they relevant and working?)
- Check length (does it match the target size?)

Only write the final file after the user approves the draft.

### 5. Final Revision Pass

Before writing the file, do a self-review cleanup of the approved draft:

- Remove any remaining AI writing patterns (filler phrases, generic transitions, "Let's", "In conclusion")
- Fix awkward phrasing, redundant sentences, and unnecessary repetition
- Verify all markdown links are correctly formatted and point to real URLs
- Ensure the tone is consistent throughout (no sudden shifts between casual and formal)
- Check that the post flows naturally when read top to bottom -- no jarring jumps between paragraphs
- Trim any section that feels like padding without adding value
- Confirm the word count is within the target range

### 6. Finalize

- Write the revised post to `docs/_posts/`
- Download any sourced images to `docs/assets/imgs/`
- Verify the post renders correctly with `cd docs/ && bundle exec jekyll serve`

## Common Mistakes

- Not matching the chosen writing style (e.g., being too casual when rigorous was requested, or too stiff when informal was chosen)
- Overusing bullet points and lists where paragraphs work better
- Adding filler intros ("In this post, I'll show you...") instead of jumping into the content
- Forgetting reference links to tools and resources mentioned
- Using stock headings like "Introduction", "Conclusion", "Summary"
