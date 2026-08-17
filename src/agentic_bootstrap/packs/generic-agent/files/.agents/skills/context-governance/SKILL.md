---
name: context-governance
description: Use when changing AGENTS.md, PROJECT_INDEX, canonical docs, templates, generated context, player adapters or context tooling. Keeps durable ownership clear and prevents instruction drift.
---

1. Read `AGENTS.md`, `docs/PROJECT_INDEX.md` and `docs/ops/CONTEXT_GOVERNANCE.md`.
2. Read `docs/ops/AGENT_ADAPTERS.md` when adapters are touched.
3. Before repeating a durable decision, identify its canonical owner.
4. Prefer linking over duplication.
5. Do not add generated docs/tooling until a real drift/discovery problem exists.
6. Run `python tools/context_check.py`.
7. For meaningful delivery also run `python tools/prepare_delivery.py`.
