# Instagram Competitor Intelligence

Python recipes for Instagram competitor intelligence: public profiles, recent posts and Reels, engagement ranking, hashtag trends, creator mentions, CSV exports, weekly reports, and scheduled monitoring.

This is not an Instagram API wrapper and it is not an automation bot. It is a practical open-source starter for turning public Instagram data into competitor reports.

## Use Cases

- Track competitor posting cadence across public brand accounts
- Rank recent Reels and posts by engagement rate
- Extract recurring hashtag and content themes
- Detect creator, influencer, and brand mentions in captions
- Generate weekly Markdown and HTML competitor reports
- Schedule recurring reports with GitHub Actions or cron

## What You Can Build

- Weekly competitor reports for brands or agency clients
- Reels performance rankings
- Hashtag trend summaries
- Creator and influencer mention research
- CSV exports for spreadsheets and dashboards
- Scheduled reports with GitHub Actions or cron

## Quick Start

Run the sample report with mock data first. No API key is required.

```bash
python3 examples/06_generate_weekly_report.py --mock
```

The generated report will be written to:

```text
reports/sample_weekly_report.md
reports/sample_weekly_report.html
```

## Use Real API Data

Copy the environment example:

```bash
cp .env.example .env
```

Add your API key:

```text
INSTAGRAM_DATA_PROVIDER=hikerapi
HIKERAPI_KEY=your_api_key_here
```

Then run:

```bash
python3 examples/06_generate_weekly_report.py
```

## Data Source

The examples use HikerAPI as one possible provider for Instagram public data. You can replace it with any compatible source by implementing the provider interface in `src/providers/base.py`.

Provider website: https://hikerapi.com/p/ha4fn2v5

Disclosure: the HikerAPI link above is an affiliate link. If you sign up through it, I may earn a commission at no extra cost to you. The examples remain provider-based, and you can use any compatible public-data provider.

## Recipes

| Recipe | What it does |
| --- | --- |
| `examples/01_get_profile.py` | Get public profile fields for competitor accounts |
| `examples/02_get_recent_media.py` | Fetch recent public posts and Reels |
| `examples/03_rank_top_reels.py` | Rank Reels and posts by engagement |
| `examples/04_extract_hashtags.py` | Extract and rank hashtags from captions |
| `examples/05_compare_competitors.py` | Compare competitor accounts side by side |
| `examples/06_generate_weekly_report.py` | Generate a Markdown and HTML weekly report |
| `examples/07_export_csv.py` | Export profile and media metrics to CSV |
| `examples/08_schedule_with_github_actions.md` | Schedule reports with GitHub Actions |
| `examples/09_extract_creator_mentions.py` | Find creator and brand mentions in captions |
| `examples/10_estimate_api_cost.py` | Estimate API request usage and rough monthly cost |

## Example Report

See:

- `reports/sample_weekly_report.md`
- `reports/sample_weekly_report.html`

The report includes:

- competitor activity summary
- top posts and Reels
- hashtag trends
- creator mentions
- practical recommendations
- raw CSV-friendly metrics

## Ethical Use

This project is for public data analysis and reporting. Do not use it for:

- private account data
- Instagram credential collection
- auto-DM, spam, scraping abuse, fake engagement, or account automation
- claiming official affiliation with Instagram, Meta, or any data provider

## Project Status

This is an early starter for practical, public-data workflows around competitor monitoring, content research, and weekly reporting.

## Need Help?

Open an issue or discussion with the workflow you are trying to build. Keep requests focused on public data analysis and reporting.
