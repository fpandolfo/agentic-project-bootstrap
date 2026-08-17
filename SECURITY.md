# Security Policy

## Supported versions

Security fixes are applied to the latest alpha or stable release. Until `1.0`,
interfaces may change between minor releases and fixes may require upgrading.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability or exposed credential.
Use GitHub private vulnerability reporting in the repository Security tab.

Include the affected version, reproduction, impact, whether a target repository
is modified, and any safe mitigation you already identified. Do not include live
credentials, personal data or private repository contents.

## Security boundary

The CLI is local-only and does not require network access. Plan and apply do not
execute target commands. Quality commands are explicit argv arrays and execute
only when the user selects `verify --run-quality`.

Community packs are not remotely installable in the alpha. That remains blocked
until provenance, compatibility, validation and trust policies are versioned.
