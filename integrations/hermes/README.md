# Hermes Agent Integration

> Load all 184+ Agency agents as Hermes Agent skills.

## Quick Start

```bash
# Step 1: Generate Hermes SKILL.md files
./scripts/convert.sh --tool hermes

# Step 2: Install to Hermes skill directory
./scripts/install.sh --tool hermes

# Or with custom path:
HERMES_SKILL_DIR=~/.hermes/profiles/my-profile/skills ./scripts/install.sh --tool hermes
```

## What Gets Installed

Each agency agent becomes a `SKILL.md` file in `~/.hermes/skills/agency/<slug>/` with YAML frontmatter:

```yaml
---
name: frontend-developer
description: Expert frontend developer specializing in modern web technologies...
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [engineering, frontend, developer]
    related_skills: []
---
```

## Usage

Ensure your Hermes Agent config includes the skills path:

```yaml
# In your Hermes config.yaml
skills:
  - ~/.hermes/skills/agency/
```

Then reference any agent in your Hermes session:

```
Use the frontend-developer skill to review this component
```

## Generated Files

- `integrations/hermes/skills/<slug>/SKILL.md` — One SKILL.md per agent

## File Format

Hermes Agent SKILL.md is a YAML-frontmattered markdown file with:

| Field | Description |
|-------|-------------|
| `name` | Lowercase kebab-case slug (e.g., `frontend-developer`) |
| `description` | One-line agent description from source |
| `version` | Always `1.0.0` |
| `platforms` | `[linux, macos, windows]` |
| `metadata.hermes.tags` | Category + name-derived tags |
| `metadata.hermes.related_skills` | Empty (can be edited post-install) |
