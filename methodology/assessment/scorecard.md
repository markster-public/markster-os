# ScaleOS Readiness Scorecard

Use this before starting any playbook. Score yourself honestly -- not against what you plan to do, but against what is actually running today.

Score each question: **1 = Yes, 0 = No.**

---

## Section 1: Foundation

### F1: Positioning & Differentiation

| # | Question | Score |
|---|----------|-------|
| 1 | Can you describe your ICP in 30 seconds with zero ambiguity -- company type, headcount, buying trigger? | |
| 2 | Do you know the specific trigger event that makes a prospect a buyer right now (not the category, the trigger)? | |
| 3 | Have you spoken to at least 5 current or past clients to validate their pain in their exact words? | |
| 4 | Do you have a competitive moat -- something defensible that competitors cannot easily copy? | |

**F1 Score: __ / 4**

### F2: Business Model Design

| # | Question | Score |
|---|----------|-------|
| 1 | Can you state your offer as an outcome (what the client achieves) rather than a deliverable (what you produce)? | |
| 2 | Is your pricing based on the value of the outcome, not the hours you spend? | |
| 3 | Do you have at least two pricing tiers with a logical progression between them? | |
| 4 | Is your LTV:CAC ratio 3:1 or higher? | |

**F2 Score: __ / 4**

### F3: Organizational Structure

| # | Question | Score |
|---|----------|-------|
| 1 | Is there a named owner for each of the three GOD Engine pillars (Growth, Operations, Delivery)? | |
| 2 | Are decision rights documented -- do people know what they can decide without asking you? | |
| 3 | Could the business run for one week without founder involvement? | |

**F3 Score: __ / 3**

### F4: Financial Architecture

| # | Question | Score |
|---|----------|-------|
| 1 | Do you know your unit economics (CAC, LTV, gross margin) without looking them up? | |
| 2 | Do you have at least 3 months of cash reserves? | |
| 3 | Do you forecast cash weekly? | |

**F4 Score: __ / 3**

**Foundation Total: __ / 14**

---

## Section 2: GOD Engine

### G1: Find

| # | Question | Score |
|---|----------|-------|
| 1 | Do you have a defined set of filter criteria for building a qualified prospect list? | |
| 2 | Can you build a new 100-person ICP-match list within 48 hours using a repeatable process? | |
| 3 | Is your prospect data verified (bounce rate below 5%)? | |

**G1 Score: __ / 3**

### G2: Warm

| # | Question | Score |
|---|----------|-------|
| 1 | Are you publishing content consistently on the platform where your ICP spends time (minimum once per week)? | |
| 2 | Do you have a nurture sequence for warm contacts who have not yet bought? | |
| 3 | Is your content tied to a specific problem your ICP has -- not just industry topics? | |

**G2 Score: __ / 3**

### G3: Book

| # | Question | Score |
|---|----------|-------|
| 1 | Are you running outreach consistently (minimum 20+ contacts per week)? | |
| 2 | Do you have a 3+ touch follow-up sequence for non-replies? | |
| 3 | Is your meeting show rate above 80%? | |

**G3 Score: __ / 3**

### O1: Standardize

| # | Question | Score |
|---|----------|-------|
| 1 | Are your core delivery processes documented in SOPs someone else could follow? | |
| 2 | Do you have a documented onboarding process for new clients? | |
| 3 | Can a new hire execute their core responsibilities within 30 days using documentation alone? | |

**O1 Score: __ / 3**

### O2: Automate

| # | Question | Score |
|---|----------|-------|
| 1 | Are you saving 10+ hours per week through automation? | |
| 2 | Do you have automated follow-up sequences running (meeting confirmation, client check-ins)? | |
| 3 | Do you have monitoring on automations so failures are caught before they affect clients? | |

**O2 Score: __ / 3**

### O3: Instrument

| # | Question | Score |
|---|----------|-------|
| 1 | Do you review your three North Star metrics (meetings booked, hours saved, NRR) every week? | |
| 2 | Can you answer "how is the business performing this week?" in under 5 minutes? | |
| 3 | Do you forecast revenue 30 days out? | |

**O3 Score: __ / 3**

### D1: Deliver

| # | Question | Score |
|---|----------|-------|
| 1 | Do you have a systematic onboarding process for new clients that runs without founder oversight? | |
| 2 | Is your on-time delivery rate above 90%? | |
| 3 | Do you have a QA process that catches quality issues before the client sees them? | |

**D1 Score: __ / 3**

### D2: Prove

| # | Question | Score |
|---|----------|-------|
| 1 | Do you have at least two specific, verifiable case studies (company type + result + timeframe)? | |
| 2 | Are proof assets actively used in outreach and proposals -- not just sitting in a folder? | |
| 3 | Do you have a systematic process for collecting client results and testimonials? | |

**D2 Score: __ / 3**

### D3: Expand

| # | Question | Score |
|---|----------|-------|
| 1 | Is your NRR above 100% (expansion revenue exceeds churn)? | |
| 2 | Do you have a structured referral ask process (not just "let me know if you know anyone")? | |
| 3 | Do you track client health scores and act on them before clients decide to churn? | |

**D3 Score: __ / 3**

**GOD Engine Total: __ / 27**

---

## Overall Scoring

**Foundation + GOD Engine Total: __ / 41**

| Score per section | Status | What it means |
|------------------|--------|---------------|
| 0-1 | Not ready | Core inputs are missing. Fix this section before any playbook will work. |
| 2 | Starting | Enough to activate. Expect rough edges. Use the playbook to get structured quickly. |
| 3 | Working | Running this area. Focus on measurement and iteration. |

---

## Playbook Routing

Find your lowest-scoring section. That is your starting point.

| Lowest Score | Go To |
|-------------|-------|
| F1 (Positioning) | `methodology/foundation/F1-positioning.md` -- do not run any channel until F1 is complete |
| F2 (Business Model) | `methodology/foundation/F2-business-model.md` -- pricing and unit economics first |
| F3 (Org Structure) | `methodology/foundation/F3-org-structure.md` -- assign owners before adding people |
| F4 (Financial) | `methodology/foundation/F4-financial.md` -- unit economics before scaling |
| G1 (Find) | `playbooks/find/README.md` -- ICP operationalization and list building |
| G2 (Warm) | `playbooks/warm/README.md` -- content, events, nurture channels |
| G3 (Book) | `playbooks/book/README.md` -- outreach sequences and qualification |
| O1 (Standardize) | `playbooks/standardize/README.md` -- document before delegating |
| O2 (Automate) | `playbooks/automate/README.md` -- standardize first, then automate |
| O3 (Instrument) | `playbooks/instrument/README.md` -- build the dashboard |
| D1 (Deliver) | `playbooks/deliver/README.md` -- onboarding and QA systems |
| D2 (Prove) | `playbooks/prove/README.md` -- case studies and proof collection |
| D3 (Expand) | `playbooks/expand/README.md` -- NRR, health scoring, referral program |

---

## Scoring Notes

- Do not inflate scores. Answer based on what is actually running today.
- If a section scores 0, the playbooks in that area will not work yet. Fix first.
- Re-run this scorecard monthly. A complete ScaleOS operation should score 35+ out of 41 within 6-12 months.
