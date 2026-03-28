# List Building SOP

Step-by-step from ICP definition to verified, send-ready prospect list. This is a repeatable process. Run it the same way every time.

---

## Prerequisites

- [ ] ICP worksheet complete: `playbooks/find/templates/icp-worksheet.md`
- [ ] Access to at least one list-building tool (Apollo, LinkedIn Sales Navigator, Hunter.io, or a lead pack)
- [ ] Email verification tool available (NeverBounce, ZeroBounce, Millionverifier)
- [ ] Target list size defined (recommend 200-500 for a first cohort)

---

## Phase 1: Define the Filter Criteria

Pull directly from your ICP worksheet. Do not build the list until all five filters are defined.

| Filter | Your value | Source |
|--------|-----------|--------|
| Industry | [specific vertical, not "B2B"] | ICP worksheet Layer 1 |
| Revenue range | [$X to $Y] | ICP worksheet Layer 2 |
| Headcount range | [X to Y employees] | ICP worksheet Layer 2 |
| Geography | [city, region, or country] | ICP worksheet Layer 3 |
| Decision-maker title | [exact title or title variants] | ICP worksheet Layer 3 |

**Buying trigger filter (if available in your tool):**
- Hiring for [specific role] -- signals they have the problem
- Recent funding -- signals budget and growth pressure
- New leadership -- new decision-makers often replace vendors
- Recent expansion -- signals scale challenges
- Technology stack signals -- using [X tool] often means they have [Y gap]

The more specific your filters, the less time you waste on contacts who will never buy.

---

## Phase 2: Source the List

### Option A: Apollo (recommended for most ICPs)

1. Go to People search
2. Apply filters: job title, industry, headcount, geography, seniority
3. Add buying trigger filter if applicable (e.g., "hiring for SDR" in job postings)
4. Review first 20 results manually -- do they match your ICP? If not, tighten the filters
5. Export 200-500 contacts per cohort
6. Export fields: First Name, Last Name, Title, Company, Email, LinkedIn URL, Company Size, Industry

**Apollo filter tips:**
- Use "include similar titles" to catch variants (VP Sales / Head of Sales / Sales Director)
- Filter by "verified email" to reduce bounce rate at source
- Sort by "last active" to prioritize contacts who are reachable

### Option B: LinkedIn Sales Navigator

1. Use People search with Lead Filters
2. Apply: title, seniority, geography, industry, company headcount
3. Add "posted on LinkedIn in last 30 days" filter -- raises response rate significantly
4. Save leads to a list
5. Export via a scraping tool (PhantomBuster, Evaboot) or manually pull emails via Hunter.io

**LinkedIn tips:**
- Max 2,500 saved leads per list
- Cross-reference with Apollo for email addresses
- "Changed jobs in last 90 days" is a strong buying trigger filter

### Option C: Lead Packs (if LEAD_PACKS_KEY is set)

Access pre-built, verified contact lists by vertical and geography. Skip Phase 2 and go directly to Phase 3 for additional quality filtering.

### Option D: Manual Research (high-value singular leads)

For enterprise or high-ACV targets where the deal justifies 30+ minutes of research per contact:
1. Find company via LinkedIn, Crunchbase, or G2
2. Identify decision-maker via LinkedIn org chart search
3. Find email via Hunter.io, Apollo single-contact search, or LinkedIn email reveal tools
4. Document company-specific trigger and personalization data in a research notes column
5. Write a singular sequence (not batch) -- every word unsendable to anyone else

---

## Phase 3: Enrich

Add the context you need to personalize the first line of each email.

**Minimum enrichment per contact:**
- Verify title is current (LinkedIn)
- Note one company-specific signal (recent news, job posting, technology they use)
- Confirm they are in a buying window (trigger event if possible)

**Enrichment tools:**
- Clearbit / Lusha / RocketReach: firmographic data
- BuiltWith / Wappalyzer: technology stack
- LinkedIn: recent activity, posts, announcements
- Google News: company news in last 90 days

**Enrichment field to add to your spreadsheet:**
- `personalization_note`: one-line observation for Email 1 hook
- `trigger`: the specific event that makes them a buyer now
- `peer_company`: a company they would recognize that you've worked with

---

## Phase 4: Verify

Do not send to an unverified list. Bounces above 3% will damage your sending domain.

**Verification process:**

1. Export email column to CSV
2. Upload to email verification tool (NeverBounce, ZeroBounce, or Millionverifier)
3. Run verification
4. Download results and remove:
   - Invalid: hard bounce, do not send
   - Catch-all with low confidence: remove if you cannot verify further
   - Duplicate: deduplicate on email address
5. Target: 95%+ deliverable contacts before importing to sending tool

**Bounce rate benchmarks:**
- Below 2%: clean list, safe to send
- 2-5%: acceptable, monitor closely
- Above 5%: list quality problem. Do not scale. Reverify or rebuild.

---

## Phase 5: Segment

Before importing, split into cohorts for testing.

**Recommended first-run structure:**

| Cohort | Size | Purpose |
|--------|------|---------|
| A | 50-100 | First test batch. Send before scaling. |
| B | 100-200 | Second batch after A is evaluated. |
| C | Remainder | Scale once sequence is proven. |

**Why cohorts matter:** A sequence change on cohort A does not contaminate B or C. You can test subject lines, openers, or CTAs on cohort A before committing the whole list.

**Segment by firmographic fit:**
- Tier 1: Perfect ICP match (all filters match + buying trigger present)
- Tier 2: Strong ICP match (all filters match, no confirmed trigger)
- Tier 3: Partial ICP match (2-3 filters match)

Send Tier 1 first with a singular sequence. Send Tier 2-3 with a batch sequence.

---

## Phase 6: Import and Schedule

1. Import verified, segmented list into sending tool (Instantly, Smartlead, Reply.io, Clay)
2. Map fields: first_name, last_name, email, company, personalization_note, trigger
3. Set daily send limit: start at 20/day per inbox. Scale up by 20/week.
4. Set send window: Tuesday-Thursday, 8am-10am recipient local time
5. Turn on open tracking (optional) and click tracking (optional)
6. Confirm reply-to address is monitored

---

## Quality Gates Before Launch

- [ ] Filters match ICP worksheet exactly
- [ ] 200+ contacts in first cohort
- [ ] Bounce rate below 3% after verification
- [ ] At least one personalization field populated per contact
- [ ] Sending infrastructure checked (separate domain, SPF/DKIM/DMARC, warmup running 2+ weeks)
- [ ] Daily send limit set (start at 20/day)
- [ ] Reply monitoring confirmed

---

## Iteration Log

After the first 100 sends, record:

| Date | Cohort | Contacts sent | Open rate | Reply rate | Change made |
|------|--------|--------------|-----------|-----------|------------|
| | | | | | |

Change one variable at a time. Evaluate after every 100 sends.

---

## Reference

- ICP worksheet: `playbooks/find/templates/icp-worksheet.md`
- Full G1 Find playbook: `playbooks/find/README.md`
- Cold email sequence: `playbooks/book/cold-email/templates/sequence-b2b.md`
