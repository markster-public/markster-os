#!/usr/bin/env bash
# Markster OS - Bootstrap Installer
#
# Installs the managed `markster-os` CLI into the user's home directory.
# The CLI manages:
# - a stable launcher at ~/bin/markster-os
# - a managed distribution at ~/.markster-os/dist/current
# - customer workspaces at ~/.markster-os/workspaces/<slug>
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
#   OR: bash install.sh (from cloned repo)
#   OR: bash install.sh --managed-update

set -euo pipefail

DEFAULT_REPO_URL="https://raw.githubusercontent.com/markster-public/markster-os/main"
DEFAULT_ARCHIVE_URL="https://github.com/markster-public/markster-os/archive/refs/heads/main.tar.gz"
REPO_URL="$DEFAULT_REPO_URL"
ARCHIVE_URL="$DEFAULT_ARCHIVE_URL"
MARKSTER_HOME="$HOME/.markster-os"
DIST_DIR="$MARKSTER_HOME/dist/current"
TMP_DIR="$MARKSTER_HOME/tmp"
BIN_DIR="$HOME/bin"
LAUNCHER_PATH="$BIN_DIR/markster-os"
CONFIG_PATH="$MARKSTER_HOME/config.json"
MANAGED_UPDATE=false

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m' # No Color

log_info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error()   { echo -e "${RED}[ERROR]${NC} $1"; }
log_header()  { echo -e "\n${BOLD}$1${NC}"; }

for arg in "$@"; do
    case "$arg" in
        --managed-update)
            MANAGED_UPDATE=true
            ;;
        *)
            log_error "Unknown argument: $arg"
            exit 1
            ;;
    esac
done

# ─── Detect Source Location ─────────────────────────────────────────────────
# Determine if we're running from a cloned repo or via curl
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-/dev/stdin}")" 2>/dev/null && pwd || echo "")"
if [[ -d "$SCRIPT_DIR/skills" ]]; then
    SOURCE_MODE="local"
    if [[ "$MANAGED_UPDATE" == true ]]; then
        log_info "Updating from local repo: $SCRIPT_DIR"
    else
        log_info "Installing from local repo: $SCRIPT_DIR"
    fi
else
    SOURCE_MODE="remote"
    log_info "Installing managed distribution from remote archive"
fi

