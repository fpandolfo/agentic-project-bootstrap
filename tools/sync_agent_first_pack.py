#!/usr/bin/env python3
"""Keep universal agent-first guidance mirrored in the distributable core pack."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_FILES = ROOT / "src" / "agentic_bootstrap" / "packs" / "core" / "files"
SHARED = [
    Path("START_HERE.md"),
    Path("CAPABILITIES.md"),
    Path("PROMPTS.md"),
    Path("playbooks/NEW_PROJECT.md"),
    Path("playbooks/ADOPT_PROJECT.md"),
    Path("playbooks/EVOLVE_PROJECT.md"),
    Path("docs/ops/AGENT_FIRST_ONBOARDING.md"),
    Path("docs/templates/DISCOVERY_BRIEF.md"),
    Path("docs/templates/ARCHITECTURE_DIAGRAMS.md"),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Update mirrored pack files")
    args = parser.parse_args()

    drift: list[str] = []
    for relative in SHARED:
        source = ROOT / relative
        destination = PACK_FILES / relative
        if args.write:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        elif not destination.is_file() or destination.read_bytes() != source.read_bytes():
            drift.append(relative.as_posix())

    if drift:
        print("Agent-first pack mirror is stale:")
        for relative in drift:
            print(f"- {relative}")
        print("Run: python tools/sync_agent_first_pack.py --write")
        return 1

    action = "updated" if args.write else "verified"
    print(f"Agent-first pack mirror {action} ({len(SHARED)} files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
