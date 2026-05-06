#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
CLAUDE_AGENTS_DIR="${CLAUDE_AGENTS_DIR:-}"
CODEX_SKILLS_DIR="${CODEX_SKILLS_DIR:-}"

GENERATE_ARGS=(
  --repo-root "$REPO_ROOT"
  --output-agents-dir "$CODEX_HOME/agents"
  --metadata-dir "$CODEX_HOME/agency-agents"
)

if [[ -n "$CLAUDE_AGENTS_DIR" ]]; then
  GENERATE_ARGS+=(--claude-agents-dir "$CLAUDE_AGENTS_DIR")
fi

if [[ -n "$CODEX_SKILLS_DIR" ]]; then
  GENERATE_ARGS+=(--codex-skills-dir "$CODEX_SKILLS_DIR")
fi

python3 "$SCRIPT_DIR/generate_codex_agents.py" "${GENERATE_ARGS[@]}"

python3 "$SCRIPT_DIR/validate_codex_agents.py" \
  --agents-dir "$CODEX_HOME/agents" \
  --manifest "$CODEX_HOME/agency-agents/manifest.json"
