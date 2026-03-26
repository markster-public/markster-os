# G2: Warm -- Content, Nurture & Branding

> **North Star Metric:** 1 post/day per platform (LinkedIn, Facebook, X) + 2 blog posts/month

---

## Processes

### G2.1 Weekly Content Calendar Generation

| Field | Value |
|-------|-------|
| **Trigger** | Friday afternoon (weekly cadence) |
| **Frequency** | Weekly |
| **Input** | Channel profiles, content pillars, brand strategy, trending topics, style corrections |
| **Output** | 7-day content calendar with topic seeds, platform assignments, tone notes |
| **Test** | Calendar covers LinkedIn (7x), Facebook (7x), X (7x), Blog (1x) |

**Steps:**
1. Generate content calendar with topic seeds
2. Reference channel profiles for platform-specific rules
3. Review and adjust calendar (quality gate)
4. Save calendar briefs for generation pipeline

---

### G2.2 Social Content Brief Creation

| Field | Value |
|-------|-------|
| **Trigger** | Calendar approved |
| **Frequency** | Weekly (after calendar approval) |
| **Input** | Approved calendar, voice guide, channel profiles, proof points |
| **Output** | Per-post briefs with topic, angle, tone, CTA, platform-specific rules |
| **Test** | Briefs for all calendar slots; each references voice guide and channel profile |

---

### G2.3 Social Content Generation

| Field | Value |
|-------|-------|
| **Trigger** | Brief ready |
| **Frequency** | Daily (1 post/day per platform) |
| **Input** | Content brief, voice guide, style corrections, channel profiles |
| **Output** | Publish-ready social assets per platform (LinkedIn, Facebook, X variants) |
| **Test** | Assets match voice guide; style corrections applied; platform formatting correct |

**Steps:**
1. Feed brief to content generation pipeline
2. Engine reads voice guide, channel profiles, style corrections
3. Generates assets across platforms
4. Review all assets (quality gate)

---

### G2.4 Blog Content Generation

| Field | Value |
|-------|-------|
| **Trigger** | SEO topic selected or blog brief created |
| **Frequency** | 2x/month |
| **Input** | Blog brief, SEO keywords, voice guide, brand strategy |
| **Output** | Publish-ready blog post (1,500-3,000 words) with SEO metadata |
| **Test** | Passes SEO checklist; matches voice guide; internal links included |

**Steps:**
1. Select topic from SEO research or content calendar
2. Create blog spec/brief
3. Generate blog post
4. Review and edit (quality gate)
5. Trigger publishing

---

### G2.5 Content QC & Approval

| Field | Value |
|-------|-------|
| **Trigger** | Content generated (social or blog) |
| **Frequency** | Per-asset |
| **Input** | Generated content, voice guide, style corrections, platform rules |
| **Output** | Approved content ready for publishing OR revision notes |
| **Test** | Review within 24 hours; rejection rate below 20% |

**Steps:**
1. Review each asset against voice guide
2. Check style corrections compliance
3. Approve or provide revision notes

**Target automation:**
- AI pre-check scores content against voice guide + style corrections
- Founder reviews flagged items only
- Rejection triggers re-generation with feedback

---

### G2.6 Social Publishing

| Field | Value |
|-------|-------|
| **Trigger** | Content approved |
| **Frequency** | Daily (1 post/day per platform) |
| **Input** | Approved content with platform formatting |
| **Output** | Published post on LinkedIn / Facebook / X |
| **Test** | Post live on correct platform within 2 hours of scheduled time |

**Target automation:**
- Approved content auto-formatted per platform
- Scheduled for optimal posting time
- Auto-publish for pre-approved content

---

### G2.7 Blog Publishing

| Field | Value |
|-------|-------|
| **Trigger** | Blog content approved |
| **Frequency** | 2x/month |
| **Input** | Approved blog post with SEO metadata |
| **Output** | Blog post live on all target platforms |
| **Test** | Published to all platforms within 1 hour; SEO metadata correct; internal links working |

**Steps:**
1. Blog post approved (trigger)
2. Auto-publish to CMS platforms (HubSpot, WordPress, Medium, Substack)
3. Post-publish SEO verification

---

### G2.8 Style Corrections Extraction

| Field | Value |
|-------|-------|
| **Trigger** | Content published and edited by founder |
| **Frequency** | Post-publish (every published piece) |
| **Input** | Generated content (pre-edit) vs published content (post-edit) |
| **Output** | New entries in style corrections file |
| **Test** | Edit patterns captured; confidence levels tracked (LOW -> MEDIUM -> HIGH) |

**Steps:**
1. Founder publishes content with edits
2. Engine compares generated vs published
3. Extracts edit patterns and adds to style-corrections file
4. Confidence: LOW (1 observation) -> MEDIUM (2-3, auto-apply) -> HIGH (5+, hard rule)
5. Next generation reads updated corrections

---

### G2.9 SEO Research & Gap Analysis

| Field | Value |
|-------|-------|
| **Trigger** | Monthly cadence |
| **Frequency** | Monthly |
| **Input** | Current keyword rankings, competitor content, ICP search intent |
| **Output** | SEO opportunity report: keywords to target, content gaps, competitor insights |
| **Test** | 5+ new target keywords identified per month; gap list prioritized |

---

### G2.10 Intelligence Feed Review

| Field | Value |
|-------|-------|
| **Trigger** | Monday (weekly cadence) |
| **Frequency** | Weekly |
| **Input** | Research library trending topics, industry news, ICP-relevant events |
| **Output** | Content opportunities: timely topics, reactive content ideas, thought leadership angles |
| **Test** | 3+ opportunities per week; at least 1 turned into published content |

---

### G2.11 Newsletter Distribution

| Field | Value |
|-------|-------|
| **Trigger** | Weekly (content ready for distribution) |
| **Frequency** | Weekly |
| **Input** | Week's best content (social + blog), subscriber list |
| **Output** | Newsletter sent with curated content + personal commentary |
| **Test** | Sent on schedule; 25%+ open rate |

**Target automation:**
- Auto-curate week's top content from published assets
- Newsletter template auto-populated
- Founder adds personal commentary (voice authenticity -- always manual)
- Scheduled send

---

### G2.12 Content Performance Review

| Field | Value |
|-------|-------|
| **Trigger** | Monday (weekly cadence) |
| **Frequency** | Weekly |
| **Input** | Engagement metrics (likes, comments, shares), website analytics, lead attribution |
| **Output** | Performance report: top content, underperformers, attribution to pipeline |
| **Test** | Report every Monday; 1+ strategy adjustment per month |

---

## Agent Architecture

| Agent | Status | Covers |
|-------|--------|--------|
| Content Generation Engine | Active | G2.3, G2.8 |
| Blog Publishing Worker | Active | G2.4, G2.7 |
| Content Calendar API | Planned | G2.1, G2.2, G2.9, G2.10 |
| Content Approval UI | Planned | G2.5 |
| Social Publisher API | Planned | G2.6 |
| Analytics Aggregator | Planned | G2.12 |

**Build priorities:**
1. Content Generation API deployment (G2.3) -- makes generation always-available
2. Content Calendar API (G2.1, G2.2) -- automates calendar + briefs
3. Approval UI (G2.5) -- replaces manual file review
4. Social publisher integration (G2.6) -- eliminates copy-paste
5. Analytics aggregation (G2.12) -- unified performance view
