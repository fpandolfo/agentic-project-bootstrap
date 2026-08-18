# Agent / Player Adapters

Canonical owner for player-specific configuration.

## Decision

Player-specific skills, steering and subagents are **adapters**.

Durable rules must not live only inside `.agents/skills/`, `.codex/agents/`, `.kiro/steering/`, `.kiro/skills/` or chat history.

`START_HERE.md` is the universal player-independent activation contract. An
adapter may point to it or improve ergonomics, but must not redefine the core
workflow privately.

Durable owners belong in:

- `AGENTS.md`;
- canonical docs;
- ADRs;
- contracts/schemas;
- tests;
- deterministic tooling.

## Adapter policy

- Create/update the durable owner before player-specific guidance.
- Keep skills focused and short.
- Prefer subagents/reviewers as read-only by default.
- Do not promise commands or files that do not exist.
- If another player enters, add a parallel adapter rather than moving durable truth into that player.
- Remove an adapter when it creates more drift than leverage.

## Codex

Included read-only specialists:

- `repo-explorer`;
- `delivery-reviewer`;
- `docs-researcher`;
- `obvious-system-reviewer`.

They are advisory specialists, not canonical owners.

## Kiro

Current conventions used by this bootstrap:

- root `AGENTS.md` is supported;
- persistent steering lives under `.kiro/steering/`;
- workspace Agent Skills live under `.kiro/skills/`;
- foundational steering commonly includes `product.md`, `tech.md`, `structure.md`.

Kiro files remain thin and route back to canonical repository owners.

## Generic Agent Skills

`.agents/skills/` contains portable workflow guidance.

The `agent-first-bootstrap` skill routes supported players into the universal
new/adopt/evolve workflow without making the skill a canonical owner.

The `software-design-review` skill activates the Ousterhout-inspired design
review at meaningful module and architecture boundaries. Its durable owner is
`docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md`; the skill must remain a concise
adapter.

Project behavior must still be owned outside the skill.
