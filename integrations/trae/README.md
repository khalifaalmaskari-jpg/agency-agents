# Trae Integration

Trae uses user-scoped `.md` agent files in `~/.trae/agents/`.

The generated files come from `scripts/convert.sh --tool trae`, which writes one
agent Markdown file per agency agent into `integrations/trae/agents/`.

## Generate

From the repository root:

```bash
./scripts/convert.sh --tool trae
```

## Install

Run the installer:

```bash
./scripts/install.sh --tool trae
```

This copies the generated agent files into:

```text
~/.trae/agents/
```

## Refresh in Trae

After installation, restart your Trae session to refresh the agent list.

## Notes

- Trae agents are user-scoped, stored in your home directory
- The generated Trae files use YAML frontmatter with `name`, `description`, and
  `color`
- If you update agents in this repo, regenerate the Trae output before
  reinstalling
