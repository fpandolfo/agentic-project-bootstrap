# Start Here — Agentic Project Bootstrap

Universal entry point for any capable coding agent or human using this suite.

This pack is a **guide and capability library**. It does not replace product
judgment, impose a stack or make final decisions for the human.

## Operating contract

Use this sequence:

```text
READ -> DISCOVER -> ASK -> PROPOSE -> APPROVE -> GENERATE -> OPERATE
```

Do not begin implementation merely because it is technically possible.

## First activation

1. Identify the target project. It may be this directory or another directory
   the human explicitly placed in scope.
2. Confirm one mode:
   - `NEW_PROJECT`: idea, empty repository or pre-implementation discovery;
   - `ADOPT_PROJECT`: an existing repository with code, docs or delivery history;
   - `EVOLVE_PROJECT`: an already-understood project receiving a new slice.
3. Run structural discovery without changing the target:

   ```bash
   python3 tools/discover_project.py --target /path/to/project --format markdown
   ```

4. Read `CAPABILITIES.md` and only the playbook for the confirmed mode.
5. Inspect target content selectively. Never read credential files, unrelated
   user configuration, dependency caches or private material outside scope.
6. Separate facts, inferences, unknowns and proposals.
7. Ask the human for missing product intent, business rules and material choices.
8. Propose the smallest useful set of artifacts and changes.
9. Wait for human approval at material product, architecture, privacy, destructive
   or release gates.
10. Generate or update only what the project needs, then validate and hand off.

## First response contract

Before writing project files, return a concise discovery brief containing:

- confirmed target and mode;
- observed facts with repository evidence;
- inferred possibilities clearly labeled as inference;
- important unknowns;
- questions for the human;
- proposed artifacts and why each one is useful;
- decisions requiring approval;
- recommended next step.

## Progressive reading

Do **not** read the full suite by default.

- New idea or empty repository: `playbooks/NEW_PROJECT.md`
- Existing repository: `playbooks/ADOPT_PROJECT.md`
- New feature or meaningful change: `playbooks/EVOLVE_PROJECT.md`
- Available tools, templates and outputs: `CAPABILITIES.md`
- Copy/paste activation prompts: `PROMPTS.md`
- Durable context rules: `docs/ops/CONTEXT_GOVERNANCE.md`
- Meaningful implementation/refactoring: `docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md`
- Available and candidate tooling: `TOOLING.md`
- Player-specific integration: `docs/ops/AGENT_ADAPTERS.md`

## Human ownership

The human owns product purpose, priority, business rules, risk acceptance,
irreversible choices and final acceptance. The agent owns discovery support,
options, implementation, validation, documentation and evidence within the
approved scope.

When the human has not decided, preserve the uncertainty. Do not manufacture
consensus or encode a convenient guess as project truth.
