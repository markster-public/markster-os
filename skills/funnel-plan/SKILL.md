---
name: funnel-plan
description: Full funnel architecture session. Diagnoses your situation, selects the right funnel type, and designs the complete offer stack with price ratios and conversion targets. Use when building a new funnel from scratch, when reviewing an existing funnel architecture, or when you need to define the offer stack before creating assets. Run before funnel-build. Triggers on "design my funnel", "funnel architecture", "what funnel should I build", "funnel strategy", "offer stack design", "plan my funnel", "which funnel type".
---

# Funnel Plan - ACTIVATED

**Read these files first:**
- `playbooks/funnel/funnel-types.md`
- `playbooks/funnel/offer-stack.md`
- `playbooks/funnel/input-spec.md`

---

## CHECK

Do not proceed past any failed check.

**1. F1 complete?**

Read `company-context/audience.md`.

Required before funnel planning:
- ICP defined with company type, headcount range, and buying trigger
- Decision-maker title named
- Specific pain in the buyer's words

If missing: "Funnel architecture without a defined ICP produces a funnel that speaks to no one. Complete F1 first."

**2. F2 complete?**

Read `company-context/offer.md`.

Required:
- Outcome statement (what the client achieves, not what you deliver)
- Mechanism name (your proprietary process has a name)
- At least one proof point with a real number, company type, and timeframe
- Price exists or price range is defined

If missing mechanism name: "Name your process before designing the funnel. A funnel without a named mechanism sells a commodity. The mechanism is what makes the VSL work."

**3. Traffic source defined?**

Ask: "Where is the traffic coming from? Cold paid ads, warm retargeting, affiliate list, organic, or cold outbound?"

This determines everything: funnel type, VSL length, trust-building required. Do not guess. Confirm.

**4. Price tier confirmed?**

Ask: "What is the front-end offer price? What is the backend price if you have one?"

Under $1K -> automated funnel is viable.
$1K-$5K -> automated funnel viable with strong proof and mechanism.
$5K+ -> route to a call. Application funnel required.

---

## DO

### Step 1: Funnel Type Selection

Using `playbooks/funnel/funnel-types.md`, select the right funnel type.

Ask the four diagnostic questions:
1. What is the offer price?
2. What is the traffic temperature (cold / warm / hot)?
3. What is the minimum trust level the buyer needs before purchasing?
4. Does this need to be affiliate-ready?

Apply the decision matrix from funnel-types.md. State the selected funnel type and the reason.

If they push back on the recommendation: show the conversion rate difference. Do not compromise on traffic-funnel matching. That is the most common failure point.

### Step 2: Offer Stack Design

Using `playbooks/funnel/offer-stack.md`, design the full price architecture.

Map each layer:

| Layer | Price | What it delivers | Job |
|-------|-------|-----------------|-----|
| Front-end / tripwire | | | Manufacture buyers |
| Order bump | | | Highest-leverage revenue per transaction |
| OTO1 | | | Identity reinforcement post-purchase |
| OTO2 / downsell | | | Recover OTO1 declines |
| Continuity | /mo | | Margin engine |
| Backend (if applicable) | | | Application-only |

Apply the ratio benchmarks from offer-stack.md:
- Order bump: 20-50% of front-end price, target 37.8% take rate
- OTO1: 51-100% of what the buyer just spent, target 16.2% take rate
- Backend: ~50x core OTO price

State the projected AOV at full-stack conversion. If it does not support the traffic cost, the economics do not work. Identify which layer to fix.

### Step 3: Conversion Targets

Set specific targets for each funnel stage before build begins.

| Stage | Target | Notes |
|-------|--------|-------|
| Opt-in rate | 25-40% warm / 10-20% cold | Depends on traffic temperature |
| VSL completion rate | 30-50% | Below 20% means hook problem |
| Purchase rate | 1-5% cold / 3-8% engaged | Model on the conservative number |
| OTO1 take rate | 16-20% | |
| Order bump take rate | 30-40% | |
| Show rate (if call) | 75-85% | With confirmation sequence |
| Close rate (if call) | 35-45% | With application filter |
| EPC | $2.00+ | If affiliate distribution planned |

### Step 4: Input Collection

Using `playbooks/funnel/input-spec.md`, run through the full pre-session checklist for the selected funnel type.

Identify every missing input. Flag each one:
- Required: cannot build this asset without it
- Recommended: build quality will suffer without it

Do not proceed to funnel-build until all Required inputs are confirmed.

### Step 5: Architecture Summary

Produce the funnel plan document:

```
FUNNEL PLAN
===========
Funnel type: [selected type]
Traffic source: [source]
Front-end price: $[X]
Offer stack: [list all layers with prices]
Projected AOV: $[X]
Affiliate-ready: [yes/no]

Conversion targets:
- Opt-in: X%
- Purchase: X%
- OTO1: X%
- [call metrics if applicable]

Assets to build (for funnel-build):
- [ ] [asset 1]
- [ ] [asset 2]
- [ ] [asset 3]

Missing inputs (must resolve before build):
- [input 1]
- [input 2]

Ready to run: funnel-build
```

---

## VERIFY

Before closing this session:

- [ ] Funnel type selected with documented reason
- [ ] Offer stack designed with all layers and prices
- [ ] Conversion targets set for each stage
- [ ] All Required inputs confirmed or flagged with a resolution plan
- [ ] Funnel plan document produced and saved to `company-context/` or the user's preferred location
- [ ] EPC target set if affiliate distribution is planned

---

## Reference files

- Funnel type decision: `playbooks/funnel/funnel-types.md`
- Price architecture: `playbooks/funnel/offer-stack.md`
- Input requirements: `playbooks/funnel/input-spec.md`
- Affiliate distribution: `playbooks/funnel/affiliate-mechanics.md`
- High-ticket backend: `playbooks/funnel/high-ticket-backend.md`
- Offer design: `playbooks/offer/README.md`
