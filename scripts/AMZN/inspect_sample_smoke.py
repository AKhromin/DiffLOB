"""Inspect a DiffLOB smoke sample and save a diagnostic plot."""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--input",
    type=Path,
    default=Path("outputs/samples/AMZN/difflob_sample_smoke.npy"),
    help="Generated .npy file",
)
args = parser.parse_args()
sample_path = args.input
plot_path = sample_path.with_suffix(".png")

samples = np.load(sample_path)
trajectories = samples.reshape(-1, *samples.shape[-3:])
trajectory = trajectories[0]
prices = trajectory[..., 0]
volumes = trajectory[..., 1]
best_ask = prices[:, 9]
best_bid = prices[:, 10]
crossed = int(np.count_nonzero(best_ask < best_bid))

fig, (price_ax, volume_ax) = plt.subplots(2, 1, figsize=(10, 7), layout="constrained")
steps = np.arange(len(trajectory))
price_ax.plot(steps, best_ask, label="Best ask")
price_ax.plot(steps, best_bid, label="Best bid")
price_ax.set(xlabel="Generated step", ylabel="Price", title="Smoke sample: best quoted prices")
price_ax.legend()
price_ax.grid(alpha=0.2)

image = volume_ax.imshow(
    np.log1p(volumes.T), aspect="auto", origin="upper", interpolation="nearest"
)
volume_ax.axhline(9.5, color="white", linestyle="--", linewidth=1)
volume_ax.set(
    xlabel="Generated step",
    ylabel="Book level (asks above, bids below)",
    title="Log-scaled generated volume",
)
fig.colorbar(image, ax=volume_ax, label="log(1 + volume)")
fig.suptitle(f"One-batch model diagnostic • crossed book at {crossed}/{len(trajectory)} steps")

plot_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(plot_path, dpi=160)
print(f"Saved {plot_path}")
print(f"Array shape: {samples.shape}; finite values: {bool(np.isfinite(samples).all())}")
print(f"Crossed book steps: {crossed}/{len(trajectory)}; maximum volume: {volumes.max():.0f}")
