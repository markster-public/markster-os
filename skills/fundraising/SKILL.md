---
name: fundraising
description: 'Run the Markster OS fundraising playbook. Investor ICP definition, warm and cold outreach, pitch prep, follow-up system. Structured from first contact to term sheet.'
---

You are running the Markster OS fundraising playbook.

## Workspace Context

Assume the user should run this skill from inside a Markster OS workspace.

Before relying on generic answers, look for:
- `company-context/identity.md`
- `company-context/offer.md`
- `company-context/messaging.md`
- `company-context/proof.md`
- `company-context/voice.md`

If these files exist, use them as the primary source of truth.
If they are missing or empty, tell the user to fill them in or provide the missing context directly.

If you update canonical workspace files such as `company-context/` or promoted learning-loop files, remind the user to run `markster-os validate .` before commit, and prefer validating before claiming the update is complete.

## Your archetype

Fundraising looks very different depending on your business type. Before running this playbook:

1. Read your segment file to understand which funding paths apply to your category.
2. Read `playbooks/biz-dev/fundraising/traction-by-archetype.md` -- what traction means for your archetype at each round.
3. Read `playbooks/biz-dev/fundraising/funding-mechanisms.md` -- especially if you are a service firm or trade business (non-VC paths apply).
4. Read `playbooks/biz-dev/fundraising/round-sizing.md` -- SAFE vs. convertible note vs. priced round, and how much to raise.

- `playbooks/segments/startup-archetypes/` -- SaaS, devtools, marketplace, DTC, hardware, indie
- `playbooks/segments/service-firms/` -- agency, consulting, IT/MSP, advisory (PE and SBA paths)
- `playbooks/segments/trade-businesses/` -- residential services, specialty trades, commercial (SBA, equipment financing, PE roll-up)

## Before starting

Ask the user:
1. What stage are they raising at? (Pre-seed, seed, Series A?)
2. How much are they raising?
3. What traction do they have? (ARR, customers, growth rate, key metrics)
4. Do they have warm intro paths to target investors, or are they starting cold?

Also ask which part they need help with:
- Building the investor target list
- Writing outreach (cold or warm intro requests)
- Preparing for pitch meetings
- Managing follow-up and the close process

## Stage 1: Investor target list

Help them define their investor ICP:
- Stage fit: who invests at their traction level?
- Sector fit: who has portfolio companies in their category?
- Check size: who writes the right check size for this raise?
- Value-add: who brings relevant introductions or operating experience?

Help them categorize into 3 tiers:
- Tier 1 (10-20): ideal fit, warm intro required
- Tier 2 (30-50): good fit, warm or cold
- Tier 3 (50-100): possible fit, cold only

Sources for building the list: Crunchbase, AngelList, LinkedIn, portfolio companies of target funds.

## Stage 2: Outreach

For warm intros:
- Map intro paths through LinkedIn second-degree connections
- Help them write the mutual connection request (short, specific, honest)
- Help them write the forward blurb (one paragraph, lead with traction)

For cold outreach:
- Use `playbooks/biz-dev/fundraising/templates/investor-outreach.md`
- Keep under 100 words
- Lead with traction, not vision
- Make the ask specific: 15-minute intro call

## Stage 3: Pitch preparation

Walk through the 10-slide deck structure:
1. Cover (company name, one-liner, date)
2. Problem (specific scenario, not a statistic)
3. Solution (what you built, one sentence)
4. Why now (market timing argument)
5. Traction (most compelling numbers)
6. Product (screenshots, not diagrams)
7. Business model (how you make money)
8. Market size (with logic)
9. Team (the 2-3 things that make you the right people)
10. The ask (amount, use of funds, milestones)

Also help with the verbal narrative: why you, why this market, why now.

## Stage 4: Follow-up and close

After every meeting: help write the follow-up using `playbooks/biz-dev/fundraising/templates/follow-up.md`.

For managing the process:
- Track every investor in CRM with stage, last contact, next action
- Set weekly review of all active investor relationships
- Create momentum: be transparent about other investor interest when genuine

For feedback after a pass: help write the feedback request. Their answer is the roadmap.

## Reference files

- Full playbook: `playbooks/biz-dev/fundraising/README.md`
- Outreach templates: `playbooks/biz-dev/fundraising/templates/investor-outreach.md`
- Follow-up templates: `playbooks/biz-dev/fundraising/templates/follow-up.md`
