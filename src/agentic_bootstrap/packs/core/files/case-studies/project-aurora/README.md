# Project Aurora — Agent-Led Commercial Website Delivery

Project Aurora is a fictionalized composite built from a successful real
commercial website delivery. The public name, company profile, industry,
content, sitemap details, visual identity, people and infrastructure are not the
source client's. This case must not be read as a one-to-one description of any
separately showcased website.

## What this case demonstrates

Agentic delivery can extend beyond code generation into client discovery,
commercial scope, visual exploration, content intake, responsive implementation,
publication, search indexing, observation and handoff.

## Evidence boundary

### Privately verified

A read-only review of the delivery repository observed:

- an Astro/TypeScript website with centralized content and reusable components;
- 266 files in structural discovery, three CI workflows and three ADR files;
- separate owners for product context, visual direction, content inventory,
  publication, search monitoring and final delivery sequence;
- versioned desktop and mobile visual evidence across multiple review cycles;
- local context generation, anti-drift checks and an aggregated delivery gate;
- automated quality/build checks with least-privilege workflow permissions;
- production publication, canonical URL controls, robots/sitemap handling and a
  staged search-indexing release;
- a clean-session handoff path that does not depend on chat history.

### Owner-reported

The delivery owner reports that:

- the work was completed through agent-assisted execution from discovery to
  production and search configuration;
- the website was sold and produced approximately BRL 8,000 in profit;
- agents also assisted with external configuration and post-publication
  verification under human approval.

The commercial result is owner-reported and intentionally detached from the
fictional scenario and private client identity.

## Delivery journey

1. Convert an initial client conversation into product outcome, MVP, non-goals,
   content gaps and approval responsibilities.
2. Make one high-value page the first trust milestone before expanding the full
   sitemap.
3. Explore a small number of visual directions, record the accepted direction
   and keep the composition reversible while real content is incomplete.
4. Centralize approved copy, media roles, permissions and placeholders instead
   of scattering final content through page files.
5. Implement and review each meaningful surface in desktop and mobile, keeping
   screenshots as delivery evidence rather than the sole design owner.
6. Curate media by editorial purpose; exclude weak, repetitive or unapproved
   assets instead of treating every received file as publishable.
7. Separate build quality, deployment, domain readiness and public indexing into
   distinct gates so a preview cannot become searchable by accident.
8. Record a production baseline and follow-up cadence rather than promising an
   arbitrary search result before evidence exists.
9. Leave maintenance, deployment, deferred scope and the next observation point
   in a clean-context handoff.

## Transferable patterns

| Pattern | Problem it solved | Reuse boundary |
|---|---|---|
| First trust milestone | A full site was too large for the first approval loop. | Choose the smallest surface that proves direction and value. |
| Reversible visual direction | Client content and identity arrived incrementally. | Keep tokens/content centralized; do not postpone all progress for perfect inputs. |
| Content and permission inventory | Placeholders, real claims and media could be confused. | Useful for any product with externally supplied content. |
| Desktop/mobile evidence loop | Responsive defects and editorial imbalance needed visible review. | Screenshots supplement code and acceptance; they do not replace either. |
| Publication gates | Deploy success did not mean the site was ready for public indexing. | Separate preview, production, canonicalization and indexing authority. |
| Observation baseline | Search outcomes are asynchronous and easy to overstate. | Record a baseline and decisions at useful intervals. |
| Durable final roadmap | The last mile crossed media, copy, domain, SEO and handoff. | Use when several independently gated concerns must survive session changes. |

## Design discipline

The delivery applied ideas from John Ousterhout's *A Philosophy of Software
Design* beyond code structure: one owner for durable decisions, small reusable
interfaces, centralized content, reversible boundaries and low cognitive load
for clean-context agents.

The result was not the largest possible framework. It was a deliberately small
system whose pages, content, validation and release process remained easy to
find and change.

## Release model

```text
content and visual approval
        -> quality/build evidence
        -> production publication
        -> domain/canonical validation
        -> explicit indexing approval
        -> observation baseline and handoff
```

Each arrow is a decision boundary, not a requirement to use any particular
hosting or search provider.

## What was deliberately not transferred

- the client name, industry and relationships;
- real copy, claims, contact channels, domains and analytics;
- logos, photographs, videos, source design files and review conversations;
- provider account details, credentials, DNS records and operational topology;
- exact page structure, components or implementation from the delivered site;
- private tickets, dates, repository paths and Git history.

If real screenshots from a separately delivered public site are later used in a
presentation, they are illustrative delivery evidence. They must not be
described as the exact source, architecture or content model of Project Aurora.

## Questions another project can reuse

- What is the smallest page or journey that can earn stakeholder confidence?
- Which content is approved, pending, placeholder or forbidden to publish?
- Which visual decision must survive a clean agent session?
- What evidence is required on desktop, mobile and assistive interaction?
- Which release gates separate preview, production and public discovery?
- What should be observed after release, and what decision would each metric
  change?

For the general workflow, continue with
[Agentic Delivery Lifecycle](../../docs/guides/AGENTIC_DELIVERY_LIFECYCLE.md).
