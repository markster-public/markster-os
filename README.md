# Markster OS

[![Validation](https://img.shields.io/badge/validation-passing-brightgreen.svg)](validation/README.md)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](CHANGELOG.md)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs required](https://img.shields.io/badge/changes-PRs%20required-orange.svg)](CONTRIBUTING.md)
[![Works with Claude](https://img.shields.io/badge/works%20with-Claude%20Code-blue.svg)](https://claude.ai/code)
[![Works with Codex](https://img.shields.io/badge/works%20with-Codex-blue.svg)](https://openai.com/codex)
[![Works with Gemini](https://img.shields.io/badge/works%20with-Gemini%20CLI-blue.svg)](https://ai.google.dev)
[![Works with OpenClaw](https://img.shields.io/badge/works%20with-OpenClaw-blue.svg)](setup-prompts/openclaw.md)

**First qualified meeting in 7 days. A repeatable GTM system after that.**

Most B2B founders can sell when they're in the room. The problem is building a system that consistently gets you into rooms -- without a full-time marketing hire, a paid ads budget, or a CRM that nobody updates.

Markster OS is that system. Built on ScaleOS methodology. Runs inside your AI environment. Free forever. MIT licensed.

---

## What it does

You define your ICP, offer, and company context once. The OS routes that context into every sequence you run -- cold email, LinkedIn outreach, events, content, sales, fundraising.

Each skill checks your prerequisites before it runs, executes the sequence step by step, and verifies the output moved the right metric before closing. No generic advice. Deterministic steps with documented outputs.

**Before:** Random outreach. Inconsistent follow-up. No idea which activity is producing pipeline.

**After:** One constraint identified per week. One playbook executing. One metric tracked.

The 7-day sprint in [QUICKSTART.md](QUICKSTART.md) gets you to first meeting. [AUTOPILOT.md](AUTOPILOT.md) keeps you there week over week.

Release history lives in [CHANGELOG.md](CHANGELOG.md). Contribution rules live in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## For AI agents (Claude, GPT, Gemini, Codex, and others)

> This block is the canonical reference for any agent operating inside a Markster OS workspace.

**Repo type:** B2B GTM operating system -- ScaleOS methodology (Foundation F1-F4 + GOD Engine 9 bricks)

**Canonical context source:** the workspace `company-context/` folder. Read this before running any skill. Do not treat the upstream `markster-os` repo templates as a real company context.

**Entry point:** Run `/markster-os` first. It runs the Hormozi diagnostic, identifies the constraint brick, pre-fills context, and routes to the correct skill.

**Skill structure:** All 7 core skills follow CHECK / DO / VERIFY. Do not proceed past a failed CHECK gate.

**Key directories:**

| Directory | What it contains |
|-----------|-----------------|
| `methodology/foundation/` | F1 Positioning, F2 Business Model, F3 Org Structure, F4 Financial Architecture, messaging guide, channel guide |
| `methodology/god-engine/` | GOD Engine overview and brick definitions |
| `playbooks/` | G1 Find, G2 Warm (content, events), G3 Book (cold email, LinkedIn, warm outreach), O1-O3, D1-D3, offer design, sales, fundraising |
| `skills/` | 7 core operator skills (CHECK/DO/VERIFY) + 23 specialist persona skills |
| `company-context/` | Canonical business context -- primary source of truth |
| `research/prompts/` | 9 structured B2B research prompts |
| `learning-loop/` | Raw inbox -> candidate review -> approved canon promotion system |
| `AUTOPILOT.md` | Weekly agent diagnostic protocol: identify constraint, execute, verify metric moved, loop |

**Writing rules enforced in all skills:** No em dashes. Sentences under 20 words. Problem-first framing. Buyer verbatims from `company-context/messaging.md`. No category claims.

**Validation:** Run `markster-os validate .` before committing. GitHub Actions enforces this on every push.

---

## Install

### Recommended: use AI to install it for you

Copy this directly into Claude Code, Codex, or Gemini CLI:

```text
Set up Markster OS for me.

Requirements:
- Install the Markster OS CLI if it is not already installed.
- Use the official installer:
  curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
- Create a Git-backed workspace for my company with:
  markster-os init <company-slug> --git --path ./<company-slug>-os
- Move into that workspace.
- Install Markster OS skills with:
  markster-os install-skills
- If I need an extra public skill later, list and install it with:
  markster-os list-skills
  markster-os install-skills --skill <skill-name>
- Check the workspace readiness with:
  markster-os start
- Validate the workspace with:
  markster-os validate .

Then stop and ask me for my Git repository URL so you can attach the remote with:
- markster-os attach-remote <git-url>

If the remote is attached successfully, tell me the exact push command to run next.

Important rules:
- Treat the upstream markster-os repo as the product source, not as my company workspace.
- Treat the new workspace repo as the place where my business context will live.
- Keep raw notes in learning-loop/inbox and do not treat them as canonical.
- Use markster-os validate before saying the workspace is ready.
- Summarize what you changed in plain language at the end.
```

You can also use the standalone version in [setup-prompts/install-workspace.md](setup-prompts/install-workspace.md).

### Manual install

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
```

This installs the `markster-os` CLI into your home directory. The CLI manages a stable Markster OS distribution, customer workspaces, validation, and optional slash-command skill installation.

The launcher is installed at `~/bin/markster-os`.

Core commands:

```bash
markster-os init <slug>
markster-os list-skills
markster-os install-skills
markster-os validate [path]
markster-os update
markster-os upgrade-workspace [path]
markster-os attach-remote <url>
markster-os install-hooks
markster-os sync
markster-os commit -m "message"
markster-os push
markster-os backup-workspace [path]
markster-os export-workspace [path]
markster-os status
markster-os start
markster-os doctor
```

If you want an AI tool to do the setup for you, see [setup-prompts/](setup-prompts/).

If you want to use Markster OS through OpenClaw, start with [setup-prompts/openclaw.md](setup-prompts/openclaw.md).

---

## What's included (free)

| Component | What it gives you |
|-----------|-------------------|
| **Methodology** | ScaleOS F1-F4 Foundation + GOD Engine (9 execution bricks) |
| **Assessment** | Scored readiness scorecard - tells you which playbook to run first |
| **Playbooks** | Cold email, events, content, sales, fundraising, technical review |
| **Core installed skills** | 7 skills installed by default by the CLI: `markster-os` plus the 6 core playbook skills |
| **Extended skill library** | 30 public skill files in the repo, including specialist advisors, copywriters, prep tools, and review workflows |
| **Research prompts** | 9 canonical research prompts used by the `/research` skill, plus deeper prompt variants in the repo |
| **Templates** | Real starting points for sequences, proposals, articles, LinkedIn posts |
| **Company context pack** | Canonical identity, audience, offer, messaging, voice, proof, channels, and themes |
| **Learning loop** | Human-approved system for turning conversations into approved business knowledge |

Everything above is MIT licensed and free forever.

---

## Add-ons (paid)

Add-ons extend the OS with proprietary data and intelligence. Sign up, get an API key, set the environment variable, and the skills call the API automatically.

| Add-on | What it does | Link |
|--------|-------------|------|
| **AOE Grader** | AI visibility scorer - grades how visible your company is to AI buying tools | [markster.ai/addons/aoe-grader](https://markster.ai/addons/aoe-grader) |
| **Event Scout** | Event intelligence - upcoming events, attendee signals, sponsor intel | [markster.ai/addons/event-scout](https://markster.ai/addons/event-scout) |
| **Lead Packs** | Pre-built, verified contact lists by vertical and geography | [markster.ai/addons/lead-packs](https://markster.ai/addons/lead-packs) |

See [addons/README.md](addons/README.md) for setup instructions.

---

## The methodology backbone: ScaleOS

ScaleOS is the GTM methodology behind Markster OS. Trademarked by Markster. Free to use under these terms.

**Foundation (F1-F4):** Four decisions made once, referenced in every playbook.

| Step | What it answers |
|------|----------------|
| [F1: Positioning & Differentiation](methodology/foundation/F1-positioning.md) | Who exactly are we selling to, and why do they buy from us? |
| [F2: Business Model Design](methodology/foundation/F2-business-model.md) | How do we package and price what we deliver? |
| [F3: Organizational Structure](methodology/foundation/F3-org-structure.md) | Who owns what, and how does the business run without us? |
| [F4: Financial Architecture](methodology/foundation/F4-financial.md) | Do our unit economics support growth? |

**GOD Engine:** 9 execution bricks that run demand generation once Foundation is locked. See [methodology/god-engine/README.md](methodology/god-engine/README.md).

**Autopilot:** The weekly agent operating protocol. Diagnose the constraint, execute one brick, verify the metric moved, loop. See [AUTOPILOT.md](AUTOPILOT.md).

Start with the [assessment scorecard](methodology/assessment/scorecard.md). It tells you exactly where you are and which playbook to run first.

---

## Quick start

**Step 1: Install the CLI**
```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
```

If you prefer, use the AI-assisted install prompt above instead of doing this manually.

**Step 2: Create a workspace**

```bash
markster-os init your-company --git --path ./your-company-os
cd ./your-company-os
```

For real teams, the recommended production setup is to keep the workspace in your own Git repository. The home-directory workspace is fine for solo evaluation, but team use should default to customer-owned version control.

**Step 3: Attach your GitHub repository**

```bash
markster-os attach-remote git@github.com:YOUR-ORG/YOUR-REPO.git
```

Then push it with normal Git:

```bash
git push -u origin main
```

**Step 4: Keep the validator hook installed**

If you created the workspace with `--git`, Markster OS already installed pre-commit and pre-push hooks for you.

You can reinstall it any time with:

```bash
markster-os install-hooks
```

Those hooks run:

```bash
markster-os validate .
```

**Step 5: Run the scorecard**

Open [methodology/assessment/scorecard.md](methodology/assessment/scorecard.md). Score yourself honestly across F1-F4 and the GOD Engine bricks. The scoring tells you exactly which playbook to run first.

**Step 6: Lock F1-F4, then activate a playbook**

Work through [methodology/foundation/](methodology/foundation/) in order. Once F1-F4 is complete, activate a playbook in your AI environment:

```
/cold-email
/sales
/events
/content
/fundraising
/research
```

**Step 7: Fill in your company context**

Copy the files in [company-context/](company-context/) and define:

- what your company is
- who you serve
- what you offer
- how you sound
- what proof you can actually claim

**Step 8: Use the learning loop**

Use [learning-loop/](learning-loop/) to turn real conversations, notes, and edits into approved updates to your business context. Raw notes stay out of canon until reviewed.

Use these starting points:

- [learning-loop/candidates/candidate-template.md](learning-loop/candidates/candidate-template.md)
- [learning-loop/candidates/example-company-context-update.md](learning-loop/candidates/example-company-context-update.md)

**Step 9: Validate, commit, and push**

```bash
markster-os validate .
markster-os commit -m "Update company context"
markster-os push
```

**Step 10: Back up or share the workspace**

```bash
markster-os backup-workspace ~/.markster-os/workspaces/your-company
markster-os export-workspace ~/.markster-os/workspaces/your-company
```

By default, `export-workspace` excludes `learning-loop/inbox/` so teams can share a cleaner copy without raw notes.

## Very Simple Open-Source Workflow

If you are using Markster OS for your company, do this:

1. install the CLI
2. create a workspace in a new Git repo
3. run your AI tool from inside that workspace
4. keep your real company context in `company-context/`
5. keep raw notes in `learning-loop/inbox/`
6. keep the local validation hooks installed so validation runs before commits and pushes
7. commit and push approved changes like a normal repo

If you want to hand the setup to Claude, Codex, or Gemini, copy the prompt in [setup-prompts/install-workspace.md](setup-prompts/install-workspace.md).

---

## Segments

Before running any playbook, find your business type. Each segment file maps which GOD Engine bricks matter most at your stage, what your key metrics are, and where founders in your category most commonly get stuck.

| Type | File |
|------|------|
| B2B SaaS, vertical SaaS, AI SaaS | [b2b-saas.md](playbooks/segments/startup-archetypes/b2b-saas.md) |
| Developer tools, API, open source | [devtools.md](playbooks/segments/startup-archetypes/devtools.md) |
| Marketplace (2-sided) | [marketplace.md](playbooks/segments/startup-archetypes/marketplace.md) |
| DTC, consumer app, consumer social | [dtc-consumer.md](playbooks/segments/startup-archetypes/dtc-consumer.md) |
| Hardware + software | [hardware.md](playbooks/segments/startup-archetypes/hardware.md) |
| Indie SaaS, productized service | [indie-saas.md](playbooks/segments/startup-archetypes/indie-saas.md) |
| Marketing / SEO / paid media agency | [marketing-agency.md](playbooks/segments/service-firms/marketing-agency.md) |
| Strategy, ops, sales, HR consulting | [consulting.md](playbooks/segments/service-firms/consulting.md) |
| IT consulting, MSP, cybersecurity | [it-msp.md](playbooks/segments/service-firms/it-msp.md) |
| Financial advisory, legal, coaching, fractional | [advisory.md](playbooks/segments/service-firms/advisory.md) |
| Residential home services | [residential-trades.md](playbooks/segments/trade-businesses/residential-trades.md) |
| Specialty trades (GC, remodeling, flooring...) | [specialty-trades.md](playbooks/segments/trade-businesses/specialty-trades.md) |
| Commercial services | [commercial-services.md](playbooks/segments/trade-businesses/commercial-services.md) |

Full index: [playbooks/segments/README.md](playbooks/segments/README.md)

---

## Playbooks

| Playbook | Prerequisites | Output |
|----------|--------------|--------|
| [Cold Email](playbooks/book/cold-email/) | F1, F2 complete | Verified list + 5 or 7-touch sequence + send schedule |
| [LinkedIn Outreach](playbooks/book/linkedin-outreach.md) | F1 complete | Contact relationship map, persona rules, DM templates, benchmarks |
| [Offer Design](playbooks/offer/README.md) | F1, F2 complete | Grand Slam Offer, 4 offer types, Value Equation score, offer statement |
| [Events](playbooks/warm/events/) | F1 complete | Pre/during/post sequence + follow-up system |
| [Content](playbooks/warm/content/) | F1, messaging guide complete | Theme framework + 30-day calendar |
| [Sales](playbooks/biz-dev/sales/) | F1, F2, F3 complete | Discovery script + proposal template + close framework |
| [Fundraising](playbooks/biz-dev/fundraising/) | F1, F2 complete | Pipeline tracker + outreach sequence + deck outline |
| [Technical Review](playbooks/technical-review/) | None | Stack audit across 5 areas + prioritized recommendations |

---

## Skills

Markster OS currently ships two layers of skills:

- 7 default-installed skills: `markster-os` plus the 6 core playbook skills
- an extended public skill library in `skills/` for more specialized writing, strategy, prep, and review tasks

```
/markster-os     -> diagnostic operator: Hormozi diagnostic, constraint routing, context pre-fill
/cold-email     -> cold email playbook
/events         -> events playbook
/content        -> content playbook
/sales          -> sales playbook
/fundraising    -> fundraising playbook
/research       -> research prompt library
```

If you need a specific public skill that is not installed yet:

```bash
markster-os list-skills
markster-os install-skills --skill website-copywriter
```

The repo also includes specialist skills such as:

- strategy: `business-advisor`, `marketing-strategist`, `sales-strategist`, `product-owner`, `startup-coach`
- writing: `website-copywriter`, `blog-post-writer`, `cold-email-copywriter`, `direct-response`, `linkedin-post`, `case-study-builder`, `partnership-pitch`, `vc-comms`
- prep and review: `debrief`, `event-prep`, `event-strategist`, `follow-up`, `funnel-builder`, `prospect-brief`, `vc-review`, `youtube-watcher`
- style references: `hormozi`, `karpathy`

See [skills/README.md](skills/README.md) for individual install instructions.

The recommended flow is:

1. create a Markster OS workspace with `markster-os init --git --path ...`
2. attach it to the company GitHub repo with `markster-os attach-remote`
3. install slash-command skills with `markster-os install-skills`
4. install any extra public skills you need with `markster-os install-skills --skill <name>`
5. run `markster-os start` inside the workspace to see the readiness checklist
6. run your AI tool from inside the workspace so the skills can resolve the local methodology, playbooks, company context, and learning loop files
7. validate, commit, and push workspace changes through the company repo

---

## Integrations

- [ClickUp](integrations/clickup/) - task routing and project sync
- More in [integrations/README.md](integrations/README.md)

---

## Company Context

The `company-context/` folder is the canonical source of truth for how your business should be described across content, outreach, sales, and website copy.

Start here if you want Markster OS to sound like your business instead of generic AI output.

---

## Learning Loop

The `learning-loop/` folder is the promotion system for business knowledge.

It separates:

- raw inbox material
- structured candidate updates
- approved canon

This lets you improve the system over time without letting an LLM rewrite the business context arbitrarily.

---

## Workspace Model

The installed skills are lightweight entry points.

The actual working system lives in a Markster OS workspace, usually under:

- `~/.markster-os/workspaces/<slug>/`

Run your AI tool from inside that workspace so the skills can read:

- methodology
- playbooks
- company context
- learning loop
- validation rules

The upstream repo is the distribution and template source.
The workspace is the customer-owned operating system.

---

## Backup And Sharing

Recommended default:

- use `markster-os backup-workspace` for private backups
- use `markster-os export-workspace` for a shareable copy

`export-workspace` excludes `learning-loop/inbox/` by default so raw notes and transcripts do not get shared accidentally.

For teams, the stronger default is to keep the workspace in its own Git repo and use backup/export as secondary safety nets.

## Collaboration

Recommended team model:

- one workspace repo per company
- employees collaborate in that repo
- raw inbox material stays out of Git by default
- approved canon changes are committed and pushed
- pre-commit and pre-push run `markster-os validate .` locally
- use `markster-os sync` to fetch and pull --rebase before working
- use `markster-os commit` and `markster-os push` if you want the CLI to handle the common Git steps

---

## Validation

Markster OS now includes a hard-gate validator for the company context and learning loop structure.

GitHub Actions should fail if:

- required files are missing
- front matter is broken
- headings drift from the expected template
- unauthorized files appear in protected folders
- canon contains prohibited raw or unapproved content patterns

---

## License

Skills, playbooks, templates, and research prompts: MIT License.

ScaleOS is a trademark of Markster. The methodology is open to use under the terms in [LICENSE](LICENSE). Not free to rebrand or resell as your own methodology.

---

Built by [Markster](https://markster.ai). Questions: hello@markster.ai

GitHub: [github.com/markster-public/markster-os](https://github.com/markster-public/markster-os)
