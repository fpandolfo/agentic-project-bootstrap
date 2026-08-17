from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "src"
    / "agentic_bootstrap"
    / "packs"
    / "core"
    / "files"
    / "tools"
    / "discover_project.py"
)
SPEC = importlib.util.spec_from_file_location("agentic_discovery", SCRIPT)
assert SPEC and SPEC.loader
DISCOVERY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DISCOVERY)


class DiscoveryTest(unittest.TestCase):
    def test_existing_project_inventory_is_content_free_and_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "synthetic-product"
            (target / "src").mkdir(parents=True)
            (target / "tests").mkdir()
            (target / ".github" / "workflows").mkdir(parents=True)
            (target / "node_modules" / "dependency").mkdir(parents=True)
            (target / "package.json").write_text('{"private": true}\n', encoding="utf-8")
            (target / "src" / "app.ts").write_text("export {}\n", encoding="utf-8")
            (target / "tests" / "app.test.ts").write_text("secret-value\n", encoding="utf-8")
            (target / ".github" / "workflows" / "quality.yml").write_text("name: CI\n")
            (target / ".env").write_text("PASSWORD=do-not-read\n", encoding="utf-8")
            (target / "node_modules" / "dependency" / "package.json").write_text("{}\n")

            outside = Path(temporary) / "outside"
            outside.mkdir()
            if os.name != "nt":
                (target / "linked-outside").symlink_to(outside, target_is_directory=True)

            before = sorted(path.relative_to(target).as_posix() for path in target.rglob("*"))
            snapshot = DISCOVERY.discover(target)
            after = sorted(path.relative_to(target).as_posix() for path in target.rglob("*"))

            self.assertEqual(before, after)
            self.assertEqual(snapshot["suggestedMode"], "ADOPT_PROJECT")
            self.assertEqual(snapshot["inventory"]["candidateStacks"], ["Node.js"])
            self.assertEqual(snapshot["inventory"]["sourceRoots"], ["src"])
            self.assertEqual(snapshot["safety"]["sensitiveCandidates"], [".env"])
            self.assertFalse(snapshot["safety"]["contentRead"])
            self.assertFalse(snapshot["safety"]["commandsExecuted"])
            self.assertNotIn("node_modules/dependency/package.json", json.dumps(snapshot))
            self.assertNotIn("do-not-read", json.dumps(snapshot))
            self.assertNotIn("secret-value", json.dumps(snapshot))
            if os.name != "nt":
                self.assertEqual(snapshot["inventory"]["symlinksSkipped"], ["linked-outside"])

    def test_empty_directory_suggests_new_project(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            snapshot = DISCOVERY.discover(Path(temporary))
            self.assertEqual(snapshot["suggestedMode"], "NEW_PROJECT")
            self.assertEqual(snapshot["inventory"]["fileCount"], 0)

    def test_markdown_omits_absolute_target_and_file_contents(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "private-machine-path"
            target.mkdir()
            (target / "pyproject.toml").write_text("PRIVATE_CONTENT\n", encoding="utf-8")
            markdown = DISCOVERY.to_markdown(DISCOVERY.discover(target))
            self.assertIn("`private-machine-path`", markdown)
            self.assertIn("`Python`", markdown)
            self.assertNotIn(temporary, markdown)
            self.assertNotIn("PRIVATE_CONTENT", markdown)

    def test_explicit_output_is_the_only_write(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "target"
            target.mkdir()
            output = root / "evidence" / "discovery.json"
            with contextlib.redirect_stdout(io.StringIO()):
                rc = DISCOVERY.main(
                    ["--target", str(target), "--format", "json", "--output", str(output)]
                )
            self.assertEqual(rc, 0)
            self.assertTrue(output.is_file())
            self.assertEqual(list(target.iterdir()), [])
            self.assertEqual(json.loads(output.read_text())["schemaVersion"], 1)

    @unittest.skipIf(os.name == "nt", "symlink behavior differs on Windows")
    def test_symlink_target_is_refused(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            actual = root / "actual"
            actual.mkdir()
            linked = root / "linked"
            linked.symlink_to(actual, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "may not be a symlink"):
                DISCOVERY.discover(linked)


if __name__ == "__main__":
    unittest.main()
