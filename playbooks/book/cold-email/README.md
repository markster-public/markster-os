# Cold Email Playbook

A systematic cold email program: from zero to a running sequence in one week.

---

## Prerequisites

- [ ] ICP documented with buying trigger (who you are targeting, what makes them a fit)
- [ ] Outcome statement defined: what the buyer gets, expressed in their language
- [ ] Problem statement written in buyer language, not internal language
- [ ] One proof point ready (a result, a case study, or a specific metric)
- [ ] Sending domain registered (separate from your primary domain)

If any of these are missing, complete them first. A cold email sequence without a clear ICP and message will generate low reply rates regardless of volume.

---

## What this produces

- A verified contact list of 200-500 ICP-matched prospects
- A 5-touch email sequence (email 1, follow-up 1-3, breakup email)
- An inbox infrastructure setup that avoids spam folders
- A send schedule (volume per day, timing, pause rules)
- A tracking template for reply rate, meeting rate, and iteration decisions
- An iteration log documenting what changed and why after the first 100 sends

---

## Steps

### Step 1: Research (60-90 minutes)

Before building a list or writing a word, run the research prompts.

**What to surface:**
- 5-10 competitor positioning claims (so you can differentiate)
- 10-20 verbatim phrases your buyer uses to describe their situation (forums, reviews, LinkedIn comments)
- The top 3 objections you will encounter in replies
- The buying trigger: the specific event or condition that makes them ready to act now

**Where to find buyer language:**
- G2, Trustpilot, or Capterra reviews for tools in their category
- Reddit and LinkedIn comments in their industry communities
- Sales call recordings if you have them
- Job postings (what they are hiring for reveals what they are struggling with)

The goal of this step is not research for its own sake. You are building a vocabulary list that goes directly into your email copy.

---

### Step 2: Segment (2-4 hours)

Build and verify the list before writing the sequence.

**2a: Define your filter criteria**

Pull directly from your ICP definition:
- Industry: specific vertical, not broad category
- Revenue range: use headcount as a proxy if revenue is unavailable
- Headcount range: small enough to have a single decision-maker, large enough to afford the engagement
- Geography: if relevant to your offering
- Decision-maker title: use "owner" as the default for small B2B service firms; it covers solo practitioners, partners, and founders
- Buying trigger signals: recent funding, hiring activity, job change, new office, technology adoption signals

**2b: Build the list**

Sources to use in order of reliability:
1. Apollo.io, LinkedIn Sales Navigator, or Hunter.io filtered by ICP criteria
2. Event attendee lists from recent industry events
3. LinkedIn Boolean search
4. Industry association directories and member lists

Target: 200-500 contacts for the first run. Do not start smaller. You need volume to see patterns.

**2c: Verify emails**

Run all emails through a verification tool (Reoon, ZeroBounce, or NeverBounce) before loading into your sending tool.

Target: under 3% bounce rate on send.

Remove:
- Generic emails (info@, contact@, hello@) unless the role is the decision-maker
- Anyone you already have an active relationship with (move them to warm outreach)
- Contacts flagged as risky or unverifiable

**Outputs from Step 2:**
- Verified list of 200-500 contacts in CSV format
- Bounce rate confirmed below 3%
- Segmented by sub-segment if applicable

---

### Step 3: Write the Sequence (2-3 hours)

Write a 5-touch sequence where each email has a different reason to reply.

**Sequence structure:**

| Touch | Timing | Channel | Purpose |
|-------|--------|---------|---------|
| Email 1 | Day 0 | Email | Value-first intro -- pain + proof, no offer yet |
| Email 2 | Day 4 | Email | Different angle -- data point or insight |
| LinkedIn | Day 2-3 | LinkedIn | Connection request with context |
| Email 3 | Day 8 | Email | First mention of diagnostic or offer -- earned by now |
| Email 4 | Day 12 | Email | Conversation starter, not a pitch |
| Email 5 | Day 16 | Email | Breakup -- "should I stop reaching out?" |

**Writing rules:**
- Email 1 subject line: 3-5 words, no question marks, no "Quick question"
- Email 1 opening: personalized first line referencing their company, role, or recent activity
- Problem statement: use buyer verbatims from Step 1, not a paraphrase
- CTA: one low-friction ask (15-minute call, or a yes/no question)
- Total length: Email 1 under 100 words. Follow-ups under 60 words.
- No marketing jargon in any email: no "pipeline," "GTM," "ICP," "funnel," "orchestration"
- Do not name specific tools in the offer (say "CRM," not a brand name)

**Each email needs a different angle:**
- E1: soft question, no offer
- E2: different asset or insight
- E3: first diagnostic mention
- E4: conversation starter
- E5: breakup

The diagnostic appears maximum 2 times across the entire sequence.

