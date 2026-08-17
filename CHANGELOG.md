# Changelog

All notable changes are documented here.

## 0.2.0-alpha.2 — 2026-08-17

### Added

- universal `START_HERE.md` entry point for any capable coding agent;
- capability catalog, copy/paste prompts and new/adopt/evolve playbooks;
- content-free, read-only structural discovery in JSON or Markdown;
- explicit guidance for contexts, Mermaid diagrams, ADRs and human gates;
- synchronized agent-first guidance inside the distributable core pack;
- synthetic end-to-end example and discovery safety tests.

### Changed

- made `READ -> DISCOVER -> ASK -> PROPOSE -> APPROVE -> GENERATE -> OPERATE`
  the primary product experience;
- repositioned manifest/plan/apply/verify as optional deterministic plumbing;
- clarified that agent proposals are guidance, not final product decisions.

## 0.2.0-alpha.1 — 2026-08-17

### Added

- player-agnostic Python CLI;
- manifest schema and safe existing-repository adoption;
- built-in pack catalog with dependency resolution;
- fingerprinted plan/apply contract;
- managed state and verification;
- conflict, tamper, target-change and symlink guards;
- core, generic-agent, GitHub, Codex and Kiro packs;
- end-to-end test suite and least-privilege GitHub Actions;
- public license, security and contribution baseline.

### Changed

- evolved the local `v0.1.0` ZIP from a static starter into an executable public alpha;
- made Kiro and Codex optional adapters rather than core requirements.
