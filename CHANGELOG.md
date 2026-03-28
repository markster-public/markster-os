# Changelog

All notable changes to this project will be documented in this file.

This project follows [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-03-28

### Added
- managed `markster-os` CLI with install, workspace init, validation, sync, commit, push, backup, export, and skill-management commands
- Git-backed workspace model with `company-context/`, `learning-loop/`, validation, and onboarding scaffolding
- public skill library with 7 default-installed core skills and on-demand extended skill installation
- deterministic validator and GitHub Action for protected structure and public-safety checks
- setup prompts for Claude, Codex, Gemini, and OpenClaw workflows
- ScaleOS methodology, playbooks, templates, research prompts, and weekly `AUTOPILOT.md` loop

### Changed
- documentation now centers the workspace model instead of treating the upstream repo as live company state
- branch governance is set up to require pull requests and validation for future changes

### Security
- removed internal working artifacts from the live repo
- rewrote Git history before public release to remove internal-path and private-reference residue
