# Canonical Dictionary

> Every system, agent, skill, repo, role, and platform name in a process block MUST match an entry here.
> If a term is not in this dictionary, it cannot appear in a block. Add it here first.
> The `/scaleos-block-writer` skill validates against this file automatically.

---

## 1. Systems

External tools, databases, and infrastructure services.

| Canonical Name | Also Known As (DO NOT USE) | What It Is |
|---|---|---|
| **Contact Database** | contact DB, CDB | Proprietary contact database with enrichment, deduplication, and list management |
| **CRM** | CRM platform | Customer relationship management system for contacts, companies, deals, email campaigns |
| **Email Sequencer** | email outreach platform | Email outreach platform for sequence execution and campaign management |
| **Deployment Platform** | backend deployment | Infrastructure-as-code deployment platform for hosted services |
| **Email Infrastructure** | cold email infrastructure | Email delivery infrastructure; multiple mailboxes across multiple domains |
| **Profile Scraper** | LinkedIn scraper, web scraper | Third-party API for social profile scraping and web data extraction |
| **Email Finder** | email discovery | Email address discovery service; part of the enrichment pipeline |
| **Email Verifier** | email verification service | Email verification and deliverability checking service |
| **Google Workspace** | Google Docs, Google Drive, Gmail | Email, document collaboration, file storage |
| **Task Manager** | task management platform | Task and project management for coordination |
| **Slack** | messaging, comms | Team communication, notifications, bot integration |
| **GitHub** | version control | Version control and issue tracking |
| **Transcription Service** | meeting recorder | Meeting transcription and note extraction |
| **LLM Provider** | AI model, GPT | Primary large language model provider for agent workloads |
| **AI Agent Platform** | agent runtime | Platform for building and deploying AI agents and automations |
| **Calendar Scheduler** | meeting scheduler | Automated meeting scheduling |
| **Newsletter Platform** | email newsletter | Email newsletter distribution |
| **Lead Database** | contact database external | External lead database; CSV export or API |
| **Local Leads API** | local business search | Local business search platform via API |
| **Automation Platform** | workflow automation | Workflow automation platform |
| **Research Engine** | deep-research | AI-powered research engine |
| **Search Console** | GSC | SEO performance data including search queries, indexing, and click-through rates |
| **Funding Database** | company funding data | Company and funding data source for research |
| **Review UI** | pitch review interface | Web UI for reviewing and approving outreach pitches |
| **Content Platform** | content dashboard | Unified content platform for calendar, approval, and analytics |

## 2. Agents

AI agents, squads, and automated workers.

| Canonical Name | Also Known As (DO NOT USE) | What It Is |
|---|---|---|
| **Research Squad** | prospect researcher pair | Agent pair for prospect and company research |
| **Person Researcher** | LinkedIn scraper agent | Component agent; scrapes profiles and web sources for prospect data |
| **Company Researcher** | company intel agent | Component agent; gathers company background and context |
| **Pitch Strategist** | email strategist | Agent that generates personalized pitches from multiple value prop angles |
| **Email Executor** | email execution agent | Agent that executes email sequences via the email sequencer |
| **Email Composer** | email generator | Component; composes personalized emails |
| **SDR Squad** | Sales Development Reps | Agent collection: Company Researcher, Person Researcher, Qualifier, Hook Generator, Email Composer, Sequencer |
| **Qualifier** | lead scoring agent | Agent (planned); auto-scores prospects on ICP fit |
| **Hook Generator** | subject line generator | Component; generates compelling email hooks |
| **Sequencer** | follow-up builder | Component; builds follow-up sequence strategy |
| **Chief of Staff Agent** | coordinator bot | Coordination agent; tells founder what to work on and routes tasks |
| **Content Engine** | content production engine | System that generates social media content in the founder's voice |
| **Blog Publisher** | autoblog worker, blog worker | Deployed worker; blog content generation and multi-platform publishing |
| **Campaign Enrollment Worker** | enrollment executor | Component; picks prospects from lists and dispatches research |
| **Event Scout** | signal monitor | Agent (planned) that scans funding, hiring, and industry signals |
| **Response Classifier** | email classifier | Agent (planned) that auto-classifies email replies |
| **Content Squad** | automated content agents | Future agent squad for automated content pipeline |
| **Enrichment Engine** | contact enrichment | Subsystem; email finder + verifier + web scrapers for data enrichment |
| **Deduplication Engine** | dedup agent | Subsystem; finds and merges duplicate contacts |
| **SEO Linker** | internal link checker | Post-publish agent; checks and suggests internal links |
| **Content Gen API** | content generation API | Planned always-on API for content generation |
| **Content Planner API** | calendar API | Planned API for calendar and brief automation |
| **Social Publisher API** | publishing API | Planned API for automated social media publishing |
| **Content Approval UI** | approval interface | Planned web UI for content QC and approval with AI pre-check |
| **Content Analytics** | analytics dashboard | Planned analytics dashboard for content performance tracking |

