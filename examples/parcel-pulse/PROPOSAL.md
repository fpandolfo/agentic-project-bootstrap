# Proposal — Review Before Generation

## Option A — Static local prototype

Use a small fictional dataset and calculate delay candidates locally.

- Benefits: fastest workflow validation, no accounts or credentials.
- Limits: does not prove carrier integration or live-event reliability.

## Option B — Mock service boundary

Add a local mock API shaped like a future carrier adapter.

- Benefits: validates an integration boundary earlier.
- Limits: more moving parts before the support workflow is proven.

## Recommendation

Start with Option A, but isolate delay evaluation behind a narrow interface so
an adapter can be evaluated later. This remains a proposal until accepted.

## Human decision

For this fictional walkthrough, assume the human accepted Option A and defined:

- a parcel is flagged when its last event is older than a stage-specific threshold;
- support needs visibility only in the first slice;
- fictional data and local execution are mandatory non-goals for integration.
