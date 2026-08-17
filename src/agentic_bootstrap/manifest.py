from __future__ import annotations

import datetime as dt
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import AgenticBootstrapError
from .io import load_json

PACK_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "project"


@dataclass(frozen=True)
class Manifest:
    raw: dict[str, Any]
    name: str
    slug: str
    description: str
    stack: str
    packs: tuple[str, ...]
    quality_commands: tuple[tuple[str, ...], ...]
    human_gates: tuple[str, ...]

    @property
    def tokens(self) -> dict[str, str]:
        return {
            "{{PROJECT_NAME}}": self.name,
            "{{PROJECT_SLUG}}": self.slug,
            "{{PROJECT_DESCRIPTION}}": self.description,
            "{{PRIMARY_STACK}}": self.stack,
            "{{BOOTSTRAP_DATE}}": dt.date.today().isoformat(),
        }


def _required_text(mapping: dict[str, Any], key: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value.strip():
        raise AgenticBootstrapError(f"manifest field project.{key} must be a non-empty string")
    return value.strip()


def validate_manifest(raw: dict[str, Any]) -> Manifest:
    if raw.get("schemaVersion") != 1:
        raise AgenticBootstrapError("manifest schemaVersion must be 1")
    project = raw.get("project")
    if not isinstance(project, dict):
        raise AgenticBootstrapError("manifest field project must be an object")
    name = _required_text(project, "name")
    slug = project.get("slug") or slugify(name)
    if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
        raise AgenticBootstrapError("manifest field project.slug must be a lowercase kebab-case slug")
    description = _required_text(project, "description")
    stack = _required_text(project, "stack")

    packs_raw = raw.get("packs", ["core"])
    if not isinstance(packs_raw, list) or not packs_raw:
        raise AgenticBootstrapError("manifest field packs must be a non-empty array")
    packs: list[str] = []
    for pack in packs_raw:
        if not isinstance(pack, str) or not PACK_RE.fullmatch(pack):
            raise AgenticBootstrapError(f"invalid pack name: {pack!r}")
        if pack not in packs:
            packs.append(pack)
    if "core" not in packs:
        packs.insert(0, "core")

    quality = raw.get("quality", {})
    if not isinstance(quality, dict):
        raise AgenticBootstrapError("manifest field quality must be an object")
    commands_raw = quality.get("commands", [])
    if not isinstance(commands_raw, list):
        raise AgenticBootstrapError("manifest field quality.commands must be an array")
    commands: list[tuple[str, ...]] = []
    for command in commands_raw:
        if (
            not isinstance(command, list)
            or not command
            or any(not isinstance(item, str) or not item for item in command)
        ):
            raise AgenticBootstrapError(
                "each quality command must be a non-empty argv array; shell strings are not accepted"
            )
        commands.append(tuple(command))

    gates_raw = raw.get("humanGates", [])
    if not isinstance(gates_raw, list) or any(not isinstance(gate, str) for gate in gates_raw):
        raise AgenticBootstrapError("manifest field humanGates must be an array of strings")

    normalized = {
        "schemaVersion": 1,
        "project": {
            "name": name,
            "slug": slug,
            "description": description,
            "stack": stack,
        },
        "packs": packs,
        "quality": {"commands": [list(command) for command in commands]},
        "humanGates": list(gates_raw),
    }
    return Manifest(
        raw=normalized,
        name=name,
        slug=slug,
        description=description,
        stack=stack,
        packs=tuple(packs),
        quality_commands=tuple(commands),
        human_gates=tuple(gates_raw),
    )


def load_manifest(path: Path) -> Manifest:
    return validate_manifest(load_json(path))


def new_manifest(
    *,
    name: str,
    slug: str | None,
    description: str,
    stack: str,
    packs: list[str],
) -> Manifest:
    return validate_manifest(
        {
            "schemaVersion": 1,
            "project": {
                "name": name,
                "slug": slug or slugify(name),
                "description": description,
                "stack": stack,
            },
            "packs": packs or ["core", "generic-agent"],
            "quality": {"commands": []},
            "humanGates": [
                "product-behavior",
                "secrets",
                "destructive-actions",
                "production-release",
            ],
        }
    )


def dumps_manifest(manifest: Manifest) -> str:
    return json.dumps(manifest.raw, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
