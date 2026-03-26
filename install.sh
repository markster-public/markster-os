#!/usr/bin/env bash
# Markster OS - Install Script
# Installs skills to the correct location for your AI environment.
# Supports: Claude Code, Codex, Gemini CLI
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/markster-public/markster-os/main/install.sh | bash
#   OR: bash install.sh (from cloned repo)

set -euo pipefail

REPO_URL="https://raw.githubusercontent.com/markster-public/markster-os/main"
SKILLS=("cold-email" "events" "content" "sales" "fundraising" "research")

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

# ─── Detect Source Location ─────────────────────────────────────────────────
# Determine if we're running from a cloned repo or via curl
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-/dev/stdin}")" 2>/dev/null && pwd || echo "")"
if [[ -d "$SCRIPT_DIR/skills" ]]; then
    SOURCE_MODE="local"
    log_info "Installing from local repo: $SCRIPT_DIR"
else
    SOURCE_MODE="remote"
    log_info "Installing from remote: $REPO_URL"
fi

# ─── Detect AI Environment ──────────────────────────────────────────────────
log_header "Detecting AI environment..."

CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
CODEX_SKILLS_DIR="$HOME/.codex/skills"
GEMINI_SKILLS_DIR="$HOME/.gemini/skills"

has_claude=false
has_codex=false
has_gemini=false

if command -v claude &>/dev/null || [[ -d "$HOME/.claude" ]]; then
    has_claude=true
    log_success "Claude Code detected"
fi

if command -v codex &>/dev/null || [[ -d "$HOME/.codex" ]]; then
    has_codex=true
    log_success "Codex detected"
fi

if command -v gemini &>/dev/null || [[ -d "$HOME/.gemini" ]]; then
    has_gemini=true
    log_success "Gemini CLI detected"
fi

if [[ "$has_claude" == false && "$has_codex" == false && "$has_gemini" == false ]]; then
    log_warn "No AI environment detected. Installing to ~/.claude/skills/ by default."
    log_warn "Manually copy skills to your AI tool's skills directory if needed."
    has_claude=true
fi

# ─── Install Function ────────────────────────────────────────────────────────
install_skill() {
    local skill="$1"
    local target_dir="$2"

    mkdir -p "$target_dir/$skill"

    if [[ "$SOURCE_MODE" == "local" ]]; then
        if [[ -f "$SCRIPT_DIR/skills/$skill/SKILL.md" ]]; then
            cp "$SCRIPT_DIR/skills/$skill/SKILL.md" "$target_dir/$skill/SKILL.md"
        else
            log_warn "Local skill not found: $skill (skipping)"
            return
        fi
    else
        curl -fsSL "$REPO_URL/skills/$skill/SKILL.md" -o "$target_dir/$skill/SKILL.md" 2>/dev/null || {
            log_warn "Could not download skill: $skill (skipping)"
            return
        }
    fi

    log_success "Installed: $skill -> $target_dir/$skill/SKILL.md"
}

# ─── Install to Claude Code ──────────────────────────────────────────────────
if [[ "$has_claude" == true ]]; then
    log_header "Installing skills for Claude Code..."
    mkdir -p "$CLAUDE_SKILLS_DIR"
    for skill in "${SKILLS[@]}"; do
        install_skill "$skill" "$CLAUDE_SKILLS_DIR"
    done
fi

# ─── Install to Codex ───────────────────────────────────────────────────────
if [[ "$has_codex" == true ]]; then
    log_header "Installing skills for Codex..."
    mkdir -p "$CODEX_SKILLS_DIR"

    # If Claude skills dir exists, symlink to it rather than duplicating
    if [[ "$has_claude" == true && -d "$CLAUDE_SKILLS_DIR" ]]; then
        for skill in "${SKILLS[@]}"; do
            if [[ -d "$CLAUDE_SKILLS_DIR/$skill" ]]; then
                if [[ ! -L "$CODEX_SKILLS_DIR/$skill" ]]; then
                    ln -sf "$CLAUDE_SKILLS_DIR/$skill" "$CODEX_SKILLS_DIR/$skill"
                    log_success "Linked: $skill -> $CODEX_SKILLS_DIR/$skill (symlink to Claude)"
                else
                    log_success "Already linked: $skill"
                fi
            else
                install_skill "$skill" "$CODEX_SKILLS_DIR"
            fi
        done
    else
        for skill in "${SKILLS[@]}"; do
            install_skill "$skill" "$CODEX_SKILLS_DIR"
        done
    fi
fi

# ─── Install to Gemini CLI ───────────────────────────────────────────────────
if [[ "$has_gemini" == true ]]; then
    log_header "Installing skills for Gemini CLI..."
    if [[ -d "$GEMINI_SKILLS_DIR" ]]; then
        for skill in "${SKILLS[@]}"; do
            install_skill "$skill" "$GEMINI_SKILLS_DIR"
        done
    else
        log_warn "Gemini skills directory not found at $GEMINI_SKILLS_DIR"
        log_warn "Create the directory and re-run, or manually copy files from skills/"
    fi
fi

# ─── Optional: Configure MCP and Plugins ────────────────────────────────────
log_header "Checking optional configuration..."

# claude-mem MCP (memory persistence for Claude)
CLAUDE_MCP_CONFIG="$HOME/.claude/mcp.json"
if [[ -f "$CLAUDE_MCP_CONFIG" ]]; then
    if ! grep -q "claude-mem" "$CLAUDE_MCP_CONFIG" 2>/dev/null; then
        log_info "claude-mem MCP not found in mcp.json. To add memory persistence:"
        log_info "  See: https://github.com/markster-public/markster-os/blob/main/integrations/README.md"
    else
        log_success "claude-mem MCP already configured"
    fi
fi

# Check for addon keys
log_header "Checking add-on keys..."
addon_count=0

if [[ -n "${AOE_GRADER_KEY:-}" ]]; then
    log_success "AOE Grader key found"
    addon_count=$((addon_count + 1))
else
    log_info "AOE_GRADER_KEY not set. Get a key at markster.ai/addons/aoe-grader"
fi

if [[ -n "${EVENT_SCOUT_KEY:-}" ]]; then
    log_success "Event Scout key found"
    addon_count=$((addon_count + 1))
else
    log_info "EVENT_SCOUT_KEY not set. Get a key at markster.ai/addons/event-scout"
fi

if [[ -n "${LEAD_PACKS_KEY:-}" ]]; then
    log_success "Lead Packs key found"
    addon_count=$((addon_count + 1))
else
    log_info "LEAD_PACKS_KEY not set. Get a key at markster.ai/addons/lead-packs"
fi

# ─── Done ───────────────────────────────────────────────────────────────────
log_header "Installation complete."
echo ""
echo -e "${BOLD}Installed skills:${NC} ${SKILLS[*]}"
echo -e "${BOLD}Active add-ons:${NC} $addon_count / 3"
echo ""
echo -e "${BOLD}Next steps:${NC}"
echo "  1. Open methodology/assessment/scorecard.md and score yourself"
echo "  2. Complete F1-F4 in methodology/foundation/ (in order)"
echo "  3. Activate a playbook in your AI environment: /cold-email, /sales, /content, etc."
echo ""
echo -e "${BOLD}Need help?${NC} https://markster.ai | hello@markster.ai"
echo ""
