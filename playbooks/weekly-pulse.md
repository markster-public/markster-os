# Weekly Pulse -- Business Health Check

## Purpose

Replace "am I on track?" anxiety with a data-driven weekly assessment. Shows pipeline health, revenue progress vs your targets, what's working, what's stalling, and what to focus on next week.

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| None | -- | All data pulled from systems |

## Steps

### 1. Revenue Check
- Pull current MRR from your CRM (deal values, recurring)
- Compare to last recorded MRR
- Compare to your ARR milestones
- Calculate: on track / behind / ahead

### 2. Pipeline Health
- Pull all active deals from your CRM
- Categorize by stage: Discovery, Proposal, Negotiation, Closed
- Flag stale deals (>14 days no activity) and deals missing next steps
- Calculate weighted pipeline value

### 3. Activity Metrics
- Outbound sent
- Replies received
- Meetings booked
- Proposals sent
- Deals closed
- Content published (LinkedIn posts, blog)

### 4. What's Working / Not Working
- Top performing campaign (by reply rate)
- Best source of new conversations
- Stalled deals and why
- Content that got traction

### 5. Generate Report

```
--- WEEKLY PULSE ---
Week of [date]

REVENUE
- MRR: $[X] (target: $[Y] by [milestone date])
- Status: [On track / Behind / Ahead]
- Net change: [+/- $X from last week]

PIPELINE
- Active deals: [N] ($[total weighted value])
- New this week: [N]
- Moved forward: [N]
- Stalled (>14 days): [N] -- needs attention
- Closed this week: [N]

ACTIVITY
- Outbound sent: [N]
- Replies: [N] ([X]% reply rate)
- Meetings booked: [N]
- Proposals sent: [N]
- LinkedIn posts: [N]

WINS
- [What worked this week]

CONCERNS
- [What's stalling or needs attention]

NEXT WEEK PRIORITIES
1. [Priority 1 -- specific action]
2. [Priority 2 -- specific action]
3. [Priority 3 -- specific action]
--------------------
```

### 6. Update Metrics
- Update your metrics tracking file if MRR or client count changed
- Log the week's summary to your activity log

## Outputs

| Output | Destination |
|--------|-------------|
| Weekly pulse report | Founder review |
| Updated metrics | Your metrics tracking file (if changes) |
| Log entry | Activity log |

## Tools Required

| Tool | Purpose |
|------|---------|
| CRM | Revenue, pipeline, deals, activities |
| Outreach sequencing tool | Outreach metrics |
| Contact database | Contact/enrichment stats |
| Playbook files | metrics, ARR milestones |

## Agent Mapping (Optional Automation)

If using an autonomous monitoring agent:

- **Trigger:** Every Monday morning (e.g. 7am local time)
- **Mode:** Generate weekly pulse, deliver via Slack DM or email to founder
