#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ALLOWED_PREFIXES = ("Merge ", "Revert ", "fixup! ", "squash! ")
COMMIT_PATTERN = re.compile(
    r"^(feat|fix|docs|chore|refactor|test|ci|perf)(\([a-z0-9][a-z0-9_-]*\))?: (.+)$"
)
MAX_SUBJECT_LENGTH = 72


def load_subject(args: argparse.Namespace) -> str:
    if args.message is not None:
        return args.message.strip()
    if args.path is None:
        raise SystemExit("error: provide --message or a commit message file path")
    lines = Path(args.path).read_text(encoding="utf-8").splitlines()
    return lines[0].strip() if lines else ""


def is_valid_subject(subject: str) -> bool:
    if any(subject.startswith(prefix) for prefix in ALLOWED_PREFIXES):
        return True
    match = COMMIT_PATTERN.match(subject)
    return match is not None and len(subject) <= MAX_SUBJECT_LENGTH


def print_error(subject: str) -> None:
    print("error: invalid commit message (Markster OS standard)", file=sys.stderr)
    print("", file=sys.stderr)
    if subject:
        print(f"subject: {subject}", file=sys.stderr)
        print("", file=sys.stderr)
    print("Expected: <type>(<scope>): <summary>", file=sys.stderr)
    print("Types: feat, fix, docs, chore, refactor, test, ci, perf", file=sys.stderr)
    print("Scope: optional, lowercase a-z0-9_-", file=sys.stderr)
    print(f"Summary: required, subject line <= {MAX_SUBJECT_LENGTH} chars", file=sys.stderr)
    print("", file=sys.stderr)
    print("Examples:", file=sys.stderr)
    print("  feat(cli): add commit message validation", file=sys.stderr)
    print("  fix(hooks): install commit-msg hook by default", file=sys.stderr)
    print("  docs(readme): explain workspace repo setup", file=sys.stderr)
    print("", file=sys.stderr)
    print("Allowed prefixes: Merge, Revert, fixup!, squash!", file=sys.stderr)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="validate_commit_message.py")
    parser.add_argument("path", nargs="?", help="commit message file path")
    parser.add_argument("--message", help="commit subject line to validate directly")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    subject = load_subject(args)
    if is_valid_subject(subject):
        return 0
    print_error(subject)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
