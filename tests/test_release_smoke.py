from __future__ import annotations

import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.release_smoke import (
    find_distributions,
    validate_text_pack_assets,
    write_checksums,
)


class ReleaseSmokeTest(unittest.TestCase):
    def test_finds_one_wheel_and_source_distribution(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            wheel = root / "example-1.0-py3-none-any.whl"
            source = root / "example-1.0.tar.gz"
            wheel.touch()
            source.touch()

            self.assertEqual(find_distributions(root), (wheel.resolve(), source.resolve()))

    def test_rejects_ambiguous_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "first-1.0-py3-none-any.whl").touch()
            (root / "second-1.0-py3-none-any.whl").touch()
            (root / "example-1.0.tar.gz").touch()

            with self.assertRaisesRegex(ValueError, "exactly one wheel"):
                find_distributions(root)

    def test_rejects_binary_pack_asset(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            wheel = Path(temporary) / "example.whl"
            with zipfile.ZipFile(wheel, "w") as archive:
                archive.writestr("agentic_bootstrap/packs/core/files/guide.md", "ok")
                archive.writestr(
                    "agentic_bootstrap/packs/core/files/tools/__pycache__/tool.pyc",
                    b"bytecode",
                )

            with self.assertRaisesRegex(ValueError, "non-text pack assets"):
                validate_text_pack_assets(wheel)

    def test_accepts_text_pack_assets(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            wheel = Path(temporary) / "example.whl"
            with zipfile.ZipFile(wheel, "w") as archive:
                archive.writestr("agentic_bootstrap/packs/core/pack.json", "{}")
                archive.writestr("agentic_bootstrap/packs/core/files/guide.md", "ok")
                archive.writestr("agentic_bootstrap/packs/core/files/tool.py", "pass")
                archive.writestr("agentic_bootstrap/packs/core/files/.gitignore", "dist/")

            validate_text_pack_assets(wheel)

    def test_writes_stable_sha256_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            wheel = root / "example.whl"
            source = root / "example.tar.gz"
            wheel.write_bytes(b"wheel")
            source.write_bytes(b"source")
            destination = root / "SHA256SUMS"

            write_checksums((source, wheel), destination)

            lines = destination.read_text(encoding="utf-8").splitlines()
            self.assertEqual(
                [line.split("  ")[1] for line in lines],
                sorted([wheel.name, source.name]),
            )


if __name__ == "__main__":
    unittest.main()
