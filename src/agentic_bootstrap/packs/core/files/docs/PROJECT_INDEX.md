# Project Index

Master navigation and current-state owner for `{{PROJECT_NAME}}`.

## Purpose

A clean-context human or agent should quickly discover what the project is, what exists now, what is not implemented, which files own durable decisions, what the next slice is and which validations matter.

Keep this file navigational. Do not duplicate deep decisions here.

## Current state

Status: `BOOTSTRAP / DISCOVERY`

Project: `{{PROJECT_NAME}}`

Description:

> {{PROJECT_DESCRIPTION}}

Primary stack:

> {{PRIMARY_STACK}}

### Implemented

- TBD — discovery required.

### Not implemented / known gaps

- TBD — discovery required.

### Current work

- Active work item: `TBD`
- Next recommended slice: `TBD`

## Canonical owners

| Area | Owner |
|---|---|
| First-time agent activation | `START_HERE.md` |
| Capability menu | `CAPABILITIES.md` |
| Mode playbooks | `playbooks/` |
| Operational entrypoint | `AGENTS.md` |
| Current state / navigation | `docs/PROJECT_INDEX.md` |
| Product/problem | `docs/contexts/PRODUCT.md` |
| Stack | `docs/contexts/STACK.md` |
| Architecture | `docs/contexts/ARCHITECTURE.md` |
| Quality / validation | `docs/contexts/QUALITY.md` |
| Delivery workflow | `docs/ops/DELIVERY_WORKFLOW.md` |
| Context governance | `docs/ops/CONTEXT_GOVERNANCE.md` |
| Agent/player adapters | `docs/ops/AGENT_ADAPTERS.md` |
| Agent-first onboarding | `docs/ops/AGENT_FIRST_ONBOARDING.md` |
| Official-docs policy | `docs/ops/OFFICIAL_DOCS_POLICY.md` |
| Change impact | `docs/checklists/CHANGE_IMPACT.md` |
| ADR history | `docs/adr/` |

Add domain-specific owners only when a real domain emerges.

## Read next

### First discovery / uncertain workflow
1. `START_HERE.md`
2. `CAPABILITIES.md`
3. one file under `playbooks/`

### Product / discovery
1. `docs/contexts/PRODUCT.md`
2. relevant domain owner
3. `docs/templates/FEATURE_SLICE.md`

### Technical implementation
1. `docs/contexts/ARCHITECTURE.md`
2. `docs/contexts/STACK.md`
3. relevant code/tests

### Risky / cross-cutting
1. `docs/checklists/CHANGE_IMPACT.md`
2. affected canonical owners
3. relevant ADRs/contracts

### Operational / agents
1. `docs/ops/CONTEXT_GOVERNANCE.md`
2. `docs/ops/AGENT_ADAPTERS.md`

## Current hotspots / unknowns

- TBD.

## Validation

```bash
python tools/context_check.py
python tools/prepare_delivery.py
```

Project-specific commands are owned by `docs/contexts/QUALITY.md`.
