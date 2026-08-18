---
name: software-design-review
description: Review meaningful implementation, architecture and refactoring for cognitive load, change amplification, information hiding, module depth, shallow interfaces and duplicated ownership. Use before creating or splitting modules, services, adapters, widgets, layers or canonical docs, and when a change feels harder to understand than its product scope suggests.
---

# Software Design Review

1. Read `docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md` and
   `docs/checklists/SOFTWARE_DESIGN.md`.
2. Identify the current owner, public interface and complexity that should be
   hidden by the affected boundary.
3. Check cognitive load, change amplification, information leakage and important
   dependencies that are difficult to discover.
4. Prefer making an existing owner deeper when it already owns the concept.
5. Reject pass-through layers, generic buckets and splits based only on file
   length unless they hide a stable responsibility.
6. Compare at least two plausible designs for consequential boundaries; report
   trade-offs and human decisions before implementation.
7. Validate the public behavior of the boundary rather than coupling tests to
   internal wiring.
8. Record intentional tactical shortcuts with residual risk and a revisit trigger.

Do not claim quality from pattern names, layer count, line count or generated
consistency. The canonical guidance explicitly applies ideas from John
Ousterhout's *A Philosophy of Software Design*; this skill is only an adapter.
