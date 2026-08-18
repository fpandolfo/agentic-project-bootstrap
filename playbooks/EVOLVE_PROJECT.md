# Playbook — EVOLVE_PROJECT

Use when the project is understood and the human requests a feature, fix,
refactor, operational change or documentation refresh.

## Goal

Deliver the smallest coherent outcome while keeping implementation, tests,
context and decisions aligned.

## Sequence

1. Restate the requested outcome and acceptance in product language.
2. Read the minimum canonical owners routed by `docs/PROJECT_INDEX.md`.
3. Map the slice: MVP, non-goals, happy path, unhappy path, relevant edge cases,
   dependencies, owners, risks and validation.
4. Apply `docs/checklists/SOFTWARE_DESIGN.md`: identify the complexity to hide,
   test whether an existing owner can become deeper and reject shallow layers.
5. Identify decisions that require human input before implementation.
6. Implement within the approved boundary.
7. Run focused checks, then broader checks proportional to blast radius.
8. Update canonical context, diagrams or ADRs only when durable truth changed.
9. Close with evidence, intentional non-goals, residual risks and follow-ups.

## Diagram and ADR triggers

Update a diagram when component relationships, interaction order, states or data
relationships changed materially. Create or supersede an ADR when a consequential
decision and its tradeoffs must survive chat history.

## Avoid

- expanding the task because nearby improvements are attractive;
- documenting transient implementation details as architecture;
- using generated prose as evidence instead of tests or executable behavior;
- silently deciding product behavior for the human.
