#!/usr/bin/env python3
"""Generate native Codex custom agents from Agency Agents markdown files."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".claude",
    "_docs",
    "examples",
    "integrations",
    "playbooks",
    "runbooks",
    "scripts",
}

EXCLUDED_FILES = {
    "README.md",
    "QUICKSTART.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING_zh-CN.md",
    "PULL_REQUEST_TEMPLATE.md",
    "EXECUTIVE-BRIEF.md",
    "agent-activation-prompts.md",
    "handoff-templates.md",
}

SECRET_PATTERNS = [
    re.compile(r"(?i)(github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,})"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._-]{20,}"),
]

WRITE_HINTS = {
    "developer",
    "engineer",
    "builder",
    "automator",
    "prototyper",
    "scripter",
    "architect",
    "cms",
    "mobile",
    "devops",
    "sre",
}

READ_ONLY_HINTS = {
    "reviewer",
    "auditor",
    "checker",
    "strategist",
    "analyst",
    "researcher",
    "advisor",
    "coach",
    "guardian",
    "compliance",
    "security",
    "legal",
    "qa",
    "tester",
    "evidence",
}

HIGH_REASONING_HINTS = {
    "architect",
    "security",
    "reviewer",
    "auditor",
    "mcp",
    "backend",
    "database",
    "data",
    "legal",
    "compliance",
    "sre",
    "incident",
}


@dataclass(frozen=True)
class AgentSource:
    source_kind: str
    source_path: Path
    source_slug: str
    category: str
    display_name: str
    description: str
    body: str
    checksum: str


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[3]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "agent"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :].lstrip()
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        meta[key.strip()] = value
    return meta, body


def read_agent(path: Path, source_kind: str, repo_root: Path) -> AgentSource | None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")

    meta, body = parse_frontmatter(text)
    display_name = meta.get("name") or path.stem.replace("-", " ").title()
    description = meta.get("description") or first_sentence(body) or display_name
    source_slug = slugify(path.stem)
    try:
        category = path.relative_to(repo_root).parts[0]
    except ValueError:
        category = "claude-active"
    if source_kind == "claude_active":
        category = "claude-active"

    checksum = hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()
    return AgentSource(
        source_kind=source_kind,
        source_path=path,
        source_slug=source_slug,
        category=category,
        display_name=display_name,
        description=clean_line(description),
        body=body.strip(),
        checksum=checksum,
    )


def first_sentence(text: str) -> str:
    for line in text.splitlines():
        line = line.strip(" #")
        if len(line) > 20:
            return clean_line(line)
    return ""


def clean_line(value: str, limit: int = 480) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def official_markdown_files(repo_root: Path) -> Iterable[Path]:
    for path in sorted(repo_root.rglob("*.md")):
        rel_parts = path.relative_to(repo_root).parts
        if len(rel_parts) < 2:
            continue
        if any(part in EXCLUDED_DIRS for part in rel_parts[:-1]):
            continue
        if path.name in EXCLUDED_FILES:
            continue
        yield path


def claude_markdown_files(claude_agents_dir: Path | None) -> Iterable[Path]:
    if not claude_agents_dir or not claude_agents_dir.exists():
        return []
    return sorted(claude_agents_dir.glob("*.md"))


def collect_agents(repo_root: Path, claude_agents_dir: Path | None) -> list[AgentSource]:
    by_name: dict[str, AgentSource] = {}

    for path in official_markdown_files(repo_root):
        agent = read_agent(path, "official", repo_root)
        if agent:
            by_name.setdefault(slugify(agent.display_name), agent)

    for path in claude_markdown_files(claude_agents_dir):
        agent = read_agent(path, "claude_active", repo_root)
        if not agent:
            continue
        name_slug = slugify(agent.display_name)
        by_name.setdefault(name_slug, agent)

    return sorted(by_name.values(), key=lambda item: (item.category, item.display_name.lower()))


def recommended_mcps(agent: AgentSource) -> list[str]:
    haystack = " ".join(
        [agent.source_slug, agent.category, agent.display_name, agent.description]
    ).lower()
    mapping = [
        ("linkedin", "linkedin-mcp"),
        ("github", "github"),
        ("git", "github"),
        ("google", "google-workspace"),
        ("gmail", "google-workspace"),
        ("sheet", "google-workspace"),
        ("document", "google-workspace"),
        ("n8n", "mcpsrv_n8n"),
        ("workflow", "mcpsrv_n8n"),
        ("automation", "mcpsrv_n8n"),
        ("crawl", "crawl4ai"),
        ("seo", "crawl4ai"),
        ("research", "crawl4ai"),
        ("web", "playwright"),
        ("browser", "playwright"),
        ("mcp", "context7"),
        ("docs", "context7"),
        ("technical writer", "context7"),
        ("pdf", "md-to-pdf"),
        ("report", "md-to-pdf"),
        ("twitter", "bird-mcp"),
        (" x ", "bird-mcp"),
        ("memory", "basic-memory"),
        ("knowledge", "basic-memory"),
    ]
    result: list[str] = []
    for needle, mcp in mapping:
        if needle in haystack and mcp not in result:
            result.append(mcp)
    if "basic-memory" not in result:
        result.append("basic-memory")
    return result


def recommended_skills(agent: AgentSource, codex_skills_dir: Path | None) -> list[str]:
    if not codex_skills_dir:
        return []
    display_slug = slugify(agent.display_name).replace("_", "-")
    candidates = [
        codex_skills_dir / f"agency-{display_slug}" / "SKILL.md",
        codex_skills_dir / f"agency-{agent.source_slug}" / "SKILL.md",
        codex_skills_dir / agent.source_slug / "SKILL.md",
        codex_skills_dir / display_slug / "SKILL.md",
    ]
    for candidate in candidates:
        if candidate.exists():
            return [candidate.parent.name]
    return []


def sandbox_mode(agent: AgentSource) -> str:
    haystack = f"{agent.source_slug} {agent.display_name} {agent.description}".lower()
    if any(hint in haystack for hint in READ_ONLY_HINTS):
        return "read-only"
    if any(hint in haystack for hint in WRITE_HINTS):
        return "workspace-write"
    return "read-only"


def reasoning_effort(agent: AgentSource) -> str:
    haystack = f"{agent.source_slug} {agent.display_name} {agent.description}".lower()
    if any(hint in haystack for hint in HIGH_REASONING_HINTS):
        return "high"
    return "medium"


def toml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def agent_name(agent: AgentSource, used: set[str]) -> str:
    base = "agency_" + slugify(agent.display_name)
    name = base
    if name in used:
        name = "agency_" + agent.source_slug
    suffix = 2
    while name in used:
        name = f"{base}_{suffix}"
        suffix += 1
    used.add(name)
    return name


def build_instructions(agent: AgentSource, name: str, mcps: list[str], skills: list[str], soul_path: Path) -> str:
    mcp_line = ", ".join(mcps) if mcps else "none"
    skill_line = ", ".join(skills) if skills else "none"
    return f"""You are {name}, a native Codex custom agent generated from the Agency Agents catalog.

