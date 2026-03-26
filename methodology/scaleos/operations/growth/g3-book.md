# G3: Book -- Outreach & Meetings

> **North Star Metric:** 2+ qualified meetings booked per week

---

## Processes

### G3.1 Campaign Launch

| Field | Value |
|-------|-------|
| **Trigger** | Business decision to target new segment or re-engage existing |
| **Frequency** | Per-decision (roughly monthly) |
| **Input** | Target segment, prospect list, campaign thesis, email sequence templates |
| **Output** | Campaign created with prospect list, sequence, and enrollment rules |
| **Test** | Campaign live with 50+ prospects enrolled within 24 hours |

**Steps:**
1. Decide on target segment and approach (strategic decision)
2. Create or select prospect list
3. Configure email sequence templates
4. Set enrollment rules and daily limits

---

### G3.2 Prospect Enrollment

| Field | Value |
|-------|-------|
| **Trigger** | Campaign created and activated |
| **Frequency** | Continuous (daily enrollment within campaign) |
| **Input** | Campaign config, prospect list, daily enrollment limit |
| **Output** | Prospects in pipeline: research -> pitch -> review -> send |
| **Test** | Daily quota met; no duplicates; all pass ICP filter |

**Steps:**
1. Enrollment worker picks prospects from list
2. Checks exclusion rules (already contacted, opted out)
3. Dispatches research task per prospect
4. Tracks count against daily limit

**Target automation:**
- Priority-based enrollment (A-tier first from G1.3)
- Auto-pause if reply rate drops below threshold
- Auto-expand to B-tier when A-tier exhausted

---

### G3.3 Pitch Strategy Generation

| Field | Value |
|-------|-------|
| **Trigger** | Research complete for enrolled prospect |
| **Frequency** | Per-prospect |
| **Input** | Research dossier, value prop angles, campaign thesis, voice guide |
| **Output** | Personalized pitch: selected angle, email copy, subject line, follow-up sequence |
| **Test** | Pitch uses research data (not generic); matches one of the key angles; voice compliant |

**Steps:**
1. Research dossier received
2. Pitch strategist analyzes company situation
3. Selects optimal value prop angle
4. Generates personalized email with full research context
5. Email queued for human review

**Key principles:**
- Founder = peer, NOT service provider diagnosing problems
- Timeline hooks outperform problem hooks (10% vs 4.4% reply rate)
- Voice guide overrides cold email best practices
- Never email without a recent trigger (funding, hiring, event)

---

### G3.4 Pitch Review & Approval

| Field | Value |
|-------|-------|
| **Trigger** | Pitch generated and queued |
| **Frequency** | Daily batch |
| **Input** | Generated pitch, research dossier, prospect context |
| **Output** | Approved (send), edited (content override), or rejected (re-dispatch with feedback) |
| **Test** | Reviews within 24 hours; batch of 10+ per session |

**Steps:**
1. Open pitch review interface
2. Review each pitch with entity context displayed
3. Approve, edit, or reject with feedback
4. Approved pitches move to send queue
5. Rejected pitches re-dispatched with feedback

---

### G3.5 Email Sequence Execution

| Field | Value |
|-------|-------|
| **Trigger** | Pitch approved |
| **Frequency** | Continuous |
| **Input** | Approved email copy, prospect email, sequence config |
| **Output** | Email sequence executing: initial + follow-ups on schedule |
| **Test** | Delivered (not bounced); sequence timing correct; deliverability > 95% |

**Steps:**
1. Approved pitch sent to email sequencer
2. Contact created in outreach sequence
3. Initial email sent per schedule
4. Follow-up emails per sequence timing
5. Delivery status tracked

---

### G3.6 Response Handling

| Field | Value |
|-------|-------|
| **Trigger** | Reply received to outreach email |
| **Frequency** | Per-reply |
| **Input** | Reply content, prospect context, conversation history |
| **Output** | Classified response (positive/negative/question/OOO) + appropriate action |
| **Test** | Positive responses replied within 4 hours; meeting proposed within 24 hours |

**Steps:**
1. Check outreach inbox
2. Classify response type
3. Positive: draft reply with meeting proposal
4. Negative/unsubscribe: mark in sequencer
5. Question: draft informative reply
6. Update CRM if applicable

**Target automation:**
- Auto-classify replies (positive/negative/question/OOO)
- Positive replies trigger alert + draft response
- OOO auto-pauses sequence and reschedules
- Negative auto-marks and updates the prospect database

---

### G3.7 Meeting Scheduling

| Field | Value |
|-------|-------|
| **Trigger** | Positive response + meeting interest confirmed |
| **Frequency** | Per-positive-response |
| **Input** | Prospect availability, founder's calendar, meeting type, prospect research |
| **Output** | Meeting scheduled with calendar invite, agenda, prep notes |
| **Test** | Scheduled within 24 hours of positive response; 80%+ show rate |

**Target automation:**
- Scheduling link in response template
- Prospect self-schedules
- Calendar invite with agenda auto-generated from research
- Confirmation: 24h reminder + 1h reminder
- No-show triggers reschedule sequence

---

### G3.8 Campaign Performance Review

| Field | Value |
|-------|-------|
| **Trigger** | Monday (weekly cadence) |
| **Frequency** | Weekly |
| **Input** | Campaign metrics (sent, delivered, opened, replied, meetings), segment data |
| **Output** | Performance report: reply rates, meeting rates, best angles, recommendations |
| **Test** | Report every Monday; 1+ campaign adjustment per week |

**Steps:**
1. Pull campaign analytics
2. Cross-reference with CRM pipeline
3. Identify top/bottom sequences
4. Adjust strategy for next week

---

## Agent Architecture

| Agent | Status | Covers |
|-------|--------|--------|
| Campaign Launcher | Active | G3.1 |
| Enrollment Worker | Active | G3.2 |
| Pitch Strategist | Building | G3.3 |
| Email Sequencer | Active | G3.5 |
| Pitch Review UI | Active | G3.4 |
| Response Classifier | Planned | G3.6 |
| Meeting Scheduler | Not started | G3.7 |

**Build priorities:**
1. Pitch Strategist completion (G3.3)
2. Response Classifier (G3.6) -- auto-classify, draft responses
3. AI pre-review for pitches (G3.4) -- reduce review volume
4. Meeting scheduler integration (G3.7)
5. Campaign analytics expansion (G3.8) -- per-angle tracking