**Test before sending:**
- Read each email out loud. Does it sound like a human wrote it?
- Send yourself a test email. Open it on mobile.
- Ask: would someone in this industry think a peer sent this?

**Templates to use:**
- [sequence-b2b.md](templates/sequence-b2b.md)
- [follow-up.md](templates/follow-up.md)

---

### Step 4: Infrastructure Setup (2-3 hours setup, then automated)

**4a: Inbox setup**
- Use a separate domain for cold outreach. If your domain is `company.com`, register `company-hq.com` or `trycompany.com` for cold email.
- Set up SPF, DKIM, and DMARC records on the sending domain.
- Warm up the inbox for 2-4 weeks before sending (tools: Lemwarm, Mailreach, or Instantly warmup).
- Configure your sending tool (Instantly, Smartlead, Reply.io, or equivalent).

**4b: Volume rules**
- Maximum 30-50 emails per inbox per day while warming.
- After warmup is complete (4+ weeks): 50-100 per inbox per day maximum.
- Spread sends across business hours. Do not send at exactly 9:00am.
- Pause sending if reply rate drops below 1% for 3 consecutive days. The problem is the message, not the volume.

**4c: Load the sequence**
- Import verified list into sending tool
- Load sequence with day delays: Email 1 day 0, FU1 day 4, FU2 day 8, FU3 day 12, breakup day 16
- Set reply detection to pause sequence on reply (standard in all major tools)
- Set unsubscribe detection to remove contacts permanently

---

### Step 5: Manage Replies (ongoing)

Respond to all replies within 4 hours during business hours.

**Positive reply ("interested," "tell me more," "let's talk"):**
- Confirm the meeting immediately. Do not negotiate scope in email. Get them on a call.
- Send a calendar link or 2-3 specific time options.
- Reference their specific situation from the reply.

**Soft no ("not right now," "maybe later," "we're in a contract"):**
- Acknowledge without pressure. Ask for a specific future date to follow up.
- Add to a quarterly follow-up cadence with a calendar reminder.
- Example: "Totally understand. When would be a better time to revisit -- Q3, or closer to the end of the year?"

**Hard no ("not interested," "remove me"):**
- Remove immediately. Do not reply with a counter-pitch.
- Log as disqualified with reason.

**Out of office:**
- Set a task to follow up 2-3 days after their return date.

**Objection reply:**
- Acknowledge the objection before responding to it. Never argue.
- Map the objection to your pre-built objection responses from Step 1 research.

---

### Step 6: Iterate After 100 Sends

After 100 sends, evaluate before scaling. Change one variable at a time.

**Diagnosis logic:**
- Open rate low (under 20%): deliverability problem. Check spam folder, review inbox warming, fix subject line.
- Open rate high but reply rate low: message problem. Subject line works; body does not. Rewrite Email 1 using buyer verbatims.
- Reply rate decent but meetings not booking: CTA problem or wrong ICP. Simplify the CTA first.

Always change one variable at a time. Changing everything at once makes it impossible to know what worked.

---

## Templates

- [sequence-b2b.md](templates/sequence-b2b.md) -- Full 5-touch sequence structure with placeholder copy
- [follow-up.md](templates/follow-up.md) -- Follow-up variants by scenario (soft no, went dark, post-meeting)

---

## Benchmarks

| Metric | Baseline | Good | Excellent |
|--------|----------|------|-----------|
| Open rate | 30%+ | 45%+ | 60%+ |
| Reply rate | 1%+ | 3%+ | 5%+ |
| Positive reply rate | 0.5%+ | 1.5%+ | 3%+ |
| Meeting rate | 0.25%+ | 0.75%+ | 1.5%+ |
| Bounce rate | Under 5% | Under 3% | Under 1% |

Pause and diagnose if reply rate drops below 1% for 3 consecutive days. Do not scale a broken message.

---

## Common Mistakes

**Sending from your primary domain.** This puts your main email infrastructure at risk. Always use a separate cold email domain.

**Skipping email verification.** Bounce rates above 5% damage deliverability. Verify every list before loading it.

**Writing the same CTA five times.** Each email must give the reader a different reason to reply. "Just checking in" is not a reason.

**Using marketing jargon in prospect-facing emails.** Words like "pipeline," "GTM," "ICP," and "funnel" signal that you wrote this for yourself, not for them. Use their industry vocabulary.

**Changing too many variables at once.** When testing, change one thing at a time: subject line first, then body copy, then CTA. Otherwise you cannot tell what worked.

**Scaling before validating.** Run 100 sends and hit 1%+ reply rate before scaling volume. Scaling a broken message just sends more emails nobody responds to.

**Starting too small.** Lists under 100 contacts do not give you enough signal to know what is working. Start with 200-500.

**Generic first lines.** "I came across your company and was impressed" reads as automation. Reference something specific: a recent post, a hire, a product change, or a relevant industry event they likely attended.
