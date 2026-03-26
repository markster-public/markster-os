# Skills

Skills are single files that activate a playbook workflow in your AI environment.

When you type `/cold-email` in Claude Code, Codex, or Gemini, the skill loads the cold email playbook context, checks your Foundation status, and walks you through the playbook step by step.

---

## Available skills

| Skill | Command | Activates |
|-------|---------|-----------|
| Cold Email | `/cold-email` | Cold email playbook (research -> segment -> write -> send -> iterate) |
| Events | `/events` | Events playbook (pre/during/post system) |
| Content | `/content` | Content machine (theme -> calendar -> publish -> distribute) |
| Sales | `/sales` | Sales playbook (discovery -> proposal -> close) |
| Fundraising | `/fundraising` | Fundraising playbook (pipeline -> pitch -> follow-up) |
| Research | `/research` | Research prompt library (8 structured prompts) |

---

## Installation methods

### Method 1: Install script (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
```

Detects your AI environment and installs all skills automatically.

### Method 2: Install individual skill via curl

```bash
# Claude Code
mkdir -p ~/.claude/skills/cold-email
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/skills/cold-email/SKILL.md \
  -o ~/.claude/skills/cold-email/SKILL.md

# Codex
mkdir -p ~/.codex/skills/cold-email
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/skills/cold-email/SKILL.md \
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

The skill does not contain the full playbook - it references it. This means updating a playbook automatically updates what the skill does when it runs.

---

## Using skills with Foundation context

Skills work best when you have your Foundation answers ready. Before running any skill except `/research`, have these documents open or ready to paste:

- F1 ICP summary (from `methodology/foundation/F1-icp.md`)
- F2 offer summary (from `methodology/foundation/F2-offer.md`)
- F3 message summary (from `methodology/foundation/F3-message.md`)
- F4 channel selection (from `methodology/foundation/F4-channel.md`)

The skill will ask for this context if you do not provide it upfront.
