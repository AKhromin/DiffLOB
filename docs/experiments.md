# Experiments

Existing launch scripts remain in `scripts/{ticker}/`.

Examples:

```bash
bash scripts/AMZN/diff_wavenet_motion_control.sh
bash scripts/AAPL/cgan.sh
bash scripts/GOOG/ar.sh
```

For new runs, prefer the packaged `uv run` commands:

```bash
uv run difflob-diffusion -c config/AMZN/Diffusion/wavenet_motion_control/train.py
uv run difflob-gan -c config/AMZN/GAN/train.py
uv run difflob-vae -c config/AMZN/VAE/train.py
uv run difflob-autoregressive -c config/AMZN/Autoregressive/train.py
```

Generated artifacts should go under `outputs/`, `models/`, or `samples/`; these paths are ignored by git.

