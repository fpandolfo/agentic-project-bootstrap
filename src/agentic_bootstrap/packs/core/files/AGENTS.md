# AGENTS

Operational entrypoint for humans and AI agents working in `{{PROJECT_NAME}}`.

## Objective

Use the **minimum sufficient context** to reach the correct owner, make a safe change, validate proportionally, and leave the repository easier to resume than it was before.

## First activation

At the beginning of a clean-context task:

1. read this `AGENTS.md`;
2. read `docs/PROJECT_INDEX.md`;
3. inspect `git status --short`;
4. identify the active work item, if one exists;
5. classify the task as product/discovery, implementation, bug/investigation, cross-cutting, architecture/security, or operational/docs/tooling;
6. classify recommended reasoning effort as `low`, `medium` or `high`;
7. open only the minimum canonical owners needed;
8. compare work-item intent, repository docs, tests and actual code before editing;
9. for meaningful new behavior, map:
   - problem/outcome;
   - hypothesis;
   - MVP;
   - non-goals;
   - happy path;
   - unhappy path;
   - relevant edge cases;
   - owners touched;
   - validation;
10. do not turn an unresolved product or architecture question into code merely because implementation is possible.

## Trust order

1. current code and tests;
2. versioned contracts/schemas, when present;
3. `docs/PROJECT_INDEX.md`;
4. canonical context/architecture docs;
5. ADRs;
6. operational docs/runbooks;
7. README summaries;
8. external work tracker;
9. chat history.

A tracker records intent and closeout. The repository records technical truth.

## Reasoning effort

Use `medium` as the pragmatic default.

Prefer `low` for factual/localized/mechanical work.

Prefer `high` for architecture, security/privacy, ambiguous bugs, cross-cutting refactors, CI/deploy/release, dependencies, external integrations, or conflicts between code/docs/work-item intent.

A workflow can recommend reasoning effort; it does not change the player/model setting automatically.

## Read next by task

### Product / discovery

1. `docs/contexts/PRODUCT.md`
2. relevant domain owner
3. `docs/templates/FEATURE_SLICE.md`

### Implementation

1. relevant product/context owner
2. `docs/contexts/ARCHITECTURE.md`
3. `docs/contexts/STACK.md`
4. nearby code/tests

### Bug / investigation

1. reproduce/reconstruct current behavior;
2. locate nearest code/test owner;
3. compare expected behavior against docs/contracts;
4. avoid broad refactors until root cause is understood;
5. add regression validation near the failure.

### Cross-cutting / risky

1. `docs/checklists/CHANGE_IMPACT.md`
2. affected canonical owners
3. relevant ADRs/contracts
4. focused tests
5. broader validation proportional to blast radius

### Operational / docs / agents

1. `docs/ops/CONTEXT_GOVERNANCE.md`
2. `docs/ops/AGENT_ADAPTERS.md`
3. `docs/checklists/CHANGE_IMPACT.md`

## System-obvious principles

Optimize for low cognitive load, low change amplification, explicit ownership, discoverable dependencies and deep modules with narrow interfaces.

- Every durable decision should have one clear canonical owner.
- Entrypoint docs should route, not duplicate deep owners.
- If a simple change requires touching many surfaces, re-check ownership.
- Make important unknowns explicit as a doc, test, blocked action or work item.
- Prefer predictable deep solutions over clever shallow wrappers.
- Split around stable concepts and information hiding, not file length.

## Durable rules vs player adapters

Durable truth must live in `AGENTS.md`, canonical docs, ADRs, contracts/schemas, tests or deterministic tooling.

`.agents/skills/`, `.codex/` and `.kiro/` are adapters.

Owner: `docs/ops/AGENT_ADAPTERS.md`.

## Official documentation rule

For version-sensitive or security-sensitive external facts, use current official documentation before consolidating framework/runtime versions, APIs, auth/security behavior, cloud/deploy configuration, platform requirements, CI/release behavior or integrations.

Owner: `docs/ops/OFFICIAL_DOCS_POLICY.md`.

## Human gates

Keep explicit human approval for material product behavior changes, irreversible migrations, legal/payment/account actions, secrets/credentials, production release authority, destructive material operations, and subjective UX/brand choices without a canonical direction.

## Change discipline

For meaningful work:

```text
MAP -> IMPLEMENT -> VALIDATE -> CLOSE
```

Before closing:

1. run focused validation;
2. run broader validation when justified;
3. run `python tools/context_check.py`;
4. run `python tools/prepare_delivery.py`;
5. inspect `git status --short`;
6. summarize what changed, validation, intentional non-goals and residual risk.
