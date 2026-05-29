# Crypto Replay Journal

Open-source crypto paper trading, strategy replay, and risk journaling dashboard.

Crypto Replay Journal helps crypto traders review market anomalies, simulate entries and exits, track drawdowns, journal decisions, and generate daily research reports.

No directional calls. No performance promises. No financial advice.

## Positioning

This project is a research and review tool, not an automated trading bot.

It is designed for:

- Paper trading before risking real money.
- Reviewing historical market context candle by candle.
- Tracking fees, slippage, drawdown, win rate, and risk exposure.
- Building a disciplined trade journal.
- Producing daily market and trade review reports.

It is not designed for:

- Buy or sell recommendations.
- Copy trading.
- Guaranteed profitability claims.
- Fully automated live execution for end users.
- Financial or investment advice.

## MVP Modules

1. Dashboard
   - Market anomaly count.
   - Paper account equity curve.
   - Current drawdown.
   - Worst daily loss.
   - Recent simulated trades.
   - Daily risk level.

2. Market Anomaly Scanner
   - 24h and 1h move.
   - Volume expansion.
   - Volatility.
   - RSI and momentum context.
   - Overheat and risk labels.

3. Paper Trading
   - Virtual balance.
   - Entry, stop, target, trailing exit.
   - Fees and slippage.
   - PnL, win rate, payoff ratio, and drawdown.

4. Trade Journal
   - Entry reason.
   - Market structure.
   - Rule adherence.
   - Exit reason.
   - Review tags such as FOMO, overtrade, good exit, bad entry.

5. Strategy Replay
   - Replay a historical move candle by candle.
   - Compare fixed target, trailing exit, and no-stop scenarios.
   - Show maximum adverse excursion and preserved profit.

6. Daily Review Report
   - Market overview.
   - Top movers.
   - High-risk symbols.
   - Paper account performance.
   - Trade review and next-day watchlist.

## Safety Language

Use these terms:

- Market anomaly
- Momentum alert
- Volatility warning
- Risk score
- Paper trade
- Historical replay
- Daily review

Avoid these terms:

- Buy signal
- Sell signal
- Guaranteed return
- Profitable bot
- Copy trading
- Investment advice

## Demo

Open the product landing page:

```text
C:\crypto-replay-journal\index.html
```

Open the static product demo:

```text
C:\crypto-replay-journal\demo\index.html
```

Open the sample daily report:

```text
C:\crypto-replay-journal\reports\daily-review-sample.html
```

The demo uses fictional sample data for product design only.

## Launch Assets

Current public-facing assets:

- Social preview: `assets/social-og.png`
- Video thumbnail: `assets/video-thumbnail-clean.png`
- Silent promo video: `video/crypto-replay-journal-promo.mp4`
- Narrated promo video: `video/crypto-replay-journal-promo-narrated.mp4`
- Subtitles: `video/narration.srt`
- Homepage screenshot: `assets/screenshots/home.png`
- Product demo screenshot: `assets/screenshots/demo.png`
- Sample report screenshot: `assets/screenshots/report.png`

Build or refresh them with:

```bash
npm run build:assets
npm run build:narrated-video
```

## Roadmap

See:

- `docs/PRODUCT_PLAN.md`
- `docs/MIGRATION_PLAN.md`
- `docs/COMPLIANCE_BOUNDARY.md`
- `marketing/LAUNCH_COPY.md`
- `marketing/DEMO_STORYBOARD.md`
- `marketing/PUBLISHING_CHECKLIST.md`

## Disclaimer

For research and educational use only. Not financial advice. Crypto markets are risky, volatile, and can result in loss of capital. Paper trading, backtests, and historical replays do not prove future live performance.
