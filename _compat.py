"""Compatibility helpers for legacy root-level entrypoints."""

from pathlib import Path
import runpy
import sys


def ensure_src_path():
    src_path = Path(__file__).resolve().parent / "src"
    src_path_str = str(src_path)
    if src_path_str not in sys.path:
        sys.path.insert(0, src_path_str)


def run_module(module_name):
    ensure_src_path()
    runpy.run_module(module_name, run_name="__main__")