github_urls_from_remote() {
    local remote_url="$1"
    local slug=""
    if [[ "$remote_url" =~ ^git@github\.com:(.+)\.git$ ]]; then
        slug="${BASH_REMATCH[1]}"
    elif [[ "$remote_url" =~ ^https://github\.com/(.+)\.git$ ]]; then
        slug="${BASH_REMATCH[1]}"
    elif [[ "$remote_url" =~ ^https://github\.com/(.+)$ ]]; then
        slug="${BASH_REMATCH[1]}"
    fi

    if [[ -n "$slug" ]]; then
        REPO_URL="https://raw.githubusercontent.com/$slug/main"
        ARCHIVE_URL="https://github.com/$slug/archive/refs/heads/main.tar.gz"
    fi
}

set_urls_from_local_origin_if_available() {
    if [[ ! -d "$SCRIPT_DIR/.git" ]]; then
        return
    fi
    local remote_url=""
    remote_url="$(git -C "$SCRIPT_DIR" remote get-url origin 2>/dev/null || true)"
    if [[ -n "$remote_url" ]]; then
        github_urls_from_remote "$remote_url"
    fi
}

set_urls_from_config_if_available() {
    if [[ ! -f "$CONFIG_PATH" ]]; then
        return
    fi
    local config_repo_url=""
    local config_archive_url=""
    config_repo_url="$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("repo_url",""))' "$CONFIG_PATH" 2>/dev/null || true)"
    config_archive_url="$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("archive_url",""))' "$CONFIG_PATH" 2>/dev/null || true)"
    if [[ -n "$config_repo_url" ]]; then
        REPO_URL="$config_repo_url"
    fi
    if [[ -n "$config_archive_url" ]]; then
        ARCHIVE_URL="$config_archive_url"
    fi
}

set_local_source_from_config_if_available() {
    if [[ ! -f "$CONFIG_PATH" ]]; then
        return
    fi
    local config_source_mode=""
    local config_source_path=""
    config_source_mode="$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("source_mode",""))' "$CONFIG_PATH" 2>/dev/null || true)"
    config_source_path="$(python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d.get("source_path",""))' "$CONFIG_PATH" 2>/dev/null || true)"
    if [[ "$config_source_mode" == "local" && -n "$config_source_path" && -d "$config_source_path/skills" ]]; then
        SCRIPT_DIR="$config_source_path"
        SOURCE_MODE="local"
        log_info "Updating from original local repo: $SCRIPT_DIR"
    fi
}

if [[ "$SOURCE_MODE" == "local" ]]; then
    set_urls_from_local_origin_if_available
elif [[ "$MANAGED_UPDATE" == true ]]; then
    set_local_source_from_config_if_available
    set_urls_from_config_if_available
    if [[ "$SOURCE_MODE" == "local" ]]; then
        set_urls_from_local_origin_if_available
    fi
fi

ensure_path_setup() {
    mkdir -p "$BIN_DIR"
    local line='export PATH="$HOME/bin:$PATH"'
    local shell_name
    shell_name="$(basename "${SHELL:-zsh}")"
    local rc_file
    case "$shell_name" in
        zsh) rc_file="$HOME/.zshrc" ;;
        bash) rc_file="$HOME/.bashrc" ;;
        *) rc_file="$HOME/.profile" ;;
    esac

    touch "$rc_file"
    if ! grep -Fq "$line" "$rc_file"; then
        {
            echo ""
            echo "# Added by Markster OS"
            echo "$line"
        } >> "$rc_file"
        log_success "Added $HOME/bin to PATH in $rc_file"
    else
        log_success "$HOME/bin already configured in PATH via $rc_file"
    fi
}

install_distribution_local() {
    mkdir -p "$DIST_DIR" "$TMP_DIR"
    rm -rf "$DIST_DIR"
    mkdir -p "$DIST_DIR"
    tar -C "$SCRIPT_DIR" --exclude='.git' --exclude='__pycache__' -cf - . | tar -C "$DIST_DIR" -xf -
}

install_distribution_remote() {
    mkdir -p "$MARKSTER_HOME" "$TMP_DIR"
    local extract_dir="$TMP_DIR/extract"
    rm -rf "$extract_dir" "$DIST_DIR"
    mkdir -p "$extract_dir"
    curl -fsSL "$ARCHIVE_URL" | tar -xz -C "$extract_dir"
    local src_dir
    src_dir="$(find "$extract_dir" -maxdepth 1 -type d -name 'markster-os-*' | head -n 1)"
    if [[ -z "$src_dir" ]]; then
        log_error "Could not find extracted Markster OS archive"
        exit 1
    fi
    mkdir -p "$DIST_DIR"
    tar -C "$src_dir" --exclude='.git' --exclude='__pycache__' -cf - . | tar -C "$DIST_DIR" -xf -
}

write_launcher() {
    mkdir -p "$BIN_DIR"
    cat > "$LAUNCHER_PATH" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
exec python3 "$HOME/.markster-os/dist/current/tools/markster_os_cli.py" "$@"
EOF
    chmod +x "$LAUNCHER_PATH"
    log_success "Installed launcher: $LAUNCHER_PATH"
}

write_config() {
    mkdir -p "$MARKSTER_HOME"
    cat > "$CONFIG_PATH" <<EOF
{
  "version": 1,
  "distribution": "$DIST_DIR",
  "launcher": "$LAUNCHER_PATH",
  "source_mode": "$SOURCE_MODE",
  "source_path": "$SCRIPT_DIR",
  "repo_url": "$REPO_URL",
  "archive_url": "$ARCHIVE_URL"
}
EOF
    log_success "Wrote config: $CONFIG_PATH"
}

verify_distribution() {
    if [[ ! -f "$DIST_DIR/tools/markster_os_cli.py" ]]; then
        log_error "Managed distribution is missing tools/markster_os_cli.py"
        exit 1
    fi
    if [[ ! -f "$DIST_DIR/install.sh" ]]; then
        log_error "Managed distribution is missing install.sh"
        exit 1
    fi
}

log_header "Installing Markster OS CLI..."

if [[ "$SOURCE_MODE" == "local" ]]; then
    install_distribution_local
else
    install_distribution_remote
fi

verify_distribution
write_launcher
write_config
ensure_path_setup

# ─── Done ───────────────────────────────────────────────────────────────────
log_header "Installation complete."
echo ""
echo -e "${BOLD}CLI launcher:${NC} $LAUNCHER_PATH"
echo -e "${BOLD}Managed distribution:${NC} $DIST_DIR"
echo -e "${BOLD}Workspace root:${NC} $MARKSTER_HOME/workspaces"
echo ""
echo -e "${BOLD}Next steps:${NC}"
echo "  1. Open a new shell or run: export PATH=\"\$HOME/bin:\$PATH\""
echo "  2. Create a team workspace in its own Git repo:"
echo "     markster-os init your-company --git --path ./your-company-os"
echo "  3. Move into that workspace: cd ./your-company-os"
echo "  4. Attach your GitHub repo: markster-os attach-remote git@github.com:YOUR-ORG/YOUR-REPO.git"
echo "  5. Install skills if needed: markster-os install-skills"
echo "  6. Validate before sharing: markster-os validate ."
echo ""
echo -e "${BOLD}Need help?${NC} https://markster.ai | hello@markster.ai"
echo ""
