#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agentic_bootstrap.packs import discover_packs  # noqa: E402

REQUIRED = [
    "START_HERE.md",
    "CAPABILITIES.md",
    "TOOLING.md",
    "PROMPTS.md",
    "AGENTS.md",
    "README.md",
    "README.pt-BR.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "pyproject.toml",
    "agentic-project.schema.json",
    "docs/PROJECT_INDEX.md",
    "docs/contexts/PRODUCT.md",
    "docs/contexts/ARCHITECTURE.md",
    "docs/contexts/STACK.md",
    "docs/contexts/QUALITY.md",
    "docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md",
    "docs/guides/AGENTIC_DELIVERY_LIFECYCLE.md",
    "docs/guides/CI_AND_DELIVERY_GATES.md",
    "docs/guides/CONTEXT_GENERATION_AND_DRIFT.md",
    "docs/guides/REAL_PROJECT_LEARNING.md",
    "docs/checklists/SOFTWARE_DESIGN.md",
    "docs/templates/CASE_STUDY.md",
    "docs/templates/QUALITY_STRATEGY.md",
    "case-studies/README.md",
    "case-studies/project-aurora/README.md",
    "case-studies/project-relay/README.md",
    "docs/ops/AGENT_FIRST_ONBOARDING.md",
    "playbooks/NEW_PROJECT.md",
    "playbooks/ADOPT_PROJECT.md",
    "playbooks/EVOLVE_PROJECT.md",
    "tools/obvious_system_check.py",
    "tools/release_smoke.py",
]
TOKEN_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required file: {relative}")

    try:
        packs = discover_packs()
    except Exception as exc:
        failures.append(f"pack discovery failed: {exc}")
        packs = {}
    for required_pack in ("core", "generic-agent", "github", "codex", "kiro"):
        if required_pack not in packs:
            failures.append(f"missing built-in pack: {required_pack}")

    # Placeholders are expected only inside pack templates and their renderer tests.
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if (
            "packs" in path.parts
            or path.name == "context_check.py"
            or path.name == "manifest.py"
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        tokens = sorted(set(TOKEN_RE.findall(text)))
        if tokens:
            failures.append(f"unresolved tokens in {path.relative_to(ROOT)}: {', '.join(tokens)}")

    schema_path = ROOT / "agentic-project.schema.json"
    if schema_path.is_file():
        try:
            json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"invalid manifest JSON schema: {exc}")

    print("Repository context check")
    print(f"- failures: {len(failures)}")
    print(f"- warnings: {len(warnings)}")
    for failure in failures:
        print("FAIL:", failure)
    for warning in warnings:
        print("WARN:", warning)
    print("Status:", "PASSED" if not failures else "FAILED")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
