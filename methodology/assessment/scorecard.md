# ScaleOS Readiness Scorecard

Use this assessment before activating any playbook. It tells you where you are solid, where you are shaky, and which playbook to run first.

Score each question: **1 = Yes, 0 = No.**
Add up your score per section.

---

## Section 1 - Foundation

### F1: ICP (Ideal Customer Profile)

| # | Question | Score |
|---|----------|-------|
| 1 | Can you describe your best customer in one sentence without using generic terms like "small business" or "anyone who needs X"? | |
| 2 | Do you know the specific trigger event that makes a prospect ready to buy right now? | |
| 3 | Have you spoken to at least 5 current or past customers to validate their pain in their own words? | |
| 4 | Do you have a written disqualifier list - types of prospects you will not take on? | |

**F1 Score: __ / 4**

### F2: Offer

| # | Question | Score |
|---|----------|-------|
| 1 | Can you state your offer as an outcome (what the client achieves) rather than a deliverable (what you produce)? | |
| 2 | Is your pricing based on the value of the outcome, not the hours you spend? | |
| 3 | Do you have a risk reversal element (guarantee, pilot, performance clause) that removes friction for new buyers? | |
| 4 | Have at least 3 clients paid full price for this exact offer in the last 90 days? | |

**F2 Score: __ / 4**

### F3: Message

| # | Question | Score |
|---|----------|-------|
| 1 | Do you have a written one-sentence offer that follows the format: "We help [ICP] achieve [outcome] in [timeframe] without [sacrifice]"? | |
| 2 | Does your message describe the problem before it mentions the solution? | |
| 3 | Do you have at least 2 proof points (case studies, testimonials, or data) that you can reference in any channel? | |
| 4 | Have you tested this message in at least one live channel and received positive signals (replies, clicks, inquiries)? | |

**F3 Score: __ / 4**

### F4: Channel

| # | Question | Score |
|---|----------|-------|
| 1 | Have you identified the one channel where your ICP is most reachable and most receptive? | |
| 2 | Are you currently running at least one channel consistently (weekly, not once a month)? | |
| 3 | Do you have a clear handoff process from channel activity to booked meeting? | |

**F4 Score: __ / 3**

**Foundation Total: __ / 15**

---

## Section 2 - GOD Engine

### G1: List Building

| # | Question | Score |
|---|----------|-------|
| 1 | Do you have a defined set of filter criteria for pulling a qualified prospect list? | |
| 2 | Is your current list verified (bounces below 5%)? | |
| 3 | Can you build a new 200-person list within 48 hours using repeatable sources? | |

**G1 Score: __ / 3**

### G2: Cold Email

| # | Question | Score |
|---|----------|-------|
| 1 | Are you sending cold email from a warmed-up domain (not your primary domain)? | |
| 2 | Do you have a 3-touch sequence written and loaded in a sending tool? | |
| 3 | Are you tracking open rate, reply rate, and meeting rate separately? | |

**G2 Score: __ / 3**

### G3: LinkedIn

| # | Question | Score |
|---|----------|-------|
| 1 | Is your LinkedIn profile optimized for your ICP (headline, about section, featured content)? | |
| 2 | Are you sending personalized connection requests to ICP-matched prospects weekly? | |
| 3 | Are you posting at least twice per week on LinkedIn? | |

**G3 Score: __ / 3**

### G4: Events

| # | Question | Score |
|---|----------|-------|
| 1 | Have you attended at least one ICP-relevant event in the last 60 days? | |
| 2 | Do you have a post-event follow-up sequence written and ready to send within 24 hours? | |
| 3 | Do you track meetings booked per event attended? | |

**G4 Score: __ / 3**

### G5: Content

| # | Question | Score |
|---|----------|-------|
| 1 | Do you publish at least one piece of long-form content per week (article, case study, deep post)? | |
| 2 | Do you repurpose long-form content into 3-5 short-form posts? | |
| 3 | Is your content tied to your F3 message - does it describe the problem your ICP has? | |

