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

## Delivery

For meaningful behavior, map:

```text
MAP -> IMPLEMENT -> VALIDATE -> CLOSE
```

Capture outcome, scope, non-goals, happy path, unhappy path, relevant edge cases,
owners, risks, human gates and validation before broad implementation.

## Validation and safety

- `tools/context_check.py`: verifies the minimal context structure;
- `tools/prepare_delivery.py`: performs the repository delivery gate;
- `tools/privacy_scan.py`: scans this bootstrap repository before publication;
- `agentic plan/apply/verify`: optional deterministic file application workflow.

Project-specific checks remain owned by `docs/contexts/QUALITY.md`.

## Optional adapters

Generic Agent Skills, Codex and Kiro packs can improve discovery in supported
players. They are optional adapters. The universal contract remains
`START_HERE.md` plus canonical repository files.
