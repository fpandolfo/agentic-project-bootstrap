# Project Relay — Agent-Led Mobile and API Delivery

Project Relay is a fictional public identity for a sanitized real-project case.
Product names, business domain, routes, API models, integrations, brands,
infrastructure and deployment details were removed or generalized. This is not a
public replica of the private application.

## What this case demonstrates

A human acting as product owner and decision authority can guide capable agents
through product discovery, architecture, design, implementation, validation and
operation of a substantial mobile/API product without personally authoring the
product code.

## Evidence boundary

### Privately verified

A read-only review of the current private repository observed:

- a Flutter/Dart mobile application and Kotlin/Spring API in one monorepo;
- PostgreSQL persistence and an OpenAPI contract between app and API;
- structural discovery across 715 files;
- 52 Flutter test files, 27 Kotlin test files and 13 golden-related test or
  baseline files;
- 13 accepted ADR files and six GitHub Actions workflow definitions;
- generated maps for routes, endpoints, dependencies, flows, contracts, drift
  and test coverage;
- local wrappers for app, API, context, golden, smoke and delivery validation;
- containerized backend operation, remote staging and physical-device flows;
- distribution-specific branding and behavior behind shared product boundaries.

Those counts describe one inspected revision. They are evidence of delivery
depth, not a target metric for other projects.

### Owner-reported

The product owner reports that:

- agents produced the product journey end to end, including architecture,
  prototypes, design work, pipelines, backend, frontend, builds and tests;
- the owner made product and business decisions but did not write the product
  code;
- the measured delivery scope reached complete unit-test coverage and included
  golden tests plus validation on a real device.

These outcomes are intentionally labeled owner-reported because the private
coverage and device evidence are not published with this case.

## Delivery journey

1. Establish a thin agent entry point, a project index and a source-of-truth
   order for code, API contract, context, design and backlog.
2. Turn product intent into bounded slices with happy path, unhappy path, edge
   cases and explicit human decisions.
3. Model app/API boundaries in OpenAPI before allowing the two sides to drift.
4. Implement vertical slices across mobile, API, persistence and documentation.
5. Generate small factual maps from the repository instead of asking every new
   agent to rediscover routes, endpoints and cross-layer contracts.
6. Validate locally with deterministic fixtures, unit/widget tests, contract
   checks, focused goldens and an integrated smoke journey.
7. Use remote staging and a physical device only for the risks they uniquely
   prove: packaging, network, authentication, deployment and real interaction.
8. Preserve stable behavior with a human confirmation gate before replacing
   validated flows or visual baselines.

## Transferable patterns

| Pattern | Problem it solved | Reuse boundary |
|---|---|---|
| Thin entry point plus project index | New sessions were expensive and inconsistent. | Universal; keep detailed truth in deeper owners. |
| Explicit trust order | Backlog, design, docs and implementation could disagree. | Adapt the sources and order to each project. |
| Vertical delivery slices | App and API work could grow into disconnected horizontal layers. | Universal for meaningful cross-layer behavior. |
| Contract crosswalk and drift maps | Interface changes were easy to miss. | Use only when a real cross-layer contract exists. |
| Focused golden tests | Visual regression needed evidence without snapshot overload. | Freeze stable, high-value surfaces rather than every screen. |
| Fixture/staging split | Remote environments were useful but too slow and stateful for regression. | Deterministic local evidence first; environment evidence second. |
| Validated-behavior gate | A new request could accidentally replace accepted behavior. | Apply after behavior is consolidated, not during every micro-iteration. |
| Distribution boundaries | Multiple branded outputs needed shared product code without client forks. | Candidate pattern; requires an actual multi-distribution product need. |

## Design discipline

The project explicitly used ideas from John Ousterhout's *A Philosophy of
Software Design* as agent guardrails. Deep modules, information hiding, small
interfaces, low cognitive load and low change amplification shaped both product
code and operational context.

This discipline reduced how much of the monorepo an agent needed to understand
for a bounded change. It is treated as a meaningful contributor to the delivery
method, not as proof that one philosophy alone caused the outcome.

## Validation ladder used

```text
unit/domain -> widget/component -> contract -> golden -> integrated smoke
            -> containers/staging -> physical device
```

The lesson is not to maximize every test category. Each layer should prove a
different risk and have a clear owner.

## What was deliberately not transferred

- product domain and business rules;
- application routes, endpoint paths, DTOs and database schema;
- authentication configuration, users and operational datasets;
- client names, brand assets, design files and UI copy;
- hosts, ports, remote topology, credentials and deployment scripts;
- the private repository or its Git history.

## Questions another project can reuse

- Which source wins when code, design, backlog and contract disagree?
- What is the smallest vertical slice that proves user value?
- Which interface needs an executable contract?
- Which visual surfaces are stable and costly enough to justify snapshots?
- Which risks need deterministic fixtures, and which need a real environment?
- Has the requested behavior already been accepted and stabilized?
- Does a new distribution require configuration, a genuine product boundary or
  an unhealthy fork?

For the general workflow, continue with
[Agentic Delivery Lifecycle](../../docs/guides/AGENTIC_DELIVERY_LIFECYCLE.md).
