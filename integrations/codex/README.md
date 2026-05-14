# Codex Integration

Codex custom agents are TOML files stored in `~/.codex/agents/`. Each Agency
agent is converted into one Codex agent with `name`, `description`, and
`developer_instructions`.

## Generate

From the repository root:

```bash
./scripts/convert.sh --tool codex
```

This writes generated agent files into:

```text
integrations/codex/agents/
```

## Install

```bash
./scripts/install.sh --tool codex
```

This copies the generated TOML files into:

```text
~/.codex/agents/
```

If you use a custom Codex home directory, set `CODEX_HOME`:

```bash
CODEX_HOME=/path/to/codex-home ./scripts/install.sh --tool codex
```

## Refresh in Codex

After installation, restart Codex or open a new session so the agent list is
reloaded.

## Regenerate

After modifying source agents:

```bash
./scripts/convert.sh --tool codex
./scripts/install.sh --tool codex
```
