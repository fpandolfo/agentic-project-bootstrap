# Agentic Delivery Lifecycle

This guide expands the universal operating contract into an end-to-end delivery
reference. It is a menu, not a mandatory stage-gate process.

Use only the phases and evidence proportional to the product, risk and current
slice.

## Lifecycle

| Phase | Agent contribution | Human authority | Useful evidence |
|---|---|---|---|
| Frame | Restate the problem, users, outcome and constraints. | Own purpose, priority and business rules. | Product brief, unknowns, non-goals. |
| Discover | Inspect structure and relevant sources; separate facts from inference. | Clarify intent the repository cannot prove. | Discovery brief, current-state map. |
| Decide | Present alternatives, trade-offs and reversible first steps. | Approve material product, architecture, privacy and cost decisions. | Decision record or ADR when justified. |
| Design | Model critical flows, contracts, states and visual direction. | Accept behavior and experience. | Small diagrams, prototypes, contract sketches. |
| Slice | Define the smallest coherent outcome and its failure modes. | Confirm MVP and acceptance. | Feature slice with happy path, unhappy path and edge cases. |
| Implement | Change code, tests and affected canonical owners. | Resolve newly discovered material ambiguity. | Focused diff and executable tests. |
| Validate | Run checks closest to the actual risk, then broader gates. | Accept residual risk and user-visible behavior. | Automated, visual, integrated and manual evidence. |
| Release | Prepare rollback, production configuration and operational handoff. | Authorize irreversible or external actions. | Release checklist, deployment evidence, rollback path. |
| Observe and learn | Inspect outcomes, drift and repeated friction. | Decide whether learning changes product or shared guidance. | Baseline, follow-up, sanitized reusable learning. |

These phases fit inside the primary contract:

```text
READ -> DISCOVER -> ASK -> PROPOSE -> APPROVE -> GENERATE -> OPERATE
```

## Validation ladder

Choose the lowest layer that proves the risk, then add higher layers only when
they prove something different.

1. **Deterministic local evidence** — unit, component, widget or domain tests
   with small fixtures.
2. **Contract and cross-layer evidence** — API schema, consumer/provider checks,
   integration tests or drift guards.
3. **Visual evidence** — focused snapshots, golden tests, responsive screenshots
   or accessibility inspection for stable high-value surfaces.
4. **Integrated smoke evidence** — a canonical user journey across real
   components with controlled data.
5. **Environment evidence** — deployment, network, authentication, container,
   browser or physical-device validation.
6. **Production evidence** — health, indexing, observability, business outcome
   or another explicitly approved post-release signal.

Fixtures and remote environments are complementary. Use deterministic fixtures
for regression and fast iteration; use staging, browsers or devices to prove
network, packaging, deployment and real integration behavior. CI should not
depend on a personal or unreliable environment for its canonical regression
signal.

## Consolidated behavior gate

Before changing behavior already supported by code, tests and durable context:

1. reconstruct the current behavior from the strongest sources;
2. show the human what currently happens and where it is proven;
3. explain the impact of the proposed replacement;
4. obtain explicit approval before changing behavior or visual baselines.

Active refinement within the same unaccepted slice can remain lightweight. The
gate becomes important after a behavior is treated as stable input to later work.

## Context maintenance

- Keep a thin operational entry point and a navigational project index.
- Generate factual maps only when repeated discovery or drift justifies them.
- Never make generated reports the sole owner of a business rule.
- Record accepted gaps with an owner and a revisit condition.
- Update diagrams, ADRs and context only when durable truth changed.
- End meaningful work with validation evidence, intentional non-goals and a
  clean-context continuation point.
