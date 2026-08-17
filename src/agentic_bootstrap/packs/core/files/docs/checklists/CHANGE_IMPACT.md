# Change Impact Checklist

Use for meaningful, risky or cross-cutting work.

## Product / behavior

- [ ] User-visible/business behavior changed?
- [ ] Expected behavior canonically documented?
- [ ] Explicit human approval required?
- [ ] Happy path, unhappy path and edge cases understood?

## Ownership / architecture

- [ ] Which file/module owns the rule?
- [ ] Am I creating a second owner?
- [ ] Does this increase change amplification?
- [ ] Can an existing module become deeper instead of adding a wrapper?
- [ ] Does target-state documentation accidentally describe unimplemented behavior as current?

## Contracts / data

- [ ] API/schema/storage contract impact?
- [ ] Backward compatibility?
- [ ] Migration/rollback needed?
- [ ] Data-loss risk?
- [ ] External integration impact?

## Security / privacy

- [ ] Authentication/authorization impact?
- [ ] New untrusted input?
- [ ] Secrets/PII handling?
- [ ] Logging/redaction impact?
- [ ] Current official docs checked where needed?

## Validation

- [ ] Focused tests identified?
- [ ] Integration/e2e needed?
- [ ] Manual/visual/device validation needed?
- [ ] Full verification justified?
- [ ] Cleanup of debug/generated artifacts planned?

## Docs / operations

- [ ] Canonical owner updated?
- [ ] ADR needed?
- [ ] Work item still matches implemented scope?
- [ ] Residual risk/follow-up explicit?
