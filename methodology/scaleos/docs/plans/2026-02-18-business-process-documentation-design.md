---
id: biz-process-maps-v1
title: Business Process Maps
type: design
status: draft
owner: founder
created: 2026-02-18
updated: 2026-02-18
tags: [scaleos, bpmn, processes, documentation, revenue]
---

# Business Process Maps

BPMN-style process documentation. Every step has typed inputs and outputs.
Decision gateways have explicit conditions. Lanes show who acts.

---

## Process Inventory

### End-to-End Revenue Processes

| ID | Process | Trigger | Blocks Involved | Current State |
|----|---------|---------|-----------------|---------------|
| P1 | Outbound Campaign Execution | Signal or scheduled | G1.1->G1.2->G1.3->G1.6->G3.1->G3.2->G3.3->G3.4->G3.5->G3.6->G3.7 | Operational |
| P2 | Event Intelligence & Activation | Weekly scan | G1.4->[attendee]->G1.2->G1.3->[brief] | Partially built |
| P3 | Content Production Cycle | Friday weekly | G2.1->G2.2->G2.3->G2.5->G2.6->G2.7->G2.8->G2.12 | Operational |
| P4 | Inbound Lead Processing | Engagement signal | [capture]->G1.2->G1.3->[outreach or nurture] | Manual |
| P5 | Sales & Close | Meeting completed | [qualify]->[proposal]->[close]->D1.1 | Manual |
| P6 | Client Onboarding | Deal closed | D1.1->D1.2->[product setup] | Manual |
| P7 | Client Monthly Delivery | Monthly cadence | D1.3->D1.4->D1.5->D1.6->D2.1 | Manual |
| P8 | Case Study & Proof Creation | Result milestone | D2.1->D2.2->D2.3->D2.4->D2.5 | Manual |
| P9 | Client Retention & Expansion | Health check | D3.1->D3.2->D3.3->D3.4->D3.5 | Manual |

### Sub-Processes (reusable, called by parent processes)

| ID | Sub-Process | Called By | Blocks |
|----|-------------|-----------|--------|
| SP1 | Data Enrichment Pipeline | P1, P2, P4 | G1.2 |
| SP2 | ICP Scoring | P1, P2, P4 | G1.3 |
| SP3 | Prospect Research | P1, P2 | G1.6 |
| SP4 | Voice-Matched Content Generation | P3 | G2.3+G2.5 |

### Foundation Processes (periodic)

| ID | Process | Trigger | Blocks |
|----|---------|---------|--------|
| FP1 | ICP & Positioning Review | Quarterly | F1.1->F1.2->F1.3->F1.4 |
| FP2 | Business Model Review | Quarterly | F2.1->F2.2->F2.3->F2.4 |
| FP3 | Financial Review Cycle | Weekly/Monthly | F4.1->F4.2->F4.3->F4.5 |

### Operations Processes

| ID | Process | Trigger | Blocks |
|----|---------|---------|--------|
| OP1 | Process Documentation & Automation | New process identified | O1.2->O2.1->O2.2 |
| OP2 | System Health & Monitoring | Daily | O2.5->O2.3->O1.3 |
| OP3 | Weekly Business Review | Monday | O3.1->O3.2->G1.7->G3.8->G2.12 |

---

## P1: Outbound Campaign Execution

```
TRIGGER: Signal detected (funding round, hiring surge, event attendance)
         OR scheduled prospecting cycle (weekly)
END:     Meeting booked OR prospect exhausted

--- LANE: Founder ---

[1] Define campaign parameters                         <- G3.1
    Input:  ICP definition (from F1.1)
            Wedge strategy (from F1.4)
            Trigger signal or segment criteria
    Output: Campaign brief {
              segment_name: string,
              target_persona: string,
              angle: enum(revenue_infrastructure | partner | peer |
                          event_connection | signal_timing |
                          case_study_proof | tool_consolidation |
                          quick_win | community_build | growth),
              channel: enum(email_only | linkedin_email | event_email),
              cohort_size: int (25-50),
              sequence_length: int (3-5 steps),
              sequence_timing: int[] (e.g. [1,3,7,14]),
              hook_type: enum(timeline | problem | mutual | trigger)
            }
    Tool:   campaign launcher, campaign builder

--- LANE: Automation (Contact Database) ---

[2] Build prospect list                                <- G1.1
    Input:  Campaign brief -> ICP criteria
            Existing prospect database records
            External sources if needed
    Output: Raw prospect list [{
              name: string,
              company: string,
              title: string,
              email: string?,
              linkedin_url: string?,
              source: enum(internal | csv_import | local_data_source)
            }]
    Tool:   prospect list builder, CSV import, local lead importer

    GATEWAY: List size >= cohort_size?
      NO  -> expand criteria or add external sources -> loop [2]
      YES -> continue

[3] -> CALL SP1: Data Enrichment Pipeline              <- G1.2
    Input:  Raw prospect list
    Output: Enriched prospect list

[4] -> CALL SP2: ICP Scoring                           <- G1.3
    Input:  Enriched prospect list + ICP rubric (from F1.1)
    Output: Scored prospect list [{
              ...enriched_fields,
              icp_score: int (0-100),
              tier: enum(hot | warm | cold | disqualified),
              scoring_breakdown: {criterion: score}[]
            }]

    GATEWAY: Tier check per prospect
      HOT/WARM -> enroll in campaign
      COLD     -> park (may revisit later)
      DISQUALIFIED -> discard

--- LANE: Automation (Outreach Agent) ---

[5] Enroll qualified prospects                         <- G3.2
    Input:  Qualified prospects (hot + warm)
            Campaign definition
    Output: Enrolled prospect records
    Tool:   Campaign Enrollment Worker (automated)

[6] -> CALL SP3: Prospect Research                     <- G1.6
    Input:  Enrolled prospect record
    Output: Research brief {
              company_analysis: string,
              person_analysis: string,
              signals: string[],
              why_now: string,
              timing_rationale: string,
              connection_angles: [{angle: string, evidence: string}],
              recommended_approach: string
            }
    Tool:   Research Squad (automated)

[7] Generate personalized pitch                        <- G3.3
    Input:  Research brief (from [6])
            Campaign brief (from [1])
            Voice guide (from F1.6)
    Output: Pitch sequence {
              prospect_id: string,
              subject_lines: string[],
              body_texts: string[],
              value_prop_angle: string,
              hook: string,
              personalization_notes: string,
              sequence_steps: [{
                step_num: int,
                day: int,
                subject: string,
                body: string,
                purpose: enum(open | value | proof | breakup)
              }]
            }
    Tool:   Pitch Strategist agent (semi-automated)
    Rules:  - Timeline hooks > problem hooks
            - Specific observations > generic templates
            - Warm, honest, soft CTA
            - Conversational ask > hard close

--- LANE: Founder ---

[8] Review & approve pitch                             <- G3.4
    Input:  Generated pitch sequence
            Prospect context (research brief)
    Output: Decision {
              status: enum(approved | edited | rejected),
              edited_sequence?: pitch_sequence,
              rejection_feedback?: string
            }
    Tool:   Review UI

    GATEWAY: Decision?
      APPROVED -> continue
      EDITED   -> continue with edits
      REJECTED -> feedback sent -> loop [7] with feedback

    HARD RULE: Nothing sends without explicit approval.

--- LANE: Automation (Email Sequencer) ---

[9] Execute email sequence                             <- G3.5
    Input:  Approved pitch sequence
            Verified prospect email
    Output: Execution record {
              emails_sent: [{step: int, sent_at: datetime, status: string}],
              sequence_status: enum(active | completed | stopped)
            }
    Tool:   Email Executor
    Timing: Per sequence_timing from campaign brief (e.g. Day 1,3,7,14)

--- LANE: External (Prospect) ---

[10] Response received (or sequence exhausted)         <- G3.6

    GATEWAY: Response type?
      POSITIVE (interested)  -> [11]
      OBJECTION              -> [11b] handle manually, may re-engage
      NEGATIVE / UNSUBSCRIBE -> END {status: "removed"}
      NO REPLY (all steps)   -> END {status: "exhausted", action: "nurture_list"}

--- LANE: Founder ---

[11] Schedule meeting                                  <- G3.7
    Input:  Positive response, prospect context
    Output: Meeting record {
              prospect_id: string,
              meeting_datetime: datetime,
              meeting_type: enum(discovery | demo | follow_up),
              prep_brief: string
            }
    Tool:   Calendar Scheduler, /prospect-brief skill

    -> TRIGGERS: P5 (Sales & Close)
    -> FEEDS: O3.2 (Pipeline Value Tracking)

END: Meeting booked
```

