# Technical Review Playbook

A lightweight stack audit for companies under 20 people: 5 areas, 30 minutes per area, a prioritized roadmap at the end.

This is not a deep technical audit. It is a structured review designed to surface the tools, gaps, and bottlenecks that are limiting GTM effectiveness - and prioritize what to fix first.

---

## Prerequisites

None. This playbook works without Foundation complete. It often reveals issues that need to be fixed before Foundation work can be done effectively.

---

## What this playbook produces

- A documented inventory of your current stack
- A gap assessment across 5 functional areas
- A prioritized fix list (what to address in the next 30, 60, and 90 days)
- A recommendation on where to standardize vs. where to experiment

---

## The 5 review areas

### Area 1: Lead Generation and List Infrastructure

**What to assess:**

- Where are you sourcing leads? (Manual research, purchased lists, scrapers, database tools)
- What is your list quality? (What is your average bounce rate on email campaigns?)
- What is the process for building a new list? (How long does it take? Who does it?)
- What tools are you using? (LinkedIn Sales Navigator, Apollo, Hunter, Clay, etc.)

**What good looks like:** You can build a targeted, verified list of 200 contacts in under 4 hours, with a bounce rate below 3%.

**Common gaps:**
- No systematic list-building process (it happens ad hoc)
- Unverified emails leading to deliverability damage
- No ICP filter applied before building (broad lists with low conversion)

**Time to assess: 30 minutes**

---

### Area 2: Outreach and Sequencing

**What to assess:**

- What is your current outbound tooling? (Reply.io, Instantly, Smartlead, Outreach, HubSpot sequences, etc.)
- Are you using a separate domain for cold outreach? (Not your primary domain)
- What does your inbox warmup setup look like?
- How is sequence performance tracked? (Open rate, reply rate, meeting rate by sequence)

**What good looks like:** A dedicated cold email domain with SPF/DKIM/DMARC configured, a warmup tool running, sequences tracked by performance, and reply detection pausing sequences automatically.

**Common gaps:**
- Sending cold email from the primary domain (deliverability risk)
- No warmup tool running
- No performance tracking beyond "how many did we send"

**Time to assess: 30 minutes**

---

### Area 3: CRM and Pipeline Management

**What to assess:**

- Where do you track active deals? (Spreadsheet, HubSpot, Salesforce, Pipedrive, ClickUp, etc.)
- Do your deal stages have clear entry and exit criteria?
- Do all open deals have a next action and date assigned?
- When was the last time you reviewed the pipeline? How long does it take to see the full picture?

**What good looks like:** One place where all active deals live, with stages, values, next actions, and last contact date visible. Pipeline reviewed weekly in under 20 minutes.

**Common gaps:**
- Multiple tools with deal information spread across them
- Deals sitting in pipeline for weeks with no activity
- No standard follow-up cadence for deals that go quiet

**Time to assess: 30 minutes**

---

### Area 4: Content and Brand Presence

**What to assess:**

- Where are you publishing? (LinkedIn, website, newsletter, X, podcast, YouTube?)
- What is the publishing cadence? (Daily, weekly, monthly, inconsistent?)
- Does the content directly address the problem your ICP has, or is it general industry content?
- Is there a clear point of view that distinguishes your content from category average?

**What good looks like:** Consistent publishing on one primary channel that generates engagement from your ICP type. A clear theme that you are known for among your buyers.

**Common gaps:**
- Publishing inconsistently (gaps of 2-4 weeks)
- Content focused on what you do rather than what the buyer struggles with
- No distribution strategy beyond posting

**Time to assess: 30 minutes**

---

### Area 5: AI and Automation

**What to assess:**

- What manual tasks in your GTM motion could be automated? (List research, email personalization, lead enrichment, follow-up scheduling, content repurposing)
- Are you using AI tools for research, writing, or workflow? (Claude, GPT, Perplexity, Gemini, n8n, Zapier, Clay)
- Where are you losing time to repetitive work that a system could handle?
- Are there gaps in your process where leads fall through because of manual handoffs?

**What good looks like:** The repetitive parts of your GTM (list enrichment, email personalization at scale, follow-up scheduling, content repurposing) are handled by tools or workflows. You focus on decisions and conversations.

**Common gaps:**
- Manual research that takes hours per batch
- No automated follow-up (relying on memory to follow up)
- Not using AI for first drafts of outreach or content
- No workflow connecting lead sources to CRM

**Time to assess: 30 minutes**

---

## Prioritization framework

After reviewing all 5 areas, rank each area 1-3:

```
1 = Critical gap (limiting your current GTM effectiveness)
2 = Improvement opportunity (would meaningfully improve results)
3 = Working well enough (do not change yet)
```

**Fix in the first 30 days:** Everything ranked 1. These are the gaps that are actively costing you.

**Fix in days 31-60:** Everything ranked 2. These are improvements that compound over time.

**Do not touch in the first 90 days:** Everything ranked 3. Leave it alone and focus on the higher-priority items.

---

## Output template

Fill this in as you complete each area review:

```
AREA 1: Lead Generation and List Infrastructure
Current tools: [list]
What is working: [what]
Critical gaps: [gaps]
Priority: [1/2/3]
First fix: [specific action]

AREA 2: Outreach and Sequencing
Current tools: [list]
What is working: [what]
Critical gaps: [gaps]
Priority: [1/2/3]
First fix: [specific action]

AREA 3: CRM and Pipeline Management
Current tools: [list]
What is working: [what]
Critical gaps: [gaps]
Priority: [1/2/3]
First fix: [specific action]

AREA 4: Content and Brand Presence
Current state: [description]
What is working: [what]
Critical gaps: [gaps]
Priority: [1/2/3]
First fix: [specific action]

AREA 5: AI and Automation
Current tools: [list]
What is working: [what]
Critical gaps: [gaps]
Priority: [1/2/3]
First fix: [specific action]

30-DAY ROADMAP:
1. [Highest priority fix]
2. [Second priority fix]
3. [Third priority fix]
```

---

## Template

[stack-audit.md](templates/stack-audit.md)
