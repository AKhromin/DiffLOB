"""Generate one short sample from a one-day smoke-test checkpoint."""

import os
from pathlib import Path
import runpy


BaseConfiguration = runpy.run_path(str(Path(__file__).with_name("sample.py")))["Configuration"]


class Configuration(BaseConfiguration):
    def __init__(self):
        super().__init__()
        self.folder_path = os.environ.get(
            "DIFFLOB_DATA_DIR", "data/LOBSTER/LOBSTER_SampleFile_AMZN_2012-06-21_10"
        )
        self.single_day_split = True
        self.diff_model_saving_path = os.environ.get(
            "DIFFLOB_CHECKPOINT", "outputs/models/AMZN/difflob_sample_smoke.pth"
        )
        self.model_kwargs = {"base_channels": 8, "num_layers": 1, "num_heads": 1}
        self.AR = False
        self.max_sample_batches = 1
        self.samples_saving_path = os.environ.get(
            "DIFFLOB_SAMPLES_OUTPUT", "outputs/samples/AMZN/difflob_sample_smoke.npy"
        )
