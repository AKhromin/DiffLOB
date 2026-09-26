"""Configurable CPU-friendly pipeline check using a LOBSTER sample.

This splits one day by time, so its validation loss is not a research result.
"""

import os
from pathlib import Path
import runpy


BaseConfiguration = runpy.run_path(str(Path(__file__).with_name("train.py")))["Configuration"]


def positive_int_setting(name, default):
    value = int(os.environ.get(name, default))
    if value < 1:
        raise ValueError(f"{name} must be at least 1")
    return value


class Configuration(BaseConfiguration):
    def __init__(self):
        super().__init__()
        self.folder_path = os.environ.get(
            "DIFFLOB_DATA_DIR", "data/LOBSTER/LOBSTER_SampleFile_AMZN_2012-06-21_10"
        )
        self.single_day_split = True
        self.n_epochs = positive_int_setting("DIFFLOB_EPOCHS", 1)
        self.training_batch_size = 2
        self.max_train_batches = positive_int_setting("DIFFLOB_TRAIN_BATCHES", 1)
        self.max_val_batches = positive_int_setting("DIFFLOB_VAL_BATCHES", 1)
        self.model_kwargs = {"base_channels": 8, "num_layers": 1, "num_heads": 1}
        self.diff_model_saving_path = os.environ.get(
            "DIFFLOB_CHECKPOINT", "outputs/models/AMZN/difflob_sample_smoke.pth"
        )
