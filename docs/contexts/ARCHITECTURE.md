# Architecture

## Boundary

Agentic Project Bootstrap is a repository-readable guidance suite with optional
deterministic tooling. It is not an agent runtime, model, IDE, wizard or hosted
control plane.

```text
Human intent / existing project
             |
       START_HERE.md
             |
 content-free structural discovery
             |
 capability catalog + selected playbook
             |
 facts / inferences / unknowns / questions
             |
 proposals + human approval gates
             |
 tailored contexts / diagrams / ADRs / tooling
             |
       validated delivery loop
```

The optional applicator is a subordinate path:

```text
manifest -> rendered packs -> fingerprinted plan -> explicit apply -> verify
```

## Contracts

### Universal entry point

`START_HERE.md` defines the player-independent activation sequence and routes an
agent to the minimum relevant playbook.

### Structural discovery

`tools/discover_project.py` inventories file names and structure without reading
contents, executing target commands or following symlinks. Its result is
evidence for agent reasoning, not a product interpretation.

### Guidance and playbooks

`CAPABILITIES.md`, `PROMPTS.md`, `playbooks/` and canonical templates help an
agent select useful artifacts. They are proposals, never mandatory final design.

### Optional manifest

Defines project metadata, selected packs, argv-only quality commands and human
gates when deterministic file application is desired. Unknown product
information remains explicit instead of being invented.

### Pack

A built-in pack has `pack.json` and a `files/` tree. Files are rendered only
from the pack allowlist. Templates never scan or rewrite arbitrary target text.

### Plan

Embeds rendered content, before/after hashes, action classification, selected
manifest, tool version and an overall SHA-256 fingerprint.

### Apply

Requires a matching fingerprint prefix, rejects any conflict, preflights every
path and verifies that target state has not changed since planning.

### State

Records only files managed by a successful apply. A local modification becomes
an explicit preserved customization on the next plan. Orphaned files are
reported but not deleted. During adoption, `--preserve-existing` keeps
pre-existing collisions untouched and outside managed state.

## Safety choices

- no shell evaluation;
- no network access;
- no home-directory discovery;
- no automatic deletion;
- no symlink traversal;
- no force overwrite;
- no execution of project commands without `--run-quality`;
- no binary pack files in the alpha.
- no content reads or target command execution in initial structural discovery;
- no mandatory player adapter or install step;
- no automatic conversion of proposals into accepted decisions.

## Extension direction

Stack packs and community packs should extend the same contracts. A future pack
API needs schema validation, provenance, compatibility, tests and an explicit
trust/install decision before remote distribution is allowed.
