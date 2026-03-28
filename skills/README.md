# Skills

Skills are single files that activate a playbook workflow in your AI environment.

When you type `/cold-email` in Claude Code, Codex, or Gemini, the skill loads the cold email playbook context, checks your Foundation status, and walks you through the playbook step by step.

---

## Default-installed skills

| Skill | Command | Activates |
|-------|---------|-----------|
| Markster OS | `/markster-os` | Workspace guide, router, and CLI-aware operator |
| Cold Email | `/cold-email` | Cold email playbook (research -> segment -> write -> send -> iterate) |
| Events | `/events` | Events playbook (pre/during/post system) |
| Content | `/content` | Content machine (theme -> calendar -> publish -> distribute) |
| Sales | `/sales` | Sales playbook (discovery -> proposal -> close) |
| Fundraising | `/fundraising` | Fundraising playbook (pipeline -> pitch -> follow-up) |
| Research | `/research` | Research prompt library (8 structured prompts) |

These 7 are installed by default when you run `markster-os install-skills`.

The skill name stays the same across environments:

- `markster-os` in Claude Code, Codex, Gemini, and local workspace installs is the full runtime skill
- `markster-os` in a marketplace package like ClawHub is only the bootstrap entrypoint before local setup

After setup, always run your AI tool from inside the workspace and use the local `markster-os` skill.

## Extended public skill library

The repo also contains additional public skills for specialized work. Current inventory:

- strategy and advisory: `business-advisor`, `marketing-strategist`, `sales-strategist`, `product-owner`, `startup-coach`
- writing and messaging: `blog-post-writer`, `case-study-builder`, `cold-email-copywriter`, `direct-response`, `linkedin-post`, `partnership-pitch`, `vc-comms`, `website-copywriter`
- prep, review, and execution support: `debrief`, `event-prep`, `event-strategist`, `follow-up`, `funnel-builder`, `prospect-brief`, `vc-review`, `youtube-watcher`
- style references and voice lenses: `hormozi`, `karpathy`

That brings the current public repo inventory to 30 skill directories in total. The CLI installs the 7 default skills because they cover the main operating workflows plus workspace routing.

---

## Installation methods

### Method 1: Install the Markster OS CLI (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/master/install.sh | bash
```

Then install skills with:

```bash
markster-os install-skills
markster-os list-skills
markster-os install-skills --skill website-copywriter --skill vc-review
markster-os install-skills --extended
```

Then create a workspace with:

```bash
markster-os init your-company --git --path ./your-company-os
```

Useful maintenance commands:

```bash
markster-os status
markster-os start
markster-os doctor
markster-os upgrade-workspace ~/.markster-os/workspaces/your-company
markster-os attach-remote git@github.com:YOUR-ORG/YOUR-REPO.git
markster-os install-hooks
markster-os validate-commit-message --message "docs(readme): clarify skill install flow"
markster-os sync
markster-os commit -m "docs(context): update canon"
markster-os push
markster-os backup-workspace ~/.markster-os/workspaces/your-company
markster-os export-workspace ~/.markster-os/workspaces/your-company
markster-os update
```

Run your AI tool from inside the workspace so the skills can resolve the local docs and templates correctly.

For teams, the recommended production setup is:

- one workspace per company
- stored in the company's own Git repository
- canonical files reviewed through normal Git workflows
- `learning-loop/inbox/` ignored by default

Very simple team workflow:

1. `markster-os init your-company --git --path ./your-company-os`
2. `cd ./your-company-os`
3. `markster-os attach-remote git@github.com:YOUR-ORG/YOUR-REPO.git`
4. `git push -u origin main`
5. `markster-os install-hooks`
6. `markster-os start`
7. run your AI tool from inside the workspace
8. `markster-os validate .`
9. `markster-os commit -m "docs(context): update workspace"`
10. `markster-os push`

`markster-os install-hooks` installs pre-commit, commit-msg, and pre-push hooks.

### Method 2: Install individual skill via curl

```bash
# Claude Code
mkdir -p ~/.claude/skills/cold-email
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/master/skills/cold-email/SKILL.md \
  -o ~/.claude/skills/cold-email/SKILL.md

# Codex
mkdir -p ~/.codex/skills/cold-email
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/master/skills/cold-email/SKILL.md \
  -o ~/.codex/skills/cold-email/SKILL.md
```

Repeat for each skill you want.

### Method 3: Clone the repo and copy

```bash
git clone https://github.com/markster-public/markster-os.git
cp -r markster-os/skills/cold-email ~/.claude/skills/
cp -r markster-os/skills/sales ~/.claude/skills/
# etc.
```

---

## Skill locations by AI tool

| Tool | Skills directory |
|------|-----------------|
| Claude Code | `~/.claude/skills/` |
| Codex | `~/.codex/skills/` |
| Gemini CLI | `~/.gemini/skills/` (if supported) |

---

## How skills work

Each skill file contains:
1. YAML frontmatter with the skill name and a description that appears in the command menu
2. Instructions for the AI on how to execute the playbook
3. References to the specific playbook files and templates

The skill does not contain the full playbook. It references the local Markster OS workspace files.

That means:

- installing skills alone is not enough for full usage
- you should run your AI tool from inside a Markster OS workspace
- the workspace contains the methodology, playbooks, company context, learning loop, and validators the skills expect

## Backup And Sharing

Workspaces are customer-owned.

Recommended options:

- private backup: `markster-os backup-workspace`
- shareable copy: `markster-os export-workspace`

The shareable export excludes `learning-loop/inbox/` by default.

---

## Using skills with Foundation context

Skills work best when you have your Foundation answers ready. Before running any skill except `/research`, have these documents open or ready to paste:

- F1 Positioning summary (from `methodology/foundation/F1-positioning.md`)
- F2 Business Model summary (from `methodology/foundation/F2-business-model.md`)
- F3 Org Structure summary (from `methodology/foundation/F3-org-structure.md`)
- F4 Financial Architecture summary (from `methodology/foundation/F4-financial.md`)

The skill will ask for this context if you do not provide it upfront.
