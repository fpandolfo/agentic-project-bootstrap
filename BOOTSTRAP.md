# Public Alpha Bootstrap

This repository was seeded from `agentic-project-bootstrap-v0.1.0.zip` and is
the canonical development home for the public tool from `0.2.0-alpha.1` onward.

## Implemented public foundation

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

## Agent-first direction

The primary experience is now:

```text
READ -> DISCOVER -> ASK -> PROPOSE -> APPROVE -> GENERATE -> OPERATE
```

Any capable agent starts at `START_HERE.md`, uses content-free structural
discovery and reads only the relevant playbook. Installation is optional. The
CLI remains available for deterministic, reviewable file application.

The public foundation also includes sanitized real-project case studies, an
end-to-end delivery lifecycle and a private-to-public learning policy. These
artifacts expose reusable decisions and validation patterns without copying
consumer products.

Meaningful implementation and refactoring are also guided by an explicit
software-design philosophy inspired by John Ousterhout, with a portable review
skill, checklist and obvious-system advisory.

## Deliberately deferred

- automatic upgrades and rollback;
- third-party pack installation and trust policy;
- stack-specific guidance packs;
- release archive automation;
- case-study media production and presentation site;
- automatic merge of user-modified managed files.

These become independent GitHub Issues rather than hidden alpha promises.

## Release-candidate boundary

Version `0.2.0-alpha.3` is intended for public review and clean-agent pilots.
Files applied to a consumer become consumer-owned; this release does not offer
automatic upgrade, deletion or rollback. Distribution smoke tests cover wheel
and source archives, while SBOM/provenance and the stable upgrade contract remain
explicit release issues.
