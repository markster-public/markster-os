# Playbooks

Each playbook is a deterministic sequence. Defined inputs, fixed steps, documented outputs.

Playbooks are not general advice. They are step-by-step operating procedures organized by the GOD Engine brick they serve. Foundation (F1-F4) must be complete before most playbooks produce useful results -- the bricks draw directly from your F1-F4 answers.

---

## How playbooks work

```
INPUTS
What you need before you start. If you do not have these, stop and complete them first.

STEPS
Numbered steps in sequence. Each step has a specific action, a tool or template reference, and a completion signal.

OUTPUTS
The concrete deliverables the playbook produces. You should be able to hand these to someone else.
```

The skills in this OS activate playbooks in your AI environment. You can also run playbooks manually -- open the README and follow the steps.

---

## Playbooks by GOD Engine Brick

### Growth

| Brick | Playbook | What it produces | Requires |
|-------|----------|-----------------|---------|
| G1: Find | [find/](find/README.md) | Qualified prospect lists, scoring, enrichment process | F1 (ICP) |
| G2: Warm | [warm/](warm/README.md) | Content calendar, nurture sequences, event follow-up | F1, F3 (message) |
| G3: Book | [book/](book/README.md) | Outreach sequences, qualification framework, show rate system | F1, F2 |

### Operations

| Brick | Playbook | What it produces | Requires |
|-------|----------|-----------------|---------|
| O1: Standardize | [standardize/](standardize/README.md) | SOPs, process documentation, training materials | None |
| O2: Automate | [automate/](automate/README.md) | Automation workflows, AI agent configs, integration map | O1 (documented processes) |
| O3: Instrument | [instrument/](instrument/README.md) | KPI dashboards, attribution setup, forecast model | O1, O2 |

### Delivery

| Brick | Playbook | What it produces | Requires |
|-------|----------|-----------------|---------|
| D1: Deliver | [deliver/](deliver/README.md) | Onboarding framework, QA checklist, communication cadence | O1 |
| D2: Prove | [prove/](prove/README.md) | Case studies, testimonials, proof asset library | D1 (results to prove) |
| D3: Expand | [expand/](expand/README.md) | Health scoring system, referral program, churn prevention | D1, D2 |

---

## Other tools in this directory

| File | Purpose |
|------|---------|
| [brief-creation.md](brief-creation.md) | Template for briefing AI tools on a task |
| [campaign-builder.md](campaign-builder.md) | End-to-end outreach campaign build |
| [debrief.md](debrief.md) | Post-session debrief and learnings capture |
| [prospect-brief.md](prospect-brief.md) | Pre-call research brief for a specific prospect |
| [sales-proposal.md](sales-proposal.md) | Proposal structure and template |
| [segments/](segments/) | Archetype guides: startups, service firms, and trade businesses -- read yours before running any playbook |
| [biz-dev/](biz-dev/) | Sales and fundraising frameworks |
| [technical-review/](technical-review/) | Tech stack audit playbook |
| [weekly-pulse.md](weekly-pulse.md) | Weekly review template |

---

## Playbook conventions

**Templates:** Each brick playbook has a `templates/` subdirectory (or sub-playbooks) with real starting-point materials. Not placeholder text -- actual drafts you can edit and use.

**Skill activation:** Each playbook has a corresponding skill in `/skills/`. The skill adds context-awareness: it checks your Foundation answers, asks clarifying questions, and tailors execution to your specific ICP and offer.

**Iteration loops:** Every playbook includes what to measure and what to change first on the next run.
