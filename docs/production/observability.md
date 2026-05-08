# Observability

Scheduled competitor reports need basic visibility. The first goal is to know whether the run happened, whether provider calls failed, and where the report artifact was saved.

## Minimum Signals

- run started
- accounts requested
- profiles fetched
- media items fetched
- provider errors
- retry count
- report files written
- artifact upload status

## GitHub Actions

The included workflow writes reports into `reports/` and uploads them as an artifact.

For scheduled runs, review:

- workflow status
- failed step logs
- artifact presence
- runtime duration

## Local Runs

For cron or local scripts, redirect logs to a file:

```bash
python3 examples/06_generate_weekly_report.py >> logs/report.log 2>&1
```

Store enough context to rerun failed accounts without repeating the entire job.

## Incident Notes

When a run fails, capture:

- provider
- account list
- schedule time
- error message
- retry behavior
- whether partial reports were generated
