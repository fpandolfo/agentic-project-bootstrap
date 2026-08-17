# Delivery Workflow

Canonical owner for how meaningful work moves through the repository.

## Core loop

```text
MAP -> IMPLEMENT -> VALIDATE -> CLOSE
```

## 1. Map

Before heavy implementation, establish a compact slice snapshot.

For new behavior:

- problem/outcome;
- hypothesis;
- MVP;
- non-goals;
- happy path;
- unhappy path;
- edge cases;
- owners touched;
- risks;
- validation.

Use `docs/templates/FEATURE_SLICE.md`.

For a narrow bug, keep the map proportional: reproduction, expected behavior, observed behavior, likely owner and regression validation.

## 2. Implement

- prefer the nearest deep owner;
- do not create a new abstraction before checking whether an existing owner can deepen;
- avoid reopening broad discovery unless new ambiguity appears;
- update tests alongside behavior;
- distinguish current state from target state.

## 3. Validate

### Entry
Reconstruct current behavior from code/tests/docs.

### During
Run the smallest anchor test/check proving the edited slice.

### Exit
Run the validation closest to real delivery risk.

Cross-cutting changes justify broader validation.

## 4. Close

Record:

- what changed;
- validation performed;
- docs/contracts updated;
- what intentionally stayed out;
- residual risks;
- follow-up work.

## Stateful commands

Run state-dependent or destructive commands serially and inspect each result: migrations, production deploys, golden updates, shared test data, release/tag operations and Git `add -> commit -> push`.

## Work-tracker policy

The repository is tracker-agnostic.

Whether the team uses GitHub Issues, Jira, Linear or another tool:

- tracker records intent, status and closeout;
- repository remains technical truth;
- compare tracker vs code/docs at task start;
- update stale intent before implementing a materially different scope.
