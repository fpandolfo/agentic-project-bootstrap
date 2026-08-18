#!/usr/bin/env python3
"""Lightweight advisory guard for navigable, obvious project context."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LONG_DOC_LINES = 220

ENTRY_SURFACES = {
    "AGENTS.md",
    "START_HERE.md",
    "CAPABILITIES.md",
    "README.md",
    "docs/PROJECT_INDEX.md",
}
ADAPTER_PREFIXES = (".agents/", ".codex/", ".kiro/")
DEEP_DIRECTORIES = ("docs/contexts", "docs/ops", "docs/guides")

REQUIRED_NAVIGATION = {
    "executive summary": re.compile(
        r"(?mi)^## (?:Executive Summary|Resumo Executivo|Resumo executivo|Resumo)\s*$"
    ),
    "when to read": re.compile(r"(?mi)^(?:## )?(?:When to read|Quando ler):?\s*$"),
    "when not to read": re.compile(
        r"(?mi)^(?:## )?(?:When not to read|Quando n[aã]o ler):?\s*$"
    ),
    "related owners": re.compile(
        r"(?mi)^(?:## )?(?:Related owners|Adjacent owners|Neighbor owners|Owners vizinhos):?\s*$"
    ),
}


def relative_path(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts:
        raise argparse.ArgumentTypeError("paths must be relative and may not traverse parents")
    return path


def deep_docs(root: Path) -> list[Path]:
    files: list[Path] = []
    for relative in DEEP_DIRECTORIES:
        directory = root / relative
        if directory.is_dir():
            files.extend(directory.glob("*.md"))
    return sorted(files)


def inspect_document(path: Path, threshold: int) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ["could not be read as UTF-8"]
    if len(text.splitlines()) < threshold:
        return []
    return [label for label, pattern in REQUIRED_NAVIGATION.items() if not pattern.search(text)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check lightweight obvious-system context guardrails."
    )
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--files", nargs="*", type=relative_path)
    parser.add_argument("--long-doc-lines", type=int, default=DEFAULT_LONG_DOC_LINES)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return failure when long deep docs miss navigation sections.",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")
    if args.long_doc_lines < 1:
        parser.error("--long-doc-lines must be positive")

    if args.files is None:
        candidates = deep_docs(root)
        relative_candidates = [path.relative_to(root) for path in candidates]
    else:
        relative_candidates = sorted(set(args.files))
        candidates = [root / relative for relative in relative_candidates]

    hints: list[str] = []
    names = {path.as_posix() for path in relative_candidates}
    if names & ENTRY_SURFACES:
        hints.append(
            "Entry surface changed: keep it thin and route to one canonical owner."
        )
    if any(name.startswith(ADAPTER_PREFIXES) for name in names):
        hints.append(
            "Player adapter changed: keep durable rules in player-independent owners."
        )

    findings: list[tuple[str, list[str]]] = []
    checked = 0
    for relative, absolute in zip(relative_candidates, candidates, strict=True):
        if not absolute.is_file() or absolute.suffix.lower() != ".md":
            continue
        if not any(
            relative.as_posix().startswith(f"{directory}/")
            for directory in DEEP_DIRECTORIES
        ):
            continue
        checked += 1
        missing = inspect_document(absolute, args.long_doc_lines)
        if missing:
            findings.append((relative.as_posix(), missing))

    for hint in hints:
        print(f"HINT: {hint}")
    for path, missing in findings:
        level = "FAIL" if args.strict else "WARN"
        print(f"{level}: {path} missing navigation for long doc: {', '.join(missing)}")

    print("Obvious system check")
    print(f"- deep docs checked: {checked}")
    print(f"- findings: {len(findings)}")
    print(f"- mode: {'strict' if args.strict else 'advisory'}")

    if args.strict and findings:
        print("Status: FAILED")
        return 1
    print("Status: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
