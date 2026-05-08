# Cost Control

Provider-backed reports can become expensive when account lists, retries, or schedule frequency grow. Estimate the workflow before turning on recurring runs.

## Basic Formula

```text
estimated_requests =
  competitors * endpoints * report_frequency * retry_factor
```

Example:

```text
10 competitors
2 endpoints per competitor
4 weekly reports per month
1.2 retry factor

10 * 2 * 4 * 1.2 = 96 requests / month
```

### Example A: Small Weekly Report

```text
5 competitors
2 endpoints per competitor
4 weekly reports per month
1.2 retry factor

5 * 2 * 4 * 1.2 = 48 requests / month
```

### Example B: Agency Workflow

```text
50 competitors
2 endpoints per competitor
20 client reports per month
1.3 retry factor

50 * 2 * 20 * 1.3 = 2,600 requests / month
```

## Start With Mock Data

Run the report locally before using a real provider:

```bash
python3 examples/06_generate_weekly_report.py --mock
```

## Estimate Request Volume

Use the cost estimation helper:

```bash
python3 examples/10_estimate_api_cost.py --mock --runs-per-month 30 --requests-per-account 2
```

Track:

- accounts per report
- requests per account
- reports per month
- retry rate
- failed runs
- artifact storage needs

## Cost Factors

- number of competitor accounts
- number of media items fetched per account
- report frequency
- retry policy
- caching strategy
- provider pricing model

## Provider Decision Point

Use a real public-data provider when your workflow needs fresh data, a recurring schedule, or client-facing exports. Compare options in `provider-comparison.md` before scaling.

HikerAPI is the first provider adapter included in this repo: https://hikerapi.com/p/ha4fn2v5

Disclosure: Some product links in this section may be affiliate links. If you buy through them, I may earn a commission at no extra cost to you. Recommendations only appear where they are directly relevant to the production workflow, and the open-source path remains documented.

When comparing providers, look at:

- successful requests, not just raw requests
- latency
- retry cost
- monthly minimums
- rate limits
- data freshness
- endpoint coverage

## Reduce Waste

- Start with 3 to 5 public accounts.
- Cache raw provider responses where your terms allow it.
- Separate daily collection from weekly report rendering.
- Avoid retry storms by setting retry limits.
- Save failed inputs for replay instead of rerunning the full account list.
- Keep mock fixtures for local report template work.
