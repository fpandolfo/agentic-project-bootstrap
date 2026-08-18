# AGENTS

Operational entrypoint for humans and AI agents working on Agentic Project Bootstrap.

## Objective

Build a portable, player-agnostic guidance pack that helps any capable coding
agent discover, structure, document and evolve a project with the human as
product owner and decision authority.

The primary public interface is `START_HERE.md`, the capability catalog and
mode-specific playbooks. The deterministic CLI is optional plumbing for users
who want reviewed file application; it is not required for agent-led adoption.

## First activation

1. Read this file and `docs/PROJECT_INDEX.md`.
2. Inspect `git status --short`.
3. Classify the work as agent experience, discovery/tooling, CLI/core,
   pack/template, docs/community, security, or release.
4. Read only the canonical owners routed by the project index.
5. For meaningful behavior, map MVP, non-goals, unhappy path, edge cases and validation.
6. Run focused tests during implementation and `python tools/prepare_delivery.py` before closeout.

## Trust order

1. code and tests;
2. manifest/plan/state schemas and contracts;
3. `docs/PROJECT_INDEX.md`;
4. canonical context and operational docs;
5. README summaries;
6. GitHub Issues;
7. chat history.

## Read next by task

### CLI, planning or apply safety

1. `docs/contexts/ARCHITECTURE.md`
2. `src/agentic_bootstrap/`
3. `tests/test_cli.py`

### Agent-first onboarding or discovery

1. `START_HERE.md`
2. `CAPABILITIES.md`
3. relevant file under `playbooks/`
4. `docs/ops/AGENT_FIRST_ONBOARDING.md`
5. discovery tests

### Meaningful implementation, architecture or refactoring

1. `docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md`
2. `docs/checklists/SOFTWARE_DESIGN.md`
3. affected architecture/context owner
4. nearby code and tests

### Packs, templates or player adapters

1. `docs/ops/AGENT_ADAPTERS.md`
2. `docs/ops/CONTEXT_GOVERNANCE.md`
3. `src/agentic_bootstrap/packs/`
4. generated-project tests

### Product, scope or roadmap

1. `docs/contexts/PRODUCT.md`
2. `BOOTSTRAP.md`
3. relevant GitHub Issue

### CI, dependencies, release or security

1. `docs/contexts/QUALITY.md`
2. `docs/ops/OFFICIAL_DOCS_POLICY.md`
3. `SECURITY.md`
4. current official documentation

## Invariants

- No wizard, account, hosted service or model dependency is required.
- Guidance proposes options; it does not silently become a final product or architecture decision.
- Initial structural discovery reads no file contents, executes no target commands and follows no symlinks.
- `core` never requires a player-specific pack.
- Plans are immutable, fingerprinted and inspectable.
- Apply requires explicit fingerprint approval.
- Unmanaged or locally modified target files are conflicts, never silent overwrites.
- Managed paths cannot escape the target or traverse symlinks.
- Removal is never automatic; obsolete managed files are reported as orphaned.
- Quality commands are argv arrays and run only after an explicit flag.
- Packs contain text files only until a versioned binary-asset contract exists.
- Durable project truth lives outside player adapters.
- New boundaries should hide meaningful complexity behind small interfaces;
  shallow wrappers and duplicated owners require explicit justification.

## Security rules

- Never read user home configuration, credentials or unrelated files during bootstrap.
- Never execute target-repository commands during plan or apply.
- Never place secrets in manifests, plans, docs, fixtures or screenshots.
- Keep GitHub Actions permissions explicit and minimal.
- Treat pack content and community contributions as untrusted until validated.
- Consult official sources for changing security, CI, packaging and platform behavior.

## Closeout

Run:

```bash
python tools/prepare_delivery.py
```

Then report behavior changed, validation, docs/contracts updated, intentional
non-goals and residual risks. Do not mark a roadmap issue complete without the
acceptance evidence in the repository or issue.
