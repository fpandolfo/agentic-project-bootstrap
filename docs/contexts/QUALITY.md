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
- software-design guidance, checklist and obvious-system advisory in generated
  core projects;
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

The package job builds both standard Python distribution formats with
`python -m build`, runs `tools/release_smoke.py` against the wheel and source
archive in isolated virtual environments, and retains the archives as workflow
artifacts. Artifact construction never grants publish permissions.

Official references checked on 2026-08-18:

- [Python Packaging User Guide](https://packaging.python.org/en/latest/flow/)
  recommends `python -m build` and publishing both a source distribution and
  wheel;
- [Python packaging metadata guidance](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license)
  owns the SPDX license expression and license-file form used by this package;
- [GitHub upload-artifact](https://github.com/actions/upload-artifact) documents
  `actions/upload-artifact@v4` for workflow artifacts;
- publishing, provenance and elevated OIDC permissions remain a separate future
  job so untrusted build steps do not receive release authority, following the
  [PyPA publish action guidance](https://github.com/pypa/gh-action-pypi-publish).

Revisit when the supported Python baseline, build backend, artifact action major
or public package index changes.

## Release gate

- full checks green;
- clean generated-project smoke;
- no unresolved non-template tokens;
- clean secret-like/path scan;
- changelog and version aligned;
- Git status understood;
- public issue records intentional follow-ups.

## Alpha upgrade boundary

Applied files become consumer-owned. The alpha does not automatically upgrade,
delete or roll back them. A future executable upgrade contract must preserve
local modifications, report obsolete files without removal and add adversarial
recovery tests before release.