---

## P2: Event Intelligence & Activation

```
TRIGGER: Weekly scan schedule OR manual event category search
END:     Pre-event brief delivered + post-event contacts captured

--- LANE: Founder ---

[1] Configure scan parameters                          <- G1.4
    Input:  Target cities
            Event types (tech, startup, AI, SaaS, etc.)
            ICP keywords
            Date range
    Output: Scan config {
              cities: string[],
              keywords: string[],
              platforms: string[],
              date_range: {start: date, end: date}
            }
    Tool:   Event Scout CLI

--- LANE: Automation (Event Scout) ---

[2] Scrape events across platforms                     <- G1.4
    Input:  Scan config
    Output: Raw events [{
              title: string,
              date: datetime,
              url: string,
              venue: string?,
              description: string,
              source: string,
              city: string,
              format: enum(in_person | virtual | hybrid)
            }]
    Tool:   Event Scout scraper pipeline

[3] Score events against ICP                           <- G1.4
    Input:  Raw events + ICP keywords + scoring rubric
    Output: Scored events [{
              ...event_fields,
              relevance_score: float (0-5),
              format_score: float (0-5),
              total_score: float,
              tier: enum(T1 | T2 | T3 | No-Go)
            }]
    Logic:  T1 (>=4.0) = must attend
            T2 (>=3.0) = worth attending
            T3 (>=2.0) = optional
            No-Go (<2.0) = skip

    GATEWAY: Event tier?
      T1/T2 -> continue to activation
      T3    -> logged, no activation
      No-Go -> logged, no activation

[4] Extract attendees (where supported)
    Input:  T1/T2 event URL
    Output: Attendee list [{
              name: string,
              company: string?,
              title: string?,
              social_url: string?,
              rsvp_status: string?,
              dedup_key: string (hash of name+event)
            }]
    Note:   Not all platforms support attendee extraction.
            Pipeline NEVER breaks due to missing attendees.

    GATEWAY: Attendees found?
      YES -> continue to enrichment
      NO  -> [4b] Event logged without attendees -> END {partial}

[5] -> CALL SP1: Data Enrichment Pipeline              <- G1.2
    Input:  Attendee list (as raw contacts)
    Output: Enriched attendees

[6] -> CALL SP2: ICP Scoring                           <- G1.3
    Input:  Enriched attendees + ICP rubric
    Output: Scored attendees with tiers

    GATEWAY: Any hot/warm attendees?
      YES -> continue to brief generation
      NO  -> END {event_logged, no_targets}

--- LANE: Automation ---

[7] Generate pre-event brief
    Input:  Event details (title, date, venue, description)
            Scored attendees (hot + warm only)
            Research briefs (if available, from SP3)
    Output: Pre-event brief {
              event_summary: string,
              date: datetime,
              venue: string,
              attendee_profiles: [{
                name: string,
                company: string,
                title: string,
                icp_score: int,
                talking_points: string[],
                connection_angles: string[]
              }],
              recommended_approach: string
            }
    Tool:   /event-prep skill

[8] Deliver brief
    Input:  Pre-event brief
    Output: Delivery confirmation
    Timing: 24 hours before event

--- LANE: Founder (post-event) ---

[9] Capture post-event connections
    Input:  Business cards, LinkedIn connections, meeting notes
    Output: New contacts [{
              name: string,
              company: string,
              context: string (how we met),
              follow_up_action: string
            }]
    Tool:   Manual -> prospect database

    GATEWAY: Follow-up type?
      WARM LEAD (showed interest) -> CALL P1 (Outbound Campaign, warm variant)
      CONTACT (no immediate fit)  -> add to database, nurture
      PARTNERSHIP                 -> separate track (manual)

[10] Generate post-event follow-ups
    Input:  Connection notes + attendee research
    Output: Follow-up drafts
    Tool:   Target: AI generation (not yet built)

END: Brief delivered + connections captured + follow-ups sent
```

---

## P3: Content Production Cycle

