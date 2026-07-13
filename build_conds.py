"""Compatibility wrapper for the packaged condition-building entrypoint."""

from _compat import run_module


def main():
    run_module("difflob.cli.build_conditions")


if __name__ == "__main__":
    main()

