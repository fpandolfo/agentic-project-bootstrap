# Quality and Validation

## Local commands

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 -m compileall -q src tests tools agentic.py
PYTHONPATH=src python3 -m agentic_bootstrap doctor
python3 tools/context_check.py
python3 tools/prepare_delivery.py
```

## Required coverage

The alpha test suite must cover:

- universal agent-first files in generated core projects;
- empty and existing project mode discovery;
- content-free discovery, ignored dependencies and skipped symlinks;
- no absolute machine path or sensitive content in discovery output;
- explicit-output-only discovery writes;
- manifest creation and validation;
- existing-repository stack inference;
- pack dependency resolution;
- plan/apply/verify happy path;
- unmanaged-file conflicts;
- locally modified managed files;
- plan tampering;
- target change after planning;
- symlink/path escape refusal;
- player independence of the core pack.

## CI

GitHub Actions runs on pull requests, `main` and manual dispatch with
`permissions: contents: read`. Action versions and Python versions are selected
from current official documentation and reviewed when their runtime baseline changes.

## Release gate

- full checks green;
- clean generated-project smoke;
- no unresolved non-template tokens;
- clean secret-like/path scan;
- changelog and version aligned;
- Git status understood;
- public issue records intentional follow-ups.