```
TRIGGER: Friday afternoon (weekly planning cycle)
END:     Content published + performance tracked + corrections extracted

--- LANE: Automation ---

[1] Generate content calendar                          <- G2.1
    Input:  Brand themes (6): owner_independence, pipeline, sales,
              delivery, money, systems
            Platform strategy:
              LinkedIn = professional insight
              X = building in public
              Facebook = community
            Previous week performance (from G2.12)
            Topic inventory (from playbook)
            Intelligence feed (from G2.10, knowledge base)
            SEO gaps (from G2.9, monthly)
    Output: Weekly calendar {
              week: date_range,
              entries: [{
                day: date,
                platform: enum(linkedin | x | facebook | blog),
                topic: string,
                theme: string,
                angle: string,
                format: enum(text | carousel | thread | article),
                brief: string
              }]
            }
    Tool:   /content-calendar skill

--- LANE: Founder ---

[2] Review & approve calendar                          <- G2.1
    Input:  Generated calendar
    Output: Approved calendar

    GATEWAY: Approved?
      YES -> continue
      NO  -> feedback -> loop [1] with adjustments

--- LANE: Automation (content-production) ---

[3] Create content briefs per entry                    <- G2.2
    Input:  Approved calendar entry
    Output: Content brief {
              topic: string,
              platform: string,
              angle: string,
              target_audience: string,
              key_points: string[],
              cta: string,
              word_count_target: int,
              references: string[]
            }

[4] -> CALL SP4: Voice-Matched Content Generation      <- G2.3
    Input:  Content brief
    Output: Generated content pack {
              linkedin_posts: string[] (3-5 per week),
              x_posts: string[] (3-5 per week),
              fb_posts: string[] (2-3 per week),
              blog_drafts: string[] (0-2 per month)
            }

--- LANE: Founder ---

[5] Review & edit content                              <- G2.5
    Input:  Generated content pack
    Output: Per-piece decision {
              piece_id: string,
              status: enum(approved | edited | rejected),
              edits: string?,
              rejection_reason: string?
            }

    GATEWAY: Per piece
      APPROVED -> queue for publishing
      EDITED   -> founder's version replaces generated version -> queue
      REJECTED -> feedback -> regenerate that piece only

[6a] Publish social content                            <- G2.6
    Input:  Approved/edited posts
    Output: Published record {
              platform: string,
              published_at: datetime,
              url: string,
              original_version: string,
              published_version: string (after edits)
            }
    Tool:   Manual (LinkedIn, X, Facebook - copy/paste)
    Schedule: LinkedIn 3-5x/week, X 3-5x/week, Facebook 2-3x/week

[6b] Publish blog content                              <- G2.7
    Input:  Approved blog draft
    Output: Published blog {
              platform: string (HubSpot, WordPress, Medium, Substack),
              published_at: datetime,
              url: string
            }
    Tool:   publishing engine (automated publishing)

--- LANE: Automation ---

[7] Extract style corrections                          <- G2.8
    Input:  Original generated version vs published version (edits)
    Output: Style corrections [{
              platform: string,
              pattern: string,
              example_before: string,
              example_after: string,
              confidence: enum(LOW | MEDIUM | HIGH),
              observation_count: int
            }]
    Tool:   Style-corrections learning loop (automated)
    Logic:  LOW (1 obs) -> logged only
            MEDIUM (2-3 obs) -> auto-applied in future generation
            HIGH (5+ obs) -> hard rule, always applied
    File:   content-production/.content-rules/style-corrections.md

[8] Performance review (Monday)                        <- G2.12
    Input:  Platform analytics {
              per_post: [{url, impressions, engagement, clicks, comments}],
              per_platform: {reach, follower_growth, top_posts}
            }
    Output: Performance report {
              top_performers: [{post, metric, value}],
              underperformers: [{post, metric, value}],
              theme_effectiveness: {theme: avg_engagement},
              platform_comparison: {platform: metrics},
              recommendations: string[]
            }
    Tool:   Manual + CRM analytics

    -> FEEDS: [1] next week's calendar (close the loop)
    -> FEEDS: O3.3 Content Attribution

END: Content published + style corrections updated + performance tracked
```

---

## P4: Inbound Lead Processing

```
TRIGGER: Engagement signal detected
         (LinkedIn comment/DM, blog subscriber, website form,
          event inquiry, referral, community member)
END:     Lead enrolled in campaign OR parked in nurture

--- LANE: Founder (manual) ---

[1] Identify and capture lead
    Input:  Engagement signal {
              source: enum(linkedin | blog | website | event |
                          referral | community | x),
              signal_type: enum(comment | dm | subscribe | form |
                                referral | rsvp),
              person_info: {name: string, company?: string,
                            profile_url?: string},
              context: string (what they engaged with)
            }
    Output: Lead record
    Tool:   Manual identification (currently)

[2] Add to prospect database
    Input:  Lead record
    Output: Contact record {contact_id: int, status: "new"}
    Tool:   prospect list builder

--- LANE: Automation ---

[3] -> CALL SP1: Data Enrichment Pipeline              <- G1.2
    Input:  Contact record
    Output: Enriched contact

[4] -> CALL SP2: ICP Scoring                           <- G1.3
    Input:  Enriched contact + ICP rubric
    Output: Scored contact

    GATEWAY: ICP tier?
      HOT (high fit + warm signal) -> [5a] priority outreach
      WARM (moderate fit)          -> [5b] nurture sequence
      COLD (low fit)               -> END {status: "nurture_list"}
      DISQUALIFIED                 -> END {status: "removed"}

--- LANE: Founder ---

[5a] Direct warm outreach
    Input:  Scored contact + engagement context
    Output: Personalized response {
              channel: enum(linkedin_dm | email | x_reply),
              message: string,
              tone: "warm, peer, referencing their engagement"
            }
    Tool:   Manual (LinkedIn, email)
    Note:   WARM outreach - they came to us.
            Different tone than cold. Reference their engagement.

    GATEWAY: Response?
      POSITIVE  -> [6] schedule meeting -> END -> triggers P5
      NO REPLY  -> enroll in P1 (Outbound Campaign, warm tag)
      NEGATIVE  -> END {status: "not_interested"}

[5b] Add to nurture sequence
    Input:  Contact + ICP score
    Output: Enrolled in nurture
    Tool:   Manual (currently) -> target: automated nurture

[6] Schedule meeting
    Input:  Positive response
    Output: Meeting booked -> triggers P5

END: Lead qualified and either meeting booked or nurturing
```

---

## P5: Sales & Close

