# Deployment

Start with local runs and GitHub Actions. Add more infrastructure only when the report workflow is already useful.

## Local Cron

Use local cron when you are still testing account lists and report format.

```bash
python3 examples/06_generate_weekly_report.py --mock
```

## GitHub Actions

Use GitHub Actions when you want a simple recurring run and artifact upload.

The starter workflow lives at:

```text
.github/workflows/weekly-report.yml
```

For real provider-backed runs:

1. Add `HIKERAPI_KEY` as a repository secret.
2. Set `INSTAGRAM_DATA_PROVIDER=hikerapi`.
3. Start with a small account list.
4. Check the first artifact manually.

## Storage

Keep generated reports in a predictable artifact location. Avoid committing private client reports to a public repository.

For client work, store outputs in a private workspace, shared drive, or internal reporting system.

## Secrets

- Do not commit `.env`.
- Do not commit API keys.
- Use GitHub Actions secrets for scheduled provider-backed jobs.
- Rotate keys if logs or artifacts expose sensitive values.
