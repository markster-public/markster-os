# AUTOPILOT.md

**Instructions for an AI agent running Markster OS week-to-week.**

This is not a guide. It is a decision protocol. Read it as executable logic, not documentation.

---

## What autopilot is

Autopilot is the weekly operating loop. The agent runs it every week, in order.

The loop has four phases:
1. Diagnose -- find the constraint
2. Execute -- run one brick, nothing else
3. Verify -- did it move?
4. Loop -- set the next week's single focus

A business fails when everything is worked on at once. Autopilot prevents that. One constraint. One brick. One week. Repeat.

---

## Phase 1: Diagnose

### Step 1.1 -- Read company context

Before anything else, read these files:

```
company-context/identity.md
company-context/audience.md
company-context/offer.md
company-context/channels.md
```

If any of these are empty or contain placeholder text, STOP. F1 and F2 are not complete. Run the Foundation sequence before any GOD Engine brick. Go to `methodology/foundation/`.

### Step 1.2 -- Run the Hormozi diagnostic

Ask: which of these five symptoms is the founder experiencing right now?

| Symptom | What they say |
|---------|---------------|
| A | "People aren't buying" / "Conversion is low" |
| B | "Not enough leads" / "Pipeline is thin" |
| C | "Revenue is lumpy" / "We close some months but not others" |
| D | "Leads aren't converting on calls" / "Show rate is low" |
| E | "We're growing but burning out" / "I can't step back" |

**Map symptom to root cause:**

| Symptom | Root Cause | Diagnostic Tool |
|---------|-----------|-----------------|
| A -- Not buying | Offer problem | Value Equation audit (see below) |
| B -- Not enough leads | Channel or sequencing problem | Core 4 check (see below) |
| C -- Lumpy revenue | Missing offer type | 4 Offer Types gap check |
| D -- Leads not closing | Execution problem | 9 Kill Skills audit |
| E -- Burning out | Operations problem | O1/O2/O3 audit |

If the founder cannot name a single symptom, run the scorecard:
`methodology/assessment/scorecard.md`

The scorecard output IS the diagnosis. Lowest scoring section = constraint brick.

### Step 1.3 -- Identify the constraint brick

Map the root cause to the GOD Engine brick that fixes it:

| Root Cause | Constraint Brick | Playbook |
|-----------|-----------------|---------|
| Offer problem | F2 (Business Model) | `methodology/foundation/F2-business-model.md` |
| ICP not defined | F1 (Positioning) | `methodology/foundation/F1-positioning.md` |
| Leads not finding you | G1 (Find) | `playbooks/find/README.md` |
| Leads not warming up | G2 (Warm) | `playbooks/warm/README.md` |
| Not enough meetings | G3 (Book) | `playbooks/book/README.md` |
| Processes not documented | O1 (Standardize) | `playbooks/standardize/README.md` |
| Too much manual work | O2 (Automate) | `playbooks/automate/README.md` |
| Blind to metrics | O3 (Instrument) | `playbooks/instrument/README.md` |
| Delivery inconsistent | D1 (Deliver) | `playbooks/deliver/README.md` |
| No proof assets | D2 (Prove) | `playbooks/prove/README.md` |
| Clients not expanding | D3 (Expand) | `playbooks/expand/README.md` |

**Rule:** Fix only one constraint brick per week. If multiple are broken, fix the earliest in the sequence first.

Sequence priority: F1 -> F2 -> G1 -> G2 -> G3 -> O1 -> O2 -> O3 -> D1 -> D2 -> D3

---

## Phase 2: Execute

### Step 2.1 -- Run the Value Equation audit (if symptom A)

```
Value = (Dream Outcome x Perceived Likelihood of Achievement)
        / (Time Delay x Effort and Sacrifice)
```

Score each lever 1-5. Any lever below 3 is the fix.

| Lever | Score | Fix if low |
|-------|-------|-----------|
| Dream Outcome | /5 | Rewrite outcome statement in client's exact words |
| Perceived Likelihood | /5 | Add case studies, specific results, guarantee |
| Time Delay | /5 | Create a quick win deliverable in week 1 |
| Effort and Sacrifice | /5 | Remove steps the client has to do themselves |

If the offer scores below 12/20 total: rewrite the offer before running any outreach.
Go to: `playbooks/offer/README.md`

### Step 2.2 -- Run the Core 4 check (if symptom B)

Have you exhausted each source in order?

| Source | Test | If not done |
|--------|------|------------|
| Warm outreach | Did you contact every person who knows you and could refer? | Run warm outreach first -- `playbooks/book/warm-outreach.md` |
| Cold outreach | Are you sending 20+ contacts per week consistently? | Run G3 Book -- `playbooks/book/README.md` |
| Content | Are you publishing once per week on your ICP's platform? | Run G2 Warm -- `playbooks/warm/README.md` |
| Paid ads | Only after the above are working. | Do not run ads until offer is proven at scale. |

**Rule:** Never run a downstream channel before an upstream channel is working. If warm outreach has not been done, running cold outreach before it is skipping a step.

### Step 2.3 -- Run the 4 Offer Types gap check (if symptom C)

Which of these do you have?

| Type | Do you have it? | If missing |
|------|----------------|-----------|
| Attraction Offer | Y/N | Entry point to convert strangers. Build first. |
| Upsell Offer | Y/N | Offered immediately after first purchase. |
| Downsell Offer | Y/N | For people who said no to upsell. |
| Continuity Offer | Y/N | Recurring revenue. Fixes lumpy cash flow. |

