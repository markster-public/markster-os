# Master Block Registry

> Complete inventory of all ScaleOS process blocks with metadata and wiring.
> The `/scaleos-block-writer` skill reads this file to validate cross-references.
> The Founder must approve this registry before block generation begins.

---

## Brick-Level Metadata

| Brick | Name | Pillar | DRI | North Star Metric | Block Count |
|-------|------|--------|-----|-------------------|-------------|
| F1 | Positioning & Differentiation | Foundation | Founder | ICP described in 30 sec, differentiation clear vs top 3 | 6 |
| F2 | Business Model Design | Foundation | Founder | Unit economics known cold, pricing defensible | 5 |
| F3 | Organizational Structure | Foundation | Founder | Every brick has one DRI, business runs 1 week without founders | 5 |
| F4 | Financial Architecture | Foundation | Founder | Cash position known 4 weeks out, LTV:CAC >= 3:1 | 5 |
| G1 | Find | Growth | Founder | 50+ qualified prospects entering pipeline per week | 8 |
| G2 | Warm | Growth | Founder | 1 post/day per platform + 2 blog posts/month | 12 |
| G3 | Book | Growth | Founder | 2+ qualified meetings booked per week | 8 |
| O1 | Standardize | Operations | CTO | Every process documented and version-controlled | 7 |
| O2 | Automate | Operations | CTO | Agent coverage expanding monthly, zero manual deploys | 6 |
| O3 | Instrument | Operations | Founder | MRR, pipeline value, and reply rate known at all times | 6 |
| D1 | Deliver | Delivery | Founder | All clients on track, NPS >= 8 | 6 |
| D2 | Prove | Delivery | Founder | Results documented monthly, 1+ case study per quarter | 5 |
| D3 | Expand | Delivery | Founder | 80%+ retention, expansion revenue growing | 5 |

**Total: 84 blocks across 13 bricks (4 pillars)**

---

## Block Inventory

### Foundation - F1: Positioning & Differentiation

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| F1.1 | ICP Review | Quarterly cadence | Monthly | Founder | manual | - | F1.3, F1.4, G1.1 |
| F1.2 | Competitive Position Audit | Quarterly cadence | Monthly | Founder | manual | - | F1.3 |
| F1.3 | Messaging Refresh | Positioning change detected | Per-event | Founder | manual | F1.1, F1.2 | G2.1, G2.3, G3.3 |
| F1.4 | Wedge Strategy Validation | Quarterly cadence | Monthly | Founder | manual | F1.1 | F2.5, G3.1 |
| F1.5 | Customer Fit Scoring | New client signed | Per-event | Founder | manual -> target: CRM health score | D1.1 | F1.1, D3.1 |
| F1.6 | Brand Voice Sync | Monthly cadence | Monthly | Founder | manual | - | G2.1, G2.3 |

### Foundation - F2: Business Model Design

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| F2.1 | Pricing Review | Quarterly cadence | Monthly | Founder | manual | D2.2 | F2.3 |
| F2.2 | Unit Economics Calculation | Month-end | Monthly | Founder | manual -> target: finance-tracker | D2.2, F4.2 | F4.3 |
| F2.3 | Service Tier Validation | Quarterly cadence | Monthly | Founder | manual | F2.1 | F2.5, D1.1 |
| F2.4 | Revenue Mix Analysis | Month-end | Monthly | Founder | manual -> target: finance-tracker | F4.1 | F4.5 |
| F2.5 | Install Sprint Pipeline | Per-prospect | Per-event | Founder | manual | F1.4, F2.3 | G3.1, D1.1 |

### Foundation - F3: Organizational Structure

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| F3.1 | Brick Ownership Audit | Monthly cadence | Monthly | Founder | manual | - | O1.1 |
| F3.2 | Decision Rights Review | Quarterly cadence | Monthly | Founder | manual | F3.1 | O1.1 |
| F3.3 | Agent Capability Inventory | Monthly cadence | Monthly | CTO | manual -> target: capabilities registry automation | O2.1 | O1.5 |
| F3.4 | Founder Independence Test | Quarterly cadence | Monthly | Founder | manual | F3.1, F3.3 | O2.4 |
| F3.5 | Session Coordination Check | Weekly cadence | Weekly | Founder | /prepexit + /prepstart | O2.4 | O1.6 |

