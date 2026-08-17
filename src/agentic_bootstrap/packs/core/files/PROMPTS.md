# Activation Prompts

These prompts are starting points. Adapt language and constraints to the project.

## New project

```text
Read START_HERE.md from Agentic Project Bootstrap and use NEW_PROJECT mode.

My idea or desired outcome is:
[describe it here]

Do not implement product code yet. Conduct discovery, separate facts from
assumptions, and ask the questions needed to clarify users, business rules,
MVP, non-goals, risks and acceptance.

Then propose the minimum useful project context, architecture options, Mermaid
diagrams, ADRs, tooling and first delivery slice. Wait for approval on material
decisions before generating or changing project files.
```

## Existing project

```text
Read START_HERE.md from Agentic Project Bootstrap and use ADOPT_PROJECT mode on
the current repository.

Start with read-only structural discovery. Do not change behavior or execute
project commands yet.

Identify the apparent product purpose, stack, architecture, tests, pipelines,
existing decisions, business-rule evidence, missing context, contradictions and
risks. Label inference explicitly. Ask me for product intent that the repository
cannot prove.

Propose a staged adoption plan that preserves existing owners and avoids
documentation or tooling created only for symmetry. Wait for approval before
writing files.
```

## Evolve an understood project

```text
Read START_HERE.md and use EVOLVE_PROJECT mode.

Requested outcome:
[describe the change]

Map the smallest coherent slice, affected owners, business rules, happy path,
unhappy path, relevant edge cases, risks, human gates and validation. Show the
plan and material decisions before implementation. Keep canonical context,
diagrams and ADRs aligned with the resulting behavior.
```

## Architecture review only

```text
Use the Agentic Project Bootstrap capability catalog for an architecture review.
Do not implement changes.

Map current components, boundaries, dependencies and critical flows from
repository evidence. Produce only the Mermaid diagrams that materially improve
understanding. Identify facts, inferences, risks, decision candidates and ADRs
that would be justified. Ask before turning a proposal into canonical truth.
```

## Context refresh only

```text
Use the Agentic Project Bootstrap context-governance guidance.

Compare code, tests, contracts and current docs. Find stale, duplicated,
contradictory or missing owners. Propose the smallest context refresh that lets
a clean-context agent resume accurately. Do not invent product intent and do not
rewrite unrelated documentation.
```
