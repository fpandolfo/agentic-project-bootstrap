# Context Governance

Canonical owner for keeping agent context small, current and trustworthy.

## Goal

A clean-context agent should not need to read the entire repository.

## Rules

- Keep `AGENTS.md` thin and operational.
- Keep `docs/PROJECT_INDEX.md` navigational.
- Put durable detail in one canonical owner.
- Link to owners instead of repeating decisions.
- Do not use chat history as the only owner of a decision.
- Treat tests as executable documentation.
- Add generated lookup/report surfaces only after enough complexity exists to justify them.

## When to create a new doc owner

Create one when:

- a stable domain has accumulated enough rules to deserve independent navigation;
- the same decision is being repeated;
- agents repeatedly rediscover the same dependency;
- change amplification shows ownership is unclear.

Do **not** create a doc merely because folder symmetry looks nicer.

## Generated docs

This bootstrap does not create `docs/generated/` by default.

If generated context is later justified:

- give it a deterministic source;
- do not make it the only source of truth;
- provide one regeneration/check command;
- do not edit generated output manually.

## Context check

```bash
python tools/context_check.py
```

This validates structural prerequisites and unresolved bootstrap tokens. It does not replace project tests.
