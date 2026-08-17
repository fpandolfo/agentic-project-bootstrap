from __future__ import annotations

from pathlib import Path
from typing import Any

from .errors import AgenticBootstrapError
from .io import (
    atomic_write_json,
    atomic_write_text,
    canonical_json,
    safe_target_path,
    sha256_bytes,
    sha256_text,
)
from .manifest import validate_manifest
from .planner import MANIFEST_PATH, STATE_PATH, compute_plan_id, summarize_plan


def _validate_plan(plan: dict[str, Any]) -> None:
    if plan.get("planVersion") != 1:
        raise AgenticBootstrapError("unsupported planVersion")
    plan_id = plan.get("planId")
    if not isinstance(plan_id, str):
        raise AgenticBootstrapError("plan is missing planId")
    without_id = {key: value for key, value in plan.items() if key != "planId"}
    expected = compute_plan_id(without_id)
    if plan_id != expected:
        raise AgenticBootstrapError("plan fingerprint does not match its contents")
    validate_manifest(plan.get("manifest", {}))


def apply_plan(plan: dict[str, Any], approval: str) -> dict[str, int]:
    _validate_plan(plan)
    plan_id = plan["planId"]
    if len(approval) < 8 or not plan_id.startswith(approval):
        raise AgenticBootstrapError(
            f"approval does not match plan; rerun with --approve {plan_id[:12]}"
        )
    counts = summarize_plan(plan)
    if counts["conflict"]:
        raise AgenticBootstrapError(
            f"plan contains {counts['conflict']} conflict(s); no files were written"
        )

    target = Path(plan["target"]).resolve()
    target.mkdir(parents=True, exist_ok=True)

    # Preflight every managed path before the first write.
    for entry in plan["files"]:
        destination = safe_target_path(target, entry["path"])
        action = entry["action"]
        if action == "create" and destination.exists():
            raise AgenticBootstrapError(f"target changed after planning: {entry['path']}")
        if action in {"update", "unchanged", "preserve"}:
            if not destination.is_file():
                raise AgenticBootstrapError(f"target changed after planning: {entry['path']}")
            current = sha256_bytes(destination.read_bytes())
            expected = entry["beforeSha256"] or entry["contentSha256"]
            if current != expected:
                raise AgenticBootstrapError(f"target changed after planning: {entry['path']}")

    managed_files: dict[str, dict[str, str]] = {}
    for entry in plan["files"]:
        destination = safe_target_path(target, entry["path"])
        if entry["action"] in {"create", "update"}:
            atomic_write_text(destination, entry["content"])
        if entry.get("managed"):
            if entry["action"] == "preserve":
                managed_hash = entry["beforeSha256"]
                customized = True
            else:
                managed_hash = entry["contentSha256"]
                customized = False
            managed_files[entry["path"]] = {
                "sha256": managed_hash,
                "pack": entry["pack"],
                "customized": customized,
            }

    state = {
        "schemaVersion": 1,
        "toolVersion": plan["toolVersion"],
        "lastPlanId": plan_id,
        "managedFiles": managed_files,
    }
    atomic_write_json(target / MANIFEST_PATH, plan["manifest"])
    atomic_write_json(target / STATE_PATH, state)
    return counts
