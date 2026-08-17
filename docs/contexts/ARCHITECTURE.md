# Architecture

## Boundary

Agentic Project Bootstrap is a deterministic repository transformation tool,
not an agent runtime or hosted control plane.

```text
manifest
   |
pack dependency resolution
   |
rendered desired files
   |
plan + fingerprint + conflict classification
   |
explicit approval
   |
preflight + atomic-per-file writes
   |
manifest/state + verify
```

## Contracts

### Manifest

Defines project metadata, selected packs, argv-only quality commands and human
gates. Unknown product information remains explicit instead of being invented.

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

## Extension direction

Stack packs and community packs should extend the same contracts. A future pack
API needs schema validation, provenance, compatibility, tests and an explicit
trust/install decision before remote distribution is allowed.
