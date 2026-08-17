# Agent / Player Adapters

Canonical owner for player-specific configuration.

## Decision

Player-specific skills, steering and subagents are **adapters**.

Durable rules must not live only inside `.agents/skills/`, `.codex/agents/`, `.kiro/steering/`, `.kiro/skills/` or chat history.

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

## Optional Codex pack

When the `codex` pack is selected, it adds these read-only specialists:

- `repo-explorer`;
- `delivery-reviewer`;
- `docs-researcher`;
- `obvious-system-reviewer`.

They are advisory specialists, not canonical owners.

## Optional Kiro pack

When the `kiro` pack is selected, it follows these conventions:

- root `AGENTS.md` is supported;
- persistent steering lives under `.kiro/steering/`;
- workspace Agent Skills live under `.kiro/skills/`;
- foundational steering commonly includes `product.md`, `tech.md`, `structure.md`.

Kiro files remain thin and route back to canonical repository owners.

## Generic Agent Skills

`.agents/skills/` contains portable workflow guidance.

Project behavior must still be owned outside the skill.
