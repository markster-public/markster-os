# Markster OS Setup

Use these commands when the user wants the full Markster OS workflow.

## Install the CLI

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
```

## Create the workspace

```bash
markster-os init your-company --git --path ./your-company-os
cd ./your-company-os
```

## Attach the company repository

```bash
markster-os attach-remote git@github.com:YOUR-ORG/YOUR-REPO.git
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

```bash
markster-os list-skills
markster-os install-skills --skill website-copywriter
```
