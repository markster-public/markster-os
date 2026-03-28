# Changelog

All notable changes to this project will be documented in this file.

This project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Fixed
- `markster-os update` now refreshes from the tracked upstream archive by default instead of reinstalling from the original local clone path

## [1.1.3] - 2026-03-28

### Added
- added explicit `markster-os install-skills --openclaw` support for installing shared local skills into `~/.openclaw/skills`
- `markster-os install-skills --all` now includes OpenClaw automatically when `~/.openclaw` exists

### Changed
- documented OpenClaw as a first-class skill install target across the CLI, installer guidance, and setup docs

### Fixed
- corrected public install and raw GitHub URLs to use the actual `master` branch for `markster-public/markster-os`

## [1.1.1] - 2026-03-28

### Changed
- clarified the single-identity skill model: `markster-os` stays the same name across marketplace bootstrap and local runtime contexts, with the ClawHub package acting as a safe entrypoint and the local installed skill acting as the full operator

## [1.1.0] - 2026-03-28

### Added
- commit message validation via local `commit-msg` hook, CLI validator, and pull request CI enforcement

### Changed
- Git workspaces now install pre-commit, commit-msg, and pre-push hooks together by default

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
