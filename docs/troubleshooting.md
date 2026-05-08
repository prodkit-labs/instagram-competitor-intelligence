# Troubleshooting

## The Mock Report Does Not Run

Run a syntax check first:

```bash
python3 -m compileall examples src
```

Then run the mock report:

```bash
python3 examples/06_generate_weekly_report.py --mock
```

If Python cannot import local modules, make sure you are running commands from the repository root.

## I Do Not See The Generated Report

The weekly report recipe writes files to:

```text
reports/sample_weekly_report.md
reports/sample_weekly_report.html
```

If the files are missing, rerun:

```bash
python3 examples/06_generate_weekly_report.py --mock
```

## My API Key Is Not Detected

For local development, copy the environment example:

```bash
cp .env.example .env
```

Set the provider-specific environment variable required by your adapter.

For the included HikerAPI adapter, use:

```text
INSTAGRAM_DATA_PROVIDER=hikerapi
HIKERAPI_KEY=your_api_key_here
```

Do not commit `.env`.

## GitHub Actions Does Not Run

Check that:

- Actions are enabled for the repository.
- `.github/workflows/weekly-report.yml` exists on the default branch.
- The mock workflow runs before trying provider-backed runs.
- Provider credentials are stored as GitHub Actions secrets, not source files.

You can start with the manual workflow trigger before relying on the schedule.

## The Report Is Empty

Check that:

- `data/sample_accounts.csv` contains account usernames.
- `data/sample_profiles.json` contains matching profile records.
- `data/sample_media.json` contains matching media records.
- media records include `username`, `caption`, `like_count`, and `comment_count`.
- provider-backed responses are normalized to the same shape as the mock fixtures.

## Provider-Backed Runs Fail

Start small:

1. Confirm the mock workflow succeeds.
2. Test one public account with the provider adapter.
3. Confirm the provider returns profile and media fields.
4. Check rate limits, provider status, and credentials.
5. Add retry and cost controls before scheduling recurring jobs.
