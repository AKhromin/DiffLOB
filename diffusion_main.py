"""Compatibility wrapper for the packaged diffusion entrypoint."""

from _compat import run_module


def main():
    run_module("difflob.cli.diffusion")


if __name__ == "__main__":
    main()

