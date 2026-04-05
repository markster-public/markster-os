---
name: funnel-build
description: Writes funnel assets step by step from a completed funnel plan. Process covers VSL script, landing page copy, OTO sequences, email nurture, and application page. Use when creating funnel copy after architecture is confirmed, or when you need to write VSL, landing page, or email assets from a defined offer. Run after funnel-plan. Triggers on "write the funnel", "build the funnel assets", "write the VSL", "write the landing page", "write the OTO", "write the email sequence", "build funnel copy".
---

# Funnel Build - ACTIVATED

**Read these files first:**
- `playbooks/funnel/vsl-architecture.md`
- `playbooks/funnel/input-spec.md`
- `playbooks/funnel/offer-stack.md`

## Contents

- [CHECK](#check) - confirm plan and inputs before writing
- [DO - Step 1](#step-1-vsl-script-if-vsl-funnel) - VSL script
- [DO - Step 2](#step-2-landing-page-all-funnel-types) - landing page
- [DO - Step 3](#step-3-oto-pages) - OTO pages
- [DO - Step 4](#step-4-email-sequence) - email sequence
- [DO - Step 5](#step-5-application-page-if-applicable) - application page
- [VERIFY](#verify) - output checklist

---

## CHECK

Do not proceed past any failed check.

**1. Funnel plan complete?**

Ask: "Have you run funnel-plan? Do you have the funnel type, offer stack, and conversion targets confirmed?"

If no funnel plan: "Build without a plan produces assets that do not fit together. Run funnel-plan first to confirm the architecture."

**2. All Required inputs collected?**

Reference `playbooks/funnel/input-spec.md`. Confirm all Required inputs for the selected funnel type:

- [ ] Mechanism name
- [ ] ICP definition (company type, headcount, buying trigger, title)
- [ ] Outcome statement with a real number
- [ ] At least one proof point (company type + number + timeframe)
- [ ] Verbatim pain language from real buyers
- [ ] Objection sequence from real sales calls
- [ ] Offer stack with all prices confirmed
- [ ] Guarantee terms
- [ ] Traffic source confirmed

If any Required input is missing: stop. State which inputs are missing and what the consequence is if built without them. Do not write assets on fabricated inputs.

**3. Brand voice confirmed?**

Read `company-context/voice.md` if it exists. If not, ask: "How do you sound? Plain and direct, or more formal? Any phrases you never use?"

---

## DO

Build assets in this order. Confirm each with the user before moving to the next.

### Step 1: VSL Script (if VSL funnel)

Using `playbooks/funnel/vsl-architecture.md`, build the full script section by section.

Produce each section as a fill-ready template with their inputs embedded:

**Opening (150-200 words)**
Write the hook. Options based on their dominant buyer emotion:
- Fear dominant: counter-intuitive claim that reframes the threat
- Frustration dominant: audience qualifier that names exactly who this is for and what they've tried
- Skepticism dominant: pattern interrupt that signals "this is structurally different"

No greetings. No company name. No price in the opening.

**Problem agitation (300-400 words)**
Use verbatim pain language collected from their buyers. Three dimensions:
- Financial cost (in dollars or percentage if possible)
- Emotional / time cost (in hours lost, decisions deferred, stress)
- Opportunity cost (what they are not achieving while the problem persists)

Do not introduce the solution yet.

**Story arc (500-700 words)**
Six beats: struggle - failed vehicles - catalyst - epiphany - system - transformation.
- Failed vehicles: name the specific things they tried (these match the Three Secrets)
- Transformation: end with a specific metric, not an emotion

**Three Secrets (300-450 words each)**
Build each secret from their objection sequence:
- Secret 1 (Vehicle): why the category they tried before failed
- Secret 2 (Internal): why they think they personally cannot do this
- Secret 3 (External): why they think outside forces prevent it

Structure: old belief -> validate why it formed -> new belief -> proof anchor.

**Repeatability proof (200-300 words)**
Two case studies minimum: one that mirrors the buyer exactly, one from a different but plausible archetype.
Format: company type + what they did + specific result + timeframe.

**Stack presentation (300-400 words)**
List all deliverables. For each one use an ROI anchor, not a retail price.
Example: "Most companies spend $6,000-$8,000 per month on a marketing hire just to manage this one function."
Never stack more than 5-6 components.

**Close (350-500 words)**
Three passes in sequence:
1. Price reveal with anchoring stepdown (start at a high anchor, step to real price)
2. Decision reframe (quantify the cost of inaction in dollars or lost time)
3. Guarantee immediately before the CTA

State the CTA clearly. One action. No options.

### Step 2: Landing Page (all funnel types)

Write the full page. Required sections:

```
HERO
Headline: [ICP] + [outcome] in [timeframe/words or less]
Sub-headline: [What they get] without [what they dread]
CTA: [Action verb] + [what happens]

THE PROBLEM
3 bullets in buyer language. Financial, emotional, opportunity.

THE SOLUTION
3-4 sentences. What the offer delivers, step by step.

HOW IT WORKS
1. [Step 1]
2. [Step 2]
3. [Step 3]

PROOF
Company type + specific result + timeframe. One case study.

CTA (repeated)
Button + friction removal line.
```

Rules:
- Headline passes the Stranger Test (unfamiliar person explains it in 10 seconds)
- No em dashes
- Sentences under 20 words
- No jargon

### Step 3: OTO Pages

Write each OTO in the stack.

OTO1 structure:
- Open with identity reinforcement ("You just made a great decision. Here's the next one.")
- State the next problem the core offer creates
- Introduce OTO1 as the natural solution
- Value stack with ROI anchors
- Price reveal (51-100% of what they just spent)
- Guarantee (if applicable)
- CTA

OTO2 / downsell structure:
- Acknowledge they passed on OTO1
- Offer a reduced version or payment plan
- One paragraph. One CTA.

### Step 4: Email Sequence

Minimum sequence for any funnel:

**Confirmation / Day 0:** Delivery or confirmation. No pitch. One observation relevant to their situation.

**Day 1-2 - Indoctrination:** Mechanism story. Why the old approach failed. Why this is different.

**Day 3 - Proof:** One case study. Company type + result + timeframe. Soft CTA.

**Day 5 - Objection:** Address the most common objection from their sales call data.

**Day 7 - Offer:** Direct CTA. Reference the Day 3 case study. Under 100 words.

For high-ticket (post-application): replace Day 7 offer with booking link for the call.

### Step 5: Application Page (if applicable)

Three sections only:
1. Who this is for (ICP definition, 3 bullets)
2. Who this is NOT for (disqualifiers, 3 bullets - makes the qualified buyer more certain)
3. Application form (5-7 fields: name, company, revenue, biggest challenge, what they've tried, why now)

No pricing on the application page. The call handles that.

---

## VERIFY

Before closing this session:

- [ ] VSL script written with all six story beats and exactly three Secrets
- [ ] All proof points in assets use company type + number + timeframe (no vague testimonials)
- [ ] Landing page headline passes the Stranger Test
- [ ] OTO1 opens with identity reinforcement, not a product pitch
- [ ] Email sequence has at least one proof email and one direct offer email
- [ ] No fabricated claims (all claims have a real evidence item behind them)
- [ ] Guarantee appears at the end of the close, not the beginning
- [ ] All assets ready for `funnel-review` scoring before launch

---

## Reference files

- VSL structure: `playbooks/funnel/vsl-architecture.md`
- Input requirements: `playbooks/funnel/input-spec.md`
- Price architecture: `playbooks/funnel/offer-stack.md`
- High-ticket backend: `playbooks/funnel/high-ticket-backend.md`
- Run after build: `skills/funnel-review/`
