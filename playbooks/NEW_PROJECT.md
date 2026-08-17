# Playbook — NEW_PROJECT

Use for an idea, empty repository or project that has not committed to an
implementation direction.

## Goal

Turn human intent into an approved, minimal and reversible project foundation.

## Sequence

1. Capture the idea in the human's language.
2. Ask about problem/outcome, users, business rules, constraints and acceptance.
3. Separate confirmed requirements from hypotheses and open questions.
4. Propose MVP, non-goals, happy path, unhappy path and relevant edge cases.
5. Present architecture and stack options with tradeoffs. Do not select merely
   because one option is familiar to the agent.
6. Propose only useful diagrams and ADR candidates.
7. Define the smallest evidence that would validate the first slice.
8. Ask for approval on product behavior, stack/architecture, privacy/security,
   external services, irreversible setup and delivery authority.
9. Generate the approved minimal context and first work slice.
10. Implement only when explicitly requested or when implementation is part of
    the approved task.

## Suggested initial artifacts

- `docs/contexts/PRODUCT.md`;
- `docs/contexts/ARCHITECTURE.md` when a real boundary exists;
- `docs/contexts/STACK.md` after a choice is approved;
- `docs/contexts/QUALITY.md`;
- one diagram when it clarifies the core flow;
- an ADR only for a consequential choice;
- one feature slice.

## Avoid

- speculative infrastructure;
- exhaustive documentation before information exists;
- choosing tools without tradeoff discussion;
- treating inferred requirements as accepted business rules;
- creating code before the human can recognize the intended product.
