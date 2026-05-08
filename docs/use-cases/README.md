# Use Cases

This directory explains practical ways to use Instagram Competitor Intelligence.

The project is designed as a workflow-first reporting starter. It can be adapted for different public-data reporting use cases, including agency reports, DTC brand monitoring, Reels research, hashtag trend tracking, creator mention research, and scheduled weekly reports.

## Use Case Index

| Use Case | Best For | Main Output |
| --- | --- | --- |
| Agency Client Report | Social media agencies, freelance marketers | Client-ready weekly competitor report |
| DTC Brand Monitoring | DTC brands, Shopify stores, cross-border ecommerce teams | Competitor content and strategy summary |
| Reels Content Research | Content teams, social media operators | Top-performing Reels and content ideas |
| Hashtag Trend Tracking | Social media managers, content strategists | Hashtag frequency and theme summary |
| Creator Mention Research | Influencer marketing teams, brand researchers | Public creator and brand mention notes |
| Weekly Report Automation | Teams that need recurring reports | Scheduled Markdown / HTML / CSV reports |

## Recommended Starting Point

If you want the fastest end-to-end demo, start with:

```bash
python3 examples/06_generate_weekly_report.py --mock
```

Then inspect:

```text
reports/sample_weekly_report.md
reports/sample_weekly_report.html
```

## How To Choose A Use Case

Start with the question you want the report to answer.

| Question | Suggested Use Case |
| --- | --- |
| How can I create weekly reports for clients? | Agency Client Report |
| What are my competitors posting? | DTC Brand Monitoring |
| Which Reels are performing best? | Reels Content Research |
| Which hashtags are competitors using repeatedly? | Hashtag Trend Tracking |
| Which creators or brands are being mentioned? | Creator Mention Research |
| How can I run this every week? | Weekly Report Automation |

## Public-Data Boundary

These workflows are designed for public-data reporting and analysis.

They are not designed for:

- private account monitoring
- Instagram password collection
- automated likes, follows, comments, or DMs
- fake engagement
- spam workflows
- bulk outreach
- claims of official affiliation with Instagram, Meta, or any provider

For more context, see:

- `docs/privacy-and-data-use.md`
- `SECURITY.md`
- `docs/production/provider-comparison.md`
