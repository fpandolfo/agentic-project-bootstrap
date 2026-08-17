# Product Context

## Problem

Coding agents can implement quickly, but projects lose reliability when durable
context, ownership, approval boundaries and validation exist only in chat or in
one vendor's configuration.

## Outcome

A human can bootstrap or adopt a repository, review exactly what will change,
apply it explicitly, and continue with any compatible coding agent while the
repository retains technical truth.

## Users

- product-minded builders acting as business owner, PO, architect or PM;
- individual developers using coding agents;
- teams standardizing agent-assisted delivery across repositories;
- maintainers creating reusable project and stack packs.

## MVP

- local CLI with no runtime dependencies;
- declarative manifest;
- built-in packs;
- deterministic plan/apply/verify;
- safe adoption of existing repositories;
- player-agnostic canonical owners;
- public contribution and security baseline.

## Non-goals

- replace an IDE or coding agent;
- host models, code or credentials;
- make product decisions for the human;
- execute production releases;
- silently rewrite user-owned files;
- provide an interactive wizard.

## Product principle

Execution can be agentic; product intent, material risk and acceptance remain
human-owned.
