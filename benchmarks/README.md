# Benchmarks

Benchmarks are designed to compare production workflows, not to declare a universal "best provider."

This project does not publish provider rankings without reproducible data.

Use this folder for benchmark notes only when the raw inputs and method can be shared.

Provider benchmark results should not be added unless:

- `benchmarks/raw/...csv` exists
- `benchmarks/scripts/...py` exists
- test date is recorded
- request count is recorded
- error definition is recorded
- affiliate disclosure is placed near any provider mention

## Benchmark Principles

- All raw data must be published in `benchmarks/raw/` when provider results are discussed.
- Scripts must be reproducible.
- Test date must be included.
- Request count must be included.
- Error definition must be included.
- Cost formula must be included.
- Affiliate links must be disclosed near any provider mention.
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

## Provider Benchmark Template

```text
Benchmark:
Test date:
Endpoint:
Request count:
Account sample:
Cache policy:
Retry policy:
Failure definition:
Latency metric:
Cost formula:
Raw data:
Script:
Limitations:
```

## First Benchmarks To Add

Start with local mock workflow benchmarks before publishing provider comparisons:

- `report_generation_mock_5_accounts`
- `report_generation_mock_50_media_items`
- `cost_estimation_example_runs`
