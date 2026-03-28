# Markster OS With OpenClaw

This is the initial OpenClaw setup path for Markster OS.

What is supported today:

- use OpenClaw as the AI runtime
- keep Markster OS in a normal Git-backed workspace repo
- use the `markster-os` CLI for install, validation, sync, and skill management
- point the OpenClaw agent at that workspace so it reads the workspace canon, not the upstream template repo

What is not claimed yet:

- one-click native OpenClaw integration
- OpenClaw-specific slash-command packaging
- automatic OpenClaw workspace provisioning from Markster OS

## Recommended model

Use this split:

- `markster-os` repo: product source, templates, validator, skills
- your company workspace repo: actual business canon and operating system
- OpenClaw: agent runtime working inside the company workspace repo

Do not use the upstream `markster-os` clone as your live company workspace.

## Setup steps

1. Install the CLI:

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
```

2. Create a Git-backed workspace:

```bash
markster-os init your-company --git --path ./your-company-os
cd ./your-company-os
```

3. Attach your remote and push:

```bash
markster-os attach-remote git@github.com:YOUR-ORG/YOUR-REPO.git
git push -u origin main
```

4. Install Markster OS skills if your OpenClaw setup uses local skill folders or repo instructions:

```bash
markster-os install-skills
```

5. Run readiness checks:

```bash
markster-os start
markster-os validate .
```

6. Configure OpenClaw to work from this workspace directory.

The important part is not a specific UI flow. The important part is that the agent runs with this repo as its working directory so it can read:

- `company-context/`
- `learning-loop/`
- `AUTOPILOT.md`
- `QUICKSTART.md`
- `skills/`

## Agent instructions for OpenClaw

When using OpenClaw, make sure the agent follows these rules:

- start from the company workspace, not the upstream Markster OS repo
- read `company-context/` before running any playbook
- treat `learning-loop/inbox/` as raw input, not canon
- run `markster-os validate .` before commit
- use `AUTOPILOT.md` for the weekly operating loop
- use `/markster-os` or the equivalent Markster OS operator entry point first

## Copy-paste prompt

You can give this to an OpenClaw agent:

```text
Set up Markster OS in this workspace.

Requirements:
- If Markster OS is not installed, install it with:
  curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
- Create a Git-backed workspace for my company:
  markster-os init <company-slug> --git --path ./<company-slug>-os
- Move into that workspace.
- Run:
  markster-os start
  markster-os validate .
- Tell me which company-context files I need to fill first.

Important rules:
- Treat the upstream markster-os repo as the product source, not my live business workspace.
- Treat this new workspace repo as the canonical business repo.
- Keep raw notes in learning-loop/inbox/.
- Validate before saying setup is complete.
```

## Current maturity

This guide is intentionally conservative.

Today, “Works with OpenClaw” means:

- Markster OS can be used from an OpenClaw-managed workspace
- the repo has a clear workspace model and agent instructions
- the validator and Git workflow still apply

Future work can add a deeper OpenClaw-specific integration guide once the exact runtime shape is stable.