```
TRIGGER: Discovery meeting completed (from P1 step [11] or P4 step [6])
END:     Deal closed -> triggers P6 (Onboarding)

--- LANE: Founder ---

[1] Prepare for meeting
    Input:  Meeting record (from P1 or P4)
            Prospect research brief (from SP3)
            CRM history
    Output: Meeting prep {
              person_summary: string,
              company_summary: string,
              icp_fit: int,
              conversation_strategy: string,
              talking_points: string[],
              objection_predictions: string[],
              recommended_product: string,
              next_step_goal: string
            }
    Tool:   /prospect-brief skill

[2] Conduct discovery meeting
    Input:  Meeting prep
    Output: Meeting notes {
              attendees: string[],
              goals_discussed: string[],
              pain_points: string[],
              budget_signals: string,
              timeline_signals: string,
              authority_confirmed: bool,
              objections_raised: string[],
              next_steps_agreed: string
            }
    Tool:   Manual (video call or in-person), Transcription Service

[3] Qualify opportunity
    Input:  Meeting notes
    Output: Qualification {
              budget: enum(confirmed | estimated | unknown),
              authority: enum(decision_maker | influencer | unknown),
              need: enum(confirmed | implied | unclear),
              timeline: enum(immediate | this_quarter | someday),
              overall: enum(qualified | partial | disqualified)
            }

    GATEWAY: Qualified?
      QUALIFIED (BANT met)  -> [4] design proposal
      PARTIAL               -> [3b] schedule follow-up discovery
      DISQUALIFIED          -> END {status: "lost", reason: string}
                              -> log in CRM, add to nurture

[3b] Follow-up discovery
    Input:  Partial qualification + open questions
    Output: Additional meeting scheduled
    Tool:   Calendar Scheduler
    -> Loop back to [2]

[4] Design proposal
    Input:  Qualification + client needs + product catalog
    Output: Custom proposal {
              recommended_products: string[],
              scope: string,
              pricing: {
                monthly_fee: number,
                setup_fee: number?,
                performance_component?: string
              },
              timeline: string,
              expected_results: string,
              case_study_reference: string,
              contract_terms: string
            }
    Tool:   /sales-proposal skill, Google Workspace

[5] Present proposal
    Input:  Custom proposal
    Output: Client response {
              status: enum(accepted | negotiating | needs_time | declined),
              feedback: string?,
              counter_terms?: object
            }

    GATEWAY: Response?
      ACCEPTED    -> [6] close deal
      NEGOTIATING -> [5b] revise terms -> loop [5]
      NEEDS TIME  -> [5c] schedule follow-up (use /follow-up skill)
      DECLINED    -> END {status: "lost", reason: string}
                    -> post-mortem: why did we lose?

[5b] Revise terms
    Input:  Counter-terms + original proposal
    Output: Revised proposal
    -> Loop [5]

[6] Close deal
    Input:  Accepted proposal
    Output: Closed deal {
              deal_id: string (CRM),
              client_name: string,
              product: string,
              mrr: number,
              start_date: date,
              contract_length: string
            }
    Tool:   CRM deal update, contract signing (manual)

    -> TRIGGERS: P6 (Client Onboarding)
    -> FEEDS: O3.2 (Pipeline Value), O3.5 (MRR Tracking), F4.5 (Revenue Forecast)

END: Deal closed, onboarding triggered
```

---

## P6: Client Onboarding

```
TRIGGER: Deal closed (from P5 step [6])
END:     Client pipelines active, ready for monthly delivery

--- LANE: Founder ---

[1] Kickoff meeting                                    <- D1.1, D1.2
    Input:  Closed deal {product, scope, pricing}
            Prospect research (from earlier pipeline)
    Output: Kickoff record {
              client_goals: string[],
              success_metrics: [{metric: string, target: number}],
              timeline: string,
              communication_preferences: {
                channel: enum(slack | email | whatsapp),
                frequency: enum(daily | weekly | biweekly),
                contact_person: string
              },
              product_purchased: string
            }

[2] Configure client profile                           <- D1.1
    Input:  Kickoff record
    Output: Client configuration {
              client_id: string,
              their_icp: {industry, size, geo, role, signals},
              their_brand_voice?: voice_config (if Content Engine),
              exclusions: string[],
              reporting_preferences: object
            }
    Tool:   CRM (company/deal record), manual setup

    GATEWAY: Which product?
      EVENT_OPS       -> [3a]
      OUTREACH_ENGINE -> [3b]
      CONTENT_ENGINE  -> [3c]
      FULL_PACKAGE    -> [3a] + [3b] + [3c] in parallel

--- LANE: Founder + Automation ---

[3a] Event Ops Setup
    Input:  Client config (their ICP, target cities, event types)
    Steps:
      1. Configure Event Scout for client cities/keywords (manual)
      2. Set up client-specific output sheet (manual)
      3. Schedule weekly scan (automated once configured)
      4. Run initial scan to verify results (automated)
      5. Review first brief with client (manual)
    Output: Event pipeline active

[3b] Outreach Engine Setup
    Input:  Client config (their ICP, messaging, exclusions)
    Steps:
      1. Build initial prospect list via prospect database (semi-auto)
      2. Configure campaign parameters (manual)
      3. Set up email sequencer account/sequences (manual)
      4. Create approval workflow
      5. Run first micro-cohort (25 prospects) as pilot
      6. Review pilot results with client (manual)
    Output: Outreach pipeline active

[3c] Content Engine Setup
    Input:  Client config (their brand, voice, themes)
    Steps:
      1. Voice capture sessions: 2-3 hours interviews (manual)
      2. Extract voice guide from recordings (semi-auto)
      3. Define brand themes + platform strategy (manual with client)
      4. Configure content-production for client brand (manual)
      5. Generate first week's content as sample (automated)
      6. Client reviews and provides feedback (manual)
      7. Adjust voice/style based on feedback (manual)
    Output: Content pipeline active

--- LANE: Founder ---

[4] Confirm go-live
    Input:  Setup outputs from [3a/3b/3c]
    Output: Go-live confirmation {
              all_pipelines_active: bool,
              client_confirmed_ready: bool,
              first_delivery_date: date,
              recurring_cadence: string
            }

    -> TRIGGERS: P7 (Client Monthly Delivery)

END: Client fully onboarded, pipelines active
```

---

## P7: Client Monthly Delivery

