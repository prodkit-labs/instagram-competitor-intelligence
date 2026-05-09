# CSV Export Guide

CSV export is the simplest way to move workflow output into spreadsheets, dashboards, and reporting tools.

## Run CSV Export

```bash
python3 examples/07_export_csv.py --mock
```

Current output:

```text
reports/media_metrics.csv
```

This file contains one row per media record with engagement metrics that can be imported into Google Sheets, Excel, Notion, Feishu / Lark, or BI tools.

## Future Report Pack Outputs

The current recipe intentionally starts with a single CSV. A future report-pack exporter may split the workflow into multiple files:

```text
profiles.csv
media_metrics.csv
top_reels.csv
hashtag_trends.csv
creator_mentions.csv
weekly_summary.csv
```

## Suggested Columns

### profiles.csv

| Column | Description |
| --- | --- |
| username | Public account username |
| follower_count | Public follower count |
| media_count | Public media count |
| bio | Public profile biography |
| is_verified | Verification flag |

### media.csv

| Column | Description |
| --- | --- |
| media_id | Media identifier |
| username | Account username |
| media_type | Reel, post, carousel, image |
| caption | Public caption |
| like_count | Public like count |
| comment_count | Public comment count |
| engagement_rate | Directional public-data metric |
| taken_at | Publish timestamp |
| permalink | Public content link |

### hashtags.csv

| Column | Description |
| --- | --- |
| hashtag | Extracted hashtag |
| frequency | Number of appearances |
| related_accounts | Accounts using the hashtag |
| content_theme | Optional theme label |

## Recommended Workflow

```text
Generate report
        ->
Export CSV
        ->
Import into spreadsheet
        ->
Create summary tables
        ->
Use template for client or internal reporting
```

## Notes

CSV export is also useful for:

- Google Sheets
- Excel
- Notion database import
- Feishu / Lark table import
- BI dashboards
