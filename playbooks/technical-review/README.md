# Technical Review Playbook

A lightweight stack audit for companies under 20 people: 5 areas, 30 minutes per area, a prioritized roadmap at the end.

This is not a deep technical audit. It is a structured review designed to surface the tools, gaps, and bottlenecks that are limiting GTM effectiveness -- and prioritize what to fix first before adding more complexity.

---

## Prerequisites

None. This playbook works without any foundation work complete. It often reveals issues that need to be fixed before any other playbook can run effectively.

Run this review:
- When onboarding a new client or team
- When outreach campaigns are underperforming without a clear explanation
- When pipeline is inconsistent or hard to track
- At the start of any new quarter as a calibration exercise

---

## What this produces

- A documented inventory of the current stack across 5 functional areas
- A gap assessment with a 1-3 priority score per area
- A prioritized fix list: what to address in the next 30, 60, and 90 days
- A recommendation on where to standardize vs. where to experiment
- A filled output template ready to share or action

---

## Steps

### Area 1: Lead Generation and List Infrastructure

**What to assess (30 minutes):**

- Where are you sourcing leads? (Manual research, purchased lists, scrapers, database tools)
- What is your list quality? (What is the average bounce rate on outreach campaigns?)
- What is the process for building a new list from scratch? How long does it take? Who does it?
- What tools are you using? (LinkedIn Sales Navigator, Apollo, Hunter, Clay, or other)

**Questions to ask:**
- Can you build a 200-contact list targeting a specific ICP segment in under 4 hours?
- Is there an ICP filter applied before building, or are lists broad?
- Are emails verified before loading into the sending tool?

**What good looks like:**
You can build a targeted, verified list of 200 contacts in under 4 hours, with a bounce rate below 3% on send.

**Common gaps:**
- No systematic list-building process (it happens ad hoc)
- Emails not verified before sending, leading to deliverability damage
- No ICP filter applied before building (broad lists with low conversion rates)

---

### Area 2: Outreach and Sequencing

**What to assess (30 minutes):**

- What is the current outbound tooling? (Reply.io, Instantly, Smartlead, Outreach, HubSpot sequences, or other)
- Is a separate domain used for cold outreach? (Not the primary domain)
- What does inbox warmup look like?
- How is sequence performance tracked? (Open rate, reply rate, meeting rate by sequence)
- Are sequences paused automatically on reply?

**Questions to ask:**
- What is the current reply rate across active sequences?
- When did the sending domain last get its SPF, DKIM, and DMARC verified?
- What is the daily send limit per inbox?

**What good looks like:**
A dedicated cold email domain with SPF/DKIM/DMARC configured, a warmup tool running, sequences tracked by performance at the sequence level, and reply detection pausing sequences automatically.

**Common gaps:**
- Sending cold email from the primary domain (deliverability risk for all company email)
- No warmup tool running on cold email inboxes
- Performance tracked only at the campaign level, not the sequence level
- No automatic reply detection (contacts keep receiving follow-ups after they reply)

---

### Area 3: CRM and Pipeline Management

**What to assess (30 minutes):**

- Where are active deals tracked? (Spreadsheet, HubSpot, Salesforce, Pipedrive, or other)
- Do deal stages have clear entry and exit criteria, or are they loosely defined?
- Do all open deals have a next action and a date assigned?
- When was the pipeline last reviewed? How long does it take to get a full picture?
- How are contacts from events and referrals captured versus cold outbound contacts?

**Questions to ask:**
- How many open deals are there right now? What is the total estimated value?
- Which deals have had no activity in more than 14 days?
- What is the current close rate from proposal to signed?

**What good looks like:**
One place where all active deals live with stages, values, next actions, and last contact date visible in a single view. Pipeline reviewed weekly in under 20 minutes.

**Common gaps:**
- Deal information spread across multiple tools (email, spreadsheet, CRM, notes app)
- Deals sitting in pipeline for weeks with no activity and no follow-up
- No standard follow-up cadence for deals that go quiet
- No close rate tracked over time (making it impossible to know if the pipeline is improving)

---

### Area 4: Content and Brand Presence

**What to assess (30 minutes):**

- Where are you publishing? (LinkedIn, website, newsletter, other)
- What is the publishing cadence? (Daily, weekly, monthly, inconsistent)
- Does the content directly address the problem the ICP has, or is it general industry content?
- Is there a clear, consistent point of view that distinguishes the content from the category average?
- Is content being repurposed into cold outreach (PS lines, DM openers, reference links)?

**Questions to ask:**
- What is the most recent post? How many days ago?
- What engagement does the typical post get from people who match the ICP profile?
- Has any piece of content generated an inbound conversation in the last 90 days?

