---
name: funnel-builder
description: Mini-funnel generator. Takes an ICP segment and creates a complete conversion pathway -- landing page copy, lead magnet spec, email nurture sequence, and CTA. Use when building a new funnel for an ICP segment or lead magnet. Triggers on "build funnel", "landing page", "lead magnet", "nurture sequence", "conversion path".
---

# Funnel Builder -- ACTIVATED

You are building a complete mini-funnel for an ICP segment.

---

## Input

Ask for:
1. Target ICP segment (IT/MSP, Agencies, Professional Services, or custom)
2. Lead magnet type preference (audit/quiz, calculator, video, PDF guide)
3. Landing page URL slug

---

## Process

1. **Select proof points** -- match existing case study proof to the ICP
2. **Design lead magnet** -- format, questions/inputs, scoring, output
3. **Write landing page copy** -- hero, problem, solution, proof, CTA
4. **Write nurture sequence** -- 3 emails (Day 0: results delivery, Day 3: case study, Day 7: main CTA)
5. **Define technical requirements** -- form, workflow, email templates

---

## Landing Page Structure

Every funnel landing page must follow this structure:

```
## HERO
[One sentence: who it's for and what they get]
[Sub-headline: the pain you're removing]
[CTA button]

## THE PROBLEM
[3 bullets: specific pain points in their language]

## THE SOLUTION
[What they receive, step by step]

## PROOF
[One case study result, specific numbers]

## HOW IT WORKS
1. [Step 1]
2. [Step 2]
3. [Step 3]

## CTA
[Action they take + what happens next]
```

## Nurture Sequence (3 Emails)

### Day 0: Results Delivery
- Subject: [lead magnet result] for [Company]
- Body: Deliver what was promised. No pitch. Add one observation.
- CTA: "Reply if you have a question."

### Day 3: Case Study
- Subject: how [similar company] [result they want]
- Body: One proof story, specific and short. Match their industry.
- CTA: "Want me to walk you through how this would work for [Company]?"

### Day 7: Main Offer CTA
- Subject: next step for [Company]
- Body: Transition to the offer. Reference their lead magnet results + the case study.
- CTA: Direct offer CTA

---

## Output

- Landing page copy (ready for CMS)
- Lead magnet specification (inputs, outputs, scoring)
- 3-email nurture sequence with actual copy
- CRM workflow description (form -> tag -> sequence -> deal creation)

---

## Rules

- Landing page must communicate the offer without JavaScript (graceful degradation)
- Every claim needs a source (case study, proof point, or "results will vary")
- Include a "how it works" section on every landing page -- buyers want process clarity
