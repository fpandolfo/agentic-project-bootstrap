from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .errors import AgenticBootstrapError
from .io import load_json
from .manifest import Manifest


@dataclass(frozen=True)
class Pack:
    name: str
    description: str
    requires: tuple[str, ...]
    root: Path


def builtin_packs_root() -> Path:
    return Path(__file__).resolve().parent / "packs"


def discover_packs() -> dict[str, Pack]:
    result: dict[str, Pack] = {}
    root = builtin_packs_root()
    for metadata_path in sorted(root.glob("*/pack.json")):
        raw = load_json(metadata_path)
        name = raw.get("name")
        description = raw.get("description")
        requires = raw.get("requires", [])
        if metadata_path.parent.name != name:
            raise AgenticBootstrapError(f"pack directory/name mismatch: {metadata_path}")
        if not isinstance(description, str) or not isinstance(requires, list):
            raise AgenticBootstrapError(f"invalid pack metadata: {metadata_path}")
        if any(not isinstance(item, str) for item in requires):
            raise AgenticBootstrapError(f"invalid pack dependencies: {metadata_path}")
        result[name] = Pack(name, description, tuple(requires), metadata_path.parent)
    return result


def resolve_packs(selected: tuple[str, ...], available: dict[str, Pack]) -> list[Pack]:
    result: list[Pack] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str) -> None:
        if name in visited:
            return
        if name in visiting:
            raise AgenticBootstrapError(f"cyclic pack dependency involving {name}")
        pack = available.get(name)
        if pack is None:
            raise AgenticBootstrapError(f"unknown pack: {name}")
        visiting.add(name)
        for dependency in pack.requires:
            visit(dependency)
        visiting.remove(name)
        visited.add(name)
        result.append(pack)

    for name in selected:
        visit(name)
    return result


def render_files(manifest: Manifest) -> tuple[dict[str, str], dict[str, str]]:
    available = discover_packs()
    packs = resolve_packs(manifest.packs, available)
    rendered: dict[str, str] = {}
    owners: dict[str, str] = {}
    for pack in packs:
        files_root = pack.root / "files"
        for source in sorted(files_root.rglob("*")):
            if not source.is_file():
                continue
            if "__pycache__" in source.parts or source.suffix in {".pyc", ".pyo"}:
                continue
            relative = source.relative_to(files_root).as_posix()
            if source.is_symlink():
                raise AgenticBootstrapError(f"pack files may not be symlinks: {source}")
            try:
                content = source.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                raise AgenticBootstrapError(f"binary pack file is not supported yet: {source}") from exc
            for token, value in manifest.tokens.items():
                content = content.replace(token, value)
            previous = rendered.get(relative)
            if previous is not None and previous != content:
                raise AgenticBootstrapError(
                    f"pack collision for {relative}: {owners[relative]} and {pack.name}"
                )
            rendered[relative] = content
            owners[relative] = pack.name
    return rendered, owners