**What good looks like:**
Consistent publishing on one primary channel that generates engagement from the ICP type. A clear theme the author is known for among buyers in the target category.

**Common gaps:**
- Publishing gaps of 2-4 weeks (resets any momentum built)
- Content focused on what you do rather than what the buyer struggles with
- No distribution strategy beyond posting (relying only on followers to see it)
- Not referencing content in outreach sequences as proof of expertise

---

### Area 5: AI and Automation

**What to assess (30 minutes):**

- What manual tasks in the GTM motion could be automated? (List research, email personalization, lead enrichment, follow-up scheduling, content repurposing)
- What AI tools are currently in use? (Claude, GPT, Perplexity, Gemini, or other)
- What workflow tools are in use? (n8n, Zapier, Make, or other)
- Where are leads falling through manual handoffs?
- What repetitive tasks consume the most time per week?

**Questions to ask:**
- How is email personalization currently done? Manual research per contact or templated at scale?
- Are follow-ups being triggered manually or automatically based on deal stage?
- What would you automate first if you had 2 hours to set it up?

**What good looks like:**
The repetitive parts of GTM (list enrichment, email personalization at scale, follow-up scheduling, content repurposing) are handled by tools or workflows. Human focus is on decisions and conversations.

**Common gaps:**
- Manual research taking 30+ minutes per batch of contacts
- No automated follow-up (relying on memory to follow up with stale deals)
- Not using AI for first drafts of outreach or content
- No workflow connecting lead source to CRM (manual data entry between tools)

---

### Prioritization

After reviewing all 5 areas, score each one:

```
1 = Critical gap (actively limiting current GTM effectiveness)
2 = Improvement opportunity (would meaningfully improve results with low effort)
3 = Working well enough (do not change in the next 90 days)
```

**Fix in the first 30 days:** Everything scored 1. These are the gaps that are actively costing you now.

**Fix in days 31-60:** Everything scored 2. These are improvements that compound over time.

**Do not touch in the first 90 days:** Everything scored 3. Leave it and focus on higher priorities.

---

## Output Template

Fill this in as you complete each area review:

```
AREA 1: Lead Generation and List Infrastructure
Current tools: [list]
What is working: [description]
Critical gaps: [list]
Priority score: [1/2/3]
First fix: [specific action]

AREA 2: Outreach and Sequencing
Current tools: [list]
What is working: [description]
Critical gaps: [list]
Priority score: [1/2/3]
First fix: [specific action]

AREA 3: CRM and Pipeline Management
Current tools: [list]
What is working: [description]
Critical gaps: [list]
Priority score: [1/2/3]
First fix: [specific action]

AREA 4: Content and Brand Presence
Current state: [description]
What is working: [description]
Critical gaps: [list]
Priority score: [1/2/3]
First fix: [specific action]

AREA 5: AI and Automation
Current tools: [list]
What is working: [description]
Critical gaps: [list]
Priority score: [1/2/3]
First fix: [specific action]

30-DAY ROADMAP:
1. [Highest priority fix with specific steps]
2. [Second priority fix with specific steps]
3. [Third priority fix with specific steps]
```

---

## Templates

- [stack-audit.md](templates/stack-audit.md) -- Pre-filled output template with examples for each area

---

## Benchmarks

| Area | What good looks like |
|------|---------------------|
| List building | 200 verified contacts built in under 4 hours |
| Email deliverability | Bounce rate below 3% on every send |
| Outreach performance | Reply rate above 1%; open rate above 30% |
| Pipeline visibility | Full pipeline review completable in under 20 minutes |
| Content cadence | No publishing gap longer than 5 days on primary channel |
| Follow-up speed | Every reply handled within 4 business hours |
| Automation baseline | No manual task taking more than 30 min/week that could be automated |

---

## Common Mistakes

**Trying to fix everything at once.** The prioritization framework exists for a reason. Start with the critical gaps. Adding new tools to a broken foundation adds complexity, not results.

**Skipping deliverability review.** Cold email infrastructure problems (no warmup, no SPF/DKIM/DMARC, sending from primary domain) silently destroy campaigns. This is the most common hidden issue.

**Not having a single pipeline view.** Deals spread across email threads, spreadsheets, and CRM are deals waiting to fall through. Consolidate to one tool even if it is imperfect.

**No content strategy before publishing.** Publishing without a defined theme and audience produces content that builds no authority and attracts no buyers. Theme first, output second.

**Automating before the manual process works.** If you cannot do a task consistently by hand, automating it will not fix the underlying problem. Get the manual version working first.

**Not tracking the right metrics.** "How many did we send" is not a useful metric. Reply rate, positive reply rate, and meeting booked rate tell you whether the system is working.
