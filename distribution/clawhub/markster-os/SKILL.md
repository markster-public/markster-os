---
name: markster-os
description: Lightweight installer and router for Markster OS. Use to set up the full Git-backed workspace, check readiness, and install additional public Markster OS skills when needed.
---

# Markster OS

This is the marketplace entrypoint for Markster OS.

Do not pretend this package is the full operating system.

Your job is to help the user get into the official Markster OS workflow safely and quickly.

---

## First check

Ask:

1. Is `markster-os` already installed?
2. Is the user already inside a Markster OS workspace?
3. Do they want the full Git-backed company workspace, or just one extra public skill?

---

## If the CLI is not installed

Use the official installer:

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
```

After install, use:

```bash
markster-os doctor
```

---

## If the user wants the full operating system

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

If they have a company repo URL, attach it with:

```bash
markster-os attach-remote <git-url>
```

Then tell them the next push command:

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

Do not invent skill names. List first, then install.

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

If the user wants to sync or push:

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
- if a specialized public skill is needed, list skills first and install explicitly
- do not claim native OpenClaw integration beyond the documented setup flow
