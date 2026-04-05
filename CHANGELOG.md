# Changelog

All notable changes to this project will be documented in this file.

This project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.2.0] - 2026-04-04

### Added
- funnel playbook with 8 reference sections: funnel types and decision matrix, offer stack architecture, VSL architecture, input specification, affiliate mechanics, high-ticket backend, market landscape
- funnel-sprint skill: quick single-ICP mini-funnel generator (landing page, lead magnet, 3-email nurture)
- funnel-plan skill: full funnel architecture session with funnel type selection and offer stack design
- funnel-build skill: asset writing workflow covering VSL script, landing page, OTO pages, and email sequence
- funnel-review skill: scored funnel audit across 5 domains with prioritized fix list
- CLAUDE.md: repo-level release process and CI rules for agent sessions

## [1.1.5] - 2026-03-28

### Fixed
- synced the README version badge with the latest released tag
- moved the updater fix into a proper `1.1.4` changelog section

### Added
- validator now enforces that `CHANGELOG.md` contains an `## [Unreleased]` section
- validator now enforces that the latest released changelog version matches the README version badge

## [1.1.4] - 2026-03-28

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
