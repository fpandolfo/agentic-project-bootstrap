from __future__ import annotations

import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

from agentic_bootstrap.apply import apply_plan
from agentic_bootstrap.cli import main
from agentic_bootstrap.errors import AgenticBootstrapError
from agentic_bootstrap.manifest import new_manifest, validate_manifest
from agentic_bootstrap.planner import build_plan, summarize_plan
from agentic_bootstrap.verify import verify_target


class BootstrapEndToEndTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.target = self.root / "product"
        self.manifest = new_manifest(
            name="Example Product",
            slug="example-product",
            description="Synthetic test product.",
            stack="Python",
            packs=["core", "generic-agent", "github"],
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_plan_apply_and_verify_without_player_lock_in(self) -> None:
        plan = build_plan(self.target, self.manifest)
        counts = summarize_plan(plan)
        self.assertGreater(counts["create"], 20)
        self.assertEqual(counts["conflict"], 0)

        applied = apply_plan(plan, plan["planId"][:12])
        self.assertEqual(applied["create"], counts["create"])
        self.assertTrue((self.target / "AGENTS.md").is_file())
        self.assertTrue((self.target / "START_HERE.md").is_file())
        self.assertTrue((self.target / "CAPABILITIES.md").is_file())
        self.assertTrue((self.target / "PROMPTS.md").is_file())
        self.assertTrue((self.target / "playbooks/ADOPT_PROJECT.md").is_file())
        self.assertTrue((self.target / "tools/discover_project.py").is_file())
        self.assertTrue((self.target / "docs/templates/ARCHITECTURE_DIAGRAMS.md").is_file())
        self.assertTrue((self.target / ".agents/skills/context-governance/SKILL.md").is_file())
        self.assertTrue((self.target / ".github/workflows/agentic-bootstrap.yml").is_file())
        self.assertFalse((self.target / ".kiro").exists())
        self.assertFalse((self.target / ".codex").exists())

        result = verify_target(self.target)
        self.assertEqual(result["status"], "passed", result)
        self.assertEqual(result["failures"], [])

    def test_existing_unmanaged_file_is_a_conflict(self) -> None:
        self.target.mkdir()
        (self.target / "AGENTS.md").write_text("user owned\n", encoding="utf-8")
        plan = build_plan(self.target, self.manifest)
        conflicts = [entry for entry in plan["files"] if entry["action"] == "conflict"]
        self.assertEqual([entry["path"] for entry in conflicts], ["AGENTS.md"])
        with self.assertRaisesRegex(AgenticBootstrapError, "conflict"):
            apply_plan(plan, plan["planId"][:12])
        self.assertEqual((self.target / "AGENTS.md").read_text(), "user owned\n")

    def test_locally_modified_managed_file_is_preserved(self) -> None:
        first = build_plan(self.target, self.manifest)
        apply_plan(first, first["planId"][:12])
        readme = self.target / "README.md"
        readme.write_text(readme.read_text() + "\nLocal decision.\n", encoding="utf-8")

        second = build_plan(self.target, self.manifest)
        entry = next(item for item in second["files"] if item["path"] == "README.md")
        self.assertEqual(entry["action"], "preserve")
        apply_plan(second, second["planId"][:12])
        self.assertIn("Local decision.", readme.read_text(encoding="utf-8"))

    def test_existing_file_can_be_explicitly_preserved_during_adoption(self) -> None:
        self.target.mkdir()
        readme = self.target / "README.md"
        readme.write_text("Existing product README.\n", encoding="utf-8")
        plan = build_plan(self.target, self.manifest, preserve_existing=True)
        entry = next(item for item in plan["files"] if item["path"] == "README.md")
        self.assertEqual(entry["action"], "preserve")
        self.assertFalse(entry["managed"])
        apply_plan(plan, plan["planId"][:12])
        self.assertEqual(readme.read_text(encoding="utf-8"), "Existing product README.\n")

    def test_target_change_after_plan_is_detected(self) -> None:
        plan = build_plan(self.target, self.manifest)
        self.target.mkdir()
        (self.target / "AGENTS.md").write_text("appeared later\n", encoding="utf-8")
        with self.assertRaisesRegex(AgenticBootstrapError, "changed after planning"):
            apply_plan(plan, plan["planId"][:12])

    def test_plan_tampering_is_detected(self) -> None:
        plan = build_plan(self.target, self.manifest)
        plan["files"][0]["content"] += "tampered"
        with self.assertRaisesRegex(AgenticBootstrapError, "fingerprint"):
            apply_plan(plan, plan["planId"][:12])

    @unittest.skipIf(os.name == "nt", "symlink behavior differs on Windows")
    def test_symlinked_target_path_is_refused(self) -> None:
        self.target.mkdir()
        outside = self.root / "outside"
        outside.mkdir()
        (self.target / "docs").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(AgenticBootstrapError, "symlink"):
            build_plan(self.target, self.manifest)


class ManifestAndCliTest(unittest.TestCase):
    def test_shell_string_quality_command_is_rejected(self) -> None:
        with self.assertRaisesRegex(AgenticBootstrapError, "argv array"):
            validate_manifest(
                {
                    "schemaVersion": 1,
                    "project": {
                        "name": "Example",
                        "slug": "example",
                        "description": "Example.",
                        "stack": "Python",
                    },
                    "packs": ["core"],
                    "quality": {"commands": ["rm -rf /"]},
                }
            )

    def test_init_cli_writes_manifest_only(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "manifest.json"
            with contextlib.redirect_stdout(io.StringIO()):
                rc = main(
                    [
                        "init",
                        "--name",
                        "My Product",
                        "--description",
                        "Example.",
                        "--stack",
                        "Python",
                        "--output",
                        str(output),
                    ]
                )
            self.assertEqual(rc, 0)
            manifest = json.loads(output.read_text())
            self.assertEqual(manifest["project"]["slug"], "my-product")
            self.assertEqual(manifest["packs"], ["core", "generic-agent"])

    def test_adopt_detects_flutter(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "mobile-app"
            target.mkdir()
            (target / "pubspec.yaml").write_text("name: mobile_app\n")
            output = Path(temporary) / "adopt.json"
            with contextlib.redirect_stdout(io.StringIO()):
                rc = main(
                    [
                        "adopt",
                        str(target),
                        "--description",
                        "Mobile app.",
                        "--output",
                        str(output),
                    ]
                )
            self.assertEqual(rc, 0)
            manifest = json.loads(output.read_text())
            self.assertEqual(manifest["project"]["stack"], "Flutter/Dart")


if __name__ == "__main__":
    unittest.main()
