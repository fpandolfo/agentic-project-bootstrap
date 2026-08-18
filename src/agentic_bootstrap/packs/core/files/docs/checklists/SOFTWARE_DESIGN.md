# Software Design Checklist

Use for meaningful implementation, architecture work and refactoring. It is
inspired by John Ousterhout's *A Philosophy of Software Design* and routes to
`docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md` for the full guidance.

## Complexity

- [ ] What complexity should this change hide?
- [ ] Does it reduce cognitive load for the next change?
- [ ] Does it reduce or contain change amplification?
- [ ] Are important dependencies discoverable before failure?

## Module depth

- [ ] Is the interface smaller and more stable than the implementation?
- [ ] Can an existing owner become deeper instead of adding a wrapper?
- [ ] Does each new layer contribute a different abstraction?
- [ ] Is the boundary based on a stable concept rather than file length?

## Information hiding

- [ ] Does one owner contain each durable decision?
- [ ] Are storage, provider, transport and configuration details kept internal?
- [ ] Are callers free from duplicated conditionals or synchronized knowledge?
- [ ] Does private knowledge stay hidden from getters, data shapes and required
      call sequences as well as from public signatures?
- [ ] Did we avoid a new generic bucket with unrelated responsibilities?

## Temporal decomposition

- [ ] Are boundaries organized around owned knowledge rather than only execution
      order?
- [ ] Can each stage change without another stage needing the same hidden rule?
- [ ] Are any methods, classes or documents always called, tested or changed
      together because they are artificially separated?
- [ ] Would merging them create a deeper owner with a smaller interface?
- [ ] If shared knowledge was extracted, does the new owner hide it rather than
      republish it through a shallow interface?
- [ ] If a staged pipeline remains, do its stages own different information and
      communicate through stable contracts?

## Strategic design

- [ ] Were at least two plausible designs considered for a consequential boundary?
- [ ] Is any extra investment tied to a concrete complexity or expected change?
- [ ] Did we avoid speculative framework or abstraction work?
- [ ] Is a tactical shortcut documented with its residual risk and revisit trigger?

## Obviousness and validation

- [ ] Can a clean-context agent find the owner through the project index?
- [ ] Are current state and target state clearly separated?
- [ ] Do names and interfaces reveal the correct abstraction?
- [ ] Do tests validate public behavior without excessive internal wiring knowledge?
- [ ] Were canonical docs updated only when durable truth changed?
