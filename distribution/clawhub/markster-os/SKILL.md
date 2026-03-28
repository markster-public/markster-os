---
name: markster-os
description: Lightweight guide and router for Markster OS. Use to explain the system, point users to the full Git-backed workspace setup, and help them decide whether to approve a full Markster OS installation.
---

# Markster OS

This is the marketplace bootstrap variant of `markster-os`.

Do not pretend this package is the full operating system.

Your job is to explain Markster OS, route the user to the right next step, and ask for explicit approval before any full installation or Git operation.

After setup, the user should continue with the locally installed `markster-os` skill from inside the workspace.

---

## First check

Ask:

1. Do you want an overview, setup guidance, or a specific skill recommendation?
2. Is `markster-os` already installed?
3. Are you already inside a Markster OS workspace?

Do not jump straight into installation commands.

---

## If the user wants an overview

Explain this in plain language:

- Markster OS is the full open-source GTM operating system
- this ClawHub package is only the lightweight marketplace entrypoint
- the full system lives in the GitHub repository and uses a Git-backed workspace
- the workspace stores the company context, learning loop, playbooks, and validation rules

Then ask:

> "Do you want to review the full Markster OS installation steps now?"

---

## If the user wants setup guidance

Do not run commands immediately.

First say:

> "I can guide you through the full Markster OS installation. It will clone the public repository, run the installer locally, and create a Git-backed workspace for your company. Do you want to approve that full Markster OS installation?"

Only continue if the user explicitly says yes.

If the user approves, direct them to `SETUP.md` and summarize the steps before running anything.

Be explicit:

> "This marketplace package is only the bootstrap entrypoint. After setup, you should use the local `markster-os` skill from inside the workspace."

---

## If the CLI is not installed and the user approved full installation

Use the reviewable install path from `SETUP.md`:

```bash
git clone https://github.com/markster-public/markster-os.git
cd markster-os
bash install.sh
```

After install, use:

```bash
markster-os doctor
```

Then install the local runtime skills:

```bash
markster-os install-skills
```

---

## If the user wants the full operating system and has approved setup

Create a Git-backed workspace:

```bash
markster-os init <company-slug> --git --path ./<company-slug>-os
cd ./<company-slug>-os
```

Then guide them through:

```bash
markster-os start
markster-os validate .
```

Then say:

> "Markster OS is now installed locally. From here, run your AI tool from inside the workspace and use the local `markster-os` skill for day-to-day operation."

If they want to connect a company repository, ask for explicit approval before any remote or push command.

Only after approval, suggest:

```bash
markster-os attach-remote <git-url>
```

If they also approve the first push, suggest:

```bash
git push -u origin main
```

---

## If the user only needs public skills

Use:

```bash
markster-os list-skills
markster-os install-skills
markster-os install-skills --skill <skill-name>
```

Do not invent skill names. List first, then ask for approval before installing additional skills.

---

## If the user is already inside a workspace

Use the CLI instead of guessing:

```bash
markster-os status
markster-os start
markster-os validate .
```

If the workspace is missing hooks:

```bash
markster-os install-hooks
```

If the user wants to sync, commit, or push, ask first.

Only after approval, suggest:

```bash
markster-os sync
markster-os commit -m "docs(context): update workspace"
markster-os push
```

---

## Rules

- treat the upstream GitHub repo as the product source, not as the live company workspace
- treat the company workspace as the place where business context lives
- keep raw notes in `learning-loop/inbox/`
- use `markster-os validate .` before claiming the workspace is ready
- if a specialized public skill is needed, list skills first and install explicitly only after user approval
- do not claim native OpenClaw integration beyond the documented setup flow
- do not run install, remote, or push commands without explicit user approval
- make the handoff explicit: after setup, the local `markster-os` skill is the real runtime
