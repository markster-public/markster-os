---
name: events
description: 'Run the Markster OS events playbook. Pre-event targeting, during-event conversation system, post-event follow-up. Turns conferences into pipeline.'
---

You are running the Markster OS events playbook.

## Workspace Context

Assume the user should run this skill from inside a Markster OS workspace.

Before relying on generic answers, look for:
- `company-context/audience.md`
- `company-context/messaging.md`
- `company-context/offer.md`
- `company-context/proof.md`

If these files exist, use them as the primary source of truth.
If they are missing or empty, tell the user to fill them in or provide the missing context directly.

If you update canonical workspace files such as `company-context/` or promoted learning-loop files, remind the user to run `markster-os validate .` before commit, and prefer validating before claiming the update is complete.

## Before starting

Ask the user:
1. Do they have an upcoming event in mind, or are they looking to identify which events to attend?
2. Is their F1 ICP complete? (The ICP defines which events are worth attending.)

If F1 is not complete, tell them: "The events playbook works best with a clear ICP so you can identify which events your buyers actually attend. Open `methodology/foundation/F1-positioning.md` and complete it first, then return to this playbook."

## Playbook steps

### Phase 1: Before the event

Help the user:
1. Identify target events: which events does their ICP actually attend? Ask them what they know about their ICP's conference and association habits. Prompt them to ask their best current clients.
2. Build a target contact list: 10-20 specific people they want to meet at the event. Use LinkedIn to identify likely attendees.
3. Write pre-event outreach: use `playbooks/events/templates/pre-event.md`. Send 5-7 days before the event.
4. Prepare a conversation setup: one-sentence company description, one qualifying question, and the agreed next step they will offer when the conversation goes well.

If they have an EVENT_SCOUT_KEY environment variable set, tell them they can use the Event Scout add-on to get attendee intelligence before committing to the event.

### Phase 2: During the event

Walk through the conversation framework:
1. Open by asking about them, not pitching yourself
2. Listen for ICP signals
3. When the signal appears, name it back
4. Offer a specific next step before ending the conversation (not "let's stay in touch")
5. Capture notes on your phone immediately after each conversation

### Phase 3: After the event

Help them send follow-ups:
- Timing: within 48 hours
- Reference the specific conversation (what they said, what was discussed)
- Offer something useful if applicable
- Confirm the next step that was agreed during the conversation

Use `playbooks/events/templates/post-event.md` as the starting point.

## Metrics to set up

Help them create a simple tracking spreadsheet:
- Event name, date, cost
- # target conversations planned
- # conversations had
- # follow-ups sent
- # meetings booked
- # deals opened

Review after each event to decide whether to attend again.

## Reference files

- Full playbook: `playbooks/events/README.md`
- Pre-event template: `playbooks/events/templates/pre-event.md`
- Post-event template: `playbooks/events/templates/post-event.md`
- Event Scout add-on: `addons/event-scout/README.md`
