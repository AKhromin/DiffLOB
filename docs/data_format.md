# Data Format

The preprocessing path expects LOBSTER-style message and orderbook files in the configured `folder_path`.

The processed orderbook frame is converted into tensors with shape `[N, 20, 3]`:

- 20 price levels: 10 ask levels followed by 10 bid levels.
- 3 features per level: price, size, and side indicator.

Training windows are created from:

- `past_window`: historical context.
- `predict_window`: future trajectory target.
- regime summaries over the future window, including trend, volatility, liquidity, and imbalance.

