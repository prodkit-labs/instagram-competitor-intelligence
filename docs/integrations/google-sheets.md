# Google Sheets Integration Guide

Google Sheets is a practical first step for turning competitor workflow outputs into a lightweight dashboard.

This guide assumes you are starting with CSV exports.

Generate the report pack:

```bash
python3 examples/12_export_report_pack.py --mock
```

## Recommended Sheets

Create a Google Sheet with these tabs:

```text
Competitor Accounts
Media Metrics
Top Reels
Hashtag Trends
Creator Mentions
Weekly Summary
```

## Tab 1: Competitor Accounts

| Column | Description |
| --- | --- |
| username | Competitor account |
| follower_count | Public follower count |
| posts_this_week | Number of posts this week |
| avg_engagement_rate | Average engagement rate |
| notes | Analyst notes |

## Tab 2: Media Metrics

| Column | Description |
| --- | --- |
| username | Account |
| media_type | Reel, post, carousel, image |
| caption | Caption |
| like_count | Likes |
| comment_count | Comments |
| engagement_rate | Directional metric |
| permalink | Link |

## Tab 3: Top Reels

Sort media records by engagement rate.

Recommended columns:

```text
rank
username
theme
hook
like_count
comment_count
engagement_rate
permalink
takeaway
```

## Tab 4: Hashtag Trends

Recommended columns:

```text
hashtag
frequency
related_accounts
content_theme
notes
```

## Tab 5: Creator Mentions

Recommended columns:

```text
mention
mentioned_by
media_type
engagement_rate
permalink
notes
```

## Tab 6: Weekly Summary

Use this tab for report writing.

```text
main finding
top content format
top competitor
top hashtag theme
notable creator mention
recommended actions
```

## Manual Workflow

```text
1. Run the report workflow.
2. Export the report pack.
3. Import `reports/export/*.csv` into matching Google Sheets tabs.
4. Refresh pivot tables or filters.
5. Write weekly summary.
6. Share with team or client.
```

## Future Automation Ideas

Possible future automations:

- Google Sheets API upload
- scheduled CSV refresh
- Apps Script report generation
- email delivery from Google Sheets
- Looker Studio dashboard
