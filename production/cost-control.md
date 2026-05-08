# Cost Control

Provider-backed reports can become expensive when account lists, retries, or schedule frequency grow. Estimate the workflow before turning on recurring runs.

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

## Provider Decision Point

Use a real public-data provider when your workflow needs fresh data, a recurring schedule, or client-facing exports. Compare options in `production/provider-comparison.md` before scaling.

HikerAPI is the first provider adapter included in this repo: https://hikerapi.com/p/ha4fn2v5

Disclosure: Some product links in this section may be affiliate links. If you buy through them, I may earn a commission at no extra cost to you. Recommendations only appear where they are directly relevant to the production workflow, and the open-source path remains documented.

## Reduce Waste

- Start with 3 to 5 public accounts.
- Cache raw provider responses where your terms allow it.
- Separate daily collection from weekly report rendering.
- Avoid retry storms by setting retry limits.
- Save failed inputs for replay instead of rerunning the full account list.
- Keep mock fixtures for local report template work.
