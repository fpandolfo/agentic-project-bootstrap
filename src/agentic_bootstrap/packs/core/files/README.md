# {{PROJECT_NAME}}

> Guided by **Agentic Project Bootstrap**.

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

## Start here — any capable agent

1. `START_HERE.md`
2. choose `NEW_PROJECT`, `ADOPT_PROJECT` or `EVOLVE_PROJECT`;
3. use the selected playbook;
4. continue through `AGENTS.md` and `docs/PROJECT_INDEX.md` once the project is understood.

If the repository has just been created, read `BOOTSTRAP.md` before implementation.

The guidance is adaptable. It helps the agent discover evidence, ask useful
questions and propose options; it does not impose final product or architecture
decisions.

## Operating model

Durable project truth belongs in code/tests, versioned contracts when present, canonical docs, ADRs and deterministic tooling.

Player-specific surfaces such as `.codex/`, `.kiro/` and `.agents/skills/` are **adapters**, not the only owners of durable rules.

No CLI installation is required to start. `tools/discover_project.py` provides a
safe structural inventory. The optional `agentic` CLI can later apply reviewed
packs through a fingerprinted plan when that control is useful.

Meaningful implementation and refactoring follow the explicit guidance in
`docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md`, inspired by John Ousterhout's
*A Philosophy of Software Design*. The aim is low cognitive load, information
hiding and deep modules with small interfaces, not ceremony or layer count.

`TOOLING.md` distinguishes tools that actually ship from case-study evidence and
future extraction candidates.

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

## Bootstrap ownership

Once generated, these files belong to this project. Upstream bootstrap changes
are proposals, not automatic updates. The alpha never silently overwrites local
decisions or removes obsolete managed files; review and approve any future
adoption explicitly.
