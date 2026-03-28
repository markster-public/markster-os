## Summary

- what changed
- why it changed

## Verification

- [ ] `python3 tools/validate_markster_os.py`
- [ ] `python3 -m py_compile tools/markster_os_cli.py tools/validate_markster_os.py tools/validate_commit_message.py` if CLI code changed
- [ ] commit subjects in this PR follow `type(scope): summary`

## Changelog

- [ ] `CHANGELOG.md` updated for user-visible changes

## Public Safety

- [ ] no secrets, private data, local paths, or internal-only references added
