# Weekly KPI Dashboard

Three North Star metrics. Reviewed every week. Takes under 5 minutes to fill in.

If you cannot answer "how is the business performing this week?" in under 5 minutes, you do not have a dashboard. You have a reporting problem.

---

## The Three North Star Metrics

| Metric | What it measures | Target |
|--------|-----------------|--------|
| **Meetings booked** | G engine health -- are qualified conversations happening? | [Set your baseline] |
| **Hours saved** | O engine health -- is the business running without founder bottleneck? | 10+ hours/week |
| **NRR (Net Revenue Retention)** | D engine health -- are clients staying and expanding? | 100%+ |

These three metrics tell you which GOD Engine brick is your constraint this week.

- Meetings below target: G brick problem (Find, Warm, or Book)
- Hours not saved: O brick problem (Standardize or Automate)
- NRR below 100%: D brick problem (Deliver, Prove, or Expand)

---

## Weekly Dashboard Template

Fill this in every Monday morning. Under 5 minutes.

```
Week of: [Date]

GROWTH
Meetings booked this week: __
Target: __
vs. last week: __ (+/-__)
vs. 4-week avg: __ (+/-__)
Primary channel: cold email / LinkedIn / referral / content / event
Constraint (if below target): [ ] list quality  [ ] sequence  [ ] show rate  [ ] other: ___

OPERATIONS
Hours saved this week (vs. manual): __
Target: 10+
Automations running: __
Automations down or broken: __
Action needed: ___

DELIVERY
Active clients: __
Deliverables on time this week: __/__ (target: 90%+)
NRR (rolling 30 days): __%  (target: 100%+)
Clients flagged at risk: __
Action needed: ___

REVENUE
MRR / ARR: $__
New revenue this week: $__
Churned this week: $__
Pipeline value: $__
Deals expected to close this month: __

WEEKLY SUMMARY
What moved: ___
What didn't move: ___
Constraint brick this week: ___
One thing to fix: ___
```

---

## Metric Definitions

### Meetings Booked

Count: number of qualified discovery or sales calls booked in the last 7 days.

**Qualified** means: the prospect matches your ICP (company type, headcount, buying trigger). Do not count exploratory calls with people who are clearly not buyers.

Source: CRM, calendar, or outreach tool (Instantly, Reply.io, Apollo sequences).

**Drill-down if below target:**

| If... | Check... |
|-------|---------|
| Outreach volume is low | List building problem -- G1 |
| Volume is high but reply rate is low | Message problem -- G3 sequence |
| Replies but no shows | Show rate problem -- confirmation sequence |
| Shows but no qualified pipeline | ICP targeting problem -- F1 |

---

### Hours Saved

Count: hours per week recovered through automation vs. what manual execution would take.

**How to calculate:** For each automated process, estimate how long it would take manually. Sum those estimates.

Example:
- Automated follow-up sequence: 3 hours/week saved
- Automated meeting confirmation and reminder: 1 hour/week saved
- Automated reporting: 2 hours/week saved
- Total: 6 hours/week saved

If below 10 hours/week: O2 (Automate) is the constraint. Identify the highest-time manual task and automate it first.

---

### Net Revenue Retention (NRR)

Formula:
```
NRR = (Starting MRR + Expansion MRR - Churned MRR - Contracted MRR) / Starting MRR x 100
```

**Example:**
- Starting MRR: $20,000
- Expansion (upsells, add-ons): +$2,000
- Churn (cancelled clients): -$1,000
- Contraction (reduced scope): -$500
- NRR = ($20,000 + $2,000 - $1,000 - $500) / $20,000 = 102.5%

**NRR interpretation:**

| NRR | What it means |
|-----|--------------|
| Below 90% | Business is shrinking from existing clients. D1 and D3 are broken. |
| 90-100% | Replacing churn but not growing from existing base. |
| 100-110% | Expansion revenue exceeds churn. Healthy. |
| 110%+ | Strong expansion motion. D3 (Expand) is working. |

---

## Secondary Metrics (Review Monthly, Not Weekly)

These matter but not every week. Review on the first Monday of each month.

| Metric | Formula | Target |
|--------|---------|--------|
| CAC | Total sales + marketing spend / new clients acquired | Payback under 12 months |
| LTV | Avg contract value x avg client lifespan | LTV:CAC ratio 3:1+ |
| Gross margin | (Revenue - direct delivery costs) / Revenue | 50%+ for services |
| Pipeline conversion rate | Deals closed / discovery calls held | Track and improve |
| On-time delivery rate | Deliverables on time / total deliverables | 90%+ |

---

## Dashboard Setup (One-Time)

The dashboard only works if the data flows in without manual lookup.

**Recommended minimum setup:**

| Metric | Where to pull from |
|--------|-------------------|
| Meetings booked | CRM (HubSpot, Pipedrive) or outreach tool (Apollo, Instantly) |
| Hours saved | Manual estimate or time tracking tool (Toggl, Harvest) |
| NRR | Spreadsheet or billing tool (Stripe, QuickBooks) |
| MRR | Billing tool or spreadsheet |
| Pipeline value | CRM pipeline view |

**Simple spreadsheet setup:**
If no CRM, a Google Sheet with columns for: Date, Meetings booked, Hours saved, NRR, MRR, Pipeline value, Notes.
Update every Monday. Chart the trends. The chart reveals the pattern.

---

## Red Flags

Act on these within 48 hours. Do not wait for the next weekly review.

- Meetings booked drops to zero for two consecutive weeks
- NRR drops below 90% in any rolling 30-day period
- On-time delivery rate drops below 80%
- Any automation failure affecting client-facing processes
- Any client with zero engagement for 14+ days

---

## Reference

- Full O3 Instrument playbook: `playbooks/instrument/README.md`
- AUTOPILOT.md: uses these metrics as the constraint-brick routing signal
- D3 Expand (NRR and health scoring): `playbooks/expand/README.md`
