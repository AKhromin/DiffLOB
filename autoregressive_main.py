"""Compatibility wrapper for the packaged autoregressive entrypoint."""

from _compat import run_module


def main():
    run_module("difflob.cli.autoregressive")


if __name__ == "__main__":
    main()

