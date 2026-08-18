#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

def run(cmd, cwd, required=True):
    print("$", " ".join(cmd))
    p = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    if p.stdout.strip():
        print(p.stdout.rstrip())
    if p.stderr.strip():
        print(p.stderr.rstrip(), file=sys.stderr)
    if required and p.returncode:
        return p.returncode
    return 0

def main() -> int:
    root = Path(__file__).resolve().parents[1]

    rc = run([sys.executable, "tools/context_check.py"], root)
    if rc:
        return rc

    rc = run([sys.executable, "tools/obvious_system_check.py"], root)
    if rc:
        return rc

    rc = run([sys.executable, "tools/privacy_scan.py"], root)
    if rc:
        return rc

    if not (root / ".git").exists():
        print("\nNo .git directory found. Skipping git checks.")
        print("Status: PASSED (context only)")
        return 0

    rc = run(["git", "diff", "--check"], root)
    if rc:
        return rc

    run(["git", "status", "--short"], root, required=False)

    print("\nProject-specific test/build commands are owned by docs/contexts/QUALITY.md.")
    print("Status: PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
