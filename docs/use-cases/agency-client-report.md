# Agency Client Report Workflow

This use case is for agencies, freelance marketers, social media consultants, and content strategy teams that need recurring competitor reports for clients.

## Problem

Agency client reports are often built manually.

A typical workflow looks like this:

1. Open multiple competitor Instagram profiles.
2. Check recent posts and Reels.
3. Copy links into a spreadsheet.
4. Guess which content performed best.
5. Take screenshots.
6. Write a summary for the client.
7. Repeat the same process every week.

This is workable once.

It becomes expensive and inconsistent when repeated across many clients.

## Goal

Use a repeatable workflow to generate a client-ready Instagram competitor report.

The report should help answer:

- What did competitors post this week?
- Which posts and Reels performed best?
- Which hashtags appeared repeatedly?
- Which creators or brands were mentioned?
- What content themes should the client consider testing next?

## Workflow

```text
client account
        ->
competitor list
        ->
public profile and media records
        ->
engagement metrics
        ->
top posts and Reels
        ->
hashtag trends
        ->
creator / brand mentions
        ->
client-ready weekly report
```

## Recommended Examples

Start with:

```bash
python3 examples/06_generate_weekly_report.py --mock
```

Useful files:

```text
examples/05_compare_competitors.py
examples/06_generate_weekly_report.py
examples/07_export_csv.py
examples/09_extract_creator_mentions.py
examples/11_agency_report_template.md
```

## Suggested Report Structure

```text
Agency Client Instagram Competitor Report

1. Executive Summary
2. Competitor Snapshot
3. Top Performing Posts and Reels
4. Hashtag Trends
5. Creator / Brand Mentions
6. Content Theme Summary
7. Recommended Actions
8. Raw Data Export
```

## Client-Ready Summary Example

```text
This week, we monitored 8 public competitor accounts and collected 96 recent posts and Reels.

The strongest content format was Reels, especially UGC-style product demonstrations and short before/after videos.

The most repeated hashtag themes were product demo, user review, and creator collaboration.

Recommended actions for next week:

1. Test one UGC-style Reel focused on product usage.
2. Repurpose the top competitor content theme into a carousel post.
3. Continue monitoring creator mentions from Brand A and Brand C.
```

## Useful Metrics

| Metric | Why It Matters |
| --- | --- |
| Posts this week | Shows competitor activity level |
| Engagement rate | Helps compare content across account sizes |
| Top-performing media | Identifies content worth studying |
| Hashtag frequency | Reveals repeated content themes |
| Creator mentions | Shows possible influencer or collaboration patterns |
| Content type distribution | Helps compare Reels, posts, carousels, and images |

## Production Notes

For production client reporting, review:

```text
docs/production/cost-control.md
docs/production/deployment.md
docs/production/observability.md
docs/production/provider-comparison.md
```

Important production decisions:

- report frequency
- number of client accounts
- number of competitor accounts
- data provider
- output format
- report delivery method
- retry policy
- cost estimate

## Output Options

Agency teams may want to export reports to:

- Markdown
- HTML
- CSV
- Google Sheets
- Notion
- Feishu / Lark
- client PDF reports
- internal dashboards

## What Not To Do

This workflow should not be used for:

- collecting private account data
- scraping private contact details
- bulk DM outreach
- fake engagement
- client reports that imply official Instagram or Meta affiliation

## Commercial Use

This workflow can be adapted into:

- one-time competitor analysis reports
- weekly client reports
- agency reporting templates
- white-label reports
- internal social media intelligence dashboards
