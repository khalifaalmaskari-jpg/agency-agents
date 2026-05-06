#!/usr/bin/env python3
"""Validate generated Codex custom agents."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path


REQUIRED_FIELDS = {"name", "description", "developer_instructions"}
SECRET_PATTERNS = [
    re.compile(r"(?i)(github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,})"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._-]{20,}"),
]


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
        data = tomllib.loads(text)
    except Exception as exc:  # noqa: BLE001 - validator should report all parse failures.
        return [f"{path}: TOML parse failed: {exc}"]

    missing = REQUIRED_FIELDS - set(data)
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(sorted(missing))}")
    if not str(data.get("name", "")).startswith("agency_"):
        errors.append(f"{path}: name must start with agency_")
    if path.stem != data.get("name"):
        errors.append(f"{path}: filename stem should match name")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            errors.append(f"{path}: contains a possible secret marker")
            break
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agents-dir", type=Path, default=Path("~/.codex/agents"))
    parser.add_argument("--manifest", type=Path, default=Path("~/.codex/agency-agents/manifest.json"))
    args = parser.parse_args()

    agents_dir = args.agents_dir.expanduser().resolve()
    manifest = args.manifest.expanduser().resolve()
    files = sorted(agents_dir.glob("agency_*.toml"))
    errors: list[str] = []

    if not files:
        errors.append(f"{agents_dir}: no agency_*.toml files found")
    for path in files:
        errors.extend(validate_file(path))

    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            manifest_count = len(data.get("agents", []))
            if manifest_count != len(files):
                errors.append(
                    f"{manifest}: manifest count {manifest_count} does not match TOML count {len(files)}"
                )
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{manifest}: JSON parse failed: {exc}")
    else:
        errors.append(f"{manifest}: missing manifest")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Validated {len(files)} Codex agency agents in {agents_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
