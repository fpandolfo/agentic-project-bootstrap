# Agentic Project Bootstrap

An open, repository-native bootstrap for disciplined agentic development.

Agentic Project Bootstrap does not provide an IDE, model or hosted control
plane. It prepares a new or existing repository so humans and capable coding
agents can share durable context, explicit ownership, proportional validation
and human approval gates without being locked to one player.

> Status: `0.2.0-alpha.1`. The plan/apply contract is functional and tested;
> pack and upgrade APIs are still evolving.

[Leia em português](README.pt-BR.md)

## Why

Agentic delivery needs more than prompts. A repository should make it easy to
answer, from a clean context:

- What is true now?
- Who owns each durable decision?
- What is the smallest coherent delivery slice?
- What may an agent change automatically?
- Which actions still require a human decision?
- What evidence proves the work is complete?

This project turns those questions into versioned files and deterministic checks.

## Safety model

```text
manifest -> plan -> human fingerprint approval -> apply -> verify
```

- `init` and `adopt` create manifests; they do not modify target repositories.
- `plan` renders selected packs and classifies create/update/conflict operations.
- `apply` refuses conflicts and requires the plan fingerprint.
- target files changed after planning invalidate the apply.
- user-modified managed files are never overwritten.
- removed pack files become visible orphans and are never deleted automatically.
- project quality commands run only with `verify --run-quality`.
- the repository delivery gate scans tracked files for common privacy and secret leaks.

## Quick start without installation

Requirements: Python 3.11+ and Git.

```bash
git clone https://github.com/fpandolfo/agentic-project-bootstrap.git
cd agentic-project-bootstrap

python3 agentic.py doctor

python3 agentic.py init \
  --name "My Product" \
  --description "A short, outcome-oriented description." \
  --stack "TBD — discover before implementation" \
  --packs core,generic-agent,github,codex \
  --output /tmp/my-product.agentic.json

python3 agentic.py plan \
  --target /path/to/my-product \
  --manifest /tmp/my-product.agentic.json \
  --output /tmp/my-product.plan.json

# Review the plan and use the fingerprint printed by the previous command.
python3 agentic.py apply \
  --plan /tmp/my-product.plan.json \
  --approve <fingerprint>

python3 agentic.py verify --target /path/to/my-product
```

For an existing repository:

```bash
python3 agentic.py adopt /path/to/existing-repo \
  --description "What this product exists to accomplish." \
  --output /tmp/existing.agentic.json

python3 agentic.py plan \
  --target /path/to/existing-repo \
  --manifest /tmp/existing.agentic.json \
  --preserve-existing \
  --output /tmp/existing.plan.json
```

`--preserve-existing` is explicit because adoption commonly finds a README,
`.gitignore` or agent instructions that already belong to the project. Preserved
files remain untouched and unmanaged; the plan still shows every collision.

## Install the CLI

```bash
python3 -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/agentic doctor
```

The runtime has no third-party Python dependencies.

## Built-in packs

| Pack | Purpose |
|---|---|
| `core` | Canonical owners, context governance, delivery workflow and checks |
| `generic-agent` | Portable Agent Skills |
| `github` | Issue/PR templates and least-privilege context CI |
| `codex` | Read-only specialist agents |
| `kiro` | Thin steering and skill adapters |

Run `python3 agentic.py list-packs` for the installed catalog.

## Operating model

```text
Human: why, priorities, business rules, risk and acceptance
Agent: discovery, implementation, tests, documentation and evidence
Repository: contracts, canonical owners, guardrails and durable memory
```

The generated project follows `MAP -> IMPLEMENT -> VALIDATE -> CLOSE` and keeps
player configuration as an adapter rather than the only owner of project truth.

## Scope

The alpha intentionally does not include:

- an interactive wizard or GUI;
- a hosted execution service;
- authentication, billing or licensing infrastructure;
- automatic deletion or three-way merge;
- remote connectors or secret management;
- stack-specific application scaffolding;
- a stable third-party pack API or automatic upgrades.

These boundaries keep the first public core inspectable and safe. Follow the
roadmap in GitHub Issues for the next slices.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

Licensed under Apache-2.0.
