# Capability Catalog

Use this catalog to select the minimum useful capability for the current task.
Capabilities are advisory building blocks, not mandatory ceremony.

## Discovery

### Structural inventory

Tool: `tools/discover_project.py`

Produces a content-free snapshot of stack markers, source roots, tests, CI,
documentation, ADRs, diagrams and sensitive path candidates. It does not read
file contents, execute project commands or follow symlinks.

### Product discovery

Use the active playbook to establish problem/outcome, users, business rules,
MVP or next slice, non-goals, risks, validation and human gates.

## Context and documentation

Generate only owners justified by real project information:

- `AGENTS.md`: thin operational router;
- `docs/PROJECT_INDEX.md`: current-state and ownership index;
- `docs/contexts/PRODUCT.md`: outcomes, users, scope and business rules;
- `docs/contexts/ARCHITECTURE.md`: boundaries, components and flows;
- `docs/contexts/STACK.md`: actual or proposed technology choices;
- `docs/contexts/QUALITY.md`: evidence and commands that prove correctness;
- `docs/adr/`: durable decisions with alternatives and consequences.

Templates live under `docs/templates/`.

## Architecture and diagrams

Use Mermaid when a relationship, flow or state transition is materially easier
to understand visually. Prefer the smallest useful type:

- `flowchart` for components, decisions and process flow;
- `sequenceDiagram` for interaction order;
- `stateDiagram-v2` for lifecycle and state transitions;
- `erDiagram` for persistent data relationships;
- `timeline` for event history.

Keep the source versioned beside the canonical architecture owner. A diagram is
an explanatory view, never the only owner of a business rule.

## Decisions

Create an ADR when a decision has meaningful alternatives, long-lived
consequences, migration cost, security impact or cross-cutting ownership.
Do not create ADRs for routine implementation details.

## Software design discipline

For meaningful implementation, architecture or refactoring, use
`docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md` and
`docs/checklists/SOFTWARE_DESIGN.md`.

The guidance explicitly applies ideas from John Ousterhout's *A Philosophy of
Software Design*: reduce cognitive load and change amplification, prefer deep
modules with small interfaces, hide information, keep layers at distinct
abstractions and invest strategically where complexity is real. These are
design heuristics, not permission for speculative frameworks or a substitute
for human architecture decisions.

## Delivery

For meaningful behavior, map:

```text
MAP -> IMPLEMENT -> VALIDATE -> CLOSE
```

Capture outcome, scope, non-goals, happy path, unhappy path, relevant edge cases,
owners, risks, human gates and validation before broad implementation.

For an end-to-end reference from product framing through release and learning,
read `docs/guides/AGENTIC_DELIVERY_LIFECYCLE.md`. Its validation ladder helps
separate deterministic tests, contract checks, visual evidence, integrated
smoke, environment/device validation and production signals.

## Learning from real delivery

`case-studies/` contains sanitized real-project evidence. Use a case to discover
questions, gates and validation strategies that may fit the current project.
Never treat a case's architecture or stack as a default decision.

When extracting learning from private or client work, follow
`docs/guides/REAL_PROJECT_LEARNING.md` and start from
`docs/templates/CASE_STUDY.md`. Evidence must remain classified as publicly
reproducible, privately verified, owner-reported or synthetic illustration.

## Validation and safety

- `tools/context_check.py`: verifies the minimal context structure;
- `tools/prepare_delivery.py`: performs the repository delivery gate;
- `tools/privacy_scan.py`: scans this bootstrap repository before publication;
- `agentic plan/apply/verify`: optional deterministic file application workflow.

Project-specific checks remain owned by `docs/contexts/QUALITY.md`.
Use `docs/templates/QUALITY_STRATEGY.md` to establish a new project's
risk-to-evidence map. `docs/guides/CONTEXT_GENERATION_AND_DRIFT.md` explains when
generated factual maps are justified, and `docs/guides/CI_AND_DELIVERY_GATES.md`
keeps remote pipelines aligned with local project-owned commands.

`TOOLING.md` is the canonical catalog of tools that are available, guidance-only,
candidate for neutral extraction or intentionally local to a consumer.

## Optional adapters

Generic Agent Skills, Codex and Kiro packs can improve discovery in supported
players. They are optional adapters. The universal contract remains
`START_HERE.md` plus canonical repository files.
