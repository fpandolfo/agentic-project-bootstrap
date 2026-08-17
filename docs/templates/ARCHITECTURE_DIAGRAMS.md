# Architecture Diagrams — [Project]

Use only the sections that improve understanding. Delete unused examples.

## System/component flow

```mermaid
flowchart LR
    User[User or external actor] --> Entry[Product entry point]
    Entry --> Core[Core capability]
    Core --> Store[(Durable state)]
```

Explain scope, boundaries and any inference that still needs confirmation.

## Critical interaction

```mermaid
sequenceDiagram
    actor User
    participant Product
    participant Dependency
    User->>Product: Intent or action
    Product->>Dependency: Validated request
    Dependency-->>Product: Result
    Product-->>User: Outcome
```

## Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Proposed
    Proposed --> Approved: human decision
    Approved --> Implemented: validated delivery
    Implemented --> [*]
```

## Diagram rules

- Prefer the smallest diagram that answers a real question.
- Keep business rules in canonical prose/tests as well as explanatory diagrams.
- Label proposals and inferences; do not render them as accepted current state.
- Update or remove a diagram when its owner changes.
- Avoid decorative complexity, undocumented colors and layout-only duplication.
