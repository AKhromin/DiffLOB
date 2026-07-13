"""Compatibility wrapper for the packaged GAN entrypoint."""

from _compat import run_module


def main():
    run_module("difflob.cli.gan")


if __name__ == "__main__":
    main()

