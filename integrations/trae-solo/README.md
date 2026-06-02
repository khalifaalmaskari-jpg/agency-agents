# Trae Solo Integration

Trae Solo uses user-scoped `.md` agent files in `~/.trae-solo/agents/`.

The generated files come from `scripts/convert.sh --tool trae-solo`, which writes one
agent Markdown file per agency agent into `integrations/trae-solo/agents/`.

## Generate

From the repository root:

```bash
./scripts/convert.sh --tool trae-solo
```

## Install

Run the installer:

```bash
./scripts/install.sh --tool trae-solo
```

This copies the generated agent files into:

```text
~/.trae-solo/agents/
```

## Refresh in Trae Solo

After installation, restart your Trae Solo session to refresh the agent list.

## Notes

- Trae Solo agents are user-scoped, stored in your home directory
- The generated Trae Solo files use YAML frontmatter with `name`, `description`, and
  `color`
- If you update agents in this repo, regenerate the Trae Solo output before
  reinstalling
