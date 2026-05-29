# Contributing

Thanks for considering a contribution to Crypto Replay Journal.

This project is positioned as crypto research, paper trading, strategy replay, and risk journaling software. Contributions must preserve that boundary.

## Product Language Rules

Use:

- Market anomaly
- Risk context
- Volatility warning
- Paper trade
- Historical replay
- Daily review

Avoid:

- Trade instructions
- Performance certainty
- Managed execution
- Copy trading
- Investment advice

## Development Checks

Run before opening a pull request:

```bash
npm run format:check
npm run lint
npm run check
```

Refresh launch assets when screenshots, copy, or product UI changes:

```bash
npm run build:assets
npm run build:narrated-video
```

## Data Rules

- Do not commit exchange API keys, account exports, private logs, or real user trading records.
- Use fictional sample data or clearly marked public datasets.
- Keep fees, slippage, and drawdown assumptions visible in examples.

## Live Trading Boundary

Public MVP contributions must not add live order execution, exchange-account control, or user API-key handling. If those features are ever discussed, they must be separate, disabled by default, and protected by deterministic risk controls.
