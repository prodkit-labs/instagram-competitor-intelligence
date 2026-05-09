# CSV Export Guide

CSV export is the simplest way to move workflow output into spreadsheets, dashboards, and reporting tools.

## Run CSV Export

```bash
python3 examples/07_export_csv.py --mock
```

## Suggested CSV Outputs

Depending on your workflow, useful CSV files may include:

```text
profiles.csv
media.csv
top_reels.csv
hashtags.csv
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
