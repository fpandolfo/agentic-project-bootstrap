# Agentic Project Bootstrap

Point any capable coding agent at one file and give it a disciplined way to
discover, structure, document and evolve a project with you.

No specific model, IDE, agent, account or installation is required. This is a
portable guidance pack: it helps an agent find evidence, ask better questions,
propose useful options and preserve durable project context. The human remains
the product owner and decision authority.

> Status: `0.2.0-alpha.3` release candidate. Agent-first onboarding and read-only discovery are
> functional; guidance and optional pack/application contracts are still evolving.

[Leia em português](README.pt-BR.md)

## Start in one prompt

Clone or download this repository, then tell your agent:

```text
Read /path/to/agentic-project-bootstrap/START_HERE.md.

Use ADOPT_PROJECT mode on my current repository. Start with read-only discovery.
Do not implement or modify project files yet.

Separate facts, inferences, unknowns and proposals. Ask me for the product intent
and business rules the repository cannot prove. Then propose the minimum useful
contexts, diagrams, ADRs, tooling and delivery plan for my approval.
```

For a new idea, replace `ADOPT_PROJECT` with `NEW_PROJECT` and describe the
desired outcome. More prompts are available in [PROMPTS.md](PROMPTS.md).

The repository-readable guidance is the primary product and needs no install.
Release artifacts also include a pure-Python wheel for the optional CLI; use the
wheel attached to the matching GitHub release and verify its published checksum
before installation.

## How it works

```text
READ -> DISCOVER -> ASK -> PROPOSE -> APPROVE -> GENERATE -> OPERATE
```

1. `START_HERE.md` establishes mode, boundaries and the first response contract.
2. `tools/discover_project.py` creates a content-free structural inventory.
3. `CAPABILITIES.md` shows what the suite can help produce.
4. One playbook guides a new, existing or already-understood project.
5. The agent inspects only relevant project evidence.
6. The human resolves product, business, risk and acceptance decisions.
7. The agent generates only the approved artifacts that are useful now.
8. The repository retains context for the next clean agent session.

The agent learns what is possible without loading this entire suite into context.

## Safe structural discovery

Python 3.11+ is needed only for the optional helper scripts.

```bash
python3 tools/discover_project.py \
  --target /path/to/project \
  --format markdown
```

The discovery tool inventories file names and structure. It does not read file
contents, execute target commands, follow symlinks or traverse common dependency,
cache and build directories. Sensitive candidates are reported by path only.

JSON output is also available for agents that prefer structured evidence:

```bash
python3 tools/discover_project.py \
  --target /path/to/project \
  --format json \
  --output /tmp/project-discovery.json
```

## Modes

| Mode | Use when | Primary outcome |
|---|---|---|
| `NEW_PROJECT` | idea or empty repository | approved minimal product/technical foundation |
| `ADOPT_PROJECT` | existing code, docs or delivery history | recovered truth and staged context adoption |
| `EVOLVE_PROJECT` | understood project receiving change | coherent delivery slice with aligned context |

See [playbooks/](playbooks/) for the exact sequences.

## What the suite can guide

- product and business-rule discovery;
- canonical project contexts and ownership index;
- architecture options and tradeoffs;
- Mermaid component, sequence, state, data and timeline diagrams;
- Architecture Decision Records;
- feature slices, edge cases and human approval gates;
- test, quality and delivery strategy;
- context audits and clean-session handoffs;
- player-specific skills or subagents as optional adapters.

Templates live under [docs/templates/](docs/templates/). They are starting points,
not a requirement to create every document.

## Evidence from real delivery

The [case-study library](case-studies/) distills reusable process from successful
private delivery without publishing consumer identity, domain code, data,
infrastructure or repository history.

- **Project Relay** covers an agent-led Flutter and Kotlin/Spring product with
  contracts, CI, containers, focused visual regression and device validation.
- **Project Aurora** covers an agent-led commercial website from discovery and
  visual direction through production publication, search indexing and handoff.

The names and scenarios are fictionalized. Each case labels privately verified,
owner-reported and synthetic evidence so examples do not become stronger claims
than their source permits. See
[Learning From Real Projects](docs/guides/REAL_PROJECT_LEARNING.md) for the
publication boundary.

## Design philosophy

The delivery method explicitly draws on John Ousterhout's *A Philosophy of
Software Design*. Agents are guided to reduce cognitive load and change
amplification, hide information, prefer deep modules with small interfaces and
avoid shallow wrappers or duplicated owners. See the
[software design philosophy](docs/guides/SOFTWARE_DESIGN_PHILOSOPHY.md).

This is a practical application of the book's ideas to agent-led delivery, not a
claim of affiliation or endorsement.

## Human and agent roles

```text
Human: purpose, priorities, business rules, material risk and acceptance
Agent: discovery, options, implementation, tests, documentation and evidence
Repository: canonical truth, decisions, guardrails and durable memory
```

An agent proposal is not a final decision. Unknown intent stays explicit until
the appropriate human confirms it.

## Optional deterministic application

The Python CLI remains available for users who want exact pack rendering,
conflict classification, fingerprint approval and managed-state verification:

```text
manifest -> plan -> human fingerprint approval -> apply -> verify
```

It is optional plumbing, not the onboarding experience. See
[docs/contexts/ARCHITECTURE.md](docs/contexts/ARCHITECTURE.md) and run
`python3 agentic.py --help` when this control is useful.

## Alpha ownership and upgrades

After adoption, generated project files belong to the consumer repository.
This alpha does not automatically upgrade, remove or roll back those files.
Replanning classifies local modifications and conflicts, but it is not a hidden
force-update mechanism. Review upstream guidance as a proposal and adopt only
the changes the project owner approves.

## Optional adapters

Built-in packs include the universal core, portable Agent Skills, GitHub
templates/CI, Codex specialists and Kiro steering. Player-specific files are
adapters; durable project truth remains in repository-owned docs, contracts,
tests and tooling.

## Safety principles

- no hosted service, credentials or model dependency;
- no content reads during initial structural discovery;
- no silent overwrite or automatic deletion in the optional applicator;
- no project command execution without explicit action;
- no proposal silently promoted into an accepted product decision;
- privacy and secret-like path scans in the public delivery gate.

## Project navigation

- External entry point: [START_HERE.md](START_HERE.md)
- Capability menu: [CAPABILITIES.md](CAPABILITIES.md)
- Copy/paste prompts: [PROMPTS.md](PROMPTS.md)
- Current state and owners: [docs/PROJECT_INDEX.md](docs/PROJECT_INDEX.md)
- Available and candidate tools: [TOOLING.md](TOOLING.md)
- Sanitized delivery evidence: [case-studies/](case-studies/)
- Contribution: [CONTRIBUTING.md](CONTRIBUTING.md)
- Security: [SECURITY.md](SECURITY.md)

Licensed under Apache-2.0.
