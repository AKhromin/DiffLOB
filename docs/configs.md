# Configs

Configs live under `config/{ticker}/{model_family}/...`.

The current config files are Python modules exposing a `Configuration` class. They are intentionally left in place for compatibility with existing experiment scripts.

Common fields:

- `is_training`: switches between training and sampling.
- `folder_path`: raw LOBSTER data folder.
- `split_rate`: train, validation, and test split.
- `past_window`: context length used as model input.
- `predict_window`: future LOB trajectory length to generate.
- `store_length`: generated trajectory length saved by samplers.
- `training_batch_size` and `sampling_batch_size`: dataloader batch sizes.
- `*_saving_path`: model checkpoint or sample output path.

Longer-term cleanup can reduce duplication by introducing base configs per ticker and model family, then generating condition-specific configs from shared templates.

