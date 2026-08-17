# Product Context

## Problem

Coding agents can implement quickly, but a human often has to teach each new
session how to understand the project, which questions to ask, what artifacts
are useful and where decisions belong. Existing solutions also tend to couple
the workflow to one player or turn a flexible practice into a rigid wizard.

## Outcome

A human can point any capable coding agent at one universal entry point. The
agent discovers the idea or repository, asks for missing product intent,
proposes useful context/architecture/tooling, waits at material human gates and
leaves durable project truth that another clean-context agent can resume.

## Users

- product-minded builders acting as business owner, PO, architect or PM;
- individual developers using coding agents;
- teams standardizing agent-assisted delivery across repositories;
- maintainers extending reusable guidance, templates and optional adapters.

## MVP

- universal `START_HERE.md` contract;
- discoverable capability catalog and copy/paste prompts;
- `NEW_PROJECT`, `ADOPT_PROJECT` and `EVOLVE_PROJECT` playbooks;
- safe read-only structural discovery;
- guided generation of contexts, Mermaid diagrams and ADRs;
- player-agnostic canonical owners;
- optional deterministic plan/apply/verify tooling;
- public contribution and security baseline.

## Non-goals

- replace an IDE or coding agent;
- host models, code or credentials;
- make product decisions for the human;
- execute production releases;
- silently rewrite user-owned files;
- provide an interactive wizard.
- require installation before an agent can use the guidance;
- force every project to adopt every document, diagram or tool;
- treat an agent proposal as an approved product decision.

## Product principle

The pack teaches an agent how to find its way and offer well-supported options.
Execution can be agentic; product intent, business rules, material risk and
acceptance remain human-owned.