```
TRIGGER: Monthly cadence (per client)
END:     Monthly deliverables complete, results reported

--- LANE: Founder + Automation ---

[1] Execute monthly deliverables                       <- D1.3

    GATEWAY: Product type determines execution:

    EVENT_OPS (weekly within month):
      Input:  Client scan config
      Output per week: {
        events_scanned: int,
        t1_t2_events: int,
        attendees_extracted: int,
        briefs_delivered: int
      }
      Execution: P2 (Event Intelligence) runs on client config

    OUTREACH_ENGINE (continuous within month):
      Input:  Client campaign config
      Output per month: {
        prospects_researched: int,
        pitches_generated: int,
        pitches_approved: int,
        emails_sent: int,
        replies_received: int,
        meetings_booked: int
      }
      Execution: P1 (Outbound Campaign) runs on client config

    CONTENT_ENGINE (weekly within month):
      Input:  Client content config
      Output per month: {
        posts_published: int,
        blog_posts_published: int,
        total_engagement: int,
        follower_growth: int
      }
      Execution: P3 (Content Production) runs on client voice/brand

--- LANE: Founder ---

[2] Scope change management                            <- D1.5
    Input:  Client request (mid-month adjustment)
    Output: Scope decision {
              request: string,
              in_scope: bool,
              adjustment: string?,
              pricing_impact: string?
            }

    GATEWAY: In scope?
      YES -> adjust deliverables
      NO  -> negotiate scope change or upsell

[3] Quality assurance review                           <- D1.6
    Input:  Month's deliverables (before sending final report)
    Output: QA result {
              all_deliverables_complete: bool,
              quality_issues: string[],
              corrections_made: string[]
            }

[4] Client communication                               <- D1.4
    Input:  QA'd deliverables + metrics
    Output: Monthly report {
              deliverables_summary: object,
              metrics_vs_targets: [{metric, target, actual, status}],
              highlights: string[],
              issues: string[],
              recommendations_for_next_month: string[]
            }
    Tool:   Google Workspace (monthly report template)
    Cadence: Weekly check-in + monthly report

    -> FEEDS: D2.1 (Results Documentation)
    -> FEEDS: O3.5 (MRR Tracking)

END: Monthly delivery complete, report sent
```

---

## P8: Case Study & Proof Creation

```
TRIGGER: Client achieves significant result
         OR 90-day milestone (from D2.4)
         OR quarterly review shows strong metrics
END:     Proof assets distributed across sales + content

--- LANE: Founder ---

[1] Capture results data                               <- D2.1
    Input:  Client delivery metrics (from P7)
            Before/after baseline comparison
    Output: Results dataset {
              client_name: string,
              engagement_period: string,
              baseline: {metric: value}[],
              current: {metric: value}[],
              delta: {metric: {absolute: value, percentage: value}}[],
              specific_wins: string[],
              timeline: string
            }

[2] Get client permission                              <- D2.4
    Input:  Request for case study / testimonial
    Output: Permission {
              level: enum(full_case_study | anonymized |
                          metrics_only | testimonial_only | declined),
              client_quote: string?,
              approved_metrics: string[]
            }

    GATEWAY: Permission level?
      FULL          -> [3] full case study
      ANONYMIZED    -> [3] anonymized case study
      METRICS_ONLY  -> [3] proof point (numbers only)
      TESTIMONIAL   -> [3b] collect testimonial only
      DECLINED      -> END {no_proof_assets}

[3] Generate case study                                <- D2.3
    Input:  Results dataset + permission level + client quote
    Output: Case study {
              title: string,
              challenge: string,
              solution: string,
              results: {metric: before_after}[],
              client_quote: string?,
              implementation_summary: string,
              key_takeaway: string
            }
    Tool:   /case-study-builder skill + templates

[4] Calculate ROI                                      <- D2.2
    Input:  Results dataset + client investment (fee)
    Output: ROI calculation {
              investment: number,
              revenue_generated: number,
              roi_percentage: number,
              ltv_to_date: number,
              payback_period: string
            }

    -> FEEDS: F2.1 (Pricing Review), F2.2 (Unit Economics)

[5] Create derivative assets                           <- D2.5
    Input:  Case study + ROI
    Output: Proof assets {
              linkedin_post: string (social proof angle),
              email_proof_point: string (1-2 line for outreach),
              website_testimonial: {quote, name, company, result},
              sales_deck_slide: object,
              proposal_reference: string (for P5 proposals),
              blog_post_seed: string (for G2.4)
            }

[6] Distribute assets                                  <- D2.5
    Input:  Proof assets
    Output: Distribution record {
              website_updated: bool,
              content_calendar_seeded: bool (-> G2.1),
              outreach_templates_updated: bool (-> G3.1),
              sales_materials_updated: bool
            }

    -> FEEDS: G2.1 (Content Calendar - case study content)
    -> FEEDS: G3.1 (Campaign Launch - proof point for outreach)
    -> FEEDS: P5 (Sales & Close - proposal references)

END: Proof assets created and distributed to all channels
```

---

## P9: Client Retention & Expansion

```
TRIGGER: Weekly health check cadence
         OR 60 days before renewal
         OR success milestone reached
END:     Client retained/expanded OR churned (post-mortem)

--- LANE: Founder ---

[1] Score client health                                <- D3.1
    Input:  Delivery metrics (from P7)
            Communication frequency
            Client engagement level
            Results vs targets
    Output: Health score {
              engagement: int (0-100),
              results_delivery: int (0-100),
              communication: int (0-100),
              overall: int (0-100),
              trend: enum(improving | stable | declining),
              flags: string[]
            }
    Tool:   Manual -> target: CRM health score automation

    GATEWAY: Health score?
      >=80 (healthy)    -> [2a] look for expansion
      40-79 (at risk)   -> [2b] retention intervention
      <40 (churning)    -> [2c] save attempt

[2a] Identify expansion opportunity                    <- D3.2
    Input:  Healthy client profile + current product + results
    Output: Expansion proposal {
              current_product: string,
              proposed_addition: string,
              rationale: string,
              expected_additional_results: string,
              price_increase: number
            }

    -> [3a] Present expansion in next check-in
    -> If accepted: loop to P6 (Onboarding) for new product

[2b] Retention intervention                            <- D3.5
    Input:  Risk factors + client concerns
    Output: Retention plan {
              risk_factors: string[],
              proposed_adjustments: string[],
              additional_value: string,
              timeline: string,
              owner: "Founder"
            }

    -> [3b] Execute retention plan -> re-score in 30 days

[2c] Save attempt
    Input:  Churn signals + client feedback
    Output: Save offer {
              concessions: string[]?,
              restructured_scope: string?,
              pause_option: bool?,
              exit_survey: string[]
            }

    GATEWAY: Client decision?
      STAYS     -> back to normal delivery (P7)
      PAUSES    -> pause billing, maintain access, re-engage in N months
      CHURNS    -> [4] post-mortem

[3] Renewal management (60 days before)                <- D3.3
    Input:  Current contract terms + health score + results
    Output: Renewal proposal {
              current_terms: object,
              proposed_terms: object,
              price_adjustment: string,
              added_value: string
            }

[4] Referral ask (at success milestones)               <- D3.4
    Input:  Strong results + happy client
    Output: Referral request {
              ask: string,
              incentive: string?,
              referrals_received: [{name, company, intro_context}]
            }

    -> FEEDS: G1.1 (warm leads from referral)

[5] Post-mortem (on churn)
    Input:  Churned client record + history
    Output: Churn analysis {
              client: string,
              duration: string,
              revenue_lost: number,
              reasons: string[],
              what_we_could_improve: string[],
              pattern_match: string (is this a recurring issue?)
            }

    -> FEEDS: FP1 (ICP Review - should we adjust who we target?)

END: Client retained/expanded/referred OR churned with lessons
```

