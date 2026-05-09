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

## Run Report Pack Export

Use the report-pack exporter when you want one CSV per spreadsheet tab:

```bash
python3 examples/12_export_report_pack.py --mock
```

Outputs:

```text
reports/export/profiles.csv
reports/export/media_metrics.csv
reports/export/top_reels.csv
reports/export/hashtag_trends.csv
reports/export/creator_mentions.csv
reports/export/weekly_summary.csv
```

These files are designed for manual import into spreadsheets, lightweight BI tools, and team workspaces. When run with `--mock`, the exported data is fictional sample fixture data.

## Report Pack Files

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
| full_name | Public display name |
| follower_count | Public follower count |
| following_count | Public following count |
| media_count | Public media count |
| sample_media_count | Media records included in the run |
| average_engagement_rate | Average sample engagement rate |
| biography | Public profile biography |
| is_verified | Verification flag |
| profile_url | Public profile URL |

### media_metrics.csv

| Column | Description |
| --- | --- |
| media_id | Media identifier |
| username | Account username |
| media_type | Reel, post, carousel, image |
| caption | Public caption |
| like_count | Public like count |
| comment_count | Public comment count |
| play_count | Public play count when available |
| follower_count | Public follower count used for metric calculation |
| engagement_rate | Directional public-data metric |
| taken_at | Publish timestamp |
| permalink | Public content link |

### top_reels.csv

| Column | Description |
| --- | --- |
| rank | Rank within exported Reels |
| username | Account username |
| media_id | Media identifier |
| caption | Public caption |
| engagement_rate | Directional public-data metric |
| permalink | Public Reel link |

### hashtag_trends.csv

| Column | Description |
| --- | --- |
| hashtag | Extracted hashtag |
| frequency | Number of appearances |
| related_accounts | Accounts using the hashtag |
| top_media_permalink | Highest-ranking matching media link |

### creator_mentions.csv

| Column | Description |
| --- | --- |
| mention | Extracted public mention |
| frequency | Number of appearances |
| mentioned_by | Accounts using the mention |
| top_media_permalink | Highest-ranking matching media link |

### weekly_summary.csv

| Column | Description |
| --- | --- |
| account_count | Number of accounts in the run |
| media_count | Number of media records in the run |
| reel_count | Number of Reel records in the run |
| top_account | Highest average-engagement account in sample |
| top_media_id | Highest-ranking media record |
| top_hashtag | Most frequent hashtag in sample |
| top_mention | Most frequent mention in sample |
| note | Export note, including fictional-data notice for mock runs |

## Recommended Workflow

```text
Generate report
        ->
Export report pack
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
