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
markster-os start
markster-os validate .
```

## Install an additional public skill

Only do this after the user explicitly approves extra skill installation.

```bash
markster-os list-skills
markster-os install-skills --skill website-copywriter
```
