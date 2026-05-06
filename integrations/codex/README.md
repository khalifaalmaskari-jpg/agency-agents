# Codex Integration

Generate native Codex custom agents from the Agency Agents catalog.

Codex loads personal custom agents from `~/.codex/agents/*.toml`. Each generated
agent uses the `agency_` prefix, includes the original Agency instructions, and
adds Codex-specific routing, safety, sandbox, MCP, and skill guidance.

## Install Locally

```bash
./scripts/install.sh --tool codex
```

You can also run the integration script directly:

```bash
./integrations/codex/scripts/install_codex_agents.sh
```

To generate repo-local integration files without installing them:

```bash
./scripts/convert.sh --tool codex
```

Optional environment variables:

- `CODEX_HOME`: Codex home directory, defaults to `~/.codex`
- `CLAUDE_AGENTS_DIR`: optional extra Claude agents directory, unset by default
- `CODEX_SKILLS_DIR`: optional Codex Agency skills directory, defaults to `~/.codex/plugins/agency-agents/skills`

## Generated Files

- `~/.codex/agents/agency_*.toml`
- `~/.codex/agency-agents/manifest.json`
- `~/.codex/agency-agents/source-map.json`
- `~/.codex/agency-agents/router.md`

## Validate

```bash
./integrations/codex/scripts/validate_codex_agents.py \
  --agents-dir ~/.codex/agents \
  --manifest ~/.codex/agency-agents/manifest.json
```

The validator checks TOML syntax, required Codex fields, `agency_` naming, manifest
count, and obvious secret markers.

## Notes

- Existing MCP server secrets are not copied into generated agent files.
- Recommended MCPs and skills are recorded in the generated instructions and manifest.
- The generated agents can coexist with the Agency Agents Codex plugin until native
  agent tests pass.
