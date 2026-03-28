# Markster OS Setup

Use these steps only after the user explicitly approves the full Markster OS installation.

## Reviewable install path

```bash
git clone https://github.com/markster-public/markster-os.git
cd markster-os
bash install.sh
```

## Create the workspace

```bash
markster-os init your-company --git --path ./your-company-os
cd ./your-company-os
```

## Attach the company repository

Only do this after the user explicitly approves connecting their repo.

```bash
markster-os attach-remote git@github.com:YOUR-ORG/YOUR-REPO.git
```

## First push

Only do this after the user explicitly approves the first push.

```bash
git push -u origin main
```

## Install the default skills

```bash
markster-os install-skills
```

## First run

```bash
markster-os install-skills
markster-os start
markster-os validate .
```

## Handoff

After setup:

- run your AI tool from inside the workspace directory
- use the local `markster-os` skill for day-to-day operation
- treat this ClawHub package as the bootstrap entrypoint, not the runtime

## Install an additional public skill

Only do this after the user explicitly approves extra skill installation.

```bash
markster-os list-skills
markster-os install-skills --skill website-copywriter
```