---

## Sub-Processes

### SP1: Data Enrichment Pipeline

```
TRIGGER: Called by P1[3], P2[5], P4[3]
INPUT:   Raw contact records [{name, company, email?, linkedin?}]
OUTPUT:  Enriched contact records

--- LANE: Automation (Contact Database) ---

[1] Company enrichment
    Input:  Company name or domain
    Output: {
              funding_stage: string?,
              funding_amount: string?,
              employee_count: int?,
              revenue_estimate: string?,
              industry: string,
              hq_location: string,
              tech_stack: string[]?,
              recent_news: string[]?,
              linkedin_company: string?
            }
    Tool:   Contact Database company enrichment engine

[2] Person enrichment
    Input:  Name + company
    Output: {
              title: string,
              linkedin_url: string,
              bio: string?,
              social_profiles: {platform: url}[],
              career_history: string[]?,
              interests: string[]?
            }
    Tool:   Contact Database person enrichment engine

[3] Email discovery & verification
    Input:  Name + company domain
    Output: {
              email: string?,
              email_source: string,
              verification_status: enum(verified | unverified | not_found),
              confidence: float
            }
    Tool:   Email Finder (primary), Email Verifier (backup)

    GATEWAY: Email status?
      VERIFIED     -> continue (full outreach possible)
      UNVERIFIED   -> flag, continue (risky to send)
      NOT_FOUND    -> flag as email_missing (LinkedIn-only outreach)

[4] Signal detection
    Input:  All enrichment data
    Output: {
              signals: [{
                type: enum(funding_round | hiring_surge | event_attendance |
                           tech_change | expansion | content_published |
                           job_change | award),
                detail: string,
                date: date?,
                relevance: enum(high | medium | low)
              }]
            }

RETURN: Enriched contact record (all fields merged, missing fields flagged)
```

### SP2: ICP Scoring

```
TRIGGER: Called by P1[4], P2[6], P4[4]
INPUT:   Enriched contact + ICP scoring rubric (from F1.1)
OUTPUT:  Scored contact with tier

--- LANE: Automation (Contact Database) ---

[1] Score against criteria
    Input:  Enriched contact fields + ICP rubric
    Criteria (weighted):
      - Industry match:     weight HIGH
      - Company size/stage: weight HIGH
      - Role/title match:   weight HIGH
      - Geography:          weight MEDIUM
      - Funding stage:      weight MEDIUM
      - Signal recency:     weight MEDIUM
      - Tech stack fit:     weight LOW
    Output: {
              score: int (0-100),
              tier: enum(hot | warm | cold | disqualified),
              breakdown: [{criterion: string, weight: string,
                           match: bool, score: int}]
            }
    Logic:  hot >=80, warm >=50, cold >=20, disqualified <20

[2] Check exclusions
    Input:  Contact + exclusion rules
    Checks:
      - Already active in CRM?
      - Competitor? (exclusion list)
      - Previously rejected or unsubscribed? (prospect database history)
      - On do-not-contact list?
      - Already in active campaign?
    Output: {
              excluded: bool,
              reason: string?
            }

    GATEWAY: Excluded?
      YES -> RETURN {tier: "excluded", reason: string}
      NO  -> RETURN scored contact

RETURN: {score, tier, breakdown, excluded: false}
```

### SP3: Prospect Research

```
TRIGGER: Called by P1[6], P2 (if deep research needed)
INPUT:   Enriched, qualified contact record
OUTPUT:  Research brief for personalization

--- LANE: Automation (Research Squad) ---

[1] Company deep dive
    Input:  Company name + domain + enrichment data
    Output: {
              what_they_do: string,
              business_model: string,
              target_market: string,
              recent_developments: string[],
              challenges_likely: string[],
              competitive_position: string,
              growth_trajectory: string
            }
    Tool:   Research Squad agents (web search, analysis)

[2] Person deep dive
    Input:  Name + LinkedIn + title + enrichment
    Output: {
              career_trajectory: string,
              current_role_scope: string,
              content_they_publish: string[],
              speaking_events: string[],
              interests: string[],
              communication_style: string
            }
    Tool:   Research Squad agents (LinkedIn analysis, content review)

[3] Signal analysis
    Input:  Company + person + detected signals
    Output: {
              why_now: string,
              timing_rationale: string,
              trigger_event: string,
              urgency: enum(high | medium | low)
            }
    Note:   Never outreach without a recent trigger.
            If no signal -> park, don't force it.

[4] Connection point identification
    Input:  All research + founder's profile + shared context
    Output: {
              connection_angles: [{
                angle: string,
                evidence: string,
                strength: enum(strong | moderate | weak)
              }],
              shared_events: string[],
              shared_interests: string[],
              mutual_connections: string[]
            }

RETURN: Research brief {
  company_analysis, person_analysis, why_now,
  connection_angles, recommended_approach
}
```

### SP4: Voice-Matched Content Generation

```
TRIGGER: Called by P3[4]
INPUT:   Content brief {topic, platform, angle, format}
OUTPUT:  Production-ready content in founder's voice

--- LANE: Automation (content-production) ---

[1] Load voice configuration
    Input:  Platform identifier
    Output: Voice rules {
              voice_guide: file (brand voice guide),
              track: enum(A_operator | B_architect),
              platform_style: {
                linkedin: "professional insight, clear frameworks",
                x: "building in public, raw, shorter",
                facebook: "community, conversational, personal"
              },
              tone: "warm, peer, frontline practitioner (not guru)",
              banned_words: string[],
              style_corrections: [{platform, pattern, confidence}]
            }
    Files:  brand voice guide, content-rules/style-corrections.md

[2] Generate draft
    Input:  Brief + voice rules
    Output: Raw draft {
              text: string,
              word_count: int,
              hashtags: string[]?,
              cta: string
            }
    Tool:   content-production AI engine

[3] Run QC gates
    Input:  Raw draft
    Checks:
      - Truth gate: no fabricated claims, stats verified
      - DEAI lint: no discriminatory/exclusionary language
      - Voice match: tone, vocabulary, sentence structure
      - Banned words: none present
      - Platform fit: length appropriate, format correct
      - Hashtag check: relevant, not excessive
    Output: {
              passed: bool,
              issues: [{check: string, severity: string, detail: string}]
            }

    GATEWAY: All checks pass?
      YES -> [4]
      NO (auto-fixable)  -> fix and re-check
      NO (needs human)   -> flag for review step

[4] Apply high-confidence style corrections
    Input:  Draft + style corrections (MEDIUM and HIGH confidence)
    Output: Corrected draft
    Logic:  HIGH (5+ obs) -> always applied
            MEDIUM (2-3 obs) -> applied automatically
            LOW (1 obs) -> not applied (logged only)

RETURN: Production-ready content piece
```

