# Quality and Validation

Canonical owner for project-specific validation.

## Required checks by change type

| Change type | Focused validation | Broader validation |
|---|---|---|
| Docs only | links/context check | optional |
| Local logic | unit/focused test | project verify |
| UI | component/widget test | smoke/golden/e2e if relevant |
| API/contract | contract + focused integration | integration suite |
| Security/auth | focused security tests | full relevant suite + review |
| Dependency/stack | official docs + targeted spike | build/test/release check |
| Cross-cutting | affected suites | full verify |

Adapt this table to the actual stack.

## Canonical commands

Format:
```bash
TBD
```

Lint/static analysis:
```bash
TBD
```

Unit tests:
```bash
TBD
```

Integration/e2e:
```bash
TBD
```

Build:
```bash
TBD
```

Full verification:
```bash
TBD
```

## Bootstrap checks

```bash
python tools/context_check.py
python tools/prepare_delivery.py
```

## Test data / cleanup policy
TBD.

## Visual / manual validation
TBD.
