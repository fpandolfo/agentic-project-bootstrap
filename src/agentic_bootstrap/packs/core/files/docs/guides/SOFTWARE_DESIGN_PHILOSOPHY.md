# Software Design Philosophy

This project explicitly draws on John Ousterhout's *A Philosophy of Software
Design*. The book's ideas are used here as practical guardrails for human-agent
software delivery, not as a claim of affiliation, endorsement or an official
interpretation of the author's work.

The central application is simple: agent speed is valuable only when the
resulting system stays easy to understand and change.

## Design outcome

Prefer systems where a future human or clean-context agent can make a meaningful
change by understanding a small number of stable concepts and interfaces.

Evaluate design pressure through three observable costs:

- **cognitive load**: how much must be understood before making a safe change;
- **change amplification**: how many places must change for one product decision;
- **unknown unknowns**: important dependencies or consequences that are hard to
  discover before they fail.

The goal is not the fewest files, layers or lines. The goal is to hide meaningful
complexity behind clear ownership and small interfaces.

## Default heuristics

### Prefer deep modules

A strong module exposes a small, stable interface while owning substantial
policy, state, validation or coordination internally.

Before adding a module, wrapper, service, widget, adapter or document, ask:

- What complexity will this boundary hide?
- Is its public interface smaller and more stable than its implementation?
- Can an existing owner become deeper instead of adding another forwarding
  layer?
- Is the boundary based on a stable concept or merely current file size?

Avoid shallow wrappers that rename or forward another interface without hiding a
real decision.

### Hide information and prevent leakage

Keep a decision in one owner whenever possible. Callers should not need to know
storage layout, transport details, provider quirks, brand selection rules or
internal workflow states unless those are part of the caller's real contract.

Repeated conditionals, duplicated configuration and synchronized edits across
unrelated surfaces are signals that information has leaked.

Access control is not sufficient evidence of information hiding. A private field
can still leak its design knowledge through getters, setters, exposed internal
data shapes, required call sequences or multiple modules that independently
understand the same rule. Look for knowledge that must change together even when
no public signature exposes it.

### Organize around knowledge, not time

Question **temporal decomposition**: splitting a capability into modules merely
because their operations happen at different times. A read, parse, transform and
write sequence may look orderly while forcing several modules to understand the
same format, state transition or policy. The result is information leakage and
modules that are independent in name only.

Methods or modules are **conjoined** when callers must invoke them in a particular
order, or when they must routinely be understood, tested or changed together
because they share hidden knowledge. Prefer boundaries around the knowledge and
decisions a module owns, not around the chronological steps in one execution.

When conjoined boundaries appear, compare at least these remedies:

1. merge closely related parts into one deeper owner that performs the complete
   operation behind a smaller interface;
2. extract the shared knowledge into a dedicated owner only if it can hide the
   details behind a meaningfully simpler interface.

Do not replace implicit coupling with a shallow coordinator that republishes the
same knowledge. A staged pipeline remains reasonable when stages own genuinely
different information, communicate through stable contracts and can be changed
or reused independently.

### Keep layers at different abstractions

Every layer should contribute a distinct responsibility. A controller, service,
repository and adapter that only forward identical parameters do not become a
good architecture merely because conventional names exist.

Prefer thin orchestration over broad interfaces, but keep domain policy inside a
deep owner rather than scattering it through leaves and entry points.

### Invest strategically

For durable or high-change surfaces, compare at least two plausible designs and
spend time reducing the interface before broad implementation. A slightly slower
first slice can be worthwhile when it makes later slices safer and smaller.

Do not use strategic design as permission for speculative frameworks. The
investment must address a concrete source of complexity or likely change.

### Make the system obvious

- Give each durable rule one canonical owner.
- Use entry points and indexes to route, not repeat deep decisions.
- Make important dependencies visible in contracts, tests, diagrams or context.
- Use consistent names for the same concept.
- Separate current state from proposed target state.
- Prefer predictable behavior over clever compression.

Comments and documentation should explain intent, invariants, trade-offs and
non-obvious constraints. They should not translate straightforward code line by
line or become a second implementation.

## Agent operating contract

Before meaningful implementation or refactoring, the agent should:

1. identify the current owner and interface of the affected behavior;
2. name the knowledge, decisions and complexity the proposed design should hide;
3. check whether shared knowledge leaks across public or private boundaries;
4. reject chronological splits whose parts must be called or changed together;
5. check whether the change increases cognitive load or change amplification;
6. compare alternatives for consequential boundaries;
7. prefer making an existing module deeper when it already owns the concept;
8. avoid adding pass-through layers, generic buckets or parallel sources of truth;
9. design validation around the public behavior of the boundary;
10. record a trade-off when a tactical shortcut is intentionally accepted.

The agent must not claim a design is good merely because it uses a familiar
pattern, has many layers, reduces line count or was generated consistently.

## Human decision points

Ask the human before a design choice when it materially changes:

- product behavior or business ownership;
- a public contract or data boundary;
- long-term coupling, migration cost or reversibility;
- security, privacy, cost or operational responsibility;
- a previously accepted architecture direction.

The agent can recommend. The human remains the decision authority.

## Review signals

Question the design when:

- a simple feature requires synchronized edits across many owners;
- a new layer has almost the same interface as the layer below it;
- callers repeat knowledge that should be internal to a module;
- private modules duplicate a format, policy or state transition without an
  explicit shared contract;
- sequential methods or classes must always be called, tested or changed together;
- module boundaries mirror execution order even though the stages share the same
  knowledge;
- a generic `utils`, `helpers`, `common` or `manager` surface accumulates unrelated
  responsibilities;
- internal data structures escape into many consumers;
- documentation repeats rules instead of linking to one owner;
- tests require excessive knowledge of internal wiring;
- a clean-context agent must read a large part of the repository to change one
  bounded behavior.

Use `docs/checklists/SOFTWARE_DESIGN.md` during mapping and review. These are
reasoning guardrails; they are not mechanically provable style rules.

## Attribution

Primary influence:

- John Ousterhout, *A Philosophy of Software Design*.

This project applies the book's design philosophy to agent-led delivery and will
keep this attribution explicit in public cases and guidance derived from that
practice.
