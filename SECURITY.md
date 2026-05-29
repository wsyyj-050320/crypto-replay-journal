# Security Policy

## Scope

Crypto Replay Journal is intended to be a local-first research, paper trading, replay, and journaling tool.

The public MVP should not store exchange API keys, place live orders, or manage user funds.

## Reporting Issues

If you find a security issue, please open a private disclosure channel before publishing details. If the project is hosted on GitHub, use GitHub private vulnerability reporting when available.

Do not include real API keys, webhook URLs, exchange secrets, or private trading records in public issues.

## Non-Goals

The public MVP does not provide:

- Financial advice.
- Trade instructions.
- Managed trading.
- Copy trading.
- Live order execution.

## Sensitive Data Rules

- Never commit secrets.
- Never commit real user artifacts.
- Never include private exchange account exports in examples.
- Keep sample data fictional unless explicitly documented otherwise.
