#!/usr/bin/env python3
"""Validate built distributions through isolated consumer journeys."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path

TEXT_PACK_SUFFIXES = {".json", ".md", ".py", ".toml", ".yaml", ".yml"}
TEXT_PACK_NAMES = {".gitignore"}


def find_distributions(dist_dir: Path) -> tuple[Path, Path]:
    wheels = sorted(dist_dir.glob("*.whl"))
    source_archives = sorted(dist_dir.glob("*.tar.gz"))
    if len(wheels) != 1 or len(source_archives) != 1:
        raise ValueError(
            "expected exactly one wheel and one source distribution; "
            f"found wheels={len(wheels)} source_archives={len(source_archives)}"
        )
    return wheels[0].resolve(), source_archives[0].resolve()


def pack_members(artifact: Path) -> list[str]:
    if artifact.suffix == ".whl":
        with zipfile.ZipFile(artifact) as archive:
            return [name for name in archive.namelist() if not name.endswith("/")]
    with tarfile.open(artifact, "r:gz") as archive:
        return [member.name for member in archive.getmembers() if member.isfile()]


def validate_text_pack_assets(artifact: Path) -> None:
    invalid: list[str] = []
    for name in pack_members(artifact):
        normalized = name.replace("\\", "/")
        if "agentic_bootstrap/packs/" not in normalized:
            continue
        path = Path(normalized)
        if path.name in TEXT_PACK_NAMES or path.suffix.lower() in TEXT_PACK_SUFFIXES:
            continue
        invalid.append(normalized)
    if invalid:
        raise ValueError(
            f"non-text pack assets found in {artifact.name}: {', '.join(invalid)}"
        )


def write_checksums(artifacts: tuple[Path, ...], destination: Path) -> None:
    lines: list[str] = []
    for artifact in sorted(artifacts, key=lambda item: item.name):
        digest = hashlib.sha256()
        with artifact.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        lines.append(f"{digest.hexdigest()}  {artifact.name}")
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def executable(venv: Path, name: str) -> Path:
    if os.name == "nt":
        return venv / "Scripts" / f"{name}.exe"
    return venv / "bin" / name


def run(command: list[str], *, cwd: Path | None = None) -> None:
    print("$", " ".join(command), flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def smoke_artifact(artifact: Path) -> None:
    label = "wheel" if artifact.suffix == ".whl" else "source distribution"
    print(f"\nSmoke: {label} ({artifact.name})", flush=True)
    with tempfile.TemporaryDirectory(prefix="agentic-release-smoke-") as temporary:
        root = Path(temporary)
        venv = root / "venv"
        target = root / "consumer-project"
        manifest = root / "manifest.json"
        plan = root / "plan.json"

        run([sys.executable, "-m", "venv", str(venv)])
        python = executable(venv, "python")
        agentic = executable(venv, "agentic")
        run(
            [
                str(python),
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                "--no-deps",
                str(artifact),
            ]
        )
        run([str(agentic), "doctor"])
        run(
            [
                str(agentic),
                "init",
                "--name",
                "Release Smoke Product",
                "--description",
                "Synthetic distribution acceptance project.",
                "--stack",
                "Python",
                "--output",
                str(manifest),
            ]
        )
        run(
            [
                str(agentic),
                "plan",
                "--target",
                str(target),
                "--manifest",
                str(manifest),
                "--output",
                str(plan),
            ]
        )
        fingerprint = json.loads(plan.read_text(encoding="utf-8"))["planId"][:12]
        run([str(agentic), "apply", "--plan", str(plan), "--approve", fingerprint])
        run([str(agentic), "verify", "--target", str(target)])
        run([str(python), "tools/prepare_delivery.py"], cwd=target)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Smoke wheel and source distributions in isolated virtual environments."
    )
    parser.add_argument("--dist-dir", type=Path, default=Path("dist"))
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        wheel, source_archive = find_distributions(args.dist_dir)
        validate_text_pack_assets(wheel)
        validate_text_pack_assets(source_archive)
        write_checksums((wheel, source_archive), args.dist_dir / "SHA256SUMS")
        smoke_artifact(wheel)
        smoke_artifact(source_archive)
    except (OSError, subprocess.CalledProcessError, ValueError, KeyError) as exc:
        print(f"Release smoke failed: {exc}", file=sys.stderr)
        return 1
    print("\nRelease smoke passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
