from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Any

from . import __version__
from .errors import AgenticBootstrapError
from .io import canonical_json, load_json, safe_target_path, sha256_bytes, sha256_text
from .manifest import Manifest
from .packs import render_files

STATE_PATH = ".agentic/state.json"
MANIFEST_PATH = ".agentic/manifest.json"


def _load_state(target: Path) -> dict[str, Any]:
    path = target / STATE_PATH
    if not path.exists():
        return {"schemaVersion": 1, "managedFiles": {}}
    raw = load_json(path)
    if raw.get("schemaVersion") != 1 or not isinstance(raw.get("managedFiles"), dict):
        raise AgenticBootstrapError(f"invalid managed state: {path}")
    return raw


def compute_plan_id(plan_without_id: dict[str, Any]) -> str:
    return sha256_text(canonical_json(plan_without_id))


def build_plan(
    target: Path, manifest: Manifest, *, preserve_existing: bool = False
) -> dict[str, Any]:
    target = target.resolve()
    rendered, owners = render_files(manifest)
    state = _load_state(target)
    managed = state.get("managedFiles", {})
    entries: list[dict[str, Any]] = []

    for relative, content in sorted(rendered.items()):
        destination = safe_target_path(target, relative)
        desired_hash = sha256_text(content)
        previous = managed.get(relative)
        managed_before = isinstance(previous, dict)
        customized = bool(previous.get("customized")) if managed_before else False
        if not destination.exists():
            action = "create"
            before_hash = None
        elif not destination.is_file():
            action = "conflict"
            before_hash = None
        else:
            existing_bytes = destination.read_bytes()
            before_hash = sha256_bytes(existing_bytes)
            if before_hash == desired_hash:
                action = "unchanged"
                customized = False
            elif managed_before and customized:
                action = "preserve"
            elif managed_before and previous.get("sha256") == before_hash:
                action = "update"
            elif managed_before:
                action = "preserve"
                customized = True
            elif preserve_existing:
                action = "preserve"
            else:
                action = "conflict"
        entries.append(
            {
                "path": relative,
                "pack": owners[relative],
                "action": action,
                "beforeSha256": before_hash,
                "contentSha256": desired_hash,
                "content": content,
                "managed": managed_before or action in {"create", "update", "unchanged"},
                "customized": customized,
            }
        )

    orphaned = sorted(set(managed) - set(rendered))
    manifest_hash = sha256_text(canonical_json(manifest.raw))
    payload: dict[str, Any] = {
        "planVersion": 1,
        "toolVersion": __version__,
        "createdAt": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "target": str(target),
        "manifestSha256": manifest_hash,
        "manifest": manifest.raw,
        "preserveExisting": preserve_existing,
        "files": entries,
        "orphanedManagedFiles": orphaned,
    }
    payload["planId"] = compute_plan_id(payload)
    return payload


def summarize_plan(plan: dict[str, Any]) -> dict[str, int]:
    counts = {
        name: 0
        for name in ("create", "update", "unchanged", "preserve", "conflict")
    }
    for entry in plan.get("files", []):
        action = entry.get("action")
        if action in counts:
            counts[action] += 1
    return counts
