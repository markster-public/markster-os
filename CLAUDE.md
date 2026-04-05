# CLAUDE.md - markster-os

Governance for the `markster-exec/markster-os` private repo and its public mirror.

---

## Two-Repo Architecture

| Repo | Role |
|------|------|
| `markster-exec/markster-os` | Private source - where all work happens |
| `markster-public/markster-os` | Public install source - what users install from |

`install.sh` hardcodes `markster-public/markster-os/master` as the install source.
Never commit to the public repo directly. Always work in `markster-exec`, then mirror.

---

## Release Checklist (run every time before pushing)

### Step 1: Make your changes

Work on a branch if the change is non-trivial. Use conventional commits:

```
feat(<scope>): <summary>
fix(<scope>): <summary>
docs(<scope>): <summary>
chore(<scope>): <summary>
refactor(<scope>): <summary>
test(<scope>): <summary>
ci(<scope>): <summary>
perf(<scope>): <summary>
```

Max 72 chars per commit subject. No other prefixes - CI will reject them.

### Step 2: Update CHANGELOG.md

- Add changes under `## [Unreleased]`
- When releasing: move items into a new `## [x.y.z] - YYYY-MM-DD` section
- Always keep an empty `## [Unreleased]` section at the top - CI requires it

### Step 3: Sync README.md version badge (most common failure point)

Find this line in README.md:

```
[![Version](https://img.shields.io/badge/version-v1.1.5-blue.svg)](CHANGELOG.md)
```

Update the version number to match the latest `## [x.y.z]` in CHANGELOG.md exactly.
These two must always match. CI hard-fails if they do not.

### Step 4: Run the validator locally before pushing

```bash
python3 tools/validate_markster_os.py
```

Fix all errors before pushing. CI is a hard gate with no warn-only mode.

### Step 5: Commit and tag

```bash
git add -p
git commit -m "chore(release): prepare vX.Y.Z"
git tag vX.Y.Z
git push origin master
git push origin vX.Y.Z
```

### Step 6: Mirror to public repo

```bash
git push git@github.com:markster-public/markster-os.git master
git push git@github.com:markster-public/markster-os.git vX.Y.Z
```

If a `public` remote is already configured: `git push public master && git push public vX.Y.Z`

---

## CI Hard Gates

The GitHub Action runs `tools/validate_markster_os.py` on every push and PR.
On PRs it also validates every commit message. All failures block merge.

| Domain | What causes failure |
|--------|-------------------|
| Repo hygiene | `STATE.md` or `MASTER_LOG.md` committed; local absolute paths or home-directory shortcuts in any tracked file - exceptions: validator and validation-spec only (see `validation/validation-spec.md` for exact patterns) |
| `company-context/` | Missing or extra files vs `manifest.json`; any file missing front matter keys (`id, title, type, status, owner, created, updated, tags`); headings missing or out of order |
| `learning-loop/` | Missing required files; markdown without front matter; `canon/` containing `TODO`, `tbd`, `Speaker N:`, `Interviewer:` |
| Release metadata | `## [Unreleased]` missing from CHANGELOG; README badge version does not match latest CHANGELOG version |
| Commit messages (PRs) | Any commit not matching `<type>(<scope>): <summary>` or exceeding 72 chars |

---

## Files That Must Never Be Committed

- `STATE.md` - internal session state
- `MASTER_LOG.md` - internal log
- Any file containing local absolute paths or home-directory shortcuts (see `validation/validation-spec.md` for exact banned patterns) - unless editing the validator or validation-spec itself

---

## Versioning

Follows semantic versioning. Current version: see README badge and latest CHANGELOG entry.

- `patch` (x.y.Z): bug fixes, metadata sync, minor corrections
- `minor` (x.Y.0): new features, new commands, new playbooks
- `major` (X.0.0): breaking changes to workspace model or CLI contract

---

## Open Branches

Check `git branch -r` before starting work. Do not merge unknown branches without understanding what they are.

`feat-paperclip-bootstrap` on origin - not Ivan's work, leave it alone.
