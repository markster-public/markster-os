# Sales Proposal -- Custom Proposal Generation

## Purpose

When a prospect says "send me something," generate a polished, personalized proposal in under 10 minutes. Not a generic deck -- a document that speaks directly to their situation.

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| Company name | Yes | Founder or CRM deal |
| Contact name | Yes | Founder or CRM |
| Recommended tier | Preferred | From debrief or founder's judgment |
| Specific pain points discussed | Preferred | Deal notes, debrief output |
| Budget signals | Optional | From conversation |

## Steps

### 1. Gather Context
- Pull company data from your contact database + CRM
- Pull deal notes, conversation history
- Research company: website, recent news, current marketing/sales approach
- Identify their specific pain points and current solutions

### 2. Select Tier + Customize
- Review your service model documentation for tier details
- Review your pricing rationale
- Customize deliverables to their specific situation
- If a specific vertical (e.g. MSPs, agencies): use vertical-specific language from your ICP documentation

### 3. Build Proposal

Use the structure below:

**Sections:**
1. **Executive Summary** -- 3 sentences: their problem, your solution, expected outcome
2. **Your Situation** -- What you understand about their GTM challenges (specific to them)
3. **Our Approach** -- How your service works (Draft Mode or equivalent: what they'll see and control)
4. **What You Get** -- Tier deliverables, personalized to their priorities
5. **Timeline** -- Onboarding sprint (e.g. 14 days) then monthly engagement
6. **Investment** -- Pricing with replacement cost comparison
7. **Proof** -- Relevant case study + metrics
8. **Next Steps** -- Clear CTA (schedule onboarding kickoff)

### 4. Generate Document
- Create Google Doc or use your preferred format
- Professional formatting, scannable, mobile-friendly
- Share directly with prospect

### 5. Log + Update CRM
- Update CRM deal: stage to "Proposal Sent"
- Attach proposal link to deal
- Set follow-up task for 3 days out

## Outputs

| Output | Destination |
|--------|-------------|
| Proposal document | Google Doc or equivalent (shared with prospect) |
| Deal stage update | CRM |
| Follow-up task | CRM (3-day reminder) |

## Tools Required

| Tool | Purpose |
|------|---------|
| CRM | Deal data, stage update |
| Contact database | Company enrichment |
| Document tool | Document creation |
| Web search | Company research |
| Playbook files | Service model, pricing, ICP, proof, templates |

## Quality Gates

| Condition | Action |
|-----------|--------|
| Company revenue below your minimum threshold | Flag -- may not afford minimum tier |
| Prospect asked for specific scope not in tiers | Customize, note deviation |
| Competitor mentioned | Include competitor comparison section |
| No specific pain identified | Do not generate -- generic proposals lose |

## Agent Mapping (Optional Automation)

If using an autonomous proposal agent:

- **Trigger:** CRM deal moves to "Proposal Needed" stage, or manual trigger
- **Mode:** Generate draft proposal from CRM data, queue for founder review and personalization
- **Key difference from manual run:** Agent generates a first draft from CRM data. Founder uses the playbook to refine with conversation context the agent does not have.
