# Project Index

Canonical navigation and current-state owner for Agentic Project Bootstrap.

## Current state

Status: public alpha; agent-first onboarding implemented on the active branch.

Version: `0.2.0-alpha.3` release candidate.

Implemented:

- universal agent-first entry point and capability catalog;
- new, adopt and evolve playbooks;
- copy/paste activation prompts;
- content-free, read-only project discovery;
- CLI commands `doctor`, `init`, `adopt`, `list-packs`, `plan`, `apply`, `verify`;
- JSON manifest schema;
- fingerprinted plans with explicit approval;
- conflict, target-change, symlink and path-escape guards;
- managed state without automatic deletion;
- core, generic-agent, GitHub, Codex and Kiro built-in packs;
- end-to-end unit tests;
- sanitized real-project cases and reusable delivery lifecycle guidance;
- explicit Ousterhout-inspired software-design guardrails and tooling catalog;
- public repository community and security baseline.

Not implemented:

- upgrade/rollback contract;
- third-party pack distribution;
- stack-specific packs;
- remote execution/connectors;
- GUI/wizard/control plane.

Release follow-ups are tracked by GitHub Issues. In particular, artifact and
supply-chain evidence, clean-agent pilots, upgrade design and public media stay
explicitly open until their acceptance evidence exists.

## Canonical owners

| Area | Owner |
|---|---|
| External agent entry point | `START_HERE.md` |
| Capability selection | `CAPABILITIES.md` |
| Activation prompts | `PROMPTS.md` |
| Mode workflows | `playbooks/` |
| Agent-first contract | `docs/ops/AGENT_FIRST_ONBOARDING.md` |
| Structural discovery | `src/agentic_bootstrap/packs/core/files/tools/discover_project.py` |
| Operational entrypoint | `AGENTS.md` |
| Product and boundaries | `docs/contexts/PRODUCT.md` |
| Architecture and safety model | `docs/contexts/ARCHITECTURE.md` |
| Stack and packaging | `docs/contexts/STACK.md` |
| Validation and CI | `docs/contexts/QUALITY.md` |
| Software design philosophy | `docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md` |
| Software design checklist | `docs/checklists/SOFTWARE_DESIGN.md` |
| Tooling availability and extraction status | `TOOLING.md` |
| End-to-end delivery guidance | `docs/guides/AGENTIC_DELIVERY_LIFECYCLE.md` |
| Generated context and drift guidance | `docs/guides/CONTEXT_GENERATION_AND_DRIFT.md` |
| CI and delivery gate guidance | `docs/guides/CI_AND_DELIVERY_GATES.md` |
| Private-to-public learning policy | `docs/guides/REAL_PROJECT_LEARNING.md` |
| Sanitized real-project evidence | `case-studies/` |
| Case-study format | `docs/templates/CASE_STUDY.md` |
| Project quality strategy format | `docs/templates/QUALITY_STRATEGY.md` |
| CLI | `src/agentic_bootstrap/cli.py` |
| Manifest contract | `src/agentic_bootstrap/manifest.py`, `agentic-project.schema.json` |
| Pack loading/rendering | `src/agentic_bootstrap/packs.py`, `src/agentic_bootstrap/packs/` |
| Plan contract | `src/agentic_bootstrap/planner.py` |
| Apply safety | `src/agentic_bootstrap/apply.py` |
| Verification | `src/agentic_bootstrap/verify.py` |
| Executable behavior | `tests/test_cli.py`, `tests/test_discovery.py` |
| Security reporting | `SECURITY.md` |
| Contributions | `CONTRIBUTING.md` |

## Read next

### Applying the suite to a project

1. `START_HERE.md`
2. `CAPABILITIES.md`
3. one file under `playbooks/`

### Learning from comparable delivery

1. `case-studies/README.md`
2. the one relevant case
3. `docs/guides/AGENTIC_DELIVERY_LIFECYCLE.md` for a reusable lifecycle view

### Meaningful implementation, architecture or refactoring

1. `docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md`
2. `docs/checklists/SOFTWARE_DESIGN.md`
3. affected architecture/context owner and nearby tests

### Finding or extracting tooling

1. `TOOLING.md`
2. the listed canonical guide or executable tool
3. current official documentation when stack/platform behavior is involved

### Extracting a new public case

1. `docs/guides/REAL_PROJECT_LEARNING.md`
2. `docs/templates/CASE_STUDY.md`
3. `tools/privacy_scan.py`

### CLI or behavior

1. `docs/contexts/ARCHITECTURE.md`
2. relevant module under `src/agentic_bootstrap/`
3. `tests/test_cli.py`

### Packs or adapters

1. `docs/ops/AGENT_ADAPTERS.md`
2. `docs/ops/CONTEXT_GOVERNANCE.md`
3. `src/agentic_bootstrap/packs/`

### Release, dependencies or CI

1. `docs/contexts/QUALITY.md`
2. `docs/ops/OFFICIAL_DOCS_POLICY.md`
3. `CHANGELOG.md`

## Current hotspots

- Universal guidance is mirrored into the core pack; the delivery gate enforces
  synchronization through `tools/sync_agent_first_pack.py`.
- Structural discovery intentionally reads no contents, so stack and product
  interpretation still requires selective agent inspection and human input.

- Plans embed rendered text to make apply deterministic; large/binary pack
  support needs a separate artifact contract.
- Apply is preflighted and atomic per file, but not transactional across a
  filesystem-wide write failure.
- Managed-file edits intentionally become conflicts; a future upgrade design
  must preserve user ownership rather than add a hidden force mode.
- Several real-project tools remain extraction candidates rather than shipped
  capabilities; `TOOLING.md` owns their status and neutralization boundary.
