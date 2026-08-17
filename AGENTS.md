# AGENTS

Operational entrypoint for humans and AI agents working on Agentic Project Bootstrap.

## Objective

Build a repository-native, player-agnostic bootstrap that makes agent-assisted
projects auditable, portable and safe to continue from a clean context.

The public interface stays small: manifest, plan, explicit apply and verify.
Complexity belongs behind those deterministic contracts, not in an interactive
wizard or a hosted control plane.

## First activation

1. Read this file and `docs/PROJECT_INDEX.md`.
2. Inspect `git status --short`.
3. Classify the work as CLI/core, pack/template, docs/community, security, or release.
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
- `core` never requires a player-specific pack.
- Plans are immutable, fingerprinted and inspectable.
- Apply requires explicit fingerprint approval.
- Unmanaged or locally modified target files are conflicts, never silent overwrites.
- Managed paths cannot escape the target or traverse symlinks.
- Removal is never automatic; obsolete managed files are reported as orphaned.
- Quality commands are argv arrays and run only after an explicit flag.
- Packs contain text files only until a versioned binary-asset contract exists.
- Durable project truth lives outside player adapters.

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
