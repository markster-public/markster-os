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
SKILLS = ["cold-email", "events", "content", "sales", "fundraising", "research"]
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
                "This workspace is the customer-owned runtime for Markster OS.",
                "",
                "Recommended team model:",
                "",
                "- keep this workspace in its own Git repository",
                "- commit canonical business context and promoted learning-loop canon",
                "- keep raw inbox material out of Git by default",
                "- run `markster-os validate` in CI",
                "",
                "Recommended version-controlled paths:",
                "",
                "- `company-context/`",
                "- `learning-loop/candidates/`",
                "- `learning-loop/canon/`",
                "- `learning-loop/prompts/`",
                "",
                "Ignored by default:",
                "",
                "- `learning-loop/inbox/`",
                "- local scratch and generated exports",
                "",
                "Suggested workflow:",
                "",
                "1. Attach a remote with `markster-os attach-remote <url>`",
                "2. Push the repo with normal Git or `markster-os push`",
                "3. Run your AI tool from inside this workspace",
                "4. Promote approved business knowledge into canon",
                "5. Run `markster-os sync` before starting new work",
                "6. Run `markster-os validate` before merging",
                "7. Commit and push approved changes",
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

    print(f"Initialized workspace: {workspace}")
    print("Next steps:")
    if args.git:
        print("  1. Add a Git remote for this workspace and push it to your own repository")
        print("  2. A pre-commit hook is already installed and will run `markster-os validate .`")
        print("  3. Fill in company-context/")
        print("  4. Store raw notes in learning-loop/inbox/")
        print("  5. Run your AI from inside the workspace when using Markster OS skills")
    else:
        print("  1. Consider re-running with `--git` for a team-ready workspace")
        print("  2. Fill in company-context/")
        print("  3. Store raw notes in learning-loop/inbox/")
        print("  4. Run `markster-os validate <workspace>`")
        print("  5. Run your AI from inside the workspace when using Markster OS skills")
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

    cwd = Path.cwd().resolve()
    metadata = load_workspace_metadata(cwd)
    if metadata is not None:
        print("")
        print("Active workspace")
        print(f"Path: {cwd}")
        if (cwd / ".git").exists():
            branch = git_output(cwd, ["branch", "--show-current"]) or "unknown"
            remote = git_output(cwd, ["remote", "get-url", "origin"])
            status = git_output(cwd, ["status", "--short"]) or ""
            print(f"Git: enabled")
            print(f"Branch: {branch}")
            print(f"Origin: {remote or 'not set'}")
            print(f"Uncommitted changes: {'yes' if status else 'no'}")
        else:
            print("Git: not initialized")
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
    write_workspace_files(workspace, slug)
    print(f"Upgraded workspace from managed distribution: {workspace}")
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

    print(f"Remote `{args.name}` now points to: {args.url}")
    print(f"Next step: git -C {workspace} push -u {args.name} main")
    return 0


def cmd_install_hooks(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    install_hooks(workspace)
    print(f"Installed pre-commit hook for workspace: {workspace}")
    print("The hook runs: markster-os validate .")
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

    print(f"Synchronized workspace from {args.remote}/{args.branch}: {workspace}")
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
        print("No changes to commit.")
        return 0

    commit = run_git(workspace, ["commit", "-m", args.message])
    if commit.returncode != 0:
        die(commit.stderr.strip() or commit.stdout.strip())

    print(commit.stdout.strip() or f"Committed workspace changes: {workspace}")
    return 0


def cmd_push(args: argparse.Namespace) -> int:
    workspace = Path(args.path).expanduser().resolve() if args.path else Path.cwd()
    ensure_git_workspace(workspace)

    push = run_git(workspace, ["push", args.remote, args.branch])
    if push.returncode != 0:
        die(push.stderr.strip() or push.stdout.strip())

    print(f"Pushed workspace to {args.remote}/{args.branch}: {workspace}")
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

    print(f"Created workspace backup: {output}")
    print(f"Included inbox: {'yes' if args.include_inbox else 'no'}")
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
    print(f"Exported workspace copy: {destination}")
    print(f"Included inbox: {'yes' if args.include_inbox else 'no'}")
    print("This export is suitable for sharing or committing to a separate repo after review.")
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
    init_parser.add_argument("--git", action="store_true", help="Initialize the workspace as its own Git repository")
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

    remote_parser = sub.add_parser("attach-remote", help="Attach or update a Git remote for a workspace")
    remote_parser.add_argument("url", help="Remote Git URL")
    remote_parser.add_argument("--name", default="origin", help="Remote name")
    remote_parser.add_argument("--path", help="Workspace path; defaults to current directory")
    remote_parser.set_defaults(func=cmd_attach_remote)

    hooks_parser = sub.add_parser("install-hooks", help="Install the pre-commit validation hook in a workspace")
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

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
