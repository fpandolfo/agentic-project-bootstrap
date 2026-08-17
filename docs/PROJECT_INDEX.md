# Project Index

Canonical navigation and current-state owner for Agentic Project Bootstrap.

## Current state

Status: public alpha; agent-first onboarding implemented on the active branch.

Version: `0.2.0-alpha.2`.

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
- public repository community and security baseline.

Not implemented:

- upgrade/rollback contract;
- third-party pack distribution;
- stack-specific packs;
- remote execution/connectors;
- GUI/wizard/control plane.

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
