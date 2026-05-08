# Data Sources

This project is provider-based. The examples can run with mock data or with a real public Instagram data provider.

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

The first real provider adapter is `src/providers/hikerapi.py`.

Set:

```text
INSTAGRAM_DATA_PROVIDER=hikerapi
HIKERAPI_KEY=your_api_key_here
```

Provider website: https://hikerapi.com/p/ha4fn2v5

Disclosure: the HikerAPI link above is an affiliate link. If you sign up through it, I may earn a commission at no extra cost to you. The examples remain provider-based, and you can use any compatible public-data provider.

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