### Foundation - F4: Financial Architecture

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| F4.1 | Weekly Cash Forecast | Monday | Weekly | Founder | manual -> target: finance-tracker | - | F2.4 |
| F4.2 | Monthly Unit Economics Review | Month-end | Monthly | Founder | manual -> target: finance-tracker | F2.2, D2.2 | F4.3 |
| F4.3 | Break-Even Tracking | Month-end | Monthly | Founder | manual -> target: finance-tracker | F4.2 | F4.5 |
| F4.4 | Reserve Health Check | Month-end | Monthly | Founder | manual -> target: finance-tracker | F4.1 | - |
| F4.5 | Revenue Forecast | Monday | Weekly | Founder | manual -> target: finance-tracker | F2.4, F4.3, O3.2 | G3.1 |

---

### Growth - G1: Find

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| G1.1 | ICP List Building | Campaign launch decision | Per-event | Founder | Founder via /contactdb + Contact Database | F1.1 | G1.2, G3.1 |
| G1.2 | Data Enrichment Pipeline | New contacts added to list | Per-event | Founder | Enrichment Engine - fully automated | G1.1, G1.8 | G1.3 |
| G1.3 | Lead Scoring | Enrichment complete | Per-event | Founder | manual -> target: Qualifier | G1.2 | G1.6, G3.2 |
| G1.4 | Intent Signal Monitoring | Continuous scan | Continuous | Founder | manual -> target: Event Scout | - | G1.1, G3.1 |
| G1.5 | Database Hygiene | Monthly cadence | Monthly | Founder | Deduplication Engine (semi-automated) | - | G1.1 |
| G1.6 | Prospect Research | Prospect enrolled in campaign | Per-event | Founder | Research Squad - fully automated | G1.3, G3.2 | G3.3 |
| G1.7 | ICP Segment Performance Review | Monday (weekly) | Weekly | Founder | /weekly-pulse + manual | G3.8, O3.2 | G1.1, F1.1 |
| G1.8 | External Source Import | Per-campaign | Per-event | Founder | /enrich-apollo + /leadsgorilla | - | G1.2 |

### Growth - G2: Warm

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| G2.1 | Weekly Content Calendar Generation | Friday afternoon | Weekly | Founder | /content-calendar -> target: Content Planner API | F1.3, F1.6 | G2.2 |
| G2.2 | Social Content Brief Creation | Calendar approved | Per-event | Founder | manual -> target: Content Planner API | G2.1 | G2.3 |
| G2.3 | Social Content Generation | Brief ready | Per-event | Founder | /content -> target: Content Gen API | G2.2 | G2.5 |
| G2.4 | Blog Content Generation | SEO topic selected | Per-event | Founder | Blog Publisher (semi-automated) | G2.9, G2.1 | G2.5 |
| G2.5 | Content QC & Approval | Content generated | Per-event | Founder | manual -> target: Content Approval UI | G2.3, G2.4 | G2.6, G2.7 |
| G2.6 | Social Publishing | Content approved | Per-event | Founder | manual -> target: Social Publisher API | G2.5 | G2.8, G2.12 |
| G2.7 | Blog Publishing | Blog approved | Per-event | Founder | Blog Publisher - fully automated | G2.5 | G2.8, G2.12 |
| G2.8 | Style Corrections Extraction | Content published | Per-event | Founder | Content Engine - fully automated | G2.6, G2.7 | G2.3 |
| G2.9 | SEO Research & Gap Analysis | Monthly cadence | Monthly | Founder | manual -> target: content-planner | - | G2.1, G2.4 |
| G2.10 | Intelligence Feed Review | Weekly cadence | Weekly | Founder | knowledge-base -> target: Content Platform | - | G2.1 |
| G2.11 | Newsletter Distribution | Weekly cadence | Weekly | Founder | manual -> target: Newsletter Platform | G2.6, G2.7 | G2.12 |
| G2.12 | Content Performance Review | Monday | Weekly | Founder | manual -> target: Content Analytics | G2.6, G2.7, G2.11 | G2.1, G2.9, O3.3 |

