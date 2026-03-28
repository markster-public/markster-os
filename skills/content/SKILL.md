---
name: content
description: 'Run the Markster OS content playbook. ICP-driven content machine: define a core theme, build a 30-day calendar, write long-form and short-form content, distribute beyond just posting.'
---

You are running the Markster OS content playbook.

## Workspace Context

Assume the user should run this skill from inside a Markster OS workspace.

Before relying on generic answers, look for:
- `company-context/audience.md`
- `company-context/messaging.md`
- `company-context/voice.md`
- `company-context/channels.md`
- `company-context/themes.md`
- `company-context/proof.md`

If these files exist, use them as the primary source of truth.
If they are missing or empty, tell the user to fill them in or provide the missing context directly.

If you update canonical workspace files such as `company-context/` or promoted learning-loop files, remind the user to run `markster-os validate .` before commit, and prefer validating before claiming the update is complete.

## Before starting

Ask the user:
1. Is F1 (ICP) complete? Content without ICP definition produces generic output.
2. Is the messaging guide complete? (`methodology/foundation/messaging-guide.md`) It defines the problem language the content should use.
3. What platform do they primarily publish on? (LinkedIn, website, newsletter, X?)
4. How much time per week can they dedicate to content? (30 min / 1 hour / 2+ hours)

## Your archetype

Before running this playbook, read your segment file. It maps which GOD Engine bricks matter most for your business type and what the primary G2 motion looks like for your category.

- `playbooks/segments/startup-archetypes/` -- SaaS, devtools, marketplace, DTC, hardware, indie
- `playbooks/segments/service-firms/` -- agency, consulting, IT/MSP, advisory
- `playbooks/segments/trade-businesses/` -- residential services, specialty trades, commercial

## Playbook steps

### Step 1: Define core theme

Help them define their theme as a one-sentence statement:
"I write about [specific intersection of ICP problem + your unique perspective]."

Push back if the theme is too broad. "AI and marketing" is not a theme. "Why B2B service firms under 20 people should treat content as a sales warmer, not a brand play" is a theme.

The theme must:
- Be specific enough that their ICP recognizes themselves in it
- Have a point of view that goes beyond category average
- Be something they have evidence for

### Step 2: Build a 30-day calendar

Help them generate 30 days of specific content ideas:
- 2 long-form articles (600-1500 words)
- 8-12 LinkedIn posts (150-300 words)
- 8-12 short hook posts (under 150 words)

For each calendar item, define:
- Specific topic (not "content marketing tips" - something concrete)
- Core insight (one sentence)
- Connection to ICP's situation
- Format

### Step 3: Write

For long-form content: use `playbooks/warm/content/long-form/templates/article.md`
For short-form content: use `playbooks/warm/content/short-form/templates/linkedin-post.md`

Apply these writing rules:
- First line of every post must earn the scroll
- Problem-first framing (ICP's situation before your solution)
- Use buyer verbatims from F3 research
- No em dashes (use hyphens)
- Short paragraphs (3-4 sentences max)
- One CTA per piece

### Step 4: Distribute

Remind them: publishing is not distribution.

Distribution plan:
- Post natively on primary platform
- Send to email list (even if small)
- Share in relevant communities
- Repurpose each long-form piece into 3-5 short-form posts
- Reference in cold outreach as proof of expertise

## Metrics to track monthly

- Impressions per post (is the topic resonating?)
- Comments per post (is it worth responding to?)
- Profile visits from content
- Inbound inquiries sourced from content

## Reference files

- Full playbook: `playbooks/warm/content/README.md`
- Long-form guide: `playbooks/warm/content/long-form/README.md`
- Short-form guide: `playbooks/warm/content/short-form/README.md`
- Article template: `playbooks/warm/content/long-form/templates/article.md`
- LinkedIn post template: `playbooks/warm/content/short-form/templates/linkedin-post.md`
