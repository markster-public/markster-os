#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_FRONT_MATTER_KEYS = [
    "id",
    "title",
    "type",
    "status",
    "owner",
    "created",
    "updated",
    "tags",
]

COMPANY_FILES = [
    "README.md",
    "identity.md",
    "audience.md",
    "offer.md",
    "messaging.md",
    "voice.md",
    "proof.md",
    "channels.md",
    "themes.md",
    "style-corrections.md",
    "truth-rules.md",
    "quality-checklist.md",
]

COMPANY_HEADINGS = {
    "identity.md": [
        "## One-Sentence Definition",
        "## Category",
        "## What We Do",
        "## What We Do Not Do",
        "## Why We Exist",
        "## Strategic Position",
        "## Known Identity Risks",
    ],
    "audience.md": [
        "## Primary ICP",
        "## Secondary ICP",
        "## Buying Triggers",
        "## Pain Points",
        "## Desired Outcomes",
        "## Objections",
        "## Current Alternatives",
        "## Buyer Language",
        "## Disqualifiers",
    ],
    "offer.md": [
        "## Core Offer",
        "## Entry Offer",
        "## Outcome Statement",
        "## Pricing Logic",
        "## Risk Reversal",
        "## Delivery Boundaries",
        "## Upgrade Paths",
    ],
    "messaging.md": [
        "## One-Liner",
        "## Short Pitch",
        "## Problem Framing",
        "## Differentiators",
        "## Key Claims",
        "## Message Variants",
        "## Banned Phrases",
        "## Required Anchors",
    ],
    "voice.md": [
        "## Tone",
        "## Sentence Style",
        "## Perspective",
        "## What We Sound Like",
        "## What We Do Not Sound Like",
        "## Preferred Moves",
        "## Avoid",
        "## Good Example",
        "## Bad Example",
    ],
    "proof.md": [
        "## Approved Metrics",
        "## Approved Case Studies",
        "## Approved Testimonials",
        "## Approved Claims",
        "## Unknowns and Unapproved Claims",
        "## Proof Gaps",
    ],
    "channels.md": [
        "## Primary Channels",
        "## Website",
        "## Cold Email",
        "## LinkedIn",
        "## Sales Calls and Proposals",
        "## Investor or Partner Channels",
        "## Cross-Channel Invariants",
    ],
    "themes.md": [
        "## Core Themes",
        "## Theme Boundaries",
        "## Reusable Angles",
        "## Theme-to-Offer Links",
    ],
    "style-corrections.md": [
        "## Correction Format",
        "## Corrections",
    ],
    "truth-rules.md": [
        "## No Fabrication",
        "## Claim Types",
        "### Verified",
        "### Approved Example",
        "### Hypothesis",
        "## Proof Plan",
        "## Banned Moves",
        "## Output Default",
    ],
    "quality-checklist.md": [
        "## Structure",
        "## Specificity",
        "## Evidence",
        "## Voice",
        "## Channel Fit",
        "## Final Gate",
    ],
}

CANDIDATE_TEMPLATE_HEADINGS = [
    "## Source",
    "## Proposed Target",
    "## Candidate Updates",
    "## Review Decision",
]

PROMPT_FILES = {
    "extract-objections.md",
    "extract-proof.md",
    "extract-style-corrections.md",
}

FORBIDDEN_REPO_FILES = {
    "STATE.md",
    "MASTER_LOG.md",
}

PROHIBITED_PATH_PATTERNS = [
    "/Users/",
    "C:\\\\",
    "~/",
]

PROHIBITED_CANON_PATTERNS = [
    r"\bTODO\b",
    r"\btbd\b",
    r"Speaker\s+\d+:",
    r"Interviewer:",
]

REPO_TEXT_EXTENSIONS = {
    ".md",
    ".json",
    ".py",
    ".sh",
    ".yml",
    ".yaml",
}

REPO_PROHIBITED_CONTENT_RULES = [
    ("/Users/", {"tools/validate_markster_os.py", "validation/validation-spec.md"}),
    ("~/Workspace/", {"tools/validate_markster_os.py", "validation/validation-spec.md"}),
    ("~/.claude/", {"skills/README.md", "tools/validate_markster_os.py"}),
    ("~/.codex/", {"skills/README.md", "tools/validate_markster_os.py"}),
]
CHANGELOG_RELEASE_RE = re.compile(r"^## \[(\d+\.\d+\.\d+)\] - \d{4}-\d{2}-\d{2}$", flags=re.MULTILINE)
README_VERSION_BADGE_RE = re.compile(r"img\.shields\.io/badge/version-v(\d+\.\d+\.\d+)-blue\.svg")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def repo_root_from_argv() -> Path:
    if len(sys.argv) > 2:
        fail("usage: validate_markster_os.py [repo_root]")
    if len(sys.argv) == 2:
        return Path(sys.argv[1]).expanduser().resolve()
    return Path(__file__).resolve().parent.parent


def parse_front_matter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(f"{path} is missing front matter")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        fail(f"{path} has malformed front matter")
    raw_front_matter = parts[0][4:]
    data: dict[str, str] = {}
    for line in raw_front_matter.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    for key in REQUIRED_FRONT_MATTER_KEYS:
        if key not in data or not data[key]:
            fail(f"{path} is missing front matter key `{key}`")
    return data


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ensure_headings_in_order(path: Path, headings: list[str]) -> None:
    text = read_text(path)
    cursor = 0
    for heading in headings:
        index = text.find(heading, cursor)
        if index == -1:
            fail(f"{path} is missing heading `{heading}`")
        cursor = index + len(heading)


