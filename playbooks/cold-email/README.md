# Cold Email Playbook

A systematic cold email program: from zero to a running sequence in one week.

---

## Prerequisites

Before starting this playbook, confirm:
- [ ] F1 complete: ICP documented with buying trigger
- [ ] F2 complete: Outcome statement and pricing defined
- [ ] F3 complete: Problem statement in buyer's language, proof point ready

If any of these are missing, complete them first. A cold email sequence without F1-F3 will generate low reply rates regardless of volume.

---

## What this playbook produces

- A verified contact list of 200-500 ICP-matched prospects
- A 3-touch email sequence (email 1, follow-up 1, follow-up 2)
- An inbox infrastructure setup that avoids spam folders
- A send schedule (volume per day, timing, pause rules)
- A tracking template for reply rate, meeting rate, and iteration decisions
- An iteration log that tells you what to change after the first 100 sends

---

## Step 1: Research

Before building a list or writing a word, run the research prompts.

**Run:**
- [competitive-intelligence.md](../../research/prompts/competitive-intelligence.md) - understand what the buyer sees from your competitors
- [buyer-jtbd.md](../../research/prompts/buyer-jtbd.md) - surface the jobs-to-be-done language your buyer uses
- [objection-research.md](../../research/prompts/objection-research.md) - identify the objections you will encounter in replies

**Outputs from Step 1:**
- A list of 5-10 competitor positioning claims (so you can differentiate)
- 10-20 verbatim phrases your buyer uses to describe their situation
- The top 3 objections you will need to address in the sequence

**Time:** 60-90 minutes

---

## Step 2: Segment

Build and verify the list before writing the sequence.

**2a: Define your filter criteria**

Pull directly from F1 (ICP):
- Industry: [from F1]
- Revenue range: [from F1]
- Headcount range: [from F1]
- Geography: [from F1]
- Decision-maker title: [from F1]
- Buying trigger signals: [what to look for in company activity]

**2b: Build the list**

Sources to use (in order of reliability):
1. Apollo.io, LinkedIn Sales Navigator, Hunter.io - filtered by F1 criteria
2. Event attendee lists (from recent industry events)
3. LinkedIn search with Boolean filters
4. Industry directories and association member lists

Target: 200-500 contacts for the first run. Do not start smaller - you need volume to see patterns.

**2c: Verify emails**

Run all emails through a verification tool (Reoon, ZeroBounce, or NeverBounce) before loading into your sending tool. Target: under 3% bounce rate on send.

Remove:
- Generic emails (info@, contact@, hello@)
- Role-based emails unless the role IS the decision-maker
- Anyone you already have an existing relationship with (move them to warm outreach)

**Outputs from Step 2:**
- Verified list of 200-500 contacts in CSV format
- Bounce rate confirmed below 3%
- Segmented by sub-segment if applicable (e.g., CPA firms vs. MSP firms)

**Time:** 2-4 hours

---

## Step 3: Write

Write the sequence using the templates as starting points.

**Sequence structure: 3 touches**

- Email 1: The main value proposition (cold intro). Short, one ask.
- Follow-up 1 (3-5 days later): Different angle, same offer. Not "just checking in."
- Follow-up 2 (5-7 days after FU1): Pattern interrupt or breakup frame. Short.

**Templates to use:**
- [sequence-b2b.md](templates/sequence-b2b.md)
- [follow-up.md](templates/follow-up.md)

**Writing rules:**
- Email 1 subject line: 3-5 words, no question marks, no "Quick question"
- Email 1 opening: personalized first line (reference their company, role, or recent activity)
- Problem statement: use your F3 language verbatim, not a paraphrase
- CTA: one low-friction ask (15-minute call, or reply with a yes/no question)
- Total length: Email 1 under 100 words. Follow-ups under 60 words.

**Test before sending:**

Read each email out loud. Ask: would a human at this company think a human wrote this? If it sounds automated or generic, rewrite it.

Send yourself a test email. Open it on mobile. Does it look right?