### Growth - G3: Book

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| G3.1 | Campaign Launch | Business decision to target segment | Per-event | Founder | Founder via /campaign-launcher | F1.4, G1.1, G1.4 | G3.2 |
| G3.2 | Prospect Enrollment | Campaign created and activated | Continuous | Founder | Campaign Enrollment Worker - fully automated | G3.1, G1.3 | G1.6, G3.3 |
| G3.3 | Pitch Strategy Generation | Research complete for prospect | Per-event | Founder | Pitch Strategist (semi-automated) | G1.6, G3.2 | G3.4 |
| G3.4 | Pitch Review & Approval | Pitch generated and queued | Daily | Founder | Founder via Review UI | G3.3 | G3.5 |
| G3.5 | Email Sequence Execution | Pitch approved | Continuous | Founder | Email Executor - fully automated | G3.4 | G3.6 |
| G3.6 | Response Handling | Reply received | Per-event | Founder | manual -> target: Response Classifier | G3.5 | G3.7, G3.8 |
| G3.7 | Meeting Scheduling | Positive response confirmed | Per-event | Founder | manual -> target: Calendar Scheduler | G3.6 | D1.2, O3.2 |
| G3.8 | Campaign Performance Review | Monday (weekly) | Weekly | Founder | /weekly-pulse + manual | G3.5, G3.6 | G1.7, G3.1, O3.4 |

---

### Operations - O1: Standardize

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| O1.1 | Repo Governance | New repo created or major change | Per-event | CTO | governance tool - fully automated | F3.1, F3.2 | O1.3 |
| O1.2 | Process Documentation | New process identified | Per-event | Founder | manual | - | O2.1 |
| O1.3 | Repo Health Check | Weekly cadence | Weekly | CTO | health check tool (semi-automated) | O1.1 | O2.5 |
| O1.4 | Contracts Sync | Contract file edited | Per-event | CTO | deploy tool - fully automated | O1.1 | O1.3 |
| O1.5 | Capability Registry Update | New project or agent added | Per-event | CTO | manual -> target: capabilities automation | F3.3, O2.1 | O1.3 |
| O1.6 | State File Maintenance | Session end | Per-event | Founder | /prepexit (semi-automated) | F3.5 | - |
| O1.7 | Knowledge Base Curation | Monthly cadence | Monthly | Founder | knowledge-base channel monitoring (semi-automated) | - | G2.10 |

### Operations - O2: Automate

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| O2.1 | Agent Development Cycle | Process documented and automation prioritized | Per-event | CTO | CTO + AI agent platform | O1.2 | O1.5, O2.2 |
| O2.2 | Deployment | PR merged or manual deploy | Per-event | CTO | Deployment Platform - fully automated | O2.1 | O2.5 |
| O2.3 | Integration Maintenance | API change or breakage detected | Per-event | CTO | CTO + manual | O2.5 | O2.2 |
| O2.4 | Multi-Session Orchestration | Parallel work needed | Per-event | Founder | worker accounts (semi-automated) | F3.4, F3.5 | O1.6 |
| O2.5 | Automation Health Monitoring | Daily cadence | Daily | CTO | logs + health endpoints (semi-automated) | O2.2 | O2.3 |
| O2.6 | New Skill Development | Repeated manual task identified | Per-event | Founder | /skill-forge (semi-automated) | O1.2 | O1.5 |

### Operations - O3: Instrument

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| O3.1 | Weekly Scorecard Review | Monday | Weekly | Founder | manual -> target: Content Platform | - | O3.2 |
| O3.2 | Pipeline Value Tracking | Daily cadence | Daily | Founder | CRM + /weekly-pulse (semi-automated) | G3.7, G3.8 | F4.5, O3.1 |
| O3.3 | Content Attribution | Weekly cadence | Weekly | Founder | manual -> target: Content Analytics | G2.12 | O3.1 |
| O3.4 | Campaign ROI Calculation | Campaign end or monthly | Monthly | Founder | manual | G3.8 | O3.1, G3.1 |
| O3.5 | MRR Tracking | Month-end | Monthly | Founder | finance-tracker + CRM (semi-automated) | D1.3 | F4.1, O3.1 |
| O3.6 | North Star Dashboard | Always-on (planned) | Continuous | Founder | manual -> target: Content Analytics | O3.1, O3.2, O3.3, O3.5 | - |

