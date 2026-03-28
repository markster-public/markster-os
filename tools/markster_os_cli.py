#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path


MARKSTER_HOME = Path.home() / ".markster-os"
DIST_ROOT = MARKSTER_HOME / "dist" / "current"
WORKSPACES_ROOT = MARKSTER_HOME / "workspaces"
CONFIG_PATH = MARKSTER_HOME / "config.json"
LAUNCHER_PATH = Path.home() / "bin" / "markster-os"
CORE_SKILLS = ["markster-os", "cold-email", "events", "content", "sales", "fundraising", "research"]
IGNORE_NAMES = {".git", "__pycache__", ".DS_Store"}
WORKSPACE_GITIGNORE = """# Markster OS workspace
learning-loop/inbox/*
!learning-loop/inbox/README.md

# Local scratch and generated artifacts
scratch/
_local/
exports/
outputs/
backups/
*.local.md

# Python
__pycache__/
*.pyc
*.pyo

# OS and editor files
.DS_Store
.idea/
.vscode/
*~
"""
PRE_COMMIT_HOOK = """#!/usr/bin/env bash
set -euo pipefail
markster-os validate .
"""
COMMIT_MSG_HOOK = """#!/usr/bin/env bash
set -euo pipefail
python3 ~/.markster-os/dist/current/tools/validate_commit_message.py "$1"
"""
PRE_PUSH_HOOK = """#!/usr/bin/env bash
set -euo pipefail
markster-os validate .
"""
PLACEHOLDER_MARKERS = (
    "Your Company",
    "Replace with your",
    "Write one plain-language sentence",
    "Write approved phrases the buyer actually uses.",
    "One sentence.",
    "Two to three sentences.",
    "list the main active channels",
    "offer name",
)
USE_COLOR = sys.stdout.isatty() and os.environ.get("TERM", "") != "dumb"
USE_COLOR_ERR = sys.stderr.isatty() and os.environ.get("TERM", "") != "dumb"
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"


def color(text: str, code: str, *, err: bool = False) -> str:
    enabled = USE_COLOR_ERR if err else USE_COLOR
    if not enabled:
        return text
    return f"{code}{text}{RESET}"


def heading(text: str) -> str:
    return color(f"== {text} ==", BOLD + BLUE)


def subheading(text: str) -> str:
    return color(text, BOLD + CYAN)


def ok(text: str) -> str:
    return color(f"ok: {text}", GREEN)


def warn(text: str) -> str:
    return color(f"warn: {text}", YELLOW)


def bad(text: str) -> str:
    return color(f"error: {text}", RED, err=True)


def kv(label: str, value: str) -> str:
    return f"{color(label + ':', BOLD)} {value}"


def bullet(text: str, marker: str = "-") -> str:
    return f"  {color(marker, CYAN)} {text}"


def die(message: str) -> None:
    print(bad(message), file=sys.stderr)
    raise SystemExit(1)


def ensure_distribution() -> None:
    if not DIST_ROOT.exists():
        die(
            "managed distribution not found. Re-run the installer with "
            "`curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/master/install.sh | bash`."
        )


def load_workspace_metadata(path: Path) -> dict | None:
    metadata_path = path / ".markster-os-workspace.json"
    if not metadata_path.exists():
        return None
    return json.loads(metadata_path.read_text(encoding="utf-8"))


def repo_name_ok(path: Path) -> bool:
    return path.name not in IGNORE_NAMES


def copy_tree(src: Path, dst: Path) -> None:
    for item in src.iterdir():
        if not repo_name_ok(item):
            continue
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)


def available_skill_names() -> list[str]:
    ensure_distribution()
    skills_root = DIST_ROOT / "skills"
    names = []
    for path in sorted(skills_root.iterdir()):
        if path.is_dir() and (path / "SKILL.md").exists():
            names.append(path.name)
    return names


def parse_skill_metadata(skill: str) -> dict[str, str]:
    skill_path = DIST_ROOT / "skills" / skill / "SKILL.md"
    metadata: dict[str, str] = {"name": skill, "description": ""}
    if not skill_path.exists():
        return metadata
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return metadata
    _, frontmatter, _ = text.split("---", 2)
    multiline_key: str | None = None
    multiline_lines: list[str] = []
    for raw_line in frontmatter.splitlines():
        if multiline_key is not None:
            if raw_line.startswith("  "):
                multiline_lines.append(raw_line.strip())
                continue
            metadata[multiline_key] = " ".join(multiline_lines).strip()
            multiline_key = None
            multiline_lines = []

        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value in {">", "|"}:
            multiline_key = key.strip()
            multiline_lines = []
            continue
        metadata[key.strip()] = value.strip("'").strip('"')
    if multiline_key is not None:
        metadata[multiline_key] = " ".join(multiline_lines).strip()
    return metadata


