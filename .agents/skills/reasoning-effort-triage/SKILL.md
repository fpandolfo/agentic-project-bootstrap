---
name: reasoning-effort-triage
description: Classify a task early as low, medium or high reasoning effort based on ambiguity, blast radius and cost of error. Use before substantial implementation or investigation; do not claim the player/model setting changed automatically.
---

1. Read `AGENTS.md` and `docs/PROJECT_INDEX.md`.
2. Recommend:
   - `low` for factual/localized/mechanical work;
   - `medium` for ordinary bounded implementation;
   - `high` for architecture, security, ambiguous bugs, cross-cutting changes, CI/deploy or external integration changes.
3. For `high`, state briefly why, likely owners and the first mapping step.
4. Do not claim this skill changes the actual model/player reasoning setting.
