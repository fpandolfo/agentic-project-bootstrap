#!/usr/bin/env python3
"""Create a safe, read-only structural snapshot for an agent or human."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

IGNORED_DIRECTORIES = {
    ".dart_tool",
    ".git",
    ".gradle",
    ".hg",
    ".idea",
    ".mypy_cache",
    ".next",
    ".pytest_cache",
    ".ruff_cache",
    ".svn",
    ".venv",
    ".vscode",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
    "vendor",
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

STACK_MARKERS = {
    "Cargo.toml": "Rust",
    "Package.swift": "Swift",
    "build.gradle": "JVM/Gradle",
    "build.gradle.kts": "JVM/Gradle",
    "composer.json": "PHP",
    "deno.json": "Deno",
    "deno.jsonc": "Deno",
    "go.mod": "Go",
    "mix.exs": "Elixir",
    "package.json": "Node.js",
    "pom.xml": "JVM/Maven",
    "pubspec.yaml": "Flutter/Dart",
    "pyproject.toml": "Python",
    "requirements.txt": "Python",
}

CONTEXT_PATHS = {
    "AGENTS.md",
    "BOOTSTRAP.md",
    "CAPABILITIES.md",
    "START_HERE.md",
    "docs/PROJECT_INDEX.md",
    "docs/contexts/ARCHITECTURE.md",
    "docs/contexts/PRODUCT.md",
    "docs/contexts/QUALITY.md",
    "docs/contexts/STACK.md",
}


def _is_sensitive(path: Path) -> bool:
    name = path.name.lower()
    return (
        name == ".env"
        or name.startswith(".env.")
        or path.suffix.lower() in SENSITIVE_SUFFIXES
        or name
        in {
            ".npmrc",
            ".pypirc",
            "credentials",
            "credentials.json",
            "google-services.json",
            "googleservice-info.plist",
            "id_ed25519",
            "id_rsa",
            "local.properties",
        }
    )


def _is_test(path: Path) -> bool:
    lowered_parts = {part.lower() for part in path.parts}
    name = path.name.lower()
    return (
        bool(lowered_parts & {"test", "tests", "spec", "specs", "integrationtest"})
        or name.startswith("test_")
        or "_test." in name
        or ".test." in name
        or ".spec." in name
    )


def _walk(target: Path, max_files: int) -> tuple[list[Path], list[str], list[str], bool]:
    files: list[Path] = []
    ignored_seen: set[str] = set()
    symlinks: list[str] = []
    truncated = False

    for current, directories, names in os.walk(target, topdown=True, followlinks=False):
        current_path = Path(current)
        kept_directories: list[str] = []
        for directory in sorted(directories):
            candidate = current_path / directory
            if candidate.is_symlink():
                symlinks.append(candidate.relative_to(target).as_posix())
            elif directory in IGNORED_DIRECTORIES:
                ignored_seen.add(directory)
            else:
                kept_directories.append(directory)
        directories[:] = kept_directories

        for name in sorted(names):
            candidate = current_path / name
            relative = candidate.relative_to(target)
            if candidate.is_symlink():
                symlinks.append(relative.as_posix())
                continue
            files.append(relative)
            if len(files) >= max_files:
                truncated = True
                return files, sorted(ignored_seen), sorted(symlinks), truncated

    return files, sorted(ignored_seen), sorted(symlinks), truncated


def discover(target: Path, max_files: int = 5000) -> dict[str, Any]:
    if target.is_symlink():
        raise ValueError(f"target may not be a symlink: {target}")
    target = target.resolve()
    if not target.is_dir():
        raise ValueError(f"target is not a directory: {target}")
    if max_files < 1:
        raise ValueError("max_files must be positive")

    files, ignored, symlinks, truncated = _walk(target, max_files)
    paths = sorted(path.as_posix() for path in files)
    names = {path.name for path in files}
    stacks = sorted({STACK_MARKERS[name] for name in names if name in STACK_MARKERS})
    sensitive = sorted(path.as_posix() for path in files if _is_sensitive(path))
    tests = sorted(path.as_posix() for path in files if _is_test(path))
    docs = sorted(
        path.as_posix()
        for path in files
        if path.suffix.lower() in {".md", ".mdx", ".rst"}
        or path.name.lower().startswith("readme")
    )
    workflows = sorted(
        path.as_posix()
        for path in files
        if ".github/workflows" in path.as_posix()
        or path.name in {".gitlab-ci.yml", "Jenkinsfile", "azure-pipelines.yml"}
    )
    diagrams = sorted(
        path.as_posix()
        for path in files
        if path.suffix.lower() in {".mmd", ".mermaid", ".puml"}
        or "diagram" in path.name.lower()
    )
    adrs = sorted(
        path.as_posix()
        for path in files
        if "adr" in {part.lower() for part in path.parts}
        and path.suffix.lower() in {".md", ".mdx", ".rst"}
    )
    contexts = sorted(path for path in paths if path in CONTEXT_PATHS)
    top_level = sorted({path.parts[0] for path in files})
    source_roots = sorted(
        name for name in {"app", "apps", "lib", "modules", "packages", "src"} if (target / name).is_dir()
    )

    has_implementation = bool(stacks or tests or source_roots)
    suggested_mode = "ADOPT_PROJECT" if has_implementation else "NEW_PROJECT"

    questions = [
        "What problem or outcome should this product own?",
        "Who are the primary users and stakeholders?",
        "What is the smallest useful first or next delivery slice?",
        "Which behaviors and constraints are non-negotiable business rules?",
        "Which decisions, risks and irreversible actions require human approval?",
    ]
    if not stacks:
        questions.append("Is a technical stack already constrained, or should alternatives be proposed?")
    if not tests:
        questions.append("What evidence should prove that the product behavior is correct?")
    if not workflows:
        questions.append("Where and how should validation run before changes are delivered?")

    return {
        "schemaVersion": 1,
        "targetLabel": target.name,
        "suggestedMode": suggested_mode,
        "safety": {
            "contentRead": False,
            "commandsExecuted": False,
            "symlinksFollowed": False,
            "ignoredDirectories": ignored,
            "sensitiveCandidates": sensitive,
            "sensitiveContentsRead": False,
            "truncated": truncated,
            "maxFiles": max_files,
        },
        "inventory": {
            "fileCount": len(files),
            "topLevel": top_level,
            "sourceRoots": source_roots,
            "stackMarkers": sorted(name for name in names if name in STACK_MARKERS),
            "candidateStacks": stacks,
            "testFiles": tests,
            "workflowFiles": workflows,
            "documentationFiles": docs,
            "existingContextFiles": contexts,
            "diagramFiles": diagrams,
            "adrFiles": adrs,
            "symlinksSkipped": symlinks,
        },
        "humanQuestions": questions,
        "recommendedNext": [
            "Confirm NEW_PROJECT or ADOPT_PROJECT with the human.",
            "Read START_HERE.md and only the workflow for the confirmed mode.",
            "Inspect relevant project files; do not infer business intent from structure alone.",
            "Present observations, unknowns and proposals separately before writing project files.",
        ],
    }


def to_markdown(snapshot: dict[str, Any]) -> str:
    inventory = snapshot["inventory"]
    safety = snapshot["safety"]

    def values(items: list[str]) -> str:
        return ", ".join(f"`{item}`" for item in items) if items else "None observed"

    lines = [
        "# Project Discovery Snapshot",
        "",
        f"- Target label: `{snapshot['targetLabel']}`",
        f"- Suggested mode: `{snapshot['suggestedMode']}`",
        f"- Files inventoried: {inventory['fileCount']}",
        f"- Scan truncated: {'yes' if safety['truncated'] else 'no'}",
        "- File contents read: no",
        "- Project commands executed: no",
        "- Symlinks followed: no",
        "",
        "## Structural observations",
        "",
        f"- Candidate stacks: {values(inventory['candidateStacks'])}",
        f"- Stack markers: {values(inventory['stackMarkers'])}",
        f"- Source roots: {values(inventory['sourceRoots'])}",
        f"- Existing contexts: {values(inventory['existingContextFiles'])}",
        f"- Tests: {len(inventory['testFiles'])}",
        f"- CI/workflows: {values(inventory['workflowFiles'])}",
        f"- ADRs: {len(inventory['adrFiles'])}",
        f"- Diagrams: {len(inventory['diagramFiles'])}",
        f"- Sensitive candidates (paths only): {values(safety['sensitiveCandidates'])}",
        "",
        "## Questions for the human",
        "",
    ]
    lines.extend(f"- {question}" for question in snapshot["humanQuestions"])
    lines.extend(["", "## Recommended next steps", ""])
    lines.extend(f"{index}. {item}" for index, item in enumerate(snapshot["recommendedNext"], start=1))
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create a content-free, read-only structural snapshot for agent-led discovery."
    )
    parser.add_argument("--target", default=".", help="Project directory to inspect")
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--output", default="-", help="Output path, or - for stdout")
    parser.add_argument("--max-files", type=int, default=5000)
    args = parser.parse_args(argv)

    try:
        snapshot = discover(Path(args.target), max_files=args.max_files)
    except ValueError as exc:
        parser.error(str(exc))
    content = (
        json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.format == "json"
        else to_markdown(snapshot)
    )
    if args.output == "-":
        print(content, end="")
    else:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")
        print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
