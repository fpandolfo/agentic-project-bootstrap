# Public Alpha Bootstrap

This repository was seeded from `agentic-project-bootstrap-v0.1.0.zip` and is
the canonical development home for the public tool from `0.2.0-alpha.1` onward.

## Implemented in the first public slice

- zero-runtime-dependency Python CLI;
- manifest creation and existing-repository adoption;
- built-in pack catalog and dependency resolution;
- reviewable plans with SHA-256 fingerprints;
- explicit, preflighted apply;
- managed-state drift detection;
- symlink/path traversal protection;
- optional, argv-only project quality commands;
- core, generic-agent, GitHub, Codex and Kiro packs;
- end-to-end tests and GitHub Actions.

## Deliberately deferred

- automatic upgrades and rollback;
- third-party pack installation and trust policy;
- stack packs;
- release archive automation;
- case-study site and media;
- automatic merge of user-modified managed files.

These become independent GitHub Issues rather than hidden alpha promises.
