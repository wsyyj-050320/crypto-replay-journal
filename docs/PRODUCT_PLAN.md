# Product Plan

## Product Name

Primary name: Crypto Replay Journal

Alternative internal descriptor: Crypto Strategy Replay & Risk Journal

## One-Line Description

An open-source crypto paper trading, strategy replay, and risk journaling dashboard for reviewing decisions, exits, drawdowns, and trading discipline.

## Product Thesis

Crypto traders do not only need another signal. They need a better way to review decisions, understand risk, and stop repeating avoidable mistakes.

The product should feel like a research notebook and risk console, not a profit machine.

## Audience

Primary:

- Self-directed crypto traders.
- Quant hobbyists.
- TradingView users who want more realistic review workflows.
- Developers building personal paper trading systems.

Secondary:

- Small research groups.
- Educators producing trading-risk examples.
- Operators who want self-hosted reporting.

## Core Promise

Review crypto trades with better context:

- What moved?
- What was the risk?
- What would a stop or trailing exit have done?
- Did the paper trade follow the plan?
- Was the loss caused by the setup, execution cost, market regime, or behavior?

## Non-Promises

The product must not promise:

- Profitability.
- Accuracy.
- Market prediction.
- Trade recommendations.
- Automated execution safety.

## MVP Scope

### Dashboard

Goal: first-screen credibility for a demo video.

Must show:

- Market anomalies today.
- Paper account equity curve.
- Current maximum drawdown.
- Worst daily loss.
- Recent paper trades.
- Risk level.
- Research-only disclaimer.

### Market Anomaly Scanner

Goal: replace signal language with neutral market monitoring.

Must show:

- Symbol.
- 1h and 24h move.
- Volume expansion.
- Volatility.
- RSI or momentum context.
- Risk score.
- Label such as Overheated, Expanding Volume, Volatility Spike.

Must not show:

- Buy signal.
- Sell signal.
- Entry recommendation.

### Paper Trading

Goal: make simulated execution realistic enough to be useful.

Must include:

- Virtual capital.
- Entry, stop, target, and exit rules.
- Fees.
- Slippage.
- Quantity precision.
- Minimum notional.
- Trade PnL.
- Equity curve.

### Trade Journal

Goal: make behavior and process review monetizable.

Must include:

- Entry reason.
- Exit reason.
- Plan adherence.
- Emotion or behavior tags.
- Screenshot or chart reference later.
- Post-trade note.

### Strategy Replay

Goal: create the strongest product differentiation.

Must include:

- Historical candle sequence.
- Replay speed.
- Volume and volatility context.
- Fixed target comparison.
- Trailing exit comparison.
- No-stop risk comparison.
- Maximum adverse excursion.

### Daily Review Report

Goal: create a shareable artifact.

Must include:

- Market overview.
- Top anomalies.
- High-risk watchlist.
- Paper trading performance.
- Largest loss explanation.
- Tomorrow watchlist.
- Disclaimer.

## Product Architecture Direction

The new product should start as a separate open-source app that can later import selected modules from the existing research system.

Recommended phases:

1. Static demo and product copy.
2. Local-only data model with sample CSV/JSON.
3. Read-only market scanner import.
4. Paper trading import.
5. Daily report generator import.
6. Optional self-hosted API.

Live execution should remain out of scope for the public MVP.

## Monetization

Start with services before SaaS:

- Local setup help: 29-99 USD.
- VPS private deployment: 99-299 USD.
- Exchange data connector: 99-499 USD.
- Custom report template: 49-199 USD.
- Small team dashboard: 300-1500 USD.

Later Pro features:

- Cloud sync.
- Multi-device history.
- Advanced drawdown analytics.
- Telegram or Discord risk reminders.
- Automated daily email reports.
- Docker one-click deployment.
- Private strategy templates for review only.

## Success Metrics

Early:

- GitHub stars.
- Demo video completion rate.
- Test users.
- Issues opened.
- Screenshots shared.

Product:

- Number of journal entries.
- Number of completed replays.
- Number of daily reports generated.
- Repeat weekly active users.

Avoid measuring success by claimed user profitability.
