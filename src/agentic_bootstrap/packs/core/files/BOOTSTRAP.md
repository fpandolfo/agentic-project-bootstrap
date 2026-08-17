# Bootstrap Runbook

This file is for the **first agent activation** of a new project.

The bootstrap is complete when a clean-context agent can navigate the repository without relying on chat history.

## Phase 0 — Confirm the applied manifest

The reviewed bootstrap declaration lives in `.agentic/manifest.json`. The
fingerprinted applied state lives in `.agentic/state.json`.

Unknown information must remain explicit as `TBD`; do not invent it. Run
`agentic verify --target .` when the `agentic` CLI is available, or use the
standalone context check below.

## Phase 1 — Discover before scaffolding

Determine whether the repository is greenfield, an existing codebase, a prototype or documentation-only discovery.

Before creating product code, establish:

1. product/problem intent;
2. current repository state;
3. target users/stakeholders, if known;
4. MVP boundary;
5. chosen or candidate stack;
6. architecture constraints;
7. validation strategy;
8. external systems/integrations;
9. security/privacy constraints;
10. human decisions still required.

## Phase 2 — Fill the minimal canonical set

Required owners:

- `docs/PROJECT_INDEX.md`
- `docs/contexts/PRODUCT.md`
- `docs/contexts/STACK.md`
- `docs/contexts/ARCHITECTURE.md`
- `docs/contexts/QUALITY.md`

Do **not** create extra docs just for symmetry.

## Phase 3 — Define the first delivery slice

Use `docs/templates/FEATURE_SLICE.md`.

At minimum define problem/outcome, hypothesis when relevant, MVP, non-goals, happy path, unhappy path, edge cases, owners, risks and validation.

## Phase 4 — Implement

Only after the slice is understood:

- prefer deep modules with narrow interfaces;
- avoid duplicate owners;
- add tests closest to actual risk;
- consult current official docs for changing external facts.

## Phase 5 — Close

1. run focused validation;
2. run broader validation when proportional;
3. run `python tools/context_check.py`;
4. run `python tools/prepare_delivery.py`;
5. update durable owners;
6. record residual risk/follow-up.

## Suggested first prompt for any capable coding agent

```text
Read AGENTS.md and BOOTSTRAP.md first.

Treat this as a clean-context bootstrap. Do not start implementing product code yet.

Inspect the repository and create a concise discovery snapshot covering:
- product/problem intent;
- current state;
- MVP boundary;
- happy path;
- unhappy path;
- relevant edge cases;
- candidate/confirmed stack;
- architecture constraints;
- canonical owners;
- validation strategy;
- material unknowns and human decisions.

Update only the minimal canonical docs needed to make the repository understandable to the next clean-context agent.

Prefer links to canonical owners over duplicated decisions.
Do not create architecture or tooling merely for symmetry.
Run python tools/context_check.py before closing the bootstrap pass.
```

## Completion test

A new agent should be able to answer without chat history:

- What does the project do?
- What exists today?
- What is not implemented?
- What is the next slice?
- Which file owns each important decision?
- Which validation commands matter?
- Which decisions require human confirmation?
