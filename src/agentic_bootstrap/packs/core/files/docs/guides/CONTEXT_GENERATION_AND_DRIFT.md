# Context Generation and Drift

Use generated context when agents repeatedly spend time reconstructing factual
repository surfaces or when code, contracts and durable docs drift without a
visible signal.

Generated context is optional enforcement. It is not a default requirement and
never owns product intent or business rules.

## Minimal contract

A generated context surface should have:

- a deterministic source already inside the repository;
- one documented regeneration command;
- small, reviewable output;
- stable ordering and no timestamps or machine-specific paths;
- a check that regenerates and reports drift;
- a canonical durable owner explaining meaning and accepted omissions;
- an explicit rule that generated files are not edited manually.

The remote workflow, when present, should call the local check rather than
reimplement its rules in CI configuration.

## Result semantics

| Result | Meaning | Delivery consequence |
|---|---|---|
| `PASS` | Generated evidence matches the current repository. | Delivery may continue. |
| `KNOWN_GAP` | A mismatch or omission is accepted, owned and has a revisit condition. | Delivery may continue when the acceptance is explicit. |
| `NEW_FAILURE` | New unexplained drift or a broken factual contract exists. | Fix or classify it before closeout. |

A valid known gap answers what is missing, why it is acceptable now, who owns
the follow-up and which event makes it important.

## Candidate maps by project shape

Choose only maps that answer recurring questions.

| Project shape | Candidate generated evidence |
|---|---|
| Small static site | source/page inventory, public asset surface, operational commands, context health |
| Frontend application | routes/screens, dependency boundaries, critical flows, test and visual-baseline inventory |
| API service | endpoints, contract index, persistence migrations, auth surface, test coverage map |
| App/API repository | frontend routes, backend endpoints, API crosswalk, flow maps, dependency maps, drift report |
| Library or tooling | public commands/APIs, schemas, compatibility matrix, fixtures and release surface |
| Documentation-only project | canonical owners, links and unresolved decision inventory |

Do not generate a backend map for a frontend-only project merely for symmetry.

## Safe generation sequence

```text
inspect sources -> generate in memory/temp -> compare -> review -> update output
                -> run context gate -> run delivery gate
```

Generation must not read credentials, dependency caches, unrelated user
configuration or files outside the project scope. Reports must not contain
absolute user paths, secrets, private hostnames or raw sensitive data.

## When not to generate

Skip generated context when:

- the repository is small enough that one index already answers the question;
- the output would repeat a durable document;
- the input requires subjective agent interpretation;
- no owner will review or regenerate it;
- every change would produce noisy, low-value diffs;
- the proposed generator is larger than the discovery problem.

Start with structural discovery and a thin project index. Add the first generated
map only after a repeated discovery or drift problem becomes concrete.