Routing:
- Use this agent for: {agent.description}
- Do not use this agent for unrelated generic work when a narrower Agency agent matches better.
- Reply in the user's language; for Ben, French is the default unless the task requires another language.

Tooling:
- Recommended MCPs: {mcp_line}
- Recommended skills: {skill_line}
- Never reveal or copy secrets, tokens, API keys, cookies, OAuth credentials, or .env values.
- If you encounter a possible secret, mention only the file path and recommend rotation.
- Prefer focused changes, existing repository patterns, and explicit verification.

Source:
- Source kind: {agent.source_kind}
- Source file: {agent.source_path}
- Source checksum: {agent.checksum}
- Codex SOUL file: {soul_path}

Original Agency Agent instructions:

{agent.body}
"""


def write_agent_file(path: Path, name: str, agent: AgentSource, mcps: list[str], skills: list[str], soul_path: Path) -> None:
    instructions = build_instructions(agent, name, mcps, skills, soul_path)
    description = f"{agent.display_name}: {agent.description}"
    content = "\n".join(
        [
            f"name = {toml_string(name)}",
            f"description = {toml_string(description)}",
            f"model_reasoning_effort = {toml_string(reasoning_effort(agent))}",
            f"sandbox_mode = {toml_string(sandbox_mode(agent))}",
            f"developer_instructions = {toml_string(instructions)}",
            "",
        ]
    )
    path.write_text(content, encoding="utf-8")


def write_soul_file(path: Path, name: str, agent: AgentSource, mcps: list[str], skills: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = {
        "agent": name,
        "role": agent.display_name,
        "category": agent.category,
        "source_kind": agent.source_kind,
        "source_path": str(agent.source_path),
        "source_checksum": agent.checksum,
        "recommended_mcp_servers": mcps,
        "recommended_skills": skills,
    }
    content = [
        "---",
        *[f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in frontmatter.items()],
        "---",
        "",
        f"# {agent.display_name} SOUL",
        "",
        "This file mirrors the original Agency Agent instructions used to generate the native Codex TOML agent.",
        "Codex loads the TOML `developer_instructions`; this SOUL file is kept for auditability, routing, and human review.",
        "",
        "## Original Agency Agent Instructions",
        "",
        agent.body,
        "",
    ]
    path.write_text("\n".join(content), encoding="utf-8")


def has_secret_marker(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def render_router(records: list[dict[str, object]]) -> str:
    lines = [
        "# Agency Agents Router for Codex",
        "",
        "Use this router before spawning an Agency agent. Prefer the narrowest matching agent from the full index.",
        "Do not rely on a fixed shortlist: inspect the request, compare it with the manifest descriptions, and route to the most specific available specialist.",
        "",
        "## Full Index",
        "",
    ]
    for record in sorted(records, key=lambda item: (str(item["category"]), str(item["agent"]))):
        mcps = ", ".join(record["recommended_mcp_servers"]) or "none"
        skills = ", ".join(record["recommended_skills"]) or "none"
        lines.append(
            f"- `{record['agent']}` ({record['category']}): {record['role']} | MCPs: {mcps} | skills: {skills} | sandbox: {record['sandbox_mode']}"
        )
    return "\n".join(lines) + "\n"


def generate(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    output_agents_dir = args.output_agents_dir.expanduser().resolve()
    metadata_dir = args.metadata_dir.expanduser().resolve()
    codex_skills_dir = args.codex_skills_dir.expanduser().resolve() if args.codex_skills_dir else None
    claude_agents_dir = args.claude_agents_dir.expanduser().resolve() if args.claude_agents_dir else None

    agents = collect_agents(repo_root, claude_agents_dir)
    output_agents_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)

    for stale in output_agents_dir.glob("agency_*.toml"):
        stale.unlink()
    souls_dir = metadata_dir / "souls"
    if souls_dir.exists():
        for stale in souls_dir.glob("agency_*/SOUL.md"):
            stale.unlink()

    used_names: set[str] = set()
    records: list[dict[str, object]] = []
    source_map: dict[str, dict[str, str]] = {}

    for agent in agents:
        name = agent_name(agent, used_names)
        file_name = f"{name}.toml"
        mcps = recommended_mcps(agent)
        skills = recommended_skills(agent, codex_skills_dir)
        destination = output_agents_dir / file_name
        soul_path = metadata_dir / "souls" / name / "SOUL.md"
        write_agent_file(destination, name, agent, mcps, skills, soul_path)
        write_soul_file(soul_path, name, agent, mcps, skills)
        if has_secret_marker(destination):
            destination.unlink(missing_ok=True)
            soul_path.unlink(missing_ok=True)
            print(f"Refused generated agent because secret marker appeared: {destination}", file=sys.stderr)
            return 2
        record = {
            "agent": name,
            "file": str(destination),
            "soul_file": str(soul_path),
            "category": agent.category,
            "role": agent.display_name,
            "description": agent.description,
            "when_to_use": agent.description,
            "when_not_to_use": "Use a narrower Agency agent when the request better matches another specialist.",
            "recommended_mcp_servers": mcps,
            "recommended_skills": skills,
            "autonomy": "execution" if sandbox_mode(agent) == "workspace-write" else "advisory",
            "sandbox_mode": sandbox_mode(agent),
            "source_kind": agent.source_kind,
            "source_path": str(agent.source_path),
            "source_checksum": agent.checksum,
        }
        records.append(record)
        source_map[name] = {
            "source_kind": agent.source_kind,
            "source_path": str(agent.source_path),
            "soul_file": str(soul_path),
            "source_checksum": agent.checksum,
            "source_slug": agent.source_slug,
        }

    (metadata_dir / "manifest.json").write_text(
        json.dumps({"agents": records}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (metadata_dir / "source-map.json").write_text(
        json.dumps(source_map, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (metadata_dir / "router.md").write_text(render_router(records), encoding="utf-8")

    print(f"Generated {len(records)} Codex agents in {output_agents_dir}")
    print(f"Metadata written to {metadata_dir}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=repo_root_from_script())
    parser.add_argument("--output-agents-dir", type=Path, default=Path("~/.codex/agents"))
    parser.add_argument("--metadata-dir", type=Path, default=Path("~/.codex/agency-agents"))
    parser.add_argument("--claude-agents-dir", type=Path, default=None)
    parser.add_argument("--codex-skills-dir", type=Path, default=None)
    args = parser.parse_args()
    return generate(args)


if __name__ == "__main__":
    raise SystemExit(main())