def resolve_skills_to_install(args: argparse.Namespace) -> list[str]:
    available = available_skill_names()
    if args.skill:
        requested = []
        unknown = []
        for skill in args.skill:
            if skill in available:
                requested.append(skill)
            else:
                unknown.append(skill)
        if unknown:
            die(
                "unknown skills requested: "
                + ", ".join(sorted(unknown))
                + ". Run `markster-os list-skills` to see available skill names."
            )
        return requested
    if args.all_skills:
        return available
    if args.extended:
        return [skill for skill in available if skill not in CORE_SKILLS]
    return [skill for skill in CORE_SKILLS if skill in available]


def should_skip_export_path(path: Path, include_inbox: bool) -> bool:
    parts = path.parts
    if ".git" in parts or "__pycache__" in parts:
        return True
    if not include_inbox and "learning-loop" in parts and "inbox" in parts:
        return True
    return False


def export_workspace_tree(src: Path, dst: Path, include_inbox: bool) -> None:
    for item in src.iterdir():
        if not repo_name_ok(item):
            continue
        if should_skip_export_path(item, include_inbox):
            continue
        target = dst / item.name
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            export_workspace_tree(item, target, include_inbox)
        else:
            shutil.copy2(item, target)


def write_workspace_metadata(path: Path, slug: str) -> None:
    metadata = {
        "version": 1,
        "slug": slug,
        "managed_distribution": str(DIST_ROOT),
    }
    (path / ".markster-os-workspace.json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )


def write_workspace_files(path: Path, slug: str) -> None:
    (path / ".gitignore").write_text(WORKSPACE_GITIGNORE, encoding="utf-8")
    (path / "WORKSPACE.md").write_text(
        "\n".join(
            [
                "# Markster OS Workspace",
                "",
                f"Workspace slug: `{slug}`",
                "",
                "This repository is the customer-owned runtime for Markster OS.",
                "The upstream `markster-os` repository is the template and CLI source.",
                "This workspace is where your team stores the real business context and the approved operating system for your company.",
                "",
                "## Start Here",
                "",
                "If you have just created this workspace, do these in order:",
                "",
                "1. Attach a remote with `markster-os attach-remote <url>`",
                "2. Push the repo to your own Git hosting",
                "3. Run `markster-os start`",
                "4. Fill in `company-context/identity.md`, `company-context/audience.md`, `company-context/offer.md`, and `company-context/messaging.md` first",
                "5. Keep raw notes and transcripts in `learning-loop/inbox/`",
                "6. Only promote approved updates into canon",
                "",
                "## What This Repo Is For",
                "",
                "- store the canonical company context for your business",
                "- run Markster OS playbooks and skills from inside this repo",
                "- review and approve changes to your business canon through Git",
                "- keep the GTM system reusable across multiple employees",
                "",
                "## Recommended Team Model",
                "",
                "- keep this workspace in its own Git repository",
                "- commit canonical business context and promoted learning-loop canon",
                "- keep raw inbox material out of Git by default",
                "- run `markster-os validate` in CI",
                "",
                "## Version-Controlled By Default",
                "",
                "- `company-context/`",
                "- `learning-loop/candidates/`",
                "- `learning-loop/canon/`",
                "- `learning-loop/prompts/`",
                "- `WORKSPACE.md`",
                "",
                "## Ignored By Default",
                "",
                "- `learning-loop/inbox/`",
                "- local scratch and generated exports",
                "",
                "## First-Time Setup",
                "",
                "1. Attach a remote with `markster-os attach-remote <url>`",
                "2. Push the repo with normal Git or `markster-os push`",
                "3. Run `markster-os start` to see what still needs work",
                "4. Fill in `company-context/` with the real business context",
                "5. Keep raw notes and transcripts in `learning-loop/inbox/`",
                "6. Run your AI tool from inside this workspace",
                "",
                "## Fill These Files First",
                "",
                "Fill these first before trying to run major playbooks:",
                "",
                "- `company-context/identity.md`",
                "- `company-context/audience.md`",
                "- `company-context/offer.md`",
                "- `company-context/messaging.md`",
                "",
                "Then fill these next:",
                "",
                "- `company-context/voice.md`",
                "- `company-context/proof.md`",
                "- `company-context/channels.md`",
                "- `company-context/themes.md`",
                "",
                "Use `learning-loop/candidates/example-company-context-update.md` as a model for how to propose canon changes.",
                "",
                "## Daily Workflow",
                "",
                "1. Run `markster-os sync` before starting work",
                "2. Run the AI tool from inside this repo",
                "3. Make changes only to the right canonical files",
                "4. Run `markster-os validate .` before committing",
                "5. Commit and push approved changes",
                "",
                "## Rules For AI Agents",
                "",
                "- do not invent files or folders outside the approved workspace structure",
                "- do not treat `learning-loop/inbox/` as canonical business truth",
                "- do not make claims that are not supported by `company-context/proof.md`",
                "- prefer updating existing canon files over creating new documents",
                "- validate before commit",
                "",
                "## Validation",
                "",
                "- pre-commit and pre-push hooks are installed for Git workspaces",
                "- pre-commit and pre-push run `markster-os validate .`",
                "- commit-msg enforces the commit subject format: `type(scope): summary`",
                "- CI should also run `markster-os validate .` on pull requests",
                "- if you push directly to the default branch, the local pre-push hook is the last safety check before the remote",
                "",
                "## Useful Commands",
                "",
                "- `markster-os status`",
                "- `markster-os start`",
                "- `markster-os doctor`",
                "- `markster-os sync`",
                "- `markster-os validate .`",
                "- `markster-os commit -m \"docs(context): update workspace\"`",
                "- `markster-os push`",
                "- `markster-os backup-workspace .`",
                "- `markster-os export-workspace .`",
                "",
                "## Recovery",
                "",
                "- if the workspace template changes upstream, run `markster-os upgrade-workspace .`",
                "- if hooks are missing, run `markster-os install-hooks .`",
                "- if the company context still shows template text, run `markster-os start` and replace the flagged files first",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def git_init_workspace(path: Path) -> None:
    if (path / ".git").exists():
        return
    result = subprocess.run(
        ["git", "init", "-b", "main", str(path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        die(f"git init failed: {result.stderr.strip() or result.stdout.strip()}")


def install_hooks(path: Path) -> None:
    ensure_git_workspace(path)
    hooks_dir = path / ".git" / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    pre_commit = hooks_dir / "pre-commit"
    pre_commit.write_text(PRE_COMMIT_HOOK, encoding="utf-8")
    pre_commit.chmod(0o755)
    commit_msg = hooks_dir / "commit-msg"
    commit_msg.write_text(COMMIT_MSG_HOOK, encoding="utf-8")
    commit_msg.chmod(0o755)
    pre_push = hooks_dir / "pre-push"
    pre_push.write_text(PRE_PUSH_HOOK, encoding="utf-8")
    pre_push.chmod(0o755)


def ensure_git_workspace(path: Path) -> None:
    if not (path / ".git").exists():
        die(f"workspace is not a Git repository: {path}. Re-run init with `--git` or run git init.")


def run_git(path: Path, args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(path), *args],
        capture_output=True,
        text=True,
    )


def git_output(path: Path, args: list[str]) -> str | None:
    result = run_git(path, args)
    if result.returncode != 0:
        return None
    return result.stdout.strip()


def is_git_workspace(path: Path) -> bool:
    return (path / ".git").exists()


def has_pre_commit_hook(path: Path) -> bool:
    hook = path / ".git" / "hooks" / "pre-commit"
    return hook.exists()


def has_pre_push_hook(path: Path) -> bool:
    hook = path / ".git" / "hooks" / "pre-push"
    return hook.exists()


def has_commit_msg_hook(path: Path) -> bool:
    hook = path / ".git" / "hooks" / "commit-msg"
    return hook.exists()


def company_context_placeholder_hits(path: Path) -> list[str]:
    hits: list[str] = []
    manifest_path = path / "company-context" / "manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            hits.append("company-context/manifest.json is not valid JSON")
        else:
            manifest_values = [
                str(manifest.get("company_name", "")),
                str(manifest.get("category", "")),
                str(manifest.get("primary_audience", "")),
                str(manifest.get("core_offer", "")),
            ]
            if any("Your Company" in value or "Replace with" in value for value in manifest_values):
                hits.append("company-context/manifest.json still contains template values")

    files_to_check = [
        "identity.md",
        "audience.md",
        "offer.md",
        "messaging.md",
        "channels.md",
        "style-corrections.md",
        "themes.md",
        "voice.md",
    ]
    for relative_name in files_to_check:
        file_path = path / "company-context" / relative_name
        if not file_path.exists():
            continue
        content = file_path.read_text(encoding="utf-8")
        for marker in PLACEHOLDER_MARKERS:
            if marker in content:
                hits.append(f"company-context/{relative_name} still includes template text")
                break
    return hits


def workspace_readiness(path: Path) -> list[tuple[str, bool, str]]:
    checks: list[tuple[str, bool, str]] = []
    git_enabled = is_git_workspace(path)
    checks.append(
        (
            "Git repository",
            git_enabled,
            "initialize Git or recreate with `markster-os init --git --path ...`",
        )
    )

    remote = git_output(path, ["remote", "get-url", "origin"]) if git_enabled else None
    checks.append(
        (
            "Git remote",
            bool(remote),
            "attach a remote with `markster-os attach-remote <url>`",
        )
    )

    checks.append(
        (
            "Pre-commit hook",
            git_enabled and has_pre_commit_hook(path),
            "install hooks with `markster-os install-hooks .`",
        )
    )
    checks.append(
        (
            "Pre-push hook",
            git_enabled and has_pre_push_hook(path),
            "install hooks with `markster-os install-hooks .`",
        )
    )
    checks.append(
        (
            "Commit message hook",
            git_enabled and has_commit_msg_hook(path),
            "install hooks with `markster-os install-hooks .`",
        )
    )

    placeholder_hits = company_context_placeholder_hits(path)
    checks.append(
        (
            "Company context filled",
            not placeholder_hits,
            "replace the remaining template text in `company-context/`",
        )
    )
    return checks


def cmd_init(args: argparse.Namespace) -> int:
    ensure_distribution()
    slug = args.slug.strip()
    if not slug:
        die("workspace slug must not be empty")

    workspace = (
        Path(args.path).expanduser().resolve()
        if args.path
        else (WORKSPACES_ROOT / slug).resolve()
    )

    if workspace.exists():
        if any(workspace.iterdir()) and not args.force:
            die(f"workspace already exists and is not empty: {workspace}")
    else:
        workspace.mkdir(parents=True, exist_ok=True)

    copy_tree(DIST_ROOT, workspace)
    write_workspace_metadata(workspace, slug)
    write_workspace_files(workspace, slug)
    if args.git:
        git_init_workspace(workspace)
        install_hooks(workspace)

    print(heading("Workspace Initialized"))
    print(kv("Path", str(workspace)))
    print("")
    print(subheading("Next steps"))
    if args.git:
        print("  1. Add a Git remote for this workspace and push it to your own repository")
        print("  2. Pre-commit and pre-push hooks are already installed and will run `markster-os validate .`")
        print("  3. Commit messages are enforced locally as `type(scope): summary`")
        print("  4. Run `markster-os start`")
        print("  5. Fill in company-context/")
        print("  6. Store raw notes in learning-loop/inbox/")
        print("  7. Run your AI from inside the workspace when using Markster OS skills")
    else:
        print("  1. Consider re-running with `--git` for a team-ready workspace")
        print("  2. Run `markster-os start --path <workspace>`")
        print("  3. Fill in company-context/")
        print("  4. Store raw notes in learning-loop/inbox/")
        print("  5. Run `markster-os validate <workspace>`")
        print("  6. Run your AI from inside the workspace when using Markster OS skills")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    ensure_distribution()
    target = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    validator = DIST_ROOT / "tools" / "validate_markster_os.py"
    result = subprocess.run([sys.executable, str(validator), str(target)])
    return result.returncode


def cmd_validate_commit_message(args: argparse.Namespace) -> int:
    ensure_distribution()
    validator = DIST_ROOT / "tools" / "validate_commit_message.py"
    command = [sys.executable, str(validator)]
    if args.message:
        command.extend(["--message", args.message])
    elif args.path:
        command.append(args.path)
    else:
        die("provide --message or a commit message file path")
    result = subprocess.run(command)
    return result.returncode


def cmd_list_skills(args: argparse.Namespace) -> int:
    skills = available_skill_names()
    core_count = len([s for s in skills if s in CORE_SKILLS])
    print(heading("Markster OS Skills"))
    print(kv("Total available", str(len(skills))))
    print(kv("Core installed by default", str(core_count)))
    print("")
    for skill in skills:
        metadata = parse_skill_metadata(skill)
        label = "core" if skill in CORE_SKILLS else "extended"
        description = metadata.get("description", "").replace("\n", " ").strip()
        label_text = color(label, GREEN if label == "core" else YELLOW)
        print(f"{color('-', CYAN)} {color(skill, BOLD)} ({label_text})")
        if description:
            print(f"  {color(description, DIM)}")
    print("")
    print(subheading("Install examples"))
    print(bullet("markster-os install-skills"))
    print(bullet("markster-os install-skills --skill website-copywriter --skill vc-review"))
    print(bullet("markster-os install-skills --extended"))
    print(bullet("markster-os install-skills --all-skills --all"))
    return 0


def install_skill_to_dir(skill: str, target_root: Path) -> None:
    src = DIST_ROOT / "skills" / skill / "SKILL.md"
    if not src.exists():
        die(f"missing skill in distribution: {skill}")
    skill_dir = target_root / skill
    skill_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, skill_dir / "SKILL.md")
    print(ok(f"installed skill {skill} -> {skill_dir / 'SKILL.md'}"))


def cmd_install_skills(args: argparse.Namespace) -> int:
    ensure_distribution()
    selected_skills = resolve_skills_to_install(args)
    homes = []
    if args.claude or args.all:
        homes.append(Path.home() / ".claude" / "skills")
    if args.codex or args.all:
        homes.append(Path.home() / ".codex" / "skills")
    if args.gemini or args.all:
        homes.append(Path.home() / ".gemini" / "skills")
    if not homes:
        homes = [Path.home() / ".claude" / "skills", Path.home() / ".codex" / "skills"]
    homes = list(dict.fromkeys(homes))

    for root in homes:
        root.mkdir(parents=True, exist_ok=True)
        for skill in selected_skills:
            install_skill_to_dir(skill, root)

    print(heading("Skills Installed"))
    print(kv("Count", str(len(selected_skills))))
    print(kv("Skills", ", ".join(selected_skills)))
    print("")
    print(warn("run your AI from inside a Markster OS workspace so the skills can resolve repo-relative docs"))
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    ensure_distribution()
    installer = DIST_ROOT / "install.sh"
    if not installer.exists():
        die(f"installer missing from distribution: {installer}")
    result = subprocess.run(["bash", str(installer), "--managed-update"])
    return result.returncode


def cmd_status(args: argparse.Namespace) -> int:
    distribution_exists = DIST_ROOT.exists()
    launcher_exists = LAUNCHER_PATH.exists()
    workspaces = []
    if WORKSPACES_ROOT.exists():
        for path in sorted(WORKSPACES_ROOT.iterdir()):
            if not path.is_dir():
                continue
            metadata = load_workspace_metadata(path)
            workspaces.append(
                {
                    "name": path.name,
                    "path": str(path),
                    "managed": metadata is not None,
                }
            )

    print(heading("Markster OS Status"))
    print(kv("Distribution", color("installed", GREEN) if distribution_exists else color("missing", RED)))
    print(kv("Launcher", color("installed", GREEN) if launcher_exists else color("missing", RED)))
    print(kv("Workspace root", str(WORKSPACES_ROOT)))
    print(kv("Workspaces", str(len(workspaces))))
    if workspaces:
        for workspace in workspaces:
            managed = "managed" if workspace["managed"] else "unmanaged"
            print(bullet(f"{workspace['name']} ({managed})"))
            print(f"    {color(workspace['path'], DIM)}")
    else:
        print(bullet("none"))

    cwd = Path.cwd().resolve()
    metadata = load_workspace_metadata(cwd)
    if metadata is not None:
        print("")
        print(subheading("Active workspace"))
        print(kv("Path", str(cwd)))
        if is_git_workspace(cwd):
            branch = git_output(cwd, ["branch", "--show-current"]) or "unknown"
            remote = git_output(cwd, ["remote", "get-url", "origin"])
            status = git_output(cwd, ["status", "--short"]) or ""
            print(kv("Git", color("enabled", GREEN)))
            print(kv("Branch", branch))
            print(kv("Origin", remote or "not set"))
            print(kv("Uncommitted changes", color("yes", YELLOW) if status else color("no", GREEN)))
            print(kv("Pre-commit hook", color("installed", GREEN) if has_pre_commit_hook(cwd) else color("missing", YELLOW)))
            print(kv("Pre-push hook", color("installed", GREEN) if has_pre_push_hook(cwd) else color("missing", YELLOW)))
            print(kv("Commit-msg hook", color("installed", GREEN) if has_commit_msg_hook(cwd) else color("missing", YELLOW)))
        else:
            print(kv("Git", color("not initialized", YELLOW)))
            print(bullet("run `git init -b main` or recreate the workspace with `markster-os init --git --path ...`"))
            print(bullet("after Git init, run `markster-os install-hooks .`"))
        placeholder_hits = company_context_placeholder_hits(cwd)
        print(kv("Company context", color("ready", GREEN) if not placeholder_hits else color("template values remain", YELLOW)))
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    problems: list[str] = []
    checks: list[str] = []

    if DIST_ROOT.exists():
        checks.append(f"ok: managed distribution exists at {DIST_ROOT}")
    else:
        problems.append(f"missing managed distribution at {DIST_ROOT}")

    if LAUNCHER_PATH.exists():
        checks.append(f"ok: launcher exists at {LAUNCHER_PATH}")
    else:
        problems.append(f"missing launcher at {LAUNCHER_PATH}")

    path_parts = os.environ.get("PATH", "").split(os.pathsep)
    if str(LAUNCHER_PATH.parent) in path_parts:
        checks.append(f"ok: {LAUNCHER_PATH.parent} is on PATH")
    else:
        problems.append(f"{LAUNCHER_PATH.parent} is not on PATH in this shell")

    if CONFIG_PATH.exists():
        checks.append(f"ok: config exists at {CONFIG_PATH}")
    else:
        problems.append(f"missing config at {CONFIG_PATH}")

    if WORKSPACES_ROOT.exists():
        checks.append(f"ok: workspaces root exists at {WORKSPACES_ROOT}")
    else:
        problems.append(f"missing workspaces root at {WORKSPACES_ROOT}")

    for line in checks:
        print(ok(line.removeprefix("ok: ")))
    if problems:
        for line in problems:
            print(warn(line))
        return 1

    print(ok("doctor: no problems found"))
    return 0


def cmd_upgrade_workspace(args: argparse.Namespace) -> int:
    ensure_distribution()
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    metadata = load_workspace_metadata(workspace)
    if metadata is None and not args.force:
        die(
            "workspace metadata not found. Run this inside a Markster OS workspace or pass --force "
            "to overlay the current distribution onto the target path."
        )

    if not workspace.exists():
        die(f"workspace does not exist: {workspace}")

    copy_tree(DIST_ROOT, workspace)
    slug = metadata.get("slug", workspace.name) if metadata else workspace.name
    write_workspace_metadata(workspace, slug)
    write_workspace_files(workspace, slug)
    print(ok(f"upgraded workspace from managed distribution: {workspace}"))
    return 0


def cmd_attach_remote(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    ensure_git_workspace(workspace)

    existing = run_git(workspace, ["remote"])
    if existing.returncode != 0:
        die(existing.stderr.strip() or existing.stdout.strip())

    remotes = {line.strip() for line in existing.stdout.splitlines() if line.strip()}
    if args.name in remotes:
        result = run_git(workspace, ["remote", "set-url", args.name, args.url])
    else:
        result = run_git(workspace, ["remote", "add", args.name, args.url])
    if result.returncode != 0:
        die(result.stderr.strip() or result.stdout.strip())

    print(ok(f"remote `{args.name}` now points to: {args.url}"))
    print(bullet(f"next: git -C {workspace} push -u {args.name} main"))
    return 0


def cmd_install_hooks(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    install_hooks(workspace)
    print(ok(f"installed pre-commit, commit-msg, and pre-push hooks for workspace: {workspace}"))
    print(bullet("pre-commit: markster-os validate ."))
    print(bullet("commit-msg: type(scope): summary"))
    print(bullet("pre-push: markster-os validate ."))
    return 0


def cmd_sync(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    ensure_git_workspace(workspace)

    fetch = run_git(workspace, ["fetch", args.remote])
    if fetch.returncode != 0:
        die(fetch.stderr.strip() or fetch.stdout.strip())

    pull = run_git(workspace, ["pull", "--rebase", args.remote, args.branch])
    if pull.returncode != 0:
        die(pull.stderr.strip() or pull.stdout.strip())

    print(ok(f"synchronized workspace from {args.remote}/{args.branch}: {workspace}"))
    return 0


def cmd_commit(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    ensure_git_workspace(workspace)

    add = run_git(workspace, ["add", "-A"])
    if add.returncode != 0:
        die(add.stderr.strip() or add.stdout.strip())

    status = run_git(workspace, ["status", "--short"])
    if status.returncode != 0:
        die(status.stderr.strip() or status.stdout.strip())
    if not status.stdout.strip():
        print(warn("no changes to commit"))
        return 0

    commit = run_git(workspace, ["commit", "-m", args.message])
    if commit.returncode != 0:
        die(commit.stderr.strip() or commit.stdout.strip())

    print(commit.stdout.strip() or ok(f"committed workspace changes: {workspace}"))
    return 0


def cmd_push(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    ensure_git_workspace(workspace)

    push = run_git(workspace, ["push", args.remote, args.branch])
    if push.returncode != 0:
        die(push.stderr.strip() or push.stdout.strip())

    print(ok(f"pushed workspace to {args.remote}/{args.branch}: {workspace}"))
    return 0


def cmd_backup_workspace(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    if not workspace.exists():
        die(f"workspace does not exist: {workspace}")

    backup_root = MARKSTER_HOME / "backups"
    backup_root.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    output = (
        Path(args.output).expanduser().resolve()
        if args.output
        else backup_root / f"{workspace.name}-{timestamp}.tar.gz"
    )

    with tarfile.open(output, "w:gz") as tar:
        for item in workspace.rglob("*"):
            if should_skip_export_path(item.relative_to(workspace), include_inbox=args.include_inbox):
                continue
            tar.add(item, arcname=item.relative_to(workspace))

    print(heading("Workspace Backup"))
    print(kv("Archive", str(output)))
    print(kv("Included inbox", "yes" if args.include_inbox else "no"))
    return 0


def cmd_export_workspace(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    if not workspace.exists():
        die(f"workspace does not exist: {workspace}")

    destination = (
        Path(args.output).expanduser().resolve()
        if args.output
        else (MARKSTER_HOME / "exports" / workspace.name).resolve()
    )
    if destination.exists():
        if any(destination.iterdir()) and not args.force:
            die(f"export destination already exists and is not empty: {destination}")
    else:
        destination.mkdir(parents=True, exist_ok=True)

    export_workspace_tree(workspace, destination, include_inbox=args.include_inbox)
    print(heading("Workspace Export"))
    print(kv("Destination", str(destination)))
    print(kv("Included inbox", "yes" if args.include_inbox else "no"))
    print(warn("this export is suitable for sharing or committing to a separate repo after review"))
    return 0


def cmd_paths(args: argparse.Namespace) -> int:
    print(heading("Markster OS Paths"))
    print(kv("Home", str(MARKSTER_HOME)))
    print(kv("Distribution", str(DIST_ROOT)))
    print(kv("Workspaces", str(WORKSPACES_ROOT)))
    print(kv("Launcher", str(LAUNCHER_PATH)))
    print(kv("Config", str(CONFIG_PATH)))
    return 0


def cmd_start(args: argparse.Namespace) -> int:
    cwd = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    metadata = load_workspace_metadata(cwd)
    if metadata is None:
        die("not inside a Markster OS workspace. Run this from a workspace or pass --path.")

    print(heading("Markster OS Start"))
    print(kv("Workspace", str(cwd)))
    print("")
    checks = workspace_readiness(cwd)
    print(subheading("Readiness checklist"))
    for label, ok, next_step in checks:
        marker = color("ok", GREEN) if ok else color("needs work", YELLOW)
        print(bullet(f"{label}: {marker}"))
        if not ok:
            print(f"    {color('next:', BOLD)} {next_step}")

    placeholder_hits = company_context_placeholder_hits(cwd)
    if placeholder_hits:
        print("")
        print(subheading("Company context gaps"))
        for hit in placeholder_hits:
            print(bullet(hit))

    print("")
    print(subheading("Recommended workflow"))
    print("  1. Run `markster-os sync` if this is a shared repo")
    print("  2. Keep raw notes in `learning-loop/inbox/`")
    print("  3. Run your AI tool from this directory")
    print("  4. Before commit: `markster-os validate .`")
    print("  5. Then: `markster-os commit -m \"docs(context): update workspace\"` and `markster-os push`")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="markster-os")
    sub = parser.add_subparsers(dest="command", required=True)

    init_parser = sub.add_parser("init", help="Create a new Markster OS workspace")
    init_parser.add_argument("slug", help="Workspace slug")
    init_parser.add_argument("--path", help="Custom workspace path")
    init_parser.add_argument("--git", action="store_true", help="Initialize the workspace as its own Git repository")
    init_parser.add_argument("--force", action="store_true", help="Allow initializing into a non-empty path")
    init_parser.set_defaults(func=cmd_init)

    validate_parser = sub.add_parser("validate", help="Validate a workspace")
    validate_parser.add_argument("path", nargs="?", help="Workspace path; defaults to current directory")
    validate_parser.set_defaults(func=cmd_validate)

    validate_commit_parser = sub.add_parser("validate-commit-message", help="Validate a commit subject line")
    validate_commit_parser.add_argument("path", nargs="?", help="Commit message file path")
    validate_commit_parser.add_argument("--message", help="Commit subject line to validate directly")
    validate_commit_parser.set_defaults(func=cmd_validate_commit_message)

    list_skills_parser = sub.add_parser("list-skills", help="List public Markster OS skills available in the distribution")
    list_skills_parser.set_defaults(func=cmd_list_skills)

    install_skills_parser = sub.add_parser("install-skills", help="Install Markster OS slash-command skills")
    install_skills_parser.add_argument("--claude", action="store_true", help="Install for Claude Code")
    install_skills_parser.add_argument("--codex", action="store_true", help="Install for Codex")
    install_skills_parser.add_argument("--gemini", action="store_true", help="Install for Gemini CLI")
    install_skills_parser.add_argument("--all", action="store_true", help="Install for all supported environments")
    install_skills_parser.add_argument("--skill", action="append", help="Install a specific skill by name; repeat for multiple skills")
    install_skills_parser.add_argument("--extended", action="store_true", help="Install all public skills except the default core set")
    install_skills_parser.add_argument("--all-skills", action="store_true", help="Install every public skill in the distribution")
    install_skills_parser.set_defaults(func=cmd_install_skills)

    update_parser = sub.add_parser("update", help="Update the managed Markster OS distribution")
    update_parser.set_defaults(func=cmd_update)

    status_parser = sub.add_parser("status", help="Show installed distribution and workspace status")
    status_parser.set_defaults(func=cmd_status)

    doctor_parser = sub.add_parser("doctor", help="Run local health checks for the Markster OS installation")
    doctor_parser.set_defaults(func=cmd_doctor)

    upgrade_parser = sub.add_parser("upgrade-workspace", help="Overlay the current distribution onto a workspace")
    upgrade_parser.add_argument("path", nargs="?", help="Workspace path; defaults to current directory")
    upgrade_parser.add_argument("--force", action="store_true", help="Allow overlaying onto a path without workspace metadata")
    upgrade_parser.set_defaults(func=cmd_upgrade_workspace)

    remote_parser = sub.add_parser("attach-remote", help="Attach or update a Git remote for a workspace")
    remote_parser.add_argument("url", help="Remote Git URL")
    remote_parser.add_argument("--name", default="origin", help="Remote name")
    remote_parser.add_argument("--path", help="Workspace path; defaults to current directory")
    remote_parser.set_defaults(func=cmd_attach_remote)

    hooks_parser = sub.add_parser("install-hooks", help="Install the local validation hooks in a workspace")
    hooks_parser.add_argument("path", nargs="?", help="Workspace path; defaults to current directory")
    hooks_parser.set_defaults(func=cmd_install_hooks)

    sync_parser = sub.add_parser("sync", help="Fetch and pull --rebase a workspace")
    sync_parser.add_argument("--path", help="Workspace path; defaults to current directory")
    sync_parser.add_argument("--remote", default="origin", help="Remote name")
    sync_parser.add_argument("--branch", default="main", help="Branch name")
    sync_parser.set_defaults(func=cmd_sync)

    commit_parser = sub.add_parser("commit", help="Add and commit all workspace changes")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")
    commit_parser.add_argument("--path", help="Workspace path; defaults to current directory")
    commit_parser.set_defaults(func=cmd_commit)

    push_parser = sub.add_parser("push", help="Push a workspace branch")
    push_parser.add_argument("--path", help="Workspace path; defaults to current directory")
    push_parser.add_argument("--remote", default="origin", help="Remote name")
    push_parser.add_argument("--branch", default="main", help="Branch name")
    push_parser.set_defaults(func=cmd_push)

    backup_parser = sub.add_parser("backup-workspace", help="Create a tar.gz backup of a workspace")
    backup_parser.add_argument("path", nargs="?", help="Workspace path; defaults to current directory")
    backup_parser.add_argument("--output", help="Output tar.gz path")
    backup_parser.add_argument("--include-inbox", action="store_true", help="Include learning-loop/inbox in the backup")
    backup_parser.set_defaults(func=cmd_backup_workspace)

    export_parser = sub.add_parser("export-workspace", help="Export a workspace copy for sharing or versioning")
    export_parser.add_argument("path", nargs="?", help="Workspace path; defaults to current directory")
    export_parser.add_argument("--output", help="Destination directory")
    export_parser.add_argument("--include-inbox", action="store_true", help="Include learning-loop/inbox in the export")
    export_parser.add_argument("--force", action="store_true", help="Allow exporting into a non-empty directory")
    export_parser.set_defaults(func=cmd_export_workspace)

    paths_parser = sub.add_parser("paths", help="Show managed Markster OS paths")
    paths_parser.set_defaults(func=cmd_paths)

    start_parser = sub.add_parser("start", help="Show the recommended next steps for a workspace")
    start_parser.add_argument("--path", help="Workspace path; defaults to current directory")
    start_parser.set_defaults(func=cmd_start)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
