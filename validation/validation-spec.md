---
id: validation-spec
title: Validation Spec
type: standard
status: active
owner: markster-os
created: 2026-03-26
updated: 2026-03-26
tags: [validation, spec, ci]
---

# Markster OS Validation Spec

This spec defines deterministic hard-gate validation for `company-context/`, `learning-loop/`, and repository public-safety hygiene.

## Goals

- keep the repo human-readable
- constrain LLM write behavior
- stop uncontrolled file sprawl
- stop unapproved claims from entering canon

## Validation Domains

## 0. Repository Hygiene

Validate:

- forbidden internal working files are not committed
- no leaked local absolute paths like `/Users/...` appear in product files
- no leaked local workspace references like `~/Workspace/...` appear in the repo
- no private org references like `private-org-slug` appear in committed content

Allow narrow exceptions only for public-facing install documentation or for the validator code/spec that explicitly describes the banned patterns.

## 1. File Inventory

Validate:

- required files exist
- no unexpected files exist in `company-context/`
- `manifest.json` lists the required company context files exactly

## 2. Front Matter

Every markdown file in protected directories must contain:

- `id`
- `title`
- `type`
- `status`
- `owner`
- `created`
- `updated`
- `tags`

## 3. Required Headings

Each canonical file must include its required headings in order.

Example:

- `identity.md` must contain:
  - `## One-Sentence Definition`
  - `## Category`
  - `## What We Do`
  - `## What We Do Not Do`
  - `## Why We Exist`
  - `## Strategic Position`
  - `## Known Identity Risks`

## 4. Protected Write Zones

Validate:

- `company-context/` contains only canonical files and `manifest.json`
- `learning-loop/inbox/` may contain raw files, but not canonical company context files
- `learning-loop/candidates/` candidate files must use candidate structure
- `learning-loop/canon/` must not contain raw transcript markers

## 5. Claim Hygiene

Block canonical content containing:

- `TODO`
- `tbd`
- transcript speaker labels like `Speaker 1:` or `Interviewer:`
- unresolved claims presented as fact

Allow labeled uncertainty only in designated “unknowns” or “proof gaps” sections.

## 6. Provenance Rules

Candidate files must contain:

- source type
- source path or label
- target file
- status

## 7. Path Hygiene

Block protected files containing:

- absolute local filesystem paths
- home-directory shorthands like `~/`

## GitHub Action Behavior

Hard gate:

- fail on any missing file
- fail on front matter mismatch
- fail on heading mismatch
- fail on prohibited content in protected folders
- fail on unauthorized files in protected folders
- fail on forbidden internal files anywhere in the repo
- fail on prohibited repository-wide leak patterns

Warn-only is not supported.

To make this block merges on GitHub, configure branch protection to require the `Validate Markster OS` workflow check before merge.
