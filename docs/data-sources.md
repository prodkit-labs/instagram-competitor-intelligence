# Data Sources and Provider Setup

This project is provider-based. The examples can run with mock data or with a real public Instagram data provider.

Mock data is the default path, so you can try the report workflow without any API key.

## Option A: Mock Data

Use mock data when you want to try the project without any API key:

```bash
python3 examples/06_generate_weekly_report.py --mock
```

Mock fixtures live in:

```text
data/sample_profiles.json
data/sample_media.json
data/sample_accounts.csv
```

## Option B: HikerAPI

For real public Instagram data, the first provider adapter included in this repo is HikerAPI. You can also implement your own provider by following `src/providers/base.py`.

Set:

```text
INSTAGRAM_DATA_PROVIDER=hikerapi
HIKERAPI_KEY=your_api_key_here
```

Use a real public-data provider when you want to:

- monitor real competitor accounts
- refresh reports weekly or daily
- export live posts and Reels data
- build dashboards for clients or internal teams
- compare public brand accounts over time

For production provider tradeoffs, see `production/provider-comparison.md`.

## Option C: Bring Your Own Provider

Implement:

```text
src/providers/base.py
```

Required methods:

- `get_profile(username)`
- `get_recent_media(username, limit=12)`

Return dictionaries matching the mock fixture shape.

## Cost Control

Before scheduling daily jobs, estimate expected requests:

```bash
python3 examples/10_estimate_api_cost.py --mock --runs-per-month 30 --requests-per-account 2
```

Start with small account lists, cache data when possible, and avoid unnecessary repeat requests.