**G5 Score: __ / 3**

### G6: Referrals

| # | Question | Score |
|---|----------|-------|
| 1 | Do you make a structured referral ask (not just "let me know if you know anyone") to happy clients at least once per quarter? | |
| 2 | Do you track which clients have referred others and how many? | |
| 3 | Do you have an incentive or acknowledgment process for referrers? | |

**G6 Score: __ / 3**

### G7: Paid

| # | Question | Score |
|---|----------|-------|
| 1 | Have you proven your offer converts at full price through at least one organic channel before running paid? | |
| 2 | Do you have a retargeting audience of at least 500 people (website visitors, email list, or video viewers)? | |
| 3 | Can you calculate your maximum allowable cost per lead based on your average deal size and close rate? | |

**G7 Score: __ / 3**

### G8: Partnerships

| # | Question | Score |
|---|----------|-------|
| 1 | Have you identified at least 3 businesses that serve your exact ICP but do not compete with you? | |
| 2 | Have you had a conversation with any of them about mutual referrals or co-marketing? | |
| 3 | Do you have a written co-sell or referral agreement with at least one partner? | |

**G8 Score: __ / 3**

### G9: SEO

| # | Question | Score |
|---|----------|-------|
| 1 | Have you identified at least 10 long-tail keywords your ICP searches when they have the problem you solve? | |
| 2 | Are you publishing SEO-optimized content targeting those keywords at least twice per month? | |
| 3 | Do you have at least 5 pages indexed and ranking for any keyword in the top 20 results? | |

**G9 Score: __ / 3**

**GOD Engine Total: __ / 27**

---

## Overall Score Interpretation

| Score Range | Status | What It Means |
|-------------|--------|---------------|
| 0-2 per section | Not Ready | Core inputs are missing. Completing this section is a prerequisite before any playbook will work. |
| 3-5 per section | Ready to Start | You have enough to activate. Expect rough edges. Use the playbook to get structured quickly. |
| 6+ per section | Optimized | You are running this area well. Focus on measurement and iteration, not setup. |

---

## Playbook Routing

Find your lowest-scoring section. That is where you start.

| Lowest Score Area | Go To |
|-------------------|-------|
| F1 (ICP) | `methodology/foundation/F1-icp.md` - do not run any playbook until F1 is complete |
| F2 (Offer) | `methodology/foundation/F2-offer.md` - your message and channel work are blocked until F2 is clear |
| F3 (Message) | `methodology/foundation/F3-message.md` - every outbound channel depends on message |
| F4 (Channel) | `methodology/foundation/F4-channel.md` - pick one channel and commit |
| G1 (List) | `playbooks/cold-email/README.md` - Step 1 covers list building |
| G2 (Cold Email) | `playbooks/cold-email/README.md` - full playbook |
| G3 (LinkedIn) | `playbooks/content/short-form/README.md` - LinkedIn posts + outreach |
| G4 (Events) | `playbooks/events/README.md` - full playbook |
| G5 (Content) | `playbooks/content/README.md` - long-form and short-form |
| G6 (Referrals) | `playbooks/biz-dev/sales/README.md` - referral ask is part of the sales process |
| G7 (Paid) | Activate paid only after G1-G5 are scoring 4+. Not covered in this release. |
| G8 (Partnerships) | `playbooks/biz-dev/fundraising/README.md` - partnership pipeline mirrors fundraising pipeline |
| G9 (SEO) | `playbooks/content/long-form/README.md` - SEO-optimized long-form content |

---

## Scoring Notes

- Do not inflate scores. Answer based on what is actually running today, not what you plan to do.
- If a section scores 0, the playbooks in that area will not work yet. Fix the foundation first.
- Re-run this scorecard monthly. A complete ScaleOS operation should score 35+ out of 42 within 6 months.
