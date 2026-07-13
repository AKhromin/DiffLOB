# Quickstart

Create and sync the environment with `uv`:

```bash
uv sync
```

Build future regime conditioning variables:

```bash
uv run difflob-build-conditions
```

Run an existing training or sampling config:

```bash
uv run difflob-diffusion -c config/AMZN/Diffusion/wavenet_motion_control/train.py
uv run difflob-diffusion -c config/AMZN/Diffusion/wavenet_motion_control/sample.py
```

The old commands still work through compatibility wrappers:

```bash
python diffusion_main.py -c config/AMZN/Diffusion/wavenet_motion_control/train.py
bash scripts/AMZN/diff_wavenet_motion_control.sh
```