**Outputs from Step 3:**
- Complete 3-touch sequence written and reviewed
- Subject lines tested (minimum 2 variations for Email 1)

**Time:** 2-3 hours

---

## Step 4: Send

Set up the infrastructure before hitting send.

**4a: Inbox setup**

- Use a separate domain for cold outreach (not your primary domain). Example: if your domain is `company.com`, register `company-hq.com` or `trycompany.com` for cold email.
- Set up SPF, DKIM, and DMARC records on the sending domain.
- Warm up the inbox for 2-4 weeks before sending (use a warmup tool like Lemwarm, Mailreach, or Instantly's warmup).
- Configure your sending tool (Instantly, Smartlead, Reply.io, or equivalent).

**4b: Volume rules**

- Maximum 30-50 emails per inbox per day (while warming).
- After warmup is complete (4+ weeks): 50-100 per inbox per day maximum.
- Spread sends across business hours. Do not send at exactly 9:00am.
- Pause sending if reply rate drops below 1% for 3 consecutive days (troubleshoot message, not volume).

**4c: Load the sequence**

- Import verified list into sending tool
- Load sequence with day delays: Email 1 -> day 0, FU1 -> day 4, FU2 -> day 9
- Set reply detection to pause sequence on reply (standard in all major tools)
- Set unsubscribe detection to remove contacts permanently

**Outputs from Step 4:**
- Sending domain configured with SPF/DKIM/DMARC
- Inbox warming active
- Sequence loaded in tool with correct delays
- First batch sending

**Time:** 2-3 hours setup, then automated

---

## Step 5: Follow-up (manual replies)

When you get a reply, respond within 4 hours during business hours.

**Reply types and responses:**

**Positive reply ("interested," "tell me more," "let's talk"):**
- Confirm the meeting immediately. Do not negotiate scope in email. Get them on a call.
- Send calendar link or 2-3 specific time options.
- Confirm what you will cover on the call (reference their specific situation from the reply).

**Soft no ("not right now," "maybe later," "we're in a contract"):**
- Acknowledge without pressure. Ask for a specific future date to follow up.
- Add to a quarterly follow-up sequence with a calendar reminder.
- Reply example: "Totally understand. When would be a better time to revisit - Q2, or closer to fall?"

**Hard no ("not interested," "remove me"):**
- Remove immediately. Do not reply with a counter-pitch.
- Mark in CRM as disqualified with reason.

**Out of office:**
- Set a task to follow up 2-3 days after their return date.

**Objection reply:**
- See [objection research](../../research/prompts/objection-research.md) for response frameworks.
- Rule: acknowledge the objection before responding to it. Never argue.

**Outputs from Step 5:**
- Reply log maintained
- Meeting booked or follow-up dated for every positive and soft-no reply

---

## Step 6: Iterate

After 100 sends, evaluate before scaling.

**Metrics to track:**

| Metric | Baseline target | Good | Excellent |
|--------|----------------|------|-----------|
| Open rate | 30%+ | 45%+ | 60%+ |
| Reply rate | 1%+ | 3%+ | 5%+ |
| Positive reply rate | 0.5%+ | 1.5%+ | 3%+ |
| Meeting rate | 0.25%+ | 0.75%+ | 1.5%+ |

**If open rate is low (under 20%):** Deliverability problem. Check spam folder, review inbox warming, fix subject line.

**If open rate is high but reply rate is low:** Message problem. The subject line works; the body does not. Rewrite Email 1 body using buyer verbatims from Step 1.

**If reply rate is decent but meetings are not booking:** CTA problem or wrong ICP. Either the ask is too big, or you are reaching the wrong people. Simplify the CTA first.

**What to change first:** Always change one variable at a time. Subject line test, then body copy test, then CTA test. Changing everything at once makes it impossible to know what worked.

**Outputs from Step 6:**
- Metrics dashboard updated
- One specific change identified and implemented
- Iteration log documenting what changed and why
