# Learning From Real Projects

Use this guide when a successful private or client project contains patterns
that may improve this public guidance pack.

The goal is to preserve reusable reasoning, process and validation without
publishing a consumer's identity, domain, implementation or infrastructure.

## Operating rule

```text
OBSERVE -> SEPARATE -> CLASSIFY -> SANITIZE -> GENERALIZE -> VALIDATE -> PUBLISH
```

A useful local pattern does not become universal guidance automatically.
Promote it only when the public artifact remains valuable after consumer details
are removed.

## Separate evidence before writing

Classify every claim used by a case study:

| Evidence class | Meaning | Public treatment |
|---|---|---|
| Publicly reproducible | A public repository, command or artifact can prove it. | Link or describe the evidence precisely. |
| Privately verified | A maintainer inspected the private source or delivery record. | State the result without exposing the source. |
| Owner-reported | The human product owner confirms an outcome that is not independently reproducible. | Label it explicitly and avoid false precision. |
| Synthetic illustration | Fictional material demonstrates a reusable pattern. | Mark it as synthetic; never present it as delivery evidence. |

Do not merge those classes into one stronger claim.

## Classify the learning

| Class | Definition | Default action |
|---|---|---|
| Consumer-specific | Depends on product domain, copy, routes, assets, hosts or local operations. | Keep it out of the public pack. |
| Candidate guidance | Looks reusable but has limited evidence or an unclear owner. | Record it in a case; do not make it a default. |
| Mature guidance | Has a clear boundary, repeated or strong evidence and proportional validation. | Promote it to a guide, template, tool or optional adapter. |
| Player adapter | Improves one agent runtime without owning the durable rule. | Keep the rule in canonical guidance and make the adapter optional. |
| Experiment | Worth testing but not ready to guide other projects. | Isolate it and define a revisit condition. |
| Rejected or deferred | Adds more rigidity, disclosure or maintenance cost than value. | Record the reason; do not publish the mechanism. |

## Privacy boundary

Never move these surfaces into a public case or example:

- client, employee, tenant, supplier or repository identities;
- domains, email addresses, phone numbers, usernames or ticket keys;
- credentials, secret names that reveal topology, private hosts, ports or paths;
- real business records, database contents, API payloads or operational logs;
- proprietary routes, endpoint names, domain models or integration mappings;
- client copy, brand tokens, logos, photographs, videos or design files without
  explicit publication rights;
- exact infrastructure topology, deployment targets or security controls that
  would increase attackability;
- a private-to-public mapping table. Keep source attribution outside the public
  checkout when maintainers need it.

Potentially reusable material still needs transformation:

- replace identities with fictional labels;
- aggregate or round sensitive business outcomes when precision is unnecessary;
- describe architecture by capability and boundary, not consumer naming;
- replace data with deterministic fixtures;
- preserve the decision and trade-off while removing the private alternative;
- use neutral diagrams rather than screenshots of internal systems.

## Promotion questions

Before adding guidance to the universal path, answer:

1. What recurring ambiguity does this remove for a new agent?
2. Does the pattern survive removal of the original product domain?
3. Is there a durable owner, and can other entry points link to it?
4. Is the guidance advisory, or would it silently impose an architecture?
5. What validation proves the pattern without the private repository?
6. Can a project omit it without breaking the core workflow?
7. Is the public artifact smaller and clearer than the source material?

If the evidence is strong but the pattern is stack-specific, keep it as an
optional recipe or case-study learning rather than a universal default.

## Case publication gate

A case is ready to publish when:

- its name and scenario cannot be mistaken for the source project's identity;
- evidence classes are visible;
- facts, interpretations and transferable lessons are separated;
- private implementation details are absent;
- the case states what must not be copied;
- any business outcome has human approval for publication;
- screenshots and media have separate rights and privacy review;
- `python tools/privacy_scan.py` and the repository delivery gate pass.
