# CI and Delivery Gates

Use this guide to turn project-owned validation into a low-privilege remote
signal without making CI the only place a developer or agent can understand a
failure.

## Local-first rule

Every required remote check should have a documented local equivalent.

```text
focused checks -> project verify -> delivery wrapper -> remote workflow
```

- Focused checks give fast feedback while implementing.
- `verify` or its equivalent aggregates stable project quality rules.
- The delivery wrapper adds context checks, cleanup and Git-state visibility.
- CI installs a clean environment and calls those project-owned commands.

Do not duplicate business or quality logic in workflow YAML when a tested local
script can own it.

## Separate concerns

Projects may need independent gates for:

- product quality: compile, typecheck, lint, unit and integration tests;
- context governance: generated evidence, links, drift and known gaps;
- supply chain: locked dependencies and security policy;
- packaging: application bundles, containers or static artifacts;
- deployment: external state change with environment authority;
- observation: health, logs, indexing or another post-release signal.

Keep deployment separate from ordinary quality checks. A pull request should not
receive production credentials merely because it needs to run tests.

## Workflow safety

- Declare permissions explicitly and start with read-only contents.
- Add write scopes only for a concrete job that needs them.
- Do not expose deployment secrets to untrusted pull-request code.
- Pin runtime and action versions according to current official documentation.
- Keep credentials in the platform's secret store, never in fixtures or docs.
- Treat contributed workflow and pack content as untrusted input.
- Prefer artifacts or job summaries over automated write-comments when a
  read-only result is sufficient.

Version-sensitive security and platform choices require current official-source
research before implementation.

## Selective execution

Path- or scope-based selection can reduce cost, but preserve an understandable
required-check contract. A required workflow that is entirely skipped by path
filters can remain pending on some platforms.

Safer options include:

- always start the workflow and make expensive jobs conditional;
- expose separate required checks with stable names;
- keep a cheap universal precheck that selects and reports affected scopes.

The local full verification command remains the fallback when selection is
ambiguous.

## Stateful validation

Run stateful or artifact-producing steps in series when one result affects the
next. Examples include golden updates, database integration, generated context,
container deployment, remote observation and Git publication.

Parallelize independent read-only or deterministic checks only when doing so
does not make failure diagnosis or shared state unreliable.

## Delivery closeout

A meaningful delivery should report:

- behavior changed;
- focused and broad validation executed;
- generated or durable context updated;
- manual, visual, browser or device evidence when relevant;
- intentional non-goals;
- residual risks and accepted known gaps;
- external actions performed and rollback path;
- clean or explicitly understood Git state.
