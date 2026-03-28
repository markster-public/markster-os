# Campaign Builder -- End-to-End Outreach Campaigns

## Purpose

Design and launch a complete outreach campaign from segment definition to live sequences. Handles the full pipeline: who to contact, what to say, how to sequence, how to measure.

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| Target segment | Yes | e.g. "Bay Area MSPs", "waitlist tier 1", "SF agencies" |
| Campaign goal | Preferred | "Book meetings", "activate waitlist", "event follow-up" |
| Volume | Preferred | How many contacts to target |
| Timeline | Preferred | When to launch, how long to run |

## Steps

### 1. Define Segment
- Read your ICP qualification criteria
- Review available segment data
- Pull contacts from your contact database matching criteria
- Exclude: existing clients, active deals, recently contacted, opted out

### 2. Research + Enrich
- Batch enrich contacts via your contact enrichment tool
- Verify emails (e.g. Reoon, Findymail, or equivalent)
- Score ICP fit per contact
- Tier: A (perfect fit), B (good fit), C (marginal)
- Drop C-tier unless volume needed

### 3. Design Sequence

Read `cold-email/templates/outreach-sequence.md` for format.

**Standard 5-touch sequence:**

| Touch | Day | Channel | Purpose |
|-------|-----|---------|---------|
| 1 | Day 0 | Email | Value-first intro -- pain + proof |
| 2 | Day 2 | LinkedIn | Connection request with context |
| 3 | Day 4 | Email | Different angle -- case study or data |
| 4 | Day 8 | Email | Objection pre-handle + soft CTA |
| 5 | Day 14 | Email | Break-up -- "should I stop reaching out?" |

**Messaging sources:**
- Touch 1: Your core messaging (5-second intro adapted for email)
- Touch 3: Relevant case studies or results
- Touch 4: Pre-handle the top objection for this segment
- Touch 5: Break-up template from `cold-email/templates/outreach-sequence.md`

### 4. Personalization Layer
- For each contact: 1-2 personalized lines referencing their company/situation
- Use enrichment data + web research
- Minimum: company name + industry-specific pain point
- Ideal: recent news, LinkedIn activity, or mutual connection

### 5. Campaign Setup
- Create campaign in your outreach sequencing tool
- Upload contact list
- Configure sequence with templates
- Set daily send limits (25-50 per mailbox)
- Configure tracking

### 6. Launch + Monitor
- Launch campaign
- Monitor deliverability (bounce rate, spam rate)
- Track: open rate, reply rate, meeting booked rate
- Adjust messaging after first 50 sends based on data

## Outputs

| Output | Destination |
|--------|-------------|
| Campaign brief | Your campaign records |
| Contact list (qualified) | Outreach sequencing tool |
| Email sequence (5 touches) | Outreach sequencing tool |
| LinkedIn messages | Draft or scheduled |
| Campaign tracking | Outreach analytics |
| CRM sync | Contacts + deals created from replies |

## Tools Required

| Tool | Purpose |
|------|---------|
| Contact database | Contact sourcing, enrichment, verification |
| Outreach sequencing tool | Campaign creation, sequence setup |
| CRM | Deal creation from warm replies |
| Playbook files | ICP, messaging, objections, proof, templates |

## Quality Gates

| Condition | Action |
|-----------|--------|
| < 70% email verification rate | Re-enrich before sending |
| Segment has < 50 qualified contacts | Expand criteria or combine segments |
| Reply rate < 1% after 100 sends | Pause, rewrite messaging |
| Bounce rate > 5% | Check infrastructure, pause campaign |
| Prospect replies with objection | Route to follow-up workflow or handle directly |

## Agent Mapping (Optional Automation)

If using an autonomous outreach agent:

- **Trigger:** Weekly campaign cycle, or new segment identified
- **Mode:** Full pipeline -- source contacts, enrich, personalize, create sequence, queue for approval
- **Key difference from manual run:** Agent handles the entire pipeline autonomously. Manual use is for one-off or strategic campaigns with custom targeting.
