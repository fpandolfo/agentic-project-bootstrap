# Agent-First Onboarding

Canonical owner for how an external agent consumes this suite.

## Decision

The primary interface is repository-readable guidance, not an installer.

```text
READ -> DISCOVER -> ASK -> PROPOSE -> APPROVE -> GENERATE -> OPERATE
```

`START_HERE.md` is universal and player-independent. Player adapters may route
to it but cannot replace it as the durable owner.

## Progressive disclosure

An agent should learn which capabilities exist without loading the full suite.

1. `START_HERE.md` establishes mode and safety.
2. `CAPABILITIES.md` exposes the menu of useful outputs.
3. One playbook defines the active sequence.
4. Canonical owners and templates are read only when relevant.
5. Code and project content are inspected selectively from target evidence.

This reduces context noise and prevents generic guidance from displacing actual
repository truth.

## Modes

- `NEW_PROJECT`: clarify intent and propose a minimal, reversible foundation;
- `ADOPT_PROJECT`: reconstruct existing truth and stage context adoption without
  changing behavior;
- `EVOLVE_PROJECT`: deliver an approved slice while keeping durable owners aligned.

Modes guide reasoning. They are not hidden execution states or mandatory CLI
configuration.

## Proposal discipline

Before writes, the agent must distinguish:

- **fact**: supported by target evidence or explicit human statement;
- **inference**: plausible interpretation that still needs confirmation;
- **unknown**: material missing information;
- **proposal**: a recommended choice with rationale and tradeoffs;
- **decision**: a proposal explicitly accepted by the appropriate human owner.

Generated docs must not collapse those categories.

## Minimal generation rule

Every proposed artifact must answer:

1. Which recurring question will this own?
2. Why is an existing file not already the owner?
3. How will a future agent discover it?
4. What evidence or decision will keep it current?

If those answers are weak, do not generate the artifact.

## Tool boundary

Initial structural discovery may inspect names, paths and filesystem structure.
It must not:

- read sensitive file contents;
- execute target project commands;
- follow symlinks;
- traverse dependency/build/cache directories;
- inspect unrelated user or machine configuration;
- write to the target without an explicit output request.

Deeper content inspection happens afterward, selectively, within the target and
under the active task scope.

## Optional deterministic application

The manifest/plan/apply/verify CLI remains useful when a human wants exact file
diffs, conflict protection and fingerprint approval. It is one application
mechanism, not a prerequisite for learning or using the suite.
