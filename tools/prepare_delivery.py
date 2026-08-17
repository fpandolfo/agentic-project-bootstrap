#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str]) -> int:
    print("$", " ".join(command), flush=True)
    env = os.environ.copy()
    source_path = str(ROOT / "src")
    env["PYTHONPATH"] = (
        source_path
        if not env.get("PYTHONPATH")
        else source_path + os.pathsep + env["PYTHONPATH"]
    )
    return subprocess.run(command, cwd=ROOT, env=env).returncode


def main() -> int:
    commands = [
        [sys.executable, "tools/context_check.py"],
        [sys.executable, "tools/privacy_scan.py"],
        [sys.executable, "-m", "compileall", "-q", "src", "tests", "tools", "agentic.py"],
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        [sys.executable, "agentic.py", "doctor"],
    ]
    for command in commands:
        rc = run(command)
        if rc:
            return rc
    if (ROOT / ".git").exists():
        rc = run(["git", "diff", "--check"])
        if rc:
            return rc
        run(["git", "status", "--short"])
    print("Status: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
