# Quickstart

Create and sync the environment with `uv`:

```bash
uv sync
```

## One-day LOBSTER sample smoke test

Place the AMZN message and orderbook CSVs directly in
`data/LOBSTER/LOBSTER_SampleFile_AMZN_2012-06-21_10/`, then run from the
repository root:

```bash
PYTHONPATH="$PWD/src" uv run --no-sync difflob-diffusion -c config/AMZN/Diffusion/wavenet_motion_control/train_sample_smoke.py
```

This config splits the single day chronologically and trains a small model for
one batch in each of the spatial, motion, and control stages. It writes a
checkpoint to `outputs/models/AMZN/difflob_sample_smoke.pth`. This confirms the
local data and training pipeline; its validation loss is not an independent-day
evaluation. The regular `train.py` config requires enough separate trading-day
files to populate the train, validation, and test splits.

Generate one 32-step trajectory from the smoke-test checkpoint and inspect it:

```bash
PYTHONPATH="$PWD/src" uv run --no-sync difflob-diffusion -c config/AMZN/Diffusion/wavenet_motion_control/sample_sample_smoke.py
uv run --no-sync python scripts/AMZN/inspect_sample_smoke.py
```

The generated array is `outputs/samples/AMZN/difflob_sample_smoke.npy`; the
diagnostic plot is saved alongside it as a PNG. The one-batch checkpoint is for
checking execution only. Its generated order books may violate market
constraints and should not be used as evidence of model quality.

To train the same small model from scratch for more batches and epochs, set
`DIFFLOB_EPOCHS`, `DIFFLOB_TRAIN_BATCHES`, and `DIFFLOB_VAL_BATCHES` before the
command. Set `DIFFLOB_CHECKPOINT` to a new path so the first smoke checkpoint is
kept. `DIFFLOB_DATA_DIR` can point to another ticker's one-day sample folder;
train a separate checkpoint for each ticker. The sample config also accepts
`DIFFLOB_DATA_DIR`, `DIFFLOB_CHECKPOINT`, and `DIFFLOB_SAMPLES_OUTPUT`.

For a multi-day experiment, place matching message and orderbook files for one
ticker in a single directory. The regular `(0.85, 0.05, 0.10)` file split needs
at least 11 trading-day pairs to give all three partitions a file. One-day
smoke runs are never a substitute for this independent-day evaluation.

Build future regime conditioning variables:

```bash
PYTHONPATH="$PWD/src" uv run --no-sync difflob-build-conditions
```

Run an existing training or sampling config:

```bash
PYTHONPATH="$PWD/src" uv run --no-sync difflob-diffusion -c config/AMZN/Diffusion/wavenet_motion_control/train.py
PYTHONPATH="$PWD/src" uv run --no-sync difflob-diffusion -c config/AMZN/Diffusion/wavenet_motion_control/sample.py
```

The old commands still work through compatibility wrappers under `legacy/`:

```bash
python legacy/diffusion_main.py -c config/AMZN/Diffusion/wavenet_motion_control/train.py
bash scripts/AMZN/diff_wavenet_motion_control.sh
```