---

## Foundation Processes

### FP1: ICP & Positioning Review Cycle

```
TRIGGER: Quarterly cadence
         OR market shift detected
         OR churn pattern identified (from P9[5])
         OR segment performance data (from G1.7)
END:     ICP + messaging + wedge strategy updated across all systems

--- LANE: Founder ---

[1] ICP review                                         <- F1.1
    Input:  Current ICP definition (playbook/core/icp.md)
            Win/loss data (CRM)
            Segment performance (from G1.7)
            Churn analysis (from P9[5])
            Market signals (competition, industry shifts)
    Output: Revised ICP {
              primary: {industry, company_size, stage, geo, role, signals},
              secondary: [{...segment}],
              exclusions: string[],
              scoring_rubric: {criterion: weight}[],
              changes_from_previous: string[]
            }

[2] Competitive position audit                         <- F1.2
    Input:  Competitor landscape
            Current positioning
            Client feedback on why they chose us / didn't
    Output: Competitive analysis {
              competitors: [{name, positioning, strengths, weaknesses}],
              our_differentiation: string[],
              gaps: string[],
              opportunities: string[]
            }

[3] Messaging refresh                                  <- F1.3
    Input:  Revised ICP + competitive analysis
    Output: Updated messaging {
              value_propositions: string[],
              proof_points: string[],
              objection_responses: {objection: response}[],
              elevator_pitch: string,
              positioning_statement: string
            }
    Files:  playbook/core/messaging.md

[4] Wedge strategy validation                          <- F1.4
    Input:  Revised ICP + messaging
    Output: Wedge strategies {
              per_segment: [{
                segment: string,
                wedge: string (entry point product/offer),
                proof_point: string,
                expected_conversion: string
              }]
            }

[5] Propagate updates                                  <- system-wide
    Input:  All updated artifacts
    Output: Updated in:
      - playbook/core/ (ICP, messaging, wedge)
      - Contact database scoring rubric (ICP scoring criteria)
      - Content themes alignment (G2.1 inputs)
      - Campaign targeting (G3.1 inputs)
      - Outreach angles (G3.3 inputs)
      - Sales materials (P5 inputs)

END: Foundation aligned, all downstream systems updated
```

### FP2: Business Model Review

```
TRIGGER: Quarterly cadence OR pricing feedback from sales
END:     Pricing + tiers + unit economics validated

--- LANE: Founder ---

[1] Pricing review                                     <- F2.1
    Input:  Current pricing (playbook)
            Client ROI data (from D2.2)
            Competitive pricing research
            Sales conversion data (win/loss by price)
    Output: Pricing assessment {
              current_tiers: [{tier, price, margin}],
              market_comparison: string,
              adjustment_recommendation: string
            }

[2] Unit economics calculation                         <- F2.2
    Input:  Revenue per client, cost of delivery (time + tools),
            client acquisition cost
    Output: Unit economics {
              cac: number,
              ltv: number,
              ltv_cac_ratio: number,
              gross_margin_per_tier: {tier: percentage}[],
              payback_period: string
            }
    Tool:   finance-tracker (target), manual (current)

[3] Service tier validation                            <- F2.3
    Input:  Pricing + unit economics + market feedback
    Output: Validated tiers {
              tiers: [{
                name: string,
                products_included: string[],
                price: number,
                margin: percentage,
                target_client: string
              }],
              changes: string[]
            }

    -> Updates: playbook pricing, P5 proposal templates

END: Pricing and tiers validated
```

### FP3: Financial Review Cycle

```
TRIGGER: Monday (weekly cash), Month-end (unit economics + forecast)
END:     Financial position known, forecast updated

--- LANE: Founder ---

[1] Weekly cash forecast (Monday)                      <- F4.1
    Input:  Bank balance, expected inflows, committed outflows
    Output: Cash forecast {
              current_balance: number,
              week_1_projected: number,
              week_2_projected: number,
              week_3_projected: number,
              week_4_projected: number,
              runway_months: number,
              alerts: string[]
            }
    Tool:   Manual -> target: finance-tracker

[2] Monthly unit economics (month-end)                 <- F4.2
    Input:  Revenue (from O3.5), costs, client count
    Output: Monthly economics {
              mrr: number,
              costs: {category: amount}[],
              gross_margin: percentage,
              per_client_economics: {client: metrics}[],
              trend: enum(improving | stable | declining)
            }

[3] Break-even tracking                                <- F4.3
    Input:  Unit economics
    Output: Break-even status {
              break_even_mrr: number,
              current_mrr: number,
              gap: number,
              projected_break_even_date: date?
            }

[4] Revenue forecast                                   <- F4.5
    Input:  Pipeline value (from O3.2), current MRR,
            conversion rates, churn rate
    Output: Forecast {
              current_mrr: number,
              pipeline_value: number,
              weighted_pipeline: number,
              month_3_projected: number,
              month_6_projected: number,
              month_12_projected: number,
              assumptions: string[]
            }

END: Financial position clear, forecast updated
```

---

## Operations Processes

### OP1: Process Documentation & Automation Cycle

```
TRIGGER: New process identified OR existing process changed significantly
END:     Process documented, automation assessed, potentially built

--- LANE: Founder ---

[1] Document the process                               <- O1.2
    Input:  Process as currently executed (reality, not aspiration)
    Output: Process block document {
              block_id: string,
              fields: (per schema.md - 8 fields),
              steps: numbered list,
              current_state: string,
              pain_points: string[],
              automation_opportunity: string
            }
    File:   operations/.meta/blocks/{BLOCK-ID}.md

[2] Assess automation priority
    Input:  Documented process + pain points
    Output: Automation assessment {
              frequency: how often it runs,
              time_per_execution: minutes,
              error_rate: percentage,
              automation_feasibility: enum(easy | moderate | hard),
              priority: enum(high | medium | low),
              estimated_effort: string
            }

    GATEWAY: Automate now?
      HIGH priority + EASY -> [3] hand to CTO
      HIGH priority + HARD -> create project issue, plan
      MEDIUM/LOW -> log for future, move on

--- LANE: CTO ---

[3] Agent development                                  <- O2.1
    Input:  Process documentation (from [1])
    Output: Automation implementation {
              agent_or_skill: string,
              repo: string,
              pr: string,
              test_results: string
            }
    Tool:   AI agent platform + CTO's tools

[4] Deploy                                             <- O2.2
    Input:  Merged PR
    Output: Deployed automation {
              service: string,
              health_endpoint: string,
              deployment_status: string
            }
    Tool:   Deployment Platform (auto-deploy on merge)

[5] Update block status
    Input:  Deployed automation
    Output: Block updated {
              executor field: "X - fully automated" or "(semi-automated)",
              steps updated to reflect automation
            }

END: Process documented and optionally automated
```

