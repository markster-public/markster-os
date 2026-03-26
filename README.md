# Markster OS

**The GTM operating system for companies under 20 people.**

Built on the ScaleOS methodology. Works with Claude Code, Codex, and Gemini CLI. Free to use. Paid add-ons for proprietary data.

---

## What it is

Markster OS is a structured GTM system - methodology, playbooks, skills, and research prompts - packaged to run inside your AI coding environment.

You define your ICP, offer, message, and company context once. The OS routes that context into every playbook you run: cold email, events, content, sales, fundraising, technical review.

Each playbook is a deterministic sequence: inputs in, steps to follow, outputs delivered. The skills activate the playbooks directly in Claude Code, Codex, or Gemini. No dashboard. No SaaS. The intelligence runs in your environment against your context.

---

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
```

Installs the `markster-os` CLI into your home directory. The CLI manages a stable Markster OS distribution, customer workspaces, validation, and optional slash-command skill installation.

The launcher is installed at `~/bin/markster-os`.

Core commands:

```bash
markster-os init <slug>
markster-os install-skills
markster-os validate [path]
markster-os update
markster-os upgrade-workspace [path]
markster-os status
markster-os doctor
```

---

## What's included (free)

| Component | What it gives you |
|-----------|-------------------|
| **Methodology** | ScaleOS F1-F4 Foundation + GOD Engine (9 execution bricks) |
| **Assessment** | Scored readiness scorecard - tells you which playbook to run first |
| **Playbooks** | Cold email, events, content, sales, fundraising, technical review |
| **Skills** | 6 skills that activate each playbook in your AI environment |
| **Research prompts** | 8 structured prompts for competitive intel, buyer JTBD, signals, objections |
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
| [F1: ICP](methodology/foundation/F1-icp.md) | Who exactly are we selling to? |
| [F2: Offer](methodology/foundation/F2-offer.md) | What outcome are we selling, and at what price? |
| [F3: Message](methodology/foundation/F3-message.md) | How do we describe the problem in their words? |
| [F4: Channel](methodology/foundation/F4-channel.md) | Where do we reach them first, given their profile? |

**GOD Engine:** 9 execution bricks that run demand generation once Foundation is locked. See [methodology/god-engine/README.md](methodology/god-engine/README.md).

Start with the [assessment scorecard](methodology/assessment/scorecard.md). It tells you exactly where you are and which playbook to run first.

---

## Quick start

**Step 1: Install the CLI**
```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
```

**Step 2: Create a workspace**

```bash
markster-os init your-company
cd ~/.markster-os/workspaces/your-company
```

**Step 3: Run the scorecard**

Open [methodology/assessment/scorecard.md](methodology/assessment/scorecard.md). Score yourself honestly across F1-F4 and the GOD Engine bricks. The scoring tells you exactly which playbook to run first.

**Step 4: Lock F1-F4, then activate a playbook**

Work through [methodology/foundation/](methodology/foundation/) in order. Once F1-F4 is complete, activate a playbook in your AI environment:

```
/cold-email
/sales
/events
/content
/fundraising
/research
```

**Step 5: Fill in your company context**

Copy the files in [company-context/](company-context/) and define:

- what your company is
- who you serve
- what you offer
- how you sound
- what proof you can actually claim

**Step 6: Use the learning loop**

Use [learning-loop/](learning-loop/) to turn real conversations, notes, and edits into approved updates to your business context. Raw notes stay out of canon until reviewed.

---

## Playbooks

| Playbook | Prerequisites | Output |
|----------|--------------|--------|
| [Cold Email](playbooks/cold-email/) | F1, F2 complete | Verified list + 3-touch sequence + send schedule |
| [Events](playbooks/events/) | F1 complete | Pre/during/post sequence + follow-up system |
| [Content](playbooks/content/) | F1, F3 complete | Theme framework + 30-day calendar |
| [Sales](playbooks/biz-dev/sales/) | F1, F2, F3 complete | Discovery script + proposal template + close framework |
| [Fundraising](playbooks/biz-dev/fundraising/) | F1, F2 complete | Pipeline tracker + outreach sequence + deck outline |
| [Technical Review](playbooks/technical-review/) | None | Stack audit across 5 areas + prioritized recommendations |

---

## Skills

Each skill activates a playbook in your AI environment with a single command.

```
/cold-email     -> cold email playbook
/events         -> events playbook
/content        -> content playbook
/sales          -> sales playbook
/fundraising    -> fundraising playbook
/research       -> research prompt library
```

See [skills/README.md](skills/README.md) for individual install instructions.

The recommended flow is:

1. create a Markster OS workspace with `markster-os init`
2. install slash-command skills with `markster-os install-skills`
3. run your AI tool from inside the workspace so the skills can resolve the local methodology, playbooks, company context, and learning loop files

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
