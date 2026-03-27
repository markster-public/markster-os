---
id: company-context-readme
title: Company Context Pack
type: reference
status: active
owner: company
created: 2026-03-26
updated: 2026-03-26
tags: [company-context, brand, voice, messaging]
---

# Company Context Pack

This folder is the canonical business context for Markster OS skills.

Skills should read from this folder when they need:

- company identity
- ICP and audience context
- offer and pricing context
- messaging and positioning
- voice rules
- approved proof
- channel-specific guidance
- recurring themes
- style corrections
- truth and quality rules

## Operating Rules

## Rule 1: Canon only

This folder is canonical.

Skills may read these files directly.
Skills must not treat raw notes, transcripts, or inbox material as canonical.

## Rule 2: Fixed file set

Only files listed in `manifest.json` are allowed in this folder unless the validator is updated first.

## Rule 3: Human-readable first

The content should be easy for a founder or operator to edit directly.
Do not turn these files into database dumps.

## Rule 4: Specificity over slogans

Every file should prefer:

- concrete claims
- real examples
- explicit unknowns
- operational language

Avoid generic brand language.

## Rule 5: Promotion only

If a conversation or draft reveals a better objection, proof point, or style correction, promote it through the learning loop.
Do not paste raw conversation content into canon.

## Files

- `identity.md`: what the company is, is not, and wants to be known for
- `audience.md`: ICP, situations, pains, buying triggers, objections
- `offer.md`: offer, pricing logic, entry offer, risk reversal
- `messaging.md`: one-liners, differentiators, problem framing, key claims
- `voice.md`: tone, sentence rules, phrasing preferences, bans
- `proof.md`: approved proof assets and approved claims
- `channels.md`: how the message shifts by channel
- `themes.md`: recurring topics and narrative lanes
- `style-corrections.md`: repeated editorial corrections
- `truth-rules.md`: no-fabrication rules and claim taxonomy
- `quality-checklist.md`: final QA gate for generated assets

## Fill Order

If this is a new workspace, fill these first:

1. `identity.md`
2. `audience.md`
3. `offer.md`
4. `messaging.md`

Then complete:

5. `voice.md`
6. `proof.md`
7. `channels.md`
8. `themes.md`

Use `truth-rules.md` and `quality-checklist.md` as the hard gate while you fill the rest.
