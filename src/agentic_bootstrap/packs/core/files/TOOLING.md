# Tooling Catalog

Canonical inventory of executable and guidance tooling available from this pack.
An agent should check this file before recreating a tool observed in a case study.

Status meanings:

- **available**: shipped and validated in this repository or the generated core
  pack;
- **guidance**: reusable contract exists, but implementation remains
  project-specific;
- **candidate**: useful source evidence exists, but a neutral portable tool and
  tests are still required;
- **local-only**: intentionally remains in the consumer because it carries stack,
  environment, provider or product coupling.

## Available

| Capability | Surface | Purpose |
|---|---|---|
| Structural discovery | `tools/discover_project.py` | Content-free inventory without target command execution. |
| Context structure check | `tools/context_check.py` | Required owners, adapters and unresolved-token checks. |
| Obvious-system advisory | `tools/obvious_system_check.py` | Navigation and long-document guardrails; strict mode is opt-in. |
| Delivery wrapper | `tools/prepare_delivery.py` | Context, design, tests and Git-state closeout. |
| Privacy scan | `tools/privacy_scan.py` | Public-repository path and secret-like leak detection. |
| Deterministic application | `agentic plan/apply/verify` | Fingerprinted, conflict-safe optional pack application. |
| Architecture/decision templates | `docs/templates/` | Context, ADR, diagram, slice, quality and handoff starting points. |

## Guidance with project-owned implementation

| Capability | Owner | Why it is not one universal script |
|---|---|---|
| Generated factual context and anti-drift | `docs/guides/CONTEXT_GENERATION_AND_DRIFT.md` | Useful maps depend on actual routes, contracts, tests and stack. |
| CI and delivery gates | `docs/guides/CI_AND_DELIVERY_GATES.md` | Commands and runners must match project risk and platform. |
| Visual/golden validation | `docs/guides/AGENTIC_DELIVERY_LIFECYCLE.md` | Stable surfaces, fonts, devices and baselines are product-specific. |
| Software design discipline | `docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md` | Module depth and information hiding require design judgment. |

## Extraction candidates

Real-project audits found these reusable candidates. They are deliberately not
advertised as available until a neutral implementation and tests exist.

| Candidate | Required neutralization before promotion |
|---|---|
| Changed-scope validation advisor | Replace repository-specific path rules with a small project-owned mapping contract. |
| Pull-request context bundle | Define portable inputs, privacy filtering and canonical-owner discovery. |
| Generated route/endpoint/contract maps | Add stack adapters and deterministic fixtures without reading secrets. |
| Mermaid/architecture validation | Define a player-independent source and drift contract. |
| Flutter app probe and golden harness | Verify current official toolchain behavior and use a neutral fixture. |
| Kotlin/Spring API and OpenAPI probe | Verify version matrices and keep endpoint/domain fixtures synthetic. |
| Node/static-site quality and launch recipe | Keep hosting, domain and indexing providers optional. |
| Media preparation helpers | Remove client naming, codecs and provider assumptions; add synthetic fixtures. |

## Local-only surfaces

Do not promote these directly from a successful product:

- credentials, hosts, ports, remote paths and deployment roots;
- customer-specific flavor names, icons, signing and brand assets;
- domain routes, endpoint models, database seeds and integration mappings;
- provider account setup or destructive operational scripts;
- real media, content, contact data and search properties;
- scripts whose safety depends on one machine or private network topology.

Extract the decision boundary and validation pattern instead. If the same need
repeats, build a neutral optional recipe with fixtures and explicit human gates.

## Agent use

1. Confirm that the named tool actually exists and read its owner before running
   it.
2. Treat case-study tooling as evidence, not as an installed capability.
3. Prefer an available tool or guidance owner over recreating a private script.
4. For candidate tooling, propose the smallest neutral contract and wait for
   approval before adding it.
5. Never infer credentials, environment topology or production authority from a
   case study.
