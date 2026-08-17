#!/usr/bin/env python3
"""Run the same standalone discovery tool shipped by the core pack."""

from __future__ import annotations

import runpy
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "src"
    / "agentic_bootstrap"
    / "packs"
    / "core"
    / "files"
    / "tools"
    / "discover_project.py"
)

runpy.run_path(str(SCRIPT), run_name="__main__")
