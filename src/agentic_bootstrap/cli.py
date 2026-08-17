from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from . import __version__
from .apply import apply_plan
from .errors import AgenticBootstrapError
from .io import atomic_write_json, load_json
from .manifest import dumps_manifest, load_manifest, new_manifest, slugify
from .packs import discover_packs
from .planner import build_plan, summarize_plan
from .verify import verify_target


def _pack_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def _write_or_print(path: str, content: str) -> None:
    if path == "-":
        print(content, end="")
    else:
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")
        print(f"Wrote {destination}")


def command_doctor(args: argparse.Namespace) -> int:
    available = discover_packs()
    checks = {
        "python": {
            "status": "passed" if sys.version_info >= (3, 11) else "failed",
            "value": sys.version.split()[0],
        },
        "git": {
            "status": "passed" if shutil.which("git") else "failed",
            "value": shutil.which("git"),
        },
        "packs": {"status": "passed" if available else "failed", "value": sorted(available)},
    }
    if args.target:
        target = Path(args.target)
        checks["target"] = {
            "status": "passed" if target.exists() else "warning",
            "value": str(target.resolve()),
        }
    print(json.dumps({"toolVersion": __version__, "checks": checks}, indent=2))
    return 1 if any(item["status"] == "failed" for item in checks.values()) else 0


def command_init(args: argparse.Namespace) -> int:
    manifest = new_manifest(
        name=args.name,
        slug=args.slug,
        description=args.description,
        stack=args.stack,
        packs=_pack_list(args.packs),
    )
    _write_or_print(args.output, dumps_manifest(manifest))
    return 0


def _infer_stack(target: Path) -> str:
    markers = [
        ("pubspec.yaml", "Flutter/Dart"),
        ("package.json", "Node.js"),
        ("pyproject.toml", "Python"),
        ("requirements.txt", "Python"),
        ("pom.xml", "JVM/Maven"),
        ("build.gradle.kts", "JVM/Gradle"),
        ("build.gradle", "JVM/Gradle"),
    ]
    for marker, stack in markers:
        if (target / marker).exists():
            return stack
    return "TBD — inspect and confirm the primary stack"


def command_adopt(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    if not target.is_dir():
        raise AgenticBootstrapError(f"target is not a directory: {target}")
    manifest = new_manifest(
        name=args.name or target.name.replace("-", " ").title(),
        slug=args.slug or slugify(target.name),
        description=args.description,
        stack=args.stack or _infer_stack(target),
        packs=_pack_list(args.packs),
    )
    _write_or_print(args.output, dumps_manifest(manifest))
    return 0


def command_list_packs(_args: argparse.Namespace) -> int:
    for name, pack in discover_packs().items():
        dependencies = f" (requires: {', '.join(pack.requires)})" if pack.requires else ""
        print(f"{name}: {pack.description}{dependencies}")
    return 0


def command_plan(args: argparse.Namespace) -> int:
    manifest = load_manifest(Path(args.manifest))
    plan = build_plan(
        Path(args.target), manifest, preserve_existing=args.preserve_existing
    )
    atomic_write_json(Path(args.output), plan)
    counts = summarize_plan(plan)
    print(f"Plan: {args.output}")
    print(f"Fingerprint: {plan['planId'][:12]}")
    print(" ".join(f"{name}={value}" for name, value in counts.items()))
    if plan["orphanedManagedFiles"]:
        print(f"orphaned={len(plan['orphanedManagedFiles'])} (never deleted automatically)")
    return 2 if counts["conflict"] else 0


def command_apply(args: argparse.Namespace) -> int:
    plan = load_json(Path(args.plan))
    counts = apply_plan(plan, args.approve)
    print(f"Applied plan {plan['planId'][:12]} to {plan['target']}")
    print(" ".join(f"{name}={value}" for name, value in counts.items()))
    return 0


def command_verify(args: argparse.Namespace) -> int:
    result = verify_target(Path(args.target), run_quality=args.run_quality)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "passed" else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agentic", description="Bootstrap an auditable agentic repository")
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser("doctor", help="Check local prerequisites and built-in packs")
    doctor.add_argument("--target")
    doctor.set_defaults(handler=command_doctor)

    init = subparsers.add_parser("init", help="Create a declarative project manifest without touching a target")
    init.add_argument("--name", required=True)
    init.add_argument("--slug")
    init.add_argument("--description", default="TBD — describe the project purpose")
    init.add_argument("--stack", default="TBD — inspect and confirm the primary stack")
    init.add_argument("--packs", default="core,generic-agent")
    init.add_argument("--output", default="agentic-project.json")
    init.set_defaults(handler=command_init)

    adopt = subparsers.add_parser("adopt", help="Create a manifest inferred from an existing repository")
    adopt.add_argument("target")
    adopt.add_argument("--name")
    adopt.add_argument("--slug")
    adopt.add_argument("--description", default="TBD — describe the project purpose")
    adopt.add_argument("--stack")
    adopt.add_argument("--packs", default="core,generic-agent")
    adopt.add_argument("--output", default="agentic-project.json")
    adopt.set_defaults(handler=command_adopt)

    list_packs = subparsers.add_parser("list-packs", help="List available built-in packs")
    list_packs.set_defaults(handler=command_list_packs)

    plan = subparsers.add_parser("plan", help="Render a reviewable, fingerprinted plan")
    plan.add_argument("--target", required=True)
    plan.add_argument("--manifest", required=True)
    plan.add_argument("--output", default="agentic-plan.json")
    plan.add_argument(
        "--preserve-existing",
        action="store_true",
        help="Keep pre-existing colliding files untouched instead of blocking the plan",
    )
    plan.set_defaults(handler=command_plan)

    apply = subparsers.add_parser("apply", help="Apply an unchanged plan after explicit fingerprint approval")
    apply.add_argument("--plan", required=True)
    apply.add_argument("--approve", required=True)
    apply.set_defaults(handler=command_apply)

    verify = subparsers.add_parser("verify", help="Verify managed state and optional project quality commands")
    verify.add_argument("--target", required=True)
    verify.add_argument("--run-quality", action="store_true")
    verify.set_defaults(handler=command_verify)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.handler(args)
    except AgenticBootstrapError as exc:
        parser.exit(1, f"error: {exc}\n")
