#!/usr/bin/env python3
"""Conservative repository scan for common privacy and secret leaks."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

RULES = {
    "absolute user path": re.compile(r"(?:/home/[^/\s]+|/Users/[^/\s]+|[A-Za-z]:\\\\Users\\\\[^\\\s]+)"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "credential-like literal": re.compile(
        r"(?i)(?:password|passwd|secret|token|api[_-]?key|private[_-]?key)"
        r"\s*[:=]\s*['\"][^'\"]+['\"]"
    ),
    "GitHub token": re.compile(r"(?:gh[pousr]_[A-Za-z0-9_]{30,}|github_pat_[A-Za-z0-9_]{30,})"),
    "AWS access key": re.compile(r"(?:AKIA|ASIA)[A-Z0-9]{16}"),
    "private IPv4 address": re.compile(
        r"\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.(?:\d{1,3}\.)\d{1,3}|"
        r"172\.(?:1[6-9]|2\d|3[01])\.(?:\d{1,3}\.)\d{1,3})\b"
    ),
}

SENSITIVE_SUFFIXES = {
    ".jks",
    ".key",
    ".keystore",
    ".p12",
    ".pem",
    ".pfx",
    ".sqlite",
    ".sqlite3",
}


def candidate_files() -> list[Path]:
    if (ROOT / ".git").exists():
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        return [ROOT / item.decode() for item in result.stdout.split(b"\0") if item]
    return [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]


def main() -> int:
    files = candidate_files()
    findings: list[tuple[str, Path, int]] = []
    for path in files:
        if path.resolve() == SELF:
            continue
        relative = path.relative_to(ROOT)
        if path.suffix.lower() in SENSITIVE_SUFFIXES or path.name.startswith(".env"):
            findings.append(("sensitive file type", relative, 0))
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in RULES.items():
                if pattern.search(line):
                    findings.append((label, relative, line_number))

    if findings:
        print("Privacy scan failed. Review these locations; values are intentionally hidden:")
        for label, path, line_number in findings:
            location = f"{path}:{line_number}" if line_number else str(path)
            print(f"- {label}: {location}")
        return 1

    print(f"Privacy scan passed ({len(files)} repository files checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
