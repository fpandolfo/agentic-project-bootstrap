# Bootstrap Provenance

This package is a generic synthesis of patterns proven useful in disciplined agent-assisted repositories.

## Patterns retained

- one operational entrypoint (`AGENTS.md`);
- one master navigation/current-state owner (`docs/PROJECT_INDEX.md`);
- trust order when sources conflict;
- minimum-context task routing;
- reasoning-effort triage;
- explicit MVP / happy / unhappy / edge-case mapping;
- strategic programming / deep-module bias;
- `MAP -> IMPLEMENT -> VALIDATE -> CLOSE`;
- canonical owners instead of repeated decisions;
- thin player adapters;
- read-only specialist reviewers;
- current official docs for changing external facts;
- deterministic context validation.

## Patterns intentionally not copied

- product-specific domains;
- stack-specific build commands;
- Jira-specific assumptions;
- generated-doc machinery before it is needed;
- CI/deploy infrastructure before a real target exists;
- a full delivery engine embedded into every consumer repo.

## Kiro compatibility assumptions

Verified against official Kiro documentation on 2026-08-08:

- AGENTS.md support;
- `.kiro/steering/`;
- foundational steering (`product.md`, `tech.md`, `structure.md`);
- `.kiro/skills/<skill>/SKILL.md`;
- Agent Skills progressive disclosure.

References:

- https://kiro.dev/docs/cli/steering/
- https://kiro.dev/docs/skills/
- https://kiro.dev/docs/cli/skills/

## Design intent

Delete, merge or simplify bootstrap surfaces when they stop paying rent.

The objective is not repository symmetry. The objective is an obvious system that a clean-context agent can safely continue.
