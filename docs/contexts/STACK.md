# Stack

## Runtime

- Markdown guidance requires only a capable agent that can read repository files;
- Python `>=3.11`;
- standard library only at runtime;
- Git for repository diagnostics and delivery checks.

Python and Git are optional for guidance-only use. They are required only for
the helper scripts, deterministic applicator and repository delivery checks.

## Packaging

- `pyproject.toml` with setuptools;
- console command: `agentic`;
- direct source fallback: `python3 agentic.py`;
- built-in text packs shipped as package data.
- universal guidance mirrored into the core pack by
  `tools/sync_agent_first_pack.py`.

## Validation

- `unittest` for executable behavior;
- `compileall` for syntax/import coverage;
- temporary directories for end-to-end target tests;
- GitHub Actions on supported Python versions.

## Compatibility

- Linux is the primary development environment;
- macOS is supported by the Python/file contracts;
- Windows support is best-effort in the alpha; symlink behavior is platform-specific;
- generated project content is player-agnostic unless optional adapters are selected.
