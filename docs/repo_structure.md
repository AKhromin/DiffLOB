# Repository Structure

DiffLOB now uses a `src/` package layout so the research code is grouped by responsibility.

```text
src/difflob/
  cli/          command-line entrypoints
  data/         LOB preprocessing and data preparation
  diffusion/    SDEs, diffusion losses, and sampler utilities
  models/       diffusion architectures and baseline models
  sampling/     sampling loops for each model family
  training/     training loops for each model family
  utils/        shared tensor, config, and dataloader helpers
```

Historical files, such as `diffusion_main.py` and `vae_main.py`, are kept under `legacy/` as compatibility wrappers. New code should import from `difflob.*`.

Other top-level directories:

- `config/`: experiment configs organized by ticker, model family, and sampling condition.
- `scripts/`: shell launchers for existing experiment batches.
- `legacy/`: compatibility wrappers for older commands and imports.
- `docs/assets/`: README and documentation figures.
- `outputs/`: ignored local output area for checkpoints, samples, and logs.
