# Event Scout - Event Intelligence

Find the events where your ICP is actually attending. Get attendee signals, speaker lists, and sponsor intel before committing to registration.

---

## What it does

Event Scout gives you intelligence on upcoming events in your ICP's category before you register - so you know whether the event is worth attending, who will be there, and how to prioritize your pre-event outreach.

**What you get:**

- Upcoming events matched to your ICP profile (industry, company size, geography, role)
- Estimated attendee composition (seniority, company size distribution, role breakdown)
- Speaker list with LinkedIn profiles (speakers are pre-identified ICP targets)
- Sponsor list (who is paying to be there - often signals high-concentration ICP presence)
- Historical event data: past attendance volume, year-over-year growth, format (in-person / virtual / hybrid)
- Pre-event outreach list: known attendees who match your ICP filter (where available)

---

## Why it matters

The events playbook depends on choosing the right events. Attending an event where 20% of attendees match your ICP is 5x less productive than attending one where 80% do.

Event Scout answers the question before you pay registration fees: is my ICP actually there?

---

## Integration with skills

When `EVENT_SCOUT_KEY` is set, the events skill gains intelligence features:

| Feature | What it does |
|---------|-------------|
| Event discovery | Finds upcoming events matched to your F1 ICP profile |
| Attendee intelligence | Returns known attendees who match your ICP filter |
| Pre-event outreach list | Identifies contacts to reach out to before the event |
| ROI estimate | Historical conversion data: expected meetings per event type |

---

## Setup

**Step 1: Get a key**

Sign up at [markster.ai/addons/event-scout](https://markster.ai/addons/event-scout).

Free tier: 10 event lookups per month (no attendee data).
Paid plans: from $79/month for full attendee intelligence + pre-event contact lists.

**Step 2: Set the environment variable**

```bash
export EVENT_SCOUT_KEY="your_key_here"
```

**Step 3: Use it in the events skill**

In your AI environment:

```
/events
```

When asked about which events to attend, the skill will query Event Scout with your ICP profile and return a ranked list of upcoming events with intelligence summaries.

---

## Sample output

```
EVENT SCOUT RESULTS - [Date range]
ICP: [your ICP filter]

Top events for your ICP:

1. [Event Name] - [City, Date]
   Format: In-person
   Estimated attendance: 800-1,200
   ICP match rate: ~65% (based on past attendee data)
   Speakers matching ICP: 12 identified
   Sponsors in your category: 4
   Pre-event contacts available: 47 matching your ICP filter
   ROI estimate: 8-15 qualified conversations per event day

2. [Event Name] - [City, Date]
   Format: In-person
   Estimated attendance: 300-450
   ICP match rate: ~80% (smaller, more targeted)
   Speakers matching ICP: 6 identified
   Pre-event contacts available: 22
   ROI estimate: 6-10 qualified conversations

Recommendation: [Event 2] has higher ICP concentration despite lower volume.
```

---

## Questions

Event Scout support: addons@markster.ai
Docs: [markster.ai/docs/event-scout](https://markster.ai/docs/event-scout)