## 3. Skills

Claude Code skills (invoked with `/` prefix).

| Canonical Name | Also Known As (DO NOT USE) | What It Is |
|---|---|---|
| **/content** | social media generator | Generates social content (LinkedIn, Facebook, X) from briefs in founder's voice |
| **/content-calendar** | calendar generator | Generates weekly content calendars with topic seeds from channel profiles |
| **/contactdb** | contact search | Searches, imports, and enriches contacts in contact database |
| **/campaign-launcher** | campaign creator | Creates outreach campaigns from contact lists |
| **/enrich-apollo** | Apollo importer | Imports Apollo CSV exports and triggers enrichment |
| **/leadsgorilla** | local business search | Local business prospecting integration |
| **/weekly-pulse** | weekly metrics | Generates weekly performance metrics across campaigns and pipeline |
| **/clickup** | task management | Accesses task manager for task operations |
| **/prepexit** | session cleanup | Logs session state and ensures standards before ending session |
| **/prepstart** | session start | Loads context and checks active plans at session start |
| **/hubspot-content** | blog publishing | Publishes blog content to CMS |
| **/hubspot-sales** | deal management | Creates contacts, deals, logs activities in CRM |
| **/scaleos-block-writer** | block writer | Generates, validates, and assembles ScaleOS process blocks (this system) |

## 4. Repos

Repository types and their purposes.

| Canonical Name | Also Known As (DO NOT USE) | What It Is |
|---|---|---|
| **content-production** | social content execution | Execution layer - social media content generation |
| **autoblog** | blog execution | Execution layer - blog content generation and multi-platform publishing |
| **outreach-agent** | growth execution, CampaignOS | Execution layer - outreach; SDR, Engage, Research squads |
| **task-manager** | coordinator backend | Prioritization layer - Chief of Staff queue, approval workflow, dispatch |
| **knowledge-base** | business KB | Research library; sourced videos and claims |
| **playbook** | business SSOT | Business positioning SSOT - content pillars, SEO topics, ICP, pricing |
| **brand-repo** | brand SSOT | Brand voice, positioning, themes, and audience |
| **scaleos** | ScaleOS methodology | Foundational IP - handbook, assessments, operational blueprint |
| **entity-api** | entity SSOT | Entity identity resolution API |
| **content-planner** | ContentOS API | Content planning and measurement |
| **seo-linker** | SEO tool | SEO tool - internal linking analysis |
| **finance-tracker** | personal finance | Personal finance and business finance tracking |
| **governance** | system contracts | System standards, schemas, coordination |

## 5. Roles

Human roles and their scopes.

| Canonical Name | Also Known As (DO NOT USE) | What It Is |
|---|---|---|
| **Founder** | CEO, owner | Primary decision maker; Growth owner (G1-G3), Delivery owner (D1-D3), brand, strategy |
| **CTO** | Co-founder tech, technical lead | Technical co-founder; Operations owner (O1-O3), infrastructure, agent development |

## 6. Platforms

Publishing and distribution channels.

| Canonical Name | Also Known As (DO NOT USE) | What It Is |
|---|---|---|
| **LinkedIn** | professional network | Primary social platform; thought leadership, networking |
| **Facebook** | FB, Meta | Secondary social platform; community engagement |
| **X** | Twitter, X/Twitter | Real-time social platform; engagement and visibility |
| **HubSpot CMS** | HubSpot blog | Blog publishing platform within HubSpot |
| **WordPress** | WP | Blog publishing platform for multi-brand blogs |
| **Medium** | Medium publication | Blog syndication platform |
| **Substack** | Substack newsletter | Newsletter and blog publication platform |
| **Beehiiv** | newsletter (planned) | Email newsletter distribution |
| **Skool** | community platform | Community hosting platform |
| **YouTube** | video platform | Video hosting and research source |

---

## Usage Rules

1. **Exact match only.** If a term is not in this dictionary by its canonical name, validation fails.
2. **Add before use.** New terms must be added to this dictionary before they can appear in any block.
3. **One name per thing.** If the same tool appears in two categories, pick the primary category.
4. **Planned = noted.** Terms marked "(planned)" or "(not yet built)" are valid but signal the process depends on future work.
