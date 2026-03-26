#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


MARKSTER_HOME = Path.home() / ".markster-os"
DIST_ROOT = MARKSTER_HOME / "dist" / "current"
WORKSPACES_ROOT = MARKSTER_HOME / "workspaces"
CONFIG_PATH = MARKSTER_HOME / "config.json"
LAUNCHER_PATH = Path.home() / "bin" / "markster-os"
SKILLS = ["cold-email", "events", "content", "sales", "fundraising", "research"]
IGNORE_NAMES = {".git", "__pycache__", ".DS_Store"}


def die(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def ensure_distribution() -> None:
    if not DIST_ROOT.exists():
        die(
            "managed distribution not found. Re-run the installer with "
            "`curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash`."
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

    print(f"Initialized workspace: {workspace}")
    print("Next steps:")
    print("  1. Fill in company-context/")
    print("  2. Store raw notes in learning-loop/inbox/")
    print("  3. Run `markster-os validate <workspace>`")
    print("  4. Run your AI from inside the workspace when using Markster OS skills")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    ensure_distribution()
    target = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    validator = DIST_ROOT / "tools" / "validate_markster_os.py"
    result = subprocess.run([sys.executable, str(validator), str(target)])
    return result.returncode


def install_skill_to_dir(skill: str, target_root: Path) -> None:
    src = DIST_ROOT / "skills" / skill / "SKILL.md"
    if not src.exists():
        die(f"missing skill in distribution: {skill}")
    skill_dir = target_root / skill
    skill_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, skill_dir / "SKILL.md")
    print(f"Installed skill: {skill_dir / 'SKILL.md'}")


def cmd_install_skills(args: argparse.Namespace) -> int:
    ensure_distribution()
    homes = []
    if args.claude or args.all:
        homes.append(Path.home() / ".claude" / "skills")
    if args.codex or args.all:
        homes.append(Path.home() / ".codex" / "skills")
    if args.gemini or args.all:
        homes.append(Path.home() / ".gemini" / "skills")
    if not homes:
        homes = [Path.home() / ".claude" / "skills", Path.home() / ".codex" / "skills"]

    for root in homes:
        root.mkdir(parents=True, exist_ok=True)
        for skill in SKILLS:
            install_skill_to_dir(skill, root)

    print("Run your AI from inside a Markster OS workspace so the skills can resolve repo-relative docs.")
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

    print("Markster OS Status")
    print(f"Distribution: {'installed' if distribution_exists else 'missing'}")
    print(f"Launcher: {'installed' if launcher_exists else 'missing'}")
    print(f"Workspace root: {WORKSPACES_ROOT}")
    print(f"Workspaces: {len(workspaces)}")
    if workspaces:
        for workspace in workspaces:
            managed = "managed" if workspace["managed"] else "unmanaged"
            print(f"  - {workspace['name']} ({managed})")
            print(f"    {workspace['path']}")
    else:
        print("  - none")
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
        print(line)
    if problems:
        for line in problems:
            print(f"problem: {line}")
        return 1

    print("doctor: no problems found")
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
    print(f"Upgraded workspace from managed distribution: {workspace}")
    return 0


def cmd_paths(args: argparse.Namespace) -> int:
    print("Markster OS Paths")
    print(f"Home: {MARKSTER_HOME}")
    print(f"Distribution: {DIST_ROOT}")
    print(f"Workspaces: {WORKSPACES_ROOT}")
    print(f"Launcher: {LAUNCHER_PATH}")
    print(f"Config: {CONFIG_PATH}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="markster-os")
    sub = parser.add_subparsers(dest="command", required=True)

    init_parser = sub.add_parser("init", help="Create a new Markster OS workspace")
    init_parser.add_argument("slug", help="Workspace slug")
    init_parser.add_argument("--path", help="Custom workspace path")
    init_parser.add_argument("--force", action="store_true", help="Allow initializing into a non-empty path")
    init_parser.set_defaults(func=cmd_init)

    validate_parser = sub.add_parser("validate", help="Validate a workspace")
    validate_parser.add_argument("path", nargs="?", help="Workspace path; defaults to current directory")
    validate_parser.set_defaults(func=cmd_validate)

    install_skills_parser = sub.add_parser("install-skills", help="Install Markster OS slash-command skills")
    install_skills_parser.add_argument("--claude", action="store_true", help="Install for Claude Code")
    install_skills_parser.add_argument("--codex", action="store_true", help="Install for Codex")
    install_skills_parser.add_argument("--gemini", action="store_true", help="Install for Gemini CLI")
    install_skills_parser.add_argument("--all", action="store_true", help="Install for all supported environments")
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

    paths_parser = sub.add_parser("paths", help="Show managed Markster OS paths")
    paths_parser.set_defaults(func=cmd_paths)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
