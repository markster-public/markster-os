---
name: funnel-sprint
description: Quick single-ICP funnel builder. Takes your ICP and offer and produces a complete conversion pathway: landing page copy, lead magnet spec, and 3-email nurture sequence. Use when you need a functional funnel fast without the full architecture session. Triggers on "quick funnel", "simple funnel", "lead magnet funnel", "landing page for", "nurture sequence", "opt-in funnel".
---

# Funnel Sprint - ACTIVATED

You are building a fast, functional mini-funnel for one ICP segment.

This skill produces a working funnel, not a comprehensive architecture. For full offer stack design, funnel type selection, and VSL scripting, use `funnel-plan` + `funnel-build` instead.

---

## CHECK

Do not proceed past any failed check.

**1. ICP defined?**

Ask: "Who exactly is this funnel for? Give me the company type, headcount range, decision-maker title, and the one pain that makes them a buyer right now."

If the answer is "businesses" or "anyone who needs marketing" - stop. That is not an ICP. A funnel built for everyone converts no one.

**2. Offer exists?**

Ask: "What do they get? Give me the outcome in one sentence with a real number or timeframe."

Acceptable: "We help 10-person agencies add 5-8 qualified calls per month in 60 days."
Not acceptable: "We help businesses grow."

If no outcome statement with a number - route to `playbooks/funnel/README.md` and `playbooks/offer/README.md` first.

**3. At least one proof point?**

Ask: "What is your best result with a client? Company type, what happened, how long it took."

No proof = no lead magnet credibility = low opt-in rates. If they have nothing, the funnel can be built but flag this as the primary conversion risk.

---

## DO

### Step 1: Lead Magnet Design

Based on their ICP pain, select the lead magnet format:

| ICP pain type | Best format |
|---------------|------------|
| "I don't know if I'm doing X right" | Audit or scorecard |
| "I don't know how to compare options" | Calculator or comparison tool |
| "I need a repeatable process for X" | Checklist or SOP template |
| "I want to see what good looks like" | Case study or before/after example |
| "I need to learn X fast" | Short video training (under 20 min) |

Write the lead magnet specification:
- Format (PDF, video, tool)
- Title (specific promise in 8 words or less)
- What it delivers (one concrete output the user walks away with)
- How it creates appetite for the core offer (Salty Pretzel Rule: it solves problem A while making problem B visible)

### Step 2: Landing Page Copy

Write the full landing page. Every section required.

**Hero:**
```
Headline: [Specific outcome for specific person in 10 words or less]
Sub-headline: [What they get + what they do not have to do]
CTA button: [Action verb + what happens] e.g. "Get the Free Audit"
```

**The Problem (3 bullets, in buyer's words):**
- [Pain point 1 - financial or operational]
- [Pain point 2 - emotional or time cost]
- [Pain point 3 - what they've already tried that didn't work]

**The Solution:**
[What the lead magnet delivers, step by step. 3-4 sentences max.]

**Proof:**
[One result. Company type + outcome + timeframe. If no proof: "Here's what the [lead magnet] covers:" and list 3-4 specific outputs.]

**How It Works:**
1. [Step 1 - what they do]
2. [Step 2 - what they get]
3. [Step 3 - what happens next]

**CTA:**
[Repeat the button. Add a single line of friction removal: "No credit card. No sales call. Just [what they get]."]

Rules:
- No em dashes
- Sentences under 20 words
- One idea per sentence
- No jargon ("leverage," "solutions," "synergy," "optimize")
- Headline must pass the Stranger Test: someone unfamiliar can explain it in 10 seconds

### Step 3: 3-Email Nurture Sequence

**Day 0 - Delivery**
Subject: [Lead magnet title] for [Company] is ready
Body: Deliver what was promised. One observation relevant to their situation. Under 150 words.
CTA: "Reply if you have a question about [specific section]."

**Day 3 - Proof**
Subject: How [similar company type] [specific result they want]
Body: One proof story. Company type + what changed + real number + timeframe. Under 150 words.
CTA: "Want me to walk you through how this would work for [Company]?"

**Day 7 - Offer**
Subject: Next step for [Company]
Body: Reference their lead magnet result + the Day 3 case study. One sentence transition to the offer. Under 100 words.
CTA: Direct CTA to the core offer or booking link.

Writing rules for all emails:
- Plain text format (not HTML)
- No unsubscribe friction in the body (let the footer handle it)
- First word of the email is not "I"
- No "just checking in"

---

## VERIFY

Before closing this session:

- [ ] Lead magnet title passes the Stranger Test (specific promise, under 8 words)
- [ ] Landing page headline names the ICP and the outcome
- [ ] Proof section uses real numbers (company type + outcome + timeframe)
- [ ] All three emails written with specific CTAs
- [ ] Day 7 email links to a real next step (booking link, offer page, or application)
- [ ] No generic phrases: "leverage," "solutions," "optimize," "game-changing"

---

## Reference files

- Full funnel architecture: `playbooks/funnel/README.md`
- Funnel type selection: `playbooks/funnel/funnel-types.md`
- Input requirements: `playbooks/funnel/input-spec.md`
- Offer design: `playbooks/offer/README.md`
