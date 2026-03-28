# ClawHub Publishing Layout

This is the proposed packaging model for publishing Markster OS into ClawHub and similar skill marketplaces.

The goal is simple:

- keep `markster-public/markster-os` as the source of truth
- publish a thin marketplace package for discovery and install
- avoid copying the whole OS into a skill package
- keep the published package easy to inspect and low-risk

---

## Source Of Truth

Do not maintain a separate repository for the main `markster-os` skill unless a marketplace forces that constraint.

The source of truth should stay here:

- repo: `markster-public/markster-os`
- local runtime skill source: `skills/markster-os/SKILL.md`
- marketplace wrapper source: `distribution/clawhub/markster-os/`
- public docs: `README.md`
- install flow: `install.sh`
- release history: `CHANGELOG.md`

The marketplace package should be generated from this repo, not maintained by hand in parallel.

---

## What To Publish

### First publish

Publish one marketplace entry first:

- `markster-os`

This is the right first package because it acts as:

- bootstrap entrypoint
- safe installer guide
- workspace setup handoff
- skill discovery surface

It can then point people to:

- the full GitHub repo
- the official installer
- the local installed `markster-os` runtime skill
- on-demand skill installation with `markster-os install-skills --skill <name>`

Important:

- the ClawHub package and the local runtime use the same skill name: `markster-os`
- the difference is stage, not branding
- ClawHub `markster-os` is the safe bootstrap wrapper
- local `markster-os` is the full operator once the workspace exists

### Next publish

After the main entrypoint is stable, publish a small number of high-intent standalone skills:

- `cold-email`
- `content`
- `sales`
- `research`
- optionally `business-advisor`

These should be separate marketplace packages, not bundled into the `markster-os` package.

---

## Proposed Layout

Proposed internal staging layout:

```text
distribution/
  clawhub/
    README.md
    markster-os/
      SKILL.md
      README.md
      SETUP.md
```

This layout is a publish-ready upload folder, not a second product source tree.

Rules:

- `SKILL.md` should be marketplace-specific
- `README.md` should be marketplace-facing copy
- supporting text files should be plain text or markdown only
- do not rely on marketplace-specific hidden metadata unless the marketplace requires it

---

## Package Boundaries

The ClawHub package for `markster-os` should be thin.

Include:

- the skill file
- a short marketplace README
- public metadata
- links to the official GitHub repo and installer

Do not include:

- the full playbook library
- large methodology directories
- customer workspace files
- hidden scripts inside markdown
- any private references
- any raw notes or example business data

The skill should instruct the agent to install and operate the full OS through the official repo and CLI, then hand off to the locally installed `markster-os` runtime.

---

## `markster-os` Package Shape

### `SKILL.md`

Role:

- bootstrap the user into the full Markster OS install path
- detect whether `markster-os` CLI is installed
- detect whether the user is inside a workspace
- hand off to the local `markster-os` runtime skill after setup
- route to `markster-os start`, `markster-os list-skills`, and `markster-os install-skills --skill <name>`
- avoid assuming the full repo is already present locally

This should be a thin marketplace wrapper, not the full repo-local operator skill.

### `README.md`

This is the marketplace-facing description.

Recommended contents:

1. what Markster OS is in one paragraph
2. who it is for
3. what this package does
4. what it does not include
5. official install commands
6. link to GitHub repo
7. link to OpenClaw setup guide

### `SETUP.md`

This should contain:

- the official install command
- the workspace init command
- the handoff to the local `markster-os` runtime skill
- the remote attach command
- the first-run commands for `start`, `validate`, and `install-skills`

This keeps the marketplace upload self-contained without bloating the skill file.

---

## Marketplace README Draft

Suggested short README for the `markster-os` marketplace package:

```md
# Markster OS

Markster OS is an open-source B2B growth operating system for small teams.

This package gives your agent a workspace-aware operator skill that can:

- check whether the business workspace is ready
- route to the right Markster OS playbook
- help install additional public skills
- guide setup of the full Git-backed company workspace

This package is not the full operating system by itself.

To install the full system:

```bash
curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/master/install.sh | bash
markster-os init your-company --git --path ./your-company-os
```

Repository:

- https://github.com/markster-public/markster-os
```

---

## Publish Flow

Recommended manual flow at first:

1. update the source docs and install flow in the main repo
2. update `CHANGELOG.md` and tag a release
3. update `distribution/clawhub/markster-os/SKILL.md`
4. update `distribution/clawhub/markster-os/README.md`
5. update `distribution/clawhub/markster-os/SETUP.md`
6. verify that all links point to `markster-public/markster-os`
7. verify that no private references or local paths are present
8. upload `distribution/clawhub/markster-os/` in ClawHub

Recommended automated flow later:

1. add `markster-os package-clawhub`
2. generate the publishable folder from repo sources
3. run a public-safety check on the generated output
4. open the folder for upload or publish through a future marketplace API

---

## Safety Rules

Every marketplace package must pass these rules:

- no secrets
- no local filesystem paths
- no private org or repo references
- no unpublished internal tools
- no client names
- no hidden install behavior
- no claims of native integration that do not exist

The package should be inspectable by a user in under five minutes.

---

## Recommendation

For now:

- keep one source repo
- publish `markster-os` as the first marketplace package
- use GitHub + the official installer as the real product entrypoint
- treat marketplace listings as discovery and guided install surfaces
- keep one user-facing skill name everywhere: `markster-os`

Do not split this into a second repository yet.
