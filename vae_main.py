"""Compatibility wrapper for the packaged VAE entrypoint."""

from _compat import run_module


def main():
    run_module("difflob.cli.vae")


if __name__ == "__main__":
    main()

