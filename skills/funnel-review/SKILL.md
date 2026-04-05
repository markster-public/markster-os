---
name: funnel-review
description: Grades a funnel against vetted research benchmarks and produces a scored fix list. Checks offer stack ratios, traffic-funnel match, VSL structure, proof quality, and affiliate readiness. Use when you want to check if a funnel is ready to launch, when conversion is below target, or when you need a structured audit before scaling spend. Triggers on "review my funnel", "grade my funnel", "audit my funnel", "why is my funnel not converting", "funnel not working", "check my funnel", "is my funnel ready".
---

# Funnel Review - ACTIVATED

**Read these files first:**
- `playbooks/funnel/funnel-types.md`
- `playbooks/funnel/offer-stack.md`
- `playbooks/funnel/vsl-architecture.md`
- `playbooks/funnel/affiliate-mechanics.md`
- `playbooks/funnel/market-landscape.md`

---

## CHECK

Confirm what exists to review.

Ask: "What do you have? Walk me through the funnel: what pages exist, what the offer is, what the price is, and what traffic source you are using."

If the funnel is not yet built: route to `funnel-plan` + `funnel-build` first.

If the funnel is live and underperforming: ask for the current metrics. Identify which stage is failing before reviewing the assets. A VSL with a 2% purchase rate looks different from a VSL with a 15% opt-in rate.

---

## DO

Score each domain. Produce a score out of 100. Identify the highest-priority fixes.

### Domain 1: Traffic-Funnel Match (20 points)

| Check | Points | Pass / Fail |
|-------|--------|-------------|
| Traffic temperature matches funnel type | 10 | Cold to VSL: pass. Cold to application: fail. |
| Funnel type matches offer price tier | 10 | Under $5K to automated: pass. Over $5K to automated only: fail. |

Use the decision matrix from `playbooks/funnel/funnel-types.md`.

Common failures:
- Cold paid traffic to an application funnel (no trust-building mechanism)
- Warm email list to a long cold-traffic VSL (over-engineered, too long)
- $10K offer with no call in the sequence

### Domain 2: Offer Stack Architecture (20 points)

| Check | Points | Criteria |
|-------|--------|----------|
| Order bump exists | 5 | Missing = leaving 30-40% AOV on the table |
| OTO1 priced at 51-100% of front-end | 5 | Below 51%: underpriced. Above 100%: too large a jump. |
| Continuity offer exists | 5 | Missing = lumpy revenue, no margin engine |
| Backend or ascension offer defined | 5 | Missing = leaving the most valuable segment unmonetized |

Compare against benchmarks from `playbooks/funnel/offer-stack.md`.

### Domain 3: Proof Quality (20 points)

| Check | Points | Criteria |
|-------|--------|----------|
| At least one proof point with a real number | 10 | Vague testimonials: 0 points |
| Proof matches target ICP | 5 | "A client" vs "a 12-person agency": big difference |
| Proof is in the first half of the VSL or landing page | 5 | Proof buried after the fold: conversion loss |

2025 standard: proof must include company type + specific number + specific timeframe. Screenshots and vague endorsements do not meet the current buyer skepticism threshold.

### Domain 4: VSL Structure (20 points - skip if no VSL)

| Check | Points | Criteria |
|-------|--------|----------|
| Hook stops the scroll in the first 15 seconds | 5 | Opens with a greeting or bio: 0 points |
| Exactly three Secrets (not two, not four) | 5 | |
| Guarantee is at the end of the close, not earlier | 5 | Guarantee before the stack: signals defensiveness |
| No YouTube embed on the conversion page | 5 | YouTube on order page: conversion killer |

Review the hook specifically. It is the highest-leverage single element.

### Domain 5: Affiliate Readiness (20 points - score 20/20 if not building for affiliate)

| Check | Points | Criteria |
|-------|--------|----------|
| Fixed price (not custom quote) | 5 | Custom pricing is not affiliatable |
| VSL or standalone page (no scheduling required) | 5 | Webinar adds friction. Application requires a call. |
| EPC target defined and plausible | 5 | $2.00+ EPC on email is the affiliate threshold |
| Commission structure defined (recurring or flat) | 5 | Undefined commission = undefined affiliate motivation |

Use benchmarks from `playbooks/funnel/affiliate-mechanics.md`.

---

## SCORE AND FIX LIST

Produce the full scorecard:

```
FUNNEL REVIEW SCORECARD
=======================
Traffic-Funnel Match:    /20
Offer Stack:             /20
Proof Quality:           /20
VSL Structure:           /20
Affiliate Readiness:     /20
--------------------------
TOTAL:                   /100
```

Grade scale:
- 90-100: Launch-ready. Minor polish only.
- 70-89: Launch with caution. Fix Priority 1 issues before scaling spend.
- 50-69: Do not launch at scale. Fix before any significant traffic.
- Under 50: Fundamental structural problem. Likely wrong funnel type or missing offer stack layers.

**Prioritized fix list:**

Rank every failed check by revenue impact:

| Fix | Why it matters | Effort | Priority |
|-----|---------------|--------|----------|
| [Issue] | [Conversion or revenue impact] | [Low/Med/High] | P1/P2/P3 |

P1 fixes must be done before launch. P2 fixes should be done before scaling. P3 fixes are optimization.

---

## VERIFY

Before closing this session:

- [ ] Scorecard produced with a number for each domain
- [ ] Every failed check has a specific fix, not a vague recommendation
- [ ] P1 fixes identified and documented
- [ ] Traffic-funnel match confirmed or flagged as the root cause
- [ ] User knows which skill to use next: funnel-build (rebuild), or launch if 80+

---

## Reference files

- Funnel type decision criteria: `playbooks/funnel/funnel-types.md`
- Offer stack benchmarks: `playbooks/funnel/offer-stack.md`
- VSL structure: `playbooks/funnel/vsl-architecture.md`
- Affiliate benchmarks: `playbooks/funnel/affiliate-mechanics.md`
- Market landscape and proof standards: `playbooks/funnel/market-landscape.md`
- Fix the funnel: `skills/funnel-build/`
