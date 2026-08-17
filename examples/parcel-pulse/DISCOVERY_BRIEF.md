# Discovery Brief — Parcel Pulse

## Target and mode

- Target: fictional empty repository
- Mode: `NEW_PROJECT`
- Requested outcome: help support notice potentially delayed parcels

## Observed facts

- The first version is an internal prototype.
- It must use fictional data.
- Workflow validation is more important than broad integration.

## Inferences to confirm

- A dashboard may be useful, but the human did not require a specific UI.
- “Delayed” may depend on parcel stage, carrier and expected timestamp.

## Important unknowns

- Who defines the delay threshold?
- Which parcel stages matter in the prototype?
- Does the team need acknowledgement or only visibility?
- What evidence will make the workflow useful enough to continue?

## Proposed artifacts

- minimal product context owning the delay-rule uncertainty;
- one component/data-flow diagram;
- one ADR if local-first mock data is accepted;
- one feature slice after business rules are confirmed.

## Human gates

- definition of delayed;
- prototype interaction and acceptance;
- any future external carrier integration or credential use.
