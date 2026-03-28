# Security Policy

## Supported versions

Security fixes are applied to the current default branch and the latest tagged release.

Current supported release:

- `v1.0.0`

Older tags and stale forks may not receive fixes.

## Reporting a vulnerability

Do not open a public GitHub issue for a suspected security vulnerability.

Report it privately to:

- `security@markster.ai`

Include:

- a short description of the issue
- affected files or commands
- reproduction steps
- impact if known
- any suggested mitigation

We will aim to:

- acknowledge receipt within 3 business days
- confirm whether the report is in scope
- provide a remediation or response plan once the issue is verified

## Scope

This repo is primarily documentation, templates, prompts, and local CLI tooling.

Security issues in scope include:

- secret leakage in repo content or generated artifacts
- unsafe CLI behavior that could expose private workspace data
- validation gaps that allow obviously unsafe public content into the repo
- release or install flows that encourage insecure defaults

Out of scope:

- issues in third-party AI runtimes or external platforms
- misconfiguration in a user's private workspace repo
- feature requests framed as security issues

## Public-safety rule

If you discover:

- secrets
- private client data
- internal-only notes
- local filesystem paths
- unpublished private repo references

treat it as a security and privacy issue and report it privately.