The missing type is the next offer to build. Go to `playbooks/offer/README.md`.

### Step 2.4 -- Run the 9 Kill Skills audit (if symptom D)

Review recordings of the last 5 sales calls. Score each Kill Skill 1-3.

| Kill Skill | What to check |
|-----------|--------------|
| 1 Breathe the Script | Script memorized? Running it word for word? |
| 2 Tone | Pace 150-170 wpm? Loud enough? Clear enunciation? |
| 3 Introduction | Call framed correctly in first 60 seconds? |
| 4 Discovery | Enough questions asked before offer presented? |
| 5 Offer | Offer presented in terms of their stated problem? |
| 6 Objections | Objections resolved without breaking rapport? |
| 7 Looping | After failed close, return to discovery? |
| 8 BAMFAM | Next meeting booked before call ends? |
| 9 Referrals | Asked every closed customer for names? |

Lowest scoring Kill Skill = the training drill for this week.

### Step 2.5 -- Load the constraint brick skill

Once the constraint brick is identified, load the corresponding skill with this context pre-filled:

```
Business type: [from company-context/identity.md]
ICP: [from company-context/audience.md]
Offer: [from company-context/offer.md]
Symptom: [from Step 1.2]
Constraint: [brick name]
```

Run the skill. Do not switch to a different playbook mid-session.

---

## Phase 3: Verify

After executing the constraint brick playbook, check these:

### Did the constraint metric move?

Each brick has one output metric. If the metric did not move, the execution was incomplete.

| Brick | Output Metric | Verify |
|-------|--------------|--------|
| F1 | ICP definition complete | All 5 layers in `playbooks/find/templates/icp-worksheet.md` filled |
| F2 | Offer written as outcome | Value Equation score 15+/20 |
| G1 | Qualified list exists | 100+ ICP-match contacts, bounce rate below 5% |
| G2 | Content published | At least 1 piece live in last 7 days |
| G3 | Meetings booked | 5+ meetings booked this week |
| O1 | SOPs written | Core delivery process documented and walkthrough-ready |
| O2 | Hours saved | 10+ hours/week recovered through automation |
| O3 | Dashboard live | 3 North Star metrics visible without looking them up |
| D1 | Onboarding complete | Client onboarded without founder involvement |
| D2 | Proof asset exists | 1+ case study with company type + result + timeframe |
| D3 | NRR above 100% | Expansion revenue exceeds churn |

If the metric moved: go to Phase 4.
If the metric did not move: identify why. Fix the specific step that stalled. Do not move to the next brick.

---

## Phase 4: Loop

### Week-end protocol

At the end of each week, record:

```
Week of: [date]
Constraint brick: [which brick was worked]
Metric before: [number]
Metric after: [number]
Did it move? Y/N
Blocker (if N): [specific step that stalled]
Next week's single focus: [next constraint brick, or same if not done]
```

Store in: `learning-loop/canon/weekly-log.md`

### Constraint resolution order

When one brick is complete, the next constraint usually appears automatically. The sequence is:

1. F1/F2 -- without these, nothing downstream works
2. G1 -- without a list, G3 cannot run
3. G3 -- without meetings, there is no revenue
4. O1 -- without documentation, you cannot delegate
5. D1 -- without repeatable delivery, NRR cannot exceed 100%
6. D2 -- without proof, G3 conversion stays low
7. G2 -- content amplifies what is already working, not what is broken
8. O2/O3 -- automate and measure after the manual version works
9. D3 -- expansion is the final lever

**A business at 35+/41 on the scorecard has a compounding revenue system. The goal is to get every brick to 3/3.**

---

## Diagnostic shortcuts

### "I don't know what's broken"

Run the scorecard: `methodology/assessment/scorecard.md`

Lowest section score = constraint. Go there.

### "Everything feels broken"

Pick the earliest broken brick in the sequence. Fix only that.

### "We have leads but they're not closing"

Go to 9 Kill Skills audit (Step 2.4). Leads not closing is almost always execution, not lead quality.

### "We keep losing clients"

Check D3 (Expand). Specifically: do you have a health scoring process? Are you catching churn signals before clients decide?

### "Revenue is fine but I'm exhausted"

You have a G-heavy, O-light business. O1 is the constraint. Document the processes before adding more growth.

### "We're growing but growth slowed"

Run the 4 Offer Types check (Step 2.3). Slowing growth usually means the Continuity or Upsell offer is missing.

---

## Archetype routing

Your business type determines which bricks matter most at your current stage. Before running the weekly loop, confirm you have read your archetype file.

Find yours: `methodology/assessment/scorecard.md` (bottom section -- "After scoring: find your segment")

The archetype file tells you:
- which bricks to prioritize at your stage
- what your key metrics are
- where founders in your category most commonly get stuck

---

## What autopilot is not

- Not a replacement for human judgment on major strategic decisions
- Not a content generator -- it routes to the playbooks that produce content
- Not a substitute for founder conversations with real customers
- Not designed for businesses above 50 people -- the GOD Engine is a system for under-20-person teams

Above 20 people, the org structure needs redesign before this loop applies.

---

## Quick reference: skill routing

```
/markster-os   -- diagnostic operator, runs this autopilot protocol
/cold-email    -- G3 Book + cold outreach sequences
/events        -- G2 Warm + event sequences
/content       -- G2 Warm + content calendar
/sales         -- G3 Book + discovery + close
/fundraising   -- investor pipeline + deck + outreach
/research      -- market research prompt library
```

Load `/markster-os` to start any session. It runs the diagnostic before routing anywhere else.
