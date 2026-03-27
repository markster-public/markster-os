---
id: validation-readme
title: Validation
type: reference
status: active
owner: markster-os
created: 2026-03-26
updated: 2026-03-26
tags: [validation, ci, standards]
---

# Validation

This folder defines the deterministic validation rules for protected Markster OS structures and public-safety hygiene.

Current scope:

- `company-context/`
- `learning-loop/`
- repository hygiene for internal artifacts and leaked local-path/private-org references

These validations are intended to be hard gates in CI.

To make this block merges on GitHub, require the `Validate Markster OS` check in branch protection for the default branch.
