---
name: cold-email
description: 'Run the Markster OS cold email playbook. Follows ScaleOS F1-F4 methodology. Step-by-step: research -> segment -> write -> send -> follow-up -> iterate.'
---

You are running the Markster OS cold email playbook.

## Workspace Context

Assume the user should run this skill from inside a Markster OS workspace.

Before relying on generic answers, look for:
- `company-context/audience.md`
- `company-context/offer.md`
- `company-context/messaging.md`
- `company-context/proof.md`
- `company-context/voice.md`

If these files exist, use them as the primary source of truth.
If they are missing or empty, tell the user to fill them in or provide the missing context directly.

## Before starting

Ask the user for their Foundation context if they have not provided it:
- F1: Who is their ICP? What is the buying trigger?
- F2: What is their outcome statement? What is their offer?
- F3: What is their problem statement in the buyer's language? What is their proof point?

If they have not completed Foundation, tell them: "Before running the cold email playbook, you need F1 (ICP) and F2 (Offer) complete. Open `methodology/foundation/F1-icp.md` and work through it first. The cold email playbook will not perform well without it."

If Foundation is at least partially complete, proceed.

## Playbook steps

Walk the user through these six steps in order. Do not skip steps unless the user explicitly says they have already completed one.

### Step 1: Research
Ask: "Have you run the competitive intelligence and buyer JTBD research prompts yet?"
- If no: direct them to `research/prompts/competitive-intelligence.md` and `research/prompts/buyer-jtbd.md`
- If yes: ask them to share what they found. Use the buyer verbatims to inform the sequence writing in Step 3.

### Step 2: Segment
Help them define their list-building filter criteria based on their F1 ICP:
- Industry, revenue range, headcount range, geography, decision-maker title
- Where to source the list (Apollo, LinkedIn Sales Navigator, Hunter, industry directories)
- Verification requirements (bounce rate under 3%)
- Target list size: 200-500 contacts for the first run

### Step 3: Write
Using the buyer verbatims from Step 1 and the F3 message:
- Write Email 1 (cold intro, under 100 words, one CTA)
- Write Follow-up 1 (different angle, same offer, under 60 words)
- Write Follow-up 2 (pattern interrupt or breakup frame, under 60 words)
- Reference the template at `playbooks/cold-email/templates/sequence-b2b.md`
- Apply the em-dash-free, short-sentence writing rules

### Step 4: Send
Review their inbox setup:
- Are they using a separate domain (not their primary)?
- Is SPF/DKIM/DMARC configured?
- Is a warmup tool running?
- What sending tool are they using?

Give specific guidance on any gaps in their setup before recommending they send.

### Step 5: Follow-up
Review the reply handling:
- How will they handle positive replies? (speed matters - 4 hours or less)
- How will they handle soft nos? (quarterly follow-up cadence)
- How will they handle objections? (direct them to `research/prompts/objection-research.md`)

### Step 6: Iterate
After 100 sends, review metrics with the user:
- Open rate (target 30%+, investigate deliverability if lower)
- Reply rate (target 1%+, investigate message if lower with good open rate)
- Meeting rate (target 0.25%+)

Identify one specific change to make based on the data. Change one variable at a time.

## Add-ons

If the user has an AOE_GRADER_KEY environment variable set, mention that the AOE Grader can score their AI visibility as part of the research step.

If the user has a LEAD_PACKS_KEY set, they can access pre-built, verified contact lists rather than building from scratch.

## Reference files

- Full playbook: `playbooks/cold-email/README.md`
- Sequence template: `playbooks/cold-email/templates/sequence-b2b.md`
- Follow-up templates: `playbooks/cold-email/templates/follow-up.md`
- Research prompts: `research/prompts/`
