# Weekly Report Automation Workflow

This use case is for teams that want to generate recurring Instagram competitor reports on a schedule.

It is especially useful for:

- agencies sending weekly client reports
- DTC brands monitoring competitors
- internal content teams
- social media analysts
- workflow automation builders

## Problem

A manual competitor report can be useful once.

The real value comes from repetition.

When the same workflow runs every week, teams can start tracking:

- competitor activity over time
- recurring content themes
- changes in hashtag usage
- top-performing content patterns
- creator mention trends
- report history

## Goal

Run the competitor reporting workflow on a recurring schedule and generate consistent Markdown / HTML / CSV outputs.

## Workflow

```text
competitor list
        ->
scheduled job
        ->
public-data provider or mock data
        ->
metrics and extraction
        ->
weekly report
        ->
artifact storage or delivery
```

## Start With Mock Data

Before scheduling provider-backed runs, make sure the mock workflow works:

```bash
python3 examples/06_generate_weekly_report.py --mock
```

Expected output:

```text
reports/sample_weekly_report.md
reports/sample_weekly_report.html
```

## GitHub Actions Scheduling

This project includes a GitHub Actions workflow example.

Relevant file:

```text
.github/workflows/weekly-report.yml
```

The scheduled workflow can be adapted to run:

- weekly
- daily
- monthly
- manually through workflow dispatch

## Suggested Schedule

For most teams, weekly is the best starting point.

```text
weekly report
lower cost
less noise
enough time to observe content patterns
```

Daily reports are useful only when:

- monitoring many competitors
- tracking campaigns
- watching launch activity
- supporting high-frequency agency reporting

## Production Checklist

Before running scheduled provider-backed reports:

- [ ] Mock workflow runs successfully.
- [ ] Competitor list is defined.
- [ ] Report frequency is defined.
- [ ] Provider choice is documented.
- [ ] API keys are stored as secrets.
- [ ] Cost estimate is calculated.
- [ ] Retry policy is defined.
- [ ] Report output location is defined.
- [ ] Failure notifications are considered.
- [ ] Data retention policy is documented.

## Cost Estimate

A simple request estimate:

```text
estimated_requests =
  competitors
  x endpoints_per_competitor
  x reports_per_month
  x retry_factor
```

Example:

```text
10 competitors
2 endpoints per competitor
4 weekly reports per month
1.2 retry factor

10 x 2 x 4 x 1.2 = 96 estimated requests / month
```

See:

```text
docs/production/cost-control.md
```

## Output Options

Scheduled reports can be stored or delivered as:

- GitHub Actions artifacts
- Markdown files
- HTML reports
- CSV exports
- Google Sheets imports
- Notion pages
- Feishu / Lark documents
- email attachments
- dashboard inputs

## Failure Scenarios

Common production failures:

### Provider Request Failed

Possible causes:

- provider outage
- rate limit
- invalid API key
- endpoint change
- retry limit reached

### Empty Report Generated

Possible causes:

- competitor list is empty
- media records are missing
- data provider returned incomplete records
- report date range is too narrow

### Cost Increased Unexpectedly

Possible causes:

- too many competitors
- too many scheduled runs
- retry factor too high
- no caching
- fetching too many media records per account

### Report Artifact Missing

Possible causes:

- workflow failed
- output path changed
- artifact upload step failed
- report generator wrote to a different directory

## Observability Notes

For production use, track:

- workflow run status
- report generation success
- failed accounts
- provider errors
- retry count
- estimated cost
- artifact location
- report freshness

See:

```text
docs/production/observability.md
```

## Recommended First Production Version

Start small.

```text
5 competitors
weekly schedule
2 endpoints per competitor
Markdown / HTML output
manual review before sending
```

Do not start with:

```text
100 competitors
daily reports
multiple clients
no cost estimate
no retry policy
no observability
```

## What This Can Become

This workflow can evolve into:

- weekly agency client reports
- internal competitor monitoring
- content strategy dashboards
- recurring research reports
- SaaS-style automated reporting
- white-label reporting systems
