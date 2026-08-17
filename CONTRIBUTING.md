# Contributing

Thank you for helping make agentic development more portable and auditable.

## Before coding

1. Search existing issues and discussions.
2. Open or select an issue for meaningful behavior.
3. State the outcome, MVP, non-goals, unhappy path and validation.
4. Keep durable behavior player-agnostic; adapters should stay thin.
5. Preserve the distinction between facts, inferences, proposals and accepted decisions.

## Development

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python tools/prepare_delivery.py
```

Changes to planning, apply, state or paths require adversarial tests. Pack
changes require a generated-project test. Version-sensitive CI, packaging or
security decisions must cite current official documentation in the pull request.

Universal agent-first guidance is authored at the repository root and mirrored
into the core pack. After changing `START_HERE.md`, `CAPABILITIES.md`, prompts,
playbooks or the shared onboarding/templates, run:

```bash
python tools/sync_agent_first_pack.py --write
```

The delivery gate fails when the mirror drifts.

## Pull requests

- keep one coherent delivery slice per PR;
- explain user impact and intentional non-goals;
- include validation evidence;
- do not include generated plans, credentials, personal paths or private data;
- update canonical docs and changelog when behavior changes.

By contributing, you agree that your contribution is licensed under Apache-2.0.
