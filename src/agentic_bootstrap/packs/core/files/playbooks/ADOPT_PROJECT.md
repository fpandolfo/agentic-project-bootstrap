# Playbook — ADOPT_PROJECT

Use for a repository that already contains code, documentation, tests or
delivery history.

## Goal

Recover current truth, expose important unknowns and add only the guidance that
makes future agent-assisted work safer and easier to resume.

## Sequence

1. Run `tools/discover_project.py` against the target.
2. Inspect existing instructions, README, manifests, source roots, tests and CI.
3. Reconstruct behavior from code/tests before trusting summaries.
4. Identify existing canonical owners and preserve them.
5. Separate observed facts, likely inferences, contradictions and unknowns.
6. Ask the human for product purpose, priorities and business rules that the
   repository cannot prove.
7. Map major components, dependencies, data and critical user/system flows.
8. Propose a staged context plan; explain the value of every new artifact.
9. Use explicit preservation when an installer would collide with existing files.
10. Validate that no behavior changed during the adoption-only pass.

## Discovery brief

Report:

- what the repository demonstrably does;
- candidate stacks and entry points;
- test and delivery evidence;
- existing docs, diagrams and ADRs;
- security/privacy-sensitive surfaces;
- missing or contradictory owners;
- material questions for the human;
- recommended adoption slices.

## Avoid

- rewriting established files for stylistic consistency;
- executing unknown project scripts during initial discovery;
- reading secrets or user-machine configuration;
- broad refactors mixed into context adoption;
- claiming inferred product intent as fact.
