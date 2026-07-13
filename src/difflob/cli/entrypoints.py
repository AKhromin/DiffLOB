"""Console-script entrypoints that preserve the historical module behavior."""

import runpy


def diffusion():
    runpy.run_module("difflob.cli.diffusion", run_name="__main__")


def gan():
    runpy.run_module("difflob.cli.gan", run_name="__main__")


def vae():
    runpy.run_module("difflob.cli.vae", run_name="__main__")


def autoregressive():
    runpy.run_module("difflob.cli.autoregressive", run_name="__main__")


def build_conditions():
    runpy.run_module("difflob.cli.build_conditions", run_name="__main__")

