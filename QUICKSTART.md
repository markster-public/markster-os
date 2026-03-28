# Quick Start: Revenue in 7 Days

This is the shortest path from zero to first qualified meeting or first sale.

Skip nothing. Do it in order. Each step depends on the one before.

---

## Before you start: 30-minute setup

**1. Read your archetype file.**
Find your business type in `playbooks/segments/README.md`. Read that one file. It tells you which steps below matter most and what your key metrics are.

**2. Fill in company context.**
Open these three files and complete them. Everything downstream depends on this.
- `company-context/audience.md` -- who you sell to
- `company-context/offer.md` -- what you sell and at what price
- `company-context/messaging.md` -- the problem you solve in your buyer's language

If you cannot fill these in, do F1 and F2 first:
- `methodology/foundation/F1-positioning.md`
- `methodology/foundation/F2-business-model.md`

---

## Day 1: Lock your ICP and offer

**Goal:** One sentence on who you sell to. One sentence on what you sell. A price.

Work through: `playbooks/find/templates/icp-worksheet.md`

Output:
- ICP: "[Title] at [company type] who [buying trigger]"
- Offer: "[Outcome] in [timeframe] for [price]"
- One qualifying question to ask every prospect

Do not move to Day 2 until you can say both sentences without hesitation.

---

## Day 2: Build your warm list

**Goal:** 20 people you already know who match the ICP or can introduce you to someone who does.

Work through: `playbooks/book/warm-outreach.md`

Where to look:
- LinkedIn connections filtered by job title
- Former colleagues and clients
- Your phone contacts
- Email history from the past 2 years

Output: A list of 20 names with contact info. Prioritize people who: (1) match the ICP themselves, or (2) work with your ICP regularly.

---

## Day 3: Send warm outreach

**Goal:** 20 messages sent. Aim for 5-8 replies.

Use the warm outreach templates in `playbooks/book/warm-outreach.md`.

The message is short: reference the relationship, name the problem you solve, ask one question. No pitch. No deck. No link.

Send all 20 today. Do not wait for replies before sending the rest.

---

## Day 4: Build your cold list and set up email

**Goal:** 50-100 verified cold contacts ready to send.

Work through: `playbooks/find/README.md`

List building:
- Apollo.io or LinkedIn Sales Navigator to filter by ICP criteria
- Export, verify emails (Hunter.io or NeverBounce)
- Aim for 90%+ data accuracy before sending

Email setup check (before sending cold):
- Are you sending from a subdomain (not your primary domain)?
- Is SPF/DKIM/DMARC configured?
- Is a warmup tool running?

If any of the above is no, fix it before sending. See `playbooks/book/cold-email/README.md` Step 4.

---

## Day 5: Send cold email sequence

**Goal:** First 50 cold emails sent.

Use: `playbooks/book/cold-email/templates/sequence-b2b.md`

The sequence is 3 emails:
- Email 1: Under 100 words. One specific problem. One CTA.
- Email 2 (3 days later): Different angle, same offer.
- Email 3 (5 days later): Pattern interrupt or breakup.

Send Email 1 to all 50 today.

---

## Day 6: Follow up warm + LinkedIn

**Goal:** Reply to warm outreach responses. Send LinkedIn connection requests to cold list.

Warm follow-up: Anyone who opened but did not reply to Day 3 messages gets one follow-up. Use `playbooks/book/warm-outreach.md` follow-up template.

LinkedIn: Connect with your 50 cold contacts on LinkedIn with a short note. This creates a second touchpoint while email is warming.

---

## Day 7: Handle replies and book meetings

**Goal:** Every reply processed within 4 hours. First meeting booked.

Use: `playbooks/book/reply-triage.md` to handle each reply type.

For positive replies: move to a discovery call. Use `playbooks/biz-dev/sales/templates/discovery-call.md`.

For soft nos: add to a 90-day follow-up sequence. Do not argue. Do not re-pitch. Just acknowledge and set a future touchpoint.

---

## After Day 7: What to do with what you learned

After 50 cold sends and 20 warm messages, you have real data.

Check:
- How many warm replies? (Target: 5+. Below 3 = messaging or relationship quality issue.)
- How many cold replies? (Target: 3-5 from 50. Below 2 = ICP, message, or deliverability issue.)
- What objections came up? (Run `research/prompts/buyer-jobs-to-be-done-prompt.md` against what you heard.)

Make one change based on the data. Run the next 50. Repeat.

---

## Full playbook map (after the 7-day sprint)

Once you have first meetings booked:

| Next step | Where to go |
|-----------|-------------|
| Run a great discovery call | `playbooks/biz-dev/sales/README.md` |
| Write a proposal | `playbooks/biz-dev/sales/templates/proposal.md` |
| Build content to warm your pipeline | `playbooks/warm/content/README.md` |
| Attend events strategically | `playbooks/warm/events/README.md` |
| Document your first client results | `playbooks/prove/README.md` |
| Build a referral system | `playbooks/expand/referral/README.md` |
| Fundraise | `playbooks/biz-dev/fundraising/README.md` |
