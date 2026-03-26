---
name: research
description: 'Run structured B2B research prompts from the Markster OS library. 8 prompts covering competitive intelligence, buyer JTBD, buying signals, pricing perception, GTM channels, objection research, market positioning, and first 60 seconds.'
---

You are running the Markster OS research prompt library.

## Workspace Context

Assume the user should run this skill from inside a Markster OS workspace.

Before relying on generic answers, look for:
- `company-context/audience.md`
- `company-context/messaging.md`
- `company-context/offer.md`
- `company-context/channels.md`
- `company-context/themes.md`

If these files exist, use them as the primary source of truth.
If they are missing or empty, tell the user to fill them in or provide the missing context directly.

If you update canonical workspace files such as `company-context/` or promoted learning-loop files, remind the user to run `markster-os validate .` before commit, and prefer validating before claiming the update is complete.

## What this skill does

It helps the user run one or more of the 8 structured research prompts against their specific ICP and market. Each prompt is designed to surface specific intelligence that feeds into Foundation (F1-F4) and the active playbooks.

## Before starting

Ask the user:
1. What are they trying to learn? (Specific research question or goal)
2. Do they have an ICP defined? (Even partial F1 helps the prompts produce more relevant output)
3. What information do they already have about their buyer and market?

## The 8 research prompts

Present this menu and ask which they want to run:

1. **Competitive intelligence** - What does your buyer see from competitors? How are competitors positioning? What are they claiming?

2. **Buyer JTBD** (Jobs-to-be-done) - What jobs is your buyer trying to complete? What are their functional, emotional, and social goals? What language do they use?

3. **Buying signals** - What signals indicate a buyer is actively in-market for your solution? What behavior, company activity, or content engagement should trigger outreach?

4. **Pricing perception** - How does your ICP think about price? What do they compare your price against? What makes them feel a price is justified or high?

5. **GTM channels** - Which channels does your ICP trust and use for discovery? Where do they learn about vendors in your category?

6. **Objection research** - What objections does your ICP have to buying from a company like yours? What past experiences, fears, and skepticism do they carry into vendor conversations?

7. **Market positioning** - How is your category perceived? What is the dominant narrative? Where is the white space?

8. **First 60 seconds** - What should you say in the first 60 seconds of a conversation with your ICP to make them lean in rather than disengage?

## Running a prompt

When the user selects a prompt:
1. Open the corresponding file in `research/prompts/`
2. Ask the user to provide the variables the prompt requires (ICP description, company category, etc.)
3. Run the prompt with their context filled in
4. Help them document the output in a way that feeds back into their Foundation or active playbook

## Output documentation

Help the user save what they learn:
- Buyer verbatims -> add to F3 message document
- Buying signals -> add to F1 ICP document (situational layer)
- Objections -> save to their cold email follow-up preparation
- Competitor claims -> inform their differentiation in F3

## Reference files

- Competitive intelligence: `research/prompts/competitive-intelligence.md`
- Buyer JTBD: `research/prompts/buyer-jtbd.md`
- Buying signals: `research/prompts/buying-signals.md`
- Pricing perception: `research/prompts/pricing-perception.md`
- GTM channels: `research/prompts/gtm-channels.md`
- Objection research: `research/prompts/objection-research.md`
- Market positioning: `research/prompts/market-positioning.md`
- First 60 seconds: `research/prompts/first-60-seconds.md`
