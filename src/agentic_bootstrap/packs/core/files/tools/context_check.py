#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUIRED = [
    "START_HERE.md",
    "CAPABILITIES.md",
    "TOOLING.md",
    "PROMPTS.md",
    "AGENTS.md",
    "README.md",
    "docs/PROJECT_INDEX.md",
    "docs/contexts/PRODUCT.md",
    "docs/contexts/STACK.md",
    "docs/contexts/ARCHITECTURE.md",
    "docs/contexts/QUALITY.md",
    "docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md",
    "docs/guides/AGENTIC_DELIVERY_LIFECYCLE.md",
    "docs/guides/CI_AND_DELIVERY_GATES.md",
    "docs/guides/CONTEXT_GENERATION_AND_DRIFT.md",
    "docs/guides/REAL_PROJECT_LEARNING.md",
    "docs/ops/DELIVERY_WORKFLOW.md",
    "docs/ops/CONTEXT_GOVERNANCE.md",
    "docs/ops/AGENT_ADAPTERS.md",
    "docs/ops/AGENT_FIRST_ONBOARDING.md",
    "docs/checklists/CHANGE_IMPACT.md",
    "docs/checklists/SOFTWARE_DESIGN.md",
    "docs/templates/CASE_STUDY.md",
    "docs/templates/QUALITY_STRATEGY.md",
    "case-studies/README.md",
    "case-studies/project-aurora/README.md",
    "case-studies/project-relay/README.md",
    "playbooks/NEW_PROJECT.md",
    "playbooks/ADOPT_PROJECT.md",
    "playbooks/EVOLVE_PROJECT.md",
    "tools/obvious_system_check.py",
    "tools/privacy_scan.py",
]

TOKEN_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-placeholders", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    failures = []
    warnings = []

    for rel in REQUIRED:
        if not (root / rel).exists():
            failures.append(f"missing required file: {rel}")

    if (root / "AGENTS.md").exists():
        text = (root / "AGENTS.md").read_text(encoding="utf-8")
        for ref in ("START_HERE.md", "docs/PROJECT_INDEX.md", "docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md", "docs/ops/AGENT_ADAPTERS.md", "tools/context_check.py"):
            if ref not in text:
                failures.append(f"AGENTS.md does not reference {ref}")

    # Player adapters are optional. Validate them only when their pack is present.
    for skills_root in (root / ".agents" / "skills", root / ".kiro" / "skills"):
        if skills_root.exists():
            for skill in skills_root.glob("*/SKILL.md"):
                text = skill.read_text(encoding="utf-8")
                if not text.startswith("---\n"):
                    failures.append(f"{skill.relative_to(root)} missing YAML frontmatter")
                    continue
                header = text.split("---", 2)[1]
                if not re.search(r"(?m)^name:\s*\S+", header):
                    failures.append(f"{skill.relative_to(root)} missing name")
                if not re.search(r"(?m)^description:\s*.+", header):
                    failures.append(f"{skill.relative_to(root)} missing description")

    codex_root = root / ".codex" / "agents"
    if codex_root.exists():
        for agent in codex_root.glob("*.toml"):
            text = agent.read_text(encoding="utf-8")
            for key in ("name =", "description =", "sandbox_mode ="):
                if key not in text:
                    failures.append(f"{agent.relative_to(root)} missing {key.strip()}")
            if 'sandbox_mode = "read-only"' not in text:
                warnings.append(f"{agent.relative_to(root)} is not read-only")

    if not args.allow_placeholders:
        excluded = {
            (root / "tools" / "context_check.py").resolve(),
        }
        for path in root.rglob("*"):
            if not path.is_file() or ".git" in path.parts or path.resolve() in excluded:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            tokens = sorted(set(TOKEN_RE.findall(text)))
            if tokens:
                failures.append(f"{path.relative_to(root)} unresolved tokens: {', '.join(tokens)}")

    print("Context check")
    print(f"- failures: {len(failures)}")
    print(f"- warnings: {len(warnings)}")
    for item in failures:
        print("FAIL:", item)
    for item in warnings:
        print("WARN:", item)

    if failures:
        print("\nStatus: FAILED")
        return 1

    print("\nStatus: PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
