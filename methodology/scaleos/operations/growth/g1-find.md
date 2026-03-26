# G1: Find -- Prospecting & List Building

> **North Star Metric:** 50+ qualified prospects entering pipeline per week

---

## Processes

### G1.1 ICP List Building

| Field | Value |
|-------|-------|
| **Trigger** | Campaign launch decision or segment expansion needed |
| **Frequency** | Per-campaign (roughly monthly) |
| **Input** | ICP definition, target segment, geographic focus |
| **Output** | Prospect list with enriched contacts (target: 100-1,000 per campaign) |
| **Test** | List created with 80%+ ICP match rate; at least 100 contacts with valid email |

**Steps:**
1. Define segment from ICP doc (strategic decision)
2. Search existing contact database for matches
3. If gap, source from prospecting tools with ICP filters
4. Import and enrich new contacts
5. Create campaign list
6. Review list quality and ICP fit (quality gate)

---

### G1.2 Data Enrichment Pipeline

| Field | Value |
|-------|-------|
| **Trigger** | New contacts added to database (batch or individual) |
| **Frequency** | Per-batch (every import or new contact event) |
| **Input** | Raw contact records (name, company, email/LinkedIn) |
| **Output** | Enriched records with verified email, company data, social profiles |
| **Test** | 90%+ email verification rate; company data populated for 80%+ of records |

**Steps:**
1. Import triggers enrichment job automatically
2. Email discovery
3. Email verification
4. Company data enrichment
5. Social profile discovery when triggered
6. Results stored in contact database

---

### G1.3 Lead Scoring

| Field | Value |
|-------|-------|
| **Trigger** | Enrichment complete for a batch |
| **Frequency** | Per-enrichment batch |
| **Input** | Enriched contact records, ICP criteria, historical conversion data |
| **Output** | Scored prospects (A/B/C tier) ready for campaign enrollment |
| **Test** | A-tier prospects convert to meetings at 2x+ rate of C-tier |

**Steps:**
1. Review enriched data against ICP criteria
2. Tag prospects by tier
3. Enroll A-tier in campaigns first

**Target automation:**
- Qualifier agent auto-scores on firmographic + behavioral signals
- Auto-tier and tag
- A-tier auto-enrolled, B-tier queued

---

### G1.4 Intent Signal Monitoring

| Field | Value |
|-------|-------|
| **Trigger** | Daily scan (continuous) |
| **Frequency** | Daily |
| **Input** | Target company list, industry keywords, funding databases, job boards |
| **Output** | Signal alerts: "Company X just raised funding / hired CMO / posted about pain point" |
| **Test** | 5+ actionable signals per week identified and routed to outreach |

**Steps:**
1. Check LinkedIn feed for ICP signals
2. Scan Crunchbase/TechCrunch for funding
3. Route high-intent signals to outreach

**Target automation:**
- Daily automated scan of funding events, hiring signals, content engagement
- High-intent signals auto-create prospect records with intent tags
- Priority outreach enrollment triggered by signal

---

### G1.5 Database Hygiene

| Field | Value |
|-------|-------|
| **Trigger** | Monthly cadence + pre-campaign check |
| **Frequency** | Monthly |
| **Input** | Full contact database |
| **Output** | Clean database: duplicates merged, bounced emails removed, stale contacts flagged |
| **Test** | Bounce rate below 3% on next campaign; zero duplicate sends |

**Steps:**
1. Run deduplication match finder
2. Review and merge duplicates (manual -- avoids data loss)
3. Re-verify emails older than 90 days
4. Remove hard bounces from active lists
5. Flag contacts with no engagement in 6+ months

---

### G1.6 Prospect Research

| Field | Value |
|-------|-------|
| **Trigger** | Prospect enrolled in campaign |
| **Frequency** | Per-prospect (batch via campaign) |
| **Input** | Prospect name, company, LinkedIn URL, enriched data |
| **Output** | Research dossier: company context, recent activity, pain points, talking points |
| **Test** | Dossier generated for 90%+ enrolled prospects within 24 hours |

**Steps:**
1. Campaign enrollment triggers research task dispatch
2. Research agent scrapes LinkedIn + web
3. Company researcher gathers company intel
4. Research dossier compiled and stored
5. Passed to pitch strategist for email crafting

---

### G1.7 ICP Segment Performance Review

| Field | Value |
|-------|-------|
| **Trigger** | Monday (weekly cadence) |
| **Frequency** | Weekly |
| **Input** | Campaign data by segment, reply rates, meeting rates, deal values |
| **Output** | Segment report: which ICPs convert, which don't, reallocation recommendations |
| **Test** | Report every Monday; at least 1 segment reallocation per month |

**Steps:**
1. Pull campaign data from sequencer
2. Cross-reference with CRM pipeline
3. Identify top/bottom segments
4. Adjust next campaign targeting

---

### G1.8 List Import from Prospecting Tools

| Field | Value |
|-------|-------|
| **Trigger** | Database lacks sufficient contacts for target segment |
| **Frequency** | Per-campaign |
| **Input** | CSV export from prospecting tool (Apollo, LeadsGorilla, etc.) |
| **Output** | Imported and enriched contacts in database |
| **Test** | 80%+ import success rate; enrichment triggered automatically |

**Steps:**
1. Export from prospecting tool with ICP filters
2. Import CSV
3. Trigger enrichment pipeline
4. Review import results, fix failures

---

## Agent Architecture

| Agent | Status | Covers |
|-------|--------|--------|
| Data Enrichment Engine | Active | G1.2, G1.5 |
| Research Squad | Active | G1.6 |
| Campaign Enrollment Worker | Active | G1.6 trigger |
| Qualifier Agent | Planned | G1.3 |
| Intent Scout Agent | Planned | G1.4 |
| Import Dedup Agent | Planned | G1.5, G1.8 |

**Build priorities:**
1. Qualifier agent for auto-scoring (G1.3)
2. Intent Scout for signal monitoring (G1.4)
3. Import dedup pre-check (G1.8)