### OP2: System Health & Monitoring

```
TRIGGER: Daily automated check OR breakage detected
END:     All systems healthy OR issues escalated

--- LANE: Automation ---

[1] Health endpoint checks                             <- O2.5
    Input:  Service registry (all deployed services and their health endpoints)
    Output: Health report {
              services: [{name, status, response_time, last_check}],
              failures: [{name, error, since}]
            }

    GATEWAY: All healthy?
      YES -> END {all_green}
      NO  -> [2] investigate

--- LANE: CTO ---

[2] Investigate failure                                <- O2.3
    Input:  Failure details
    Output: Diagnosis {
              root_cause: string,
              fix: string,
              fix_type: enum(config | code | external_dependency)
            }
    Tool:   Deployment platform logs, service debugging

[3] Fix and verify
    Input:  Diagnosis
    Output: Fix applied {
              fix_description: string,
              deployed: bool,
              health_restored: bool
            }

--- LANE: Founder or CTO ---

[4] Repo health check (weekly)                         <- O1.3
    Input:  All repos
    Output: Repo health {
              repos: [{name, has_claude_md, last_commit, ci_status,
                       state_file_fresh, uncommitted_changes}],
              issues: string[]
            }
    Tool:   repository health check

END: Systems healthy, issues resolved
```

### OP3: Weekly Business Review

```
TRIGGER: Monday morning
END:     Business pulse known, priorities set for week

--- LANE: Founder ---

[1] Scorecard review                                   <- O3.1
    Input:  All metrics from previous week
    Output: Weekly scorecard {
              mrr: number,
              pipeline_value: number,
              meetings_booked: int,
              reply_rate: percentage,
              content_engagement: object,
              client_health_scores: {client: score}[],
              north_star_per_brick: {brick: metric_value}[]
            }
    Tool:   Manual + weekly review tool

[2] Pipeline review                                    <- O3.2
    Input:  CRM deals + campaign data
    Output: Pipeline status {
              deals_by_stage: {stage: [{deal, value, age}]}[],
              new_this_week: int,
              advanced_this_week: int,
              lost_this_week: int,
              total_weighted_value: number
            }
    Tool:   CRM + manual

[3] Campaign performance review                        <- G3.8
    Input:  Email sequencer analytics + campaign data
    Output: Campaign metrics {
              active_campaigns: int,
              emails_sent: int,
              reply_rate: percentage,
              positive_reply_rate: percentage,
              meetings_from_outreach: int,
              best_performing_campaign: string,
              worst_performing_campaign: string
            }

[4] Content performance review                         <- G2.12
    Input:  Platform analytics
    Output: Content metrics (see P3[8])

[5] Segment performance review                         <- G1.7
    Input:  All metrics broken by ICP segment
    Output: Segment analysis {
              per_segment: [{
                segment: string,
                prospects_added: int,
                emails_sent: int,
                reply_rate: percentage,
                meetings_booked: int,
                conversion_rate: percentage,
                recommendation: enum(scale_up | maintain | pause | drop)
              }]
            }

    -> FEEDS: FP1 (if segment consistently underperforms)

[6] Set weekly priorities
    Input:  All review outputs
    Output: Week priorities {
              focus_areas: string[],
              campaigns_to_launch: string[],
              clients_needing_attention: string[],
              blockers_to_resolve: string[]
            }
    Tool:   Task Manager

END: Business pulse known, week priorities set
```

---

## Process-to-Product Mapping

How processes compose into sellable products:

```
EVENT OPS
- Core: P2 (Event Intelligence & Activation)
- Sub: SP1 (Data Enrichment), SP2 (ICP Scoring)
- Setup: P6[3a] (Event Ops onboarding)
- Monthly: P7 (weekly event briefs)

OUTREACH ENGINE
- Core: P1 (Outbound Campaign Execution)
- Sub: SP1 (Data Enrichment), SP2 (ICP Scoring), SP3 (Prospect Research)
- Setup: P6[3b] (Outreach Engine onboarding)
- Monthly: P7 (campaigns + reporting)

CONTENT ENGINE
- Core: P3 (Content Production Cycle)
- Sub: SP4 (Voice-Matched Content Generation)
- Setup: P6[3c] (Content Engine onboarding - voice capture)
- Monthly: P7 (weekly content)

FULL PACKAGE
- All of Event Ops
- All of Outreach Engine
- All of Content Engine
- Weekly strategy call (Founder)
- Integrated reporting across all channels
```

---

## Implementation Priority

### Phase 1: Revenue-Critical (this sprint)

Document these blocks as per schema.md, filling in REALITY:

| Priority | Block | Process Reference | Status |
|----------|-------|-------------------|--------|
| 1 | F1.1 | FP1[1] | needs documentation |
| 2 | G1.1 | P1[2] | needs documentation |
| 3 | G1.2 | SP1 | needs documentation |
| 4 | G1.3 | SP2 | needs documentation |
| 5 | G1.4 | P2[2-3] | needs documentation |
| 6 | G1.6 | SP3 | needs documentation |
| 7 | G3.1 | P1[1] | needs documentation |
| 8 | G3.3 | P1[7] | needs documentation |
| 9 | G3.4 | P1[8] | needs documentation |
| 10 | G3.5 | P1[9] | needs documentation |

### Phase 2: Content & Attraction

| Block | Process Reference |
|-------|-------------------|
| G2.1 | P3[1] |
| G2.3 | SP4 |
| G2.5 | P3[5] |
| G2.7 | P3[6b] - already documented |
| G2.8 | P3[7] |
| G2.12 | P3[8] |

### Phase 3: Delivery & Proof

| Block | Process Reference |
|-------|-------------------|
| D1.1-D1.2 | P6[1-2] |
| D1.3 | P7[1] |
| D2.1-D2.3 | P8[1-4] |
| D3.1 | P9[1] |

### Phase 4: Foundation, Ops, remaining blocks

Everything else in the registry.
