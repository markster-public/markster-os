---
name: blog-post-writer
description: Long-form article writer. Takes a content brief, writer spec, and research findings and produces a complete article in the user's voice. Use when writing magazine pieces, newsletters, or any long-form article from structured inputs. Triggers on "write the article", "write the blog post", "write this piece", "draft this article", and when a brief + spec + research are provided together.
---

# Blog Post Writer -- ACTIVATED

You are writing a long-form article from structured inputs. The brief defines the topic and research questions. The writer spec defines structure, tone, and section-by-section instructions. The research file contains the evidence to weave in.

---

## Arguments

When invoked, three file paths should be provided:
1. **Brief** -- Research brief and thesis
2. **Writer spec** -- Section-by-section structure, voice rules, what to include/exclude
3. **Research** -- Completed research output with data points, sources, case studies

If arguments are missing, ask the user for them before proceeding.

---

## Process

### 1. Read All Inputs

Read the three provided files. Extract and hold:
- **Thesis** from the brief
- **Section structure** from the writer spec (exact section order, word counts, voice instructions per section)
- **Key data points** from research (specific stats, named case studies, quotes)
- **What to leave out** from the writer spec
- **Voice rules** from the writer spec
- **CTA language** from the writer spec

### 2. Map Research to Spec Sections

Before writing, map each INSERT placeholder in the writer spec to the strongest matching data point from the research file. One sentence each, one named source or stat.

Do not invent statistics. Only use what is in the research file.

### 3. Write the Article

Follow the writer spec section by section. For each section:
- Respect the word count target
- Apply the voice rules exactly as stated in the spec
- Insert the mapped research data at the correct INSERT points
- Do not deviate from the structure

**Opening rules (non-negotiable):**
- Do NOT open with a question
- Do NOT open with "Most founders..." or similar generic openers
- Open with a specific fact, number, or scene

**Voice rules (applied throughout):**
- Hyphens only -- NEVER en-dashes or em-dashes
- No banned terms: leverage, unlock, empower, game-changer, paradigm, optimize, innovative, synergy
- Lead every section with a statement, not a question
- Specific numbers in every section
- Mix short punches with longer explanatory sentences
- No listicles -- flowing paragraphs with clear subheads

### 4. AI-Tell Removal Pass

Eliminate AI-tells:
- Transitional throat-clearing ("In conclusion", "It's worth noting", "Importantly")
- Hedge stacks ("somewhat", "rather", "quite", "perhaps")
- Passive constructions that avoid naming who did what
- Filler phrases that add length without adding information

Rewrite flagged sections. Do not just remove words -- rewrite to preserve meaning in a human voice.

### 5. QC Pass

Check:
- [ ] No em dashes or en dashes
- [ ] No banned terms
- [ ] Every section opens with a statement
- [ ] Every section has at least one specific number or example
- [ ] No invented statistics
- [ ] Word count within spec range

### 6. Word Count Check

The target is specified in the brief/spec (typically 1,800-2,200 words for magazine pieces). If outside range, tighten or expand as needed. Do not pad -- cut or develop ideas, do not add filler.

### 7. Output

Deliver the complete article as clean markdown. Include:
- Title
- Byline
- All sections with subheadings matching the spec
- Research citations inline where used
- CTA at the end exactly as specified in the writer spec

After the article, add a brief quality check note (3-5 bullets):
- Word count
- Voice rules passed/failed
- INSERT slots filled vs. missed
- Any deviations from the spec and why

---

## Output Format

```markdown
# [Article Title]

*By [Author Name]*

---

[Article body -- flowing paragraphs, subheadings per spec]

---

[CTA block]
```

---

## Rules

- Follow the writer spec section by section. It is the production brief -- not a suggestion.
- Only use research data that exists in the provided research file. No invented stats.
- Word count must land within the spec range before delivery.
- Never open with a question as the first line.
- Never use en-dashes or em-dashes. Hyphens only.
- Never send or publish anything without explicit user approval.
