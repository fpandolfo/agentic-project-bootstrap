# Official Documentation Policy

Canonical policy for version-sensitive and security-sensitive external facts.

## Consult current official documentation when changing

- frameworks/runtimes;
- dependencies;
- authentication/security;
- cryptography;
- mobile/platform APIs;
- cloud/deployment;
- CI/release;
- third-party integrations;
- data formats/protocols;
- legal/store/platform requirements.

## Record material decisions

Capture:

- topic;
- official source;
- date checked;
- selected behavior/version;
- why;
- validation performed;
- revisit trigger.

## Source preference

1. official product/framework docs;
2. official standards/specifications;
3. primary vendor release notes;
4. high-quality secondary sources only when necessary.

Agent memory is useful for orientation, not final proof of current external behavior.

## Secrets

Never persist passwords, tokens, API keys, private keys, session cookies or production secrets in agent instructions, steering, docs, screenshots or generated artifacts.
