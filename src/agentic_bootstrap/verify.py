from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from .errors import AgenticBootstrapError
from .io import load_json, safe_target_path, sha256_bytes
from .manifest import validate_manifest
from .packs import discover_packs, resolve_packs
from .planner import MANIFEST_PATH, STATE_PATH

TOKEN_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def verify_target(target: Path, *, run_quality: bool = False) -> dict[str, Any]:
    target = target.resolve()
    manifest = validate_manifest(load_json(target / MANIFEST_PATH))
    state = load_json(target / STATE_PATH)
    managed = state.get("managedFiles")
    if state.get("schemaVersion") != 1 or not isinstance(managed, dict):
        raise AgenticBootstrapError("invalid .agentic/state.json")
    resolve_packs(manifest.packs, discover_packs())

    failures: list[str] = []
    warnings: list[str] = []
    for relative, metadata in sorted(managed.items()):
        path = safe_target_path(target, relative)
        if not path.is_file():
            failures.append(f"missing managed file: {relative}")
            continue
        current = sha256_bytes(path.read_bytes())
        if not isinstance(metadata, dict) or current != metadata.get("sha256"):
            warnings.append(f"managed file changed locally: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        tokens = sorted(set(TOKEN_RE.findall(text)))
        if tokens:
            failures.append(f"unresolved tokens in {relative}: {', '.join(tokens)}")

    context_check = target / "tools/context_check.py"
    if context_check.is_file():
        process = subprocess.run(
            [sys.executable, str(context_check)], cwd=target, text=True, capture_output=True
        )
        if process.returncode:
            failures.append("generated context check failed")

    quality_results: list[dict[str, Any]] = []
    if run_quality:
        for command in manifest.quality_commands:
            process = subprocess.run(list(command), cwd=target, text=True)
            quality_results.append({"command": list(command), "returnCode": process.returncode})
            if process.returncode:
                failures.append(f"quality command failed: {list(command)!r}")
                break

    return {
        "status": "passed" if not failures else "failed",
        "failures": failures,
        "warnings": warnings,
        "quality": quality_results,
    }
