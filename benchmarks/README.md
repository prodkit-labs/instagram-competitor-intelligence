# Benchmarks

This project does not publish provider rankings without reproducible data.

Use this folder for benchmark notes only when the raw inputs and method can be shared.

## Benchmark Principles

- Record the account list shape without exposing private client data.
- Record run date, provider, request count, success rate, latency, and estimated cost.
- Keep raw benchmark data separate from marketing copy.
- Do not claim a provider is best without a reproducible scenario.
- Keep the open-source mock workflow documented even when provider-backed results are discussed.

## Suggested Metrics

| Metric | Why it matters |
| --- | --- |
| Success rate | Whether reports complete without missing accounts |
| Median latency | How long scheduled jobs take |
| Retry rate | Hidden driver of cost and delay |
| Cost per report | Useful for client or internal budgeting |
| Freshness | Whether data is recent enough for the workflow |

## Template

```text
Scenario:
Provider:
Run date:
Accounts:
Requests:
Success rate:
Median latency:
Retry rate:
Estimated cost:
Notes:
```
