# Migration Plan From Existing Research System

## Boundary

Do not modify the existing personal trading project during product extraction.

The existing project remains the private research and live-risk-control system. Crypto Replay Journal is a separate public-facing product folder.

## Source Capabilities To Reuse Later

Candidate modules from the existing system:

- Market scanner.
- Paper trading service.
- Replay utilities.
- Daily HTML report generation.
- Execution cost model.
- Drawdown and risk analytics.
- Trade journal model.

Do not migrate live automation, exchange account access, control tokens, or emergency-stop workflows into the public MVP.

## Phase 0: Product Wrapper

Status: started in this folder.

Deliverables:

- English README.
- Product plan.
- Compliance boundary.
- Launch copy.
- Static demo UI.

No source code copied from the private project.

## Phase 1: Sample Data MVP

Goal: make the app demoable without secrets or exchange credentials.

Deliverables:

- Sample market anomalies JSON.
- Sample paper trades JSON.
- Sample trade journal JSON.
- Static daily report output.
- Screenshot-ready dashboard.

Data must be marked as sample or simulated.

## Phase 2: Read-Only Engine Extraction

Goal: migrate only safe, read-only modules.

Allowed:

- Indicator calculations.
- Cost calculations.
- Replay calculations.
- Report rendering.
- Paper trading simulator.

Blocked:

- Live order placement.
- Binance account access.
- Control server.
- Webhook tokens.
- Any real API key or secret.
- Existing artifacts containing user trading data.

## Phase 3: Open-Source Repo

Goal: publish a clean public repository.

Checklist:

- No secrets.
- No real user artifacts.
- No live trading defaults.
- No private server paths.
- No claims of profitability.
- License selected.
- Contribution guide.
- Issue templates.
- Demo screenshots.

## Phase 4: Service Offers

Goal: monetize implementation help, not financial advice.

Offers:

- Local install support.
- VPS deployment.
- Report customization.
- Data source connector.
- Private dashboard.

All offers must say that setup support does not include investment advice or trade recommendations.

## Candidate Folder Structure

```text
crypto-replay-journal/
  README.md
  docs/
  marketing/
  demo/
  src/
    scanner/
    paper/
    journal/
    replay/
    reports/
    risk/
  sample_data/
  tests/
```

## Migration Acceptance Criteria

A migrated feature is acceptable only when:

- It runs without real exchange credentials.
- It uses sample or user-provided local data.
- It displays fees and slippage assumptions.
- It includes the research-only disclaimer.
- It does not emit buy or sell recommendations.
