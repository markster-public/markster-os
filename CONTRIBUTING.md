# Contributing

Thanks for contributing to Markster OS.

## Ground rules

- changes to the default branch go through pull requests
- `Validate Markster OS` must pass before merge
- do not commit secrets, private client data, local filesystem paths, or internal-only notes
- keep the repo human-readable and workspace-oriented
- prefer updating existing canon, docs, and playbooks over inventing new structure

## Before you open a PR

1. run the validator:

```bash
python3 tools/validate_markster_os.py
```

2. if you changed CLI behavior, compile the Python entry points:

```bash
python3 -m py_compile tools/markster_os_cli.py tools/validate_markster_os.py
```

3. update `CHANGELOG.md` for any user-visible change

## Versioning

Markster OS follows Semantic Versioning.

- patch: fixes, doc corrections, validation hardening, non-breaking cleanup
- minor: new playbooks, skills, templates, or commands that are backward compatible
- major: breaking repo structure, CLI behavior, or workflow expectations

## Pull request expectations

- explain the user-visible change clearly
- link to the files or workflows affected
- mention any migration or release note impact
- keep PRs focused; do not mix unrelated cleanup into feature work

## Public-safety rule

This repo is intended for public use.

Never add:

- secrets or tokens
- client-identifying information
- internal company notes
- local machine paths
- references to unpublished internal tools or repos
