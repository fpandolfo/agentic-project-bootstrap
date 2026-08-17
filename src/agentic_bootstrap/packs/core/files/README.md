# {{PROJECT_NAME}}

> Bootstrapped with **Agentic Project Bootstrap v0.1.0**.

{{PROJECT_DESCRIPTION}}

This repository is prepared for disciplined, highly agent-assisted development while remaining **player-agnostic**.

The goal is not documentation for its own sake. The goal is to let a clean-context human or agent answer quickly:

- What is this project?
- What is true now?
- Where does each durable decision live?
- What should I read for this task?
- What is the smallest safe slice?
- How do I validate it?
- What still requires a human decision?

## Start here

1. `AGENTS.md`
2. `docs/PROJECT_INDEX.md`
3. the canonical owner for the task
4. relevant code/tests

If the repository has just been created, read `BOOTSTRAP.md` before implementation.

## Operating model

Durable project truth belongs in code/tests, versioned contracts when present, canonical docs, ADRs and deterministic tooling.

Player-specific surfaces such as `.codex/`, `.kiro/` and `.agents/skills/` are **adapters**, not the only owners of durable rules.

## Current bootstrap assumptions

- Project name: `{{PROJECT_NAME}}`
- Slug: `{{PROJECT_SLUG}}`
- Primary stack: `{{PRIMARY_STACK}}`
- Bootstrap date: `{{BOOTSTRAP_DATE}}`

## Baseline checks

```bash
python tools/context_check.py
python tools/prepare_delivery.py
```

Project-specific build/test/lint commands belong in `docs/contexts/QUALITY.md`.