---

### Delivery - D1: Deliver

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| D1.1 | Client Onboarding | Deal closed | Per-event | Founder | manual | F1.5, F2.3, F2.5 | D1.2 |
| D1.2 | Kickoff Meeting | Onboarding start | Per-event | Founder | manual | D1.1, G3.7 | D1.3 |
| D1.3 | Monthly Delivery Execution | Monthly cadence | Monthly | Founder | manual (agent-assisted) | D1.2 | D1.4, D2.1 |
| D1.4 | Client Communication | Weekly cadence | Weekly | Founder | manual | D1.3 | D3.1 |
| D1.5 | Scope Management | Client request received | Per-event | Founder | manual | D1.2 | D1.3 |
| D1.6 | Quality Assurance Review | Before delivery | Per-event | Founder | manual + QC gates | D1.3 | D2.1 |

### Delivery - D2: Prove

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| D2.1 | Results Documentation | Month-end per client | Monthly | Founder | manual -> target: agent-drafted | D1.3, D1.6 | D2.2 |
| D2.2 | ROI Calculation | Quarterly per client | Monthly | Founder | manual | D2.1 | F2.1, F2.2, F4.2 |
| D2.3 | Case Study Creation | Significant result achieved | Per-event | Founder | manual -> target: /case-study-builder | D2.1, D2.2 | D2.5, G2.4 |
| D2.4 | Testimonial Collection | 90-day milestone | Per-event | Founder | manual | D2.1 | D2.5, G2.3 |
| D2.5 | Proof Asset Distribution | Case study or testimonial complete | Per-event | Founder | manual -> target: Content Engine | D2.3, D2.4 | G2.1, G2.3 |

### Delivery - D3: Expand

| ID | Name | Trigger | Freq | Owner | Executor | Upstream | Downstream |
|----|------|---------|------|-------|----------|----------|------------|
| D3.1 | Client Health Scoring | Weekly cadence | Weekly | Founder | manual -> target: CRM health score | D1.4, F1.5 | D3.2, D3.5 |
| D3.2 | Expansion Opportunity ID | Health score > 80 | Per-event | Founder | manual | D3.1 | D3.3 |
| D3.3 | Renewal Management | 60 days before renewal | Per-event | Founder | manual | D3.2 | D1.1 |
| D3.4 | Referral Ask | Success milestone | Per-event | Founder | manual | D2.3 | G1.1 |
| D3.5 | Churn Prevention | Health score < 40 | Per-event | Founder | manual | D3.1 | D1.4 |

---

## Wiring Summary

Cross-pillar connections (blocks that feed across pillar boundaries):

| From | To | What Flows |
|------|-----|-----------|
| F1.1 -> G1.1 | ICP definition feeds list building |
| F1.3 -> G2.1, G2.3, G3.3 | Updated messaging feeds content + pitches |
| F1.4 -> G3.1 | Wedge strategy feeds campaign targeting |
| F2.5 -> G3.1, D1.1 | Install sprint pipeline feeds campaigns + onboarding |
| G1.7 -> F1.1 | Segment performance feeds ICP review |
| G2.12 -> O3.3 | Content performance feeds attribution |
| G3.7 -> D1.2, O3.2 | Meetings feed kickoff + pipeline tracking |
| G3.8 -> O3.4 | Campaign metrics feed ROI calculation |
| D1.3 -> O3.5 | Delivery execution feeds MRR tracking |
| D2.2 -> F2.1, F2.2, F4.2 | Client ROI feeds pricing + unit economics |
| D2.3 -> G2.4 | Case studies feed blog content |
| D2.5 -> G2.1, G2.3 | Proof assets feed content pipeline |
| D3.4 -> G1.1 | Referrals feed list building |
| F3.5 -> O2.4 | Session coordination feeds multi-session orchestration |
| O1.2 -> O2.1 | Documented processes feed agent development |
| O3.2 -> F4.5 | Pipeline data feeds revenue forecast |

---

## Status Key

- **- fully automated**: No human in the loop during execution
- **(semi-automated)**: Human triggers or reviews, but execution is automated
- **manual -> target: X**: Currently manual, target automation is X
- **manual**: Currently manual, no specific automation target yet