def ensure_no_prohibited_paths(path: Path) -> None:
    text = read_text(path)
    for pattern in PROHIBITED_PATH_PATTERNS:
        if pattern in text:
            fail(f"{path} contains prohibited path pattern `{pattern}`")


def ensure_no_prohibited_canon_content(path: Path) -> None:
    text = read_text(path)
    for pattern in PROHIBITED_CANON_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            fail(f"{path} contains prohibited canonical content matching `{pattern}`")


def validate_repository_hygiene(repo_root: Path) -> None:
    for file_name in FORBIDDEN_REPO_FILES:
        path = repo_root / file_name
        if path.exists():
            fail(f"{path} must not be committed")

    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix not in REPO_TEXT_EXTENSIONS:
            continue

        relative_path = path.relative_to(repo_root).as_posix()
        text = read_text(path)
        for pattern, allowed_files in REPO_PROHIBITED_CONTENT_RULES:
            if pattern in text and relative_path not in allowed_files:
                fail(f"{path} contains prohibited repository content `{pattern}`")


def validate_company_context(repo_root: Path) -> None:
    company_context = repo_root / "company-context"
    if not company_context.exists():
        fail("company-context/ is missing")

    manifest_path = company_context / "manifest.json"
    if not manifest_path.exists():
        fail("company-context/manifest.json is missing")

    manifest = json.loads(read_text(manifest_path))
    required_files = manifest.get("required_files")
    if required_files != COMPANY_FILES:
        fail("company-context/manifest.json required_files does not match expected file inventory")

    allowed_entries = set(COMPANY_FILES + ["manifest.json"])
    actual_entries = {path.name for path in company_context.iterdir()}
    if actual_entries != allowed_entries:
        fail(
            "company-context/ file inventory mismatch. "
            f"expected {sorted(allowed_entries)}, got {sorted(actual_entries)}"
        )

    for file_name in COMPANY_FILES:
        path = company_context / file_name
        text = read_text(path)
        parse_front_matter(text, path)
        ensure_no_prohibited_paths(path)
        if file_name in COMPANY_HEADINGS:
            ensure_headings_in_order(path, COMPANY_HEADINGS[file_name])


def validate_learning_loop(repo_root: Path) -> None:
    learning_loop = repo_root / "learning-loop"
    if not learning_loop.exists():
        fail("learning-loop/ is missing")

    required_static_files = [
        learning_loop / "README.md",
        learning_loop / "promotion-rules.md",
        learning_loop / "inbox" / "README.md",
        learning_loop / "candidates" / "README.md",
        learning_loop / "candidates" / "candidate-template.md",
        learning_loop / "canon" / "README.md",
    ]
    for path in required_static_files:
        if not path.exists():
            fail(f"{path} is missing")

    prompts_dir = learning_loop / "prompts"
    actual_prompt_files = {path.name for path in prompts_dir.glob("*.md")}
    if actual_prompt_files != PROMPT_FILES:
        fail(
            "learning-loop/prompts file inventory mismatch. "
            f"expected {sorted(PROMPT_FILES)}, got {sorted(actual_prompt_files)}"
        )

    protected_markdown_paths = list(learning_loop.rglob("*.md"))
    for path in protected_markdown_paths:
        text = read_text(path)
        parse_front_matter(text, path)
        ensure_no_prohibited_paths(path)

    ensure_headings_in_order(
        learning_loop / "candidates" / "candidate-template.md",
        CANDIDATE_TEMPLATE_HEADINGS,
    )

    candidate_dir = learning_loop / "candidates"
    for path in candidate_dir.glob("*.md"):
        if path.name in {"README.md", "candidate-template.md"}:
            continue
        ensure_headings_in_order(path, CANDIDATE_TEMPLATE_HEADINGS)

    canon_dir = learning_loop / "canon"
    for path in canon_dir.glob("*.md"):
        if path.name == "README.md":
            continue
        ensure_no_prohibited_canon_content(path)


def validate_validation_docs(repo_root: Path) -> None:
    validation = repo_root / "validation"
    if not validation.exists():
        fail("validation/ is missing")
    for path in [validation / "README.md", validation / "validation-spec.md"]:
        if not path.exists():
            fail(f"{path} is missing")
        text = read_text(path)
        parse_front_matter(text, path)


def validate_release_metadata(repo_root: Path) -> None:
    changelog_path = repo_root / "CHANGELOG.md"
    readme_path = repo_root / "README.md"
    if not changelog_path.exists():
        fail("CHANGELOG.md is missing")
    if not readme_path.exists():
        fail("README.md is missing")

    changelog_text = read_text(changelog_path)
    readme_text = read_text(readme_path)

    if "## [Unreleased]" not in changelog_text:
        fail("CHANGELOG.md is missing the `## [Unreleased]` section")

    releases = CHANGELOG_RELEASE_RE.findall(changelog_text)
    if not releases:
        fail("CHANGELOG.md does not contain any released version sections")
    latest_release = releases[0]

    badge_match = README_VERSION_BADGE_RE.search(readme_text)
    if badge_match is None:
        fail("README.md is missing the version badge")
    readme_version = badge_match.group(1)

    if readme_version != latest_release:
        fail(
            "README.md version badge does not match the latest release in CHANGELOG.md. "
            f"expected v{latest_release}, found v{readme_version}"
        )


def main() -> None:
    repo_root = repo_root_from_argv()
    validate_repository_hygiene(repo_root)
    validate_company_context(repo_root)
    validate_learning_loop(repo_root)
    validate_validation_docs(repo_root)
    validate_release_metadata(repo_root)
    print(f"Markster OS validation passed: {repo_root}")


if __name__ == "__main__":
    try:
        main()
    except json.JSONDecodeError as exc:
        fail(f"manifest.json is invalid JSON: {exc}")
