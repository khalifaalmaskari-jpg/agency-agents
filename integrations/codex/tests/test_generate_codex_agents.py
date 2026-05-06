#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_codex_agents.py"
VALIDATE = Path(__file__).resolve().parents[1] / "scripts" / "validate_codex_agents.py"


class GenerateCodexAgentsTest(unittest.TestCase):
    def test_generates_valid_toml_from_markdown_agent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            agent_dir = root / "engineering"
            nested_agent_dir = root / "game-development" / "unity"
            out = Path(tmp) / "agents"
            meta = Path(tmp) / "meta"
            agent_dir.mkdir(parents=True)
            nested_agent_dir.mkdir(parents=True)
            (agent_dir / "engineering-test-agent.md").write_text(
                "---\n"
                "name: Test Agent\n"
                "description: Helps test Codex generation.\n"
                "---\n\n"
                "# Test Agent\n\n"
                "Follow the test instructions.\n",
                encoding="utf-8",
            )
            (nested_agent_dir / "unity-test-agent.md").write_text(
                "---\n"
                "name: Unity Test Agent\n"
                "description: Verifies nested Codex agent discovery.\n"
                "---\n\n"
                "# Unity Test Agent\n\n"
                "Follow the nested test instructions.\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    "--repo-root",
                    str(root),
                    "--output-agents-dir",
                    str(out),
                    "--metadata-dir",
                    str(meta),
                ],
                check=False,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((out / "agency_test_agent.toml").exists())
            self.assertTrue((out / "agency_unity_test_agent.toml").exists())

            validation = subprocess.run(
                [
                    "python3",
                    str(VALIDATE),
                    "--agents-dir",
                    str(out),
                    "--manifest",
                    str(meta / "manifest.json"),
                ],
                check=False,
                text=True,
                capture_output=True,
            )
            self.assertEqual(validation.returncode, 0, validation.stderr)


if __name__ == "__main__":
    unittest.main()
