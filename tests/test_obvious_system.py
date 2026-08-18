from __future__ import annotations

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "obvious_system_check.py"
SPEC = importlib.util.spec_from_file_location("obvious_system_check", SCRIPT)
assert SPEC and SPEC.loader
OBVIOUS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(OBVIOUS)


class ObviousSystemCheckTest(unittest.TestCase):
    def write_long_doc(self, root: Path, *, complete: bool) -> None:
        path = root / "docs" / "guides" / "design.md"
        path.parent.mkdir(parents=True)
        sections = ["# Design", "", "## Executive Summary", ""]
        if complete:
            sections.extend(
                [
                    "When to read:",
                    "",
                    "When not to read:",
                    "",
                    "Related owners:",
                    "",
                ]
            )
        sections.extend(f"- line {index}" for index in range(230))
        path.write_text("\n".join(sections) + "\n", encoding="utf-8")

    def test_advisory_mode_reports_without_failing(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.write_long_doc(root, complete=False)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rc = OBVIOUS.main(["--root", str(root)])
            self.assertEqual(rc, 0)
            self.assertIn("WARN: docs/guides/design.md", output.getvalue())
            self.assertIn("Status: PASSED", output.getvalue())

    def test_strict_mode_fails_incomplete_long_doc(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.write_long_doc(root, complete=False)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rc = OBVIOUS.main(["--root", str(root), "--strict"])
            self.assertEqual(rc, 1)
            self.assertIn("Status: FAILED", output.getvalue())

    def test_complete_long_doc_passes_strict_mode(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.write_long_doc(root, complete=True)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rc = OBVIOUS.main(["--root", str(root), "--strict"])
            self.assertEqual(rc, 0)
            self.assertIn("findings: 0", output.getvalue())

    def test_entry_and_adapter_changes_emit_hints(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
            adapter = root / ".agents" / "skills" / "example" / "SKILL.md"
            adapter.parent.mkdir(parents=True)
            adapter.write_text("# Skill\n", encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rc = OBVIOUS.main(
                    [
                        "--root",
                        str(root),
                        "--files",
                        "AGENTS.md",
                        ".agents/skills/example/SKILL.md",
                    ]
                )
            self.assertEqual(rc, 0)
            self.assertIn("Entry surface changed", output.getvalue())
            self.assertIn("Player adapter changed", output.getvalue())


if __name__ == "__main__":
    unittest.main()
