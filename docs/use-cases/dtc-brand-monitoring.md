# DTC Brand Monitoring Workflow

This use case is for DTC brands, Shopify stores, cross-border ecommerce teams, and social media operators that want to monitor public competitor activity on Instagram.

## Problem

Brand teams often know they should watch competitors, but the process is usually informal.

Common problems:

- competitor observations are scattered
- screenshots are hard to compare over time
- Reels performance is checked manually
- hashtag patterns are not tracked
- content ideas are based on memory instead of repeatable reporting

## Goal

Create a repeatable competitor monitoring workflow for brand teams.

The report should help answer:

- What are competitors posting this week?
- Which content formats are performing best?
- Which Reels or posts should we study?
- Which hashtags are competitors using repeatedly?
- Are competitors working with creators or influencers?
- What should we test in our own content plan?

## Workflow

```text
brand category
        ->
competitor account list
        ->
public posts and Reels
        ->
engagement ranking
        ->
hashtag trend summary
        ->
creator mention notes
        ->
weekly brand monitoring report
```

## Suggested Competitor List

Start with 5 to 10 competitor accounts.

A useful list might include:

- direct product competitors
- brands in the same category
- aspirational brands
- fast-growing challenger brands
- creator-led brands
- brands using similar content formats

## Recommended Examples

```text
examples/02_get_recent_media.py
examples/03_rank_top_reels.py
examples/04_extract_hashtags.py
examples/05_compare_competitors.py
examples/06_generate_weekly_report.py
examples/09_extract_creator_mentions.py
```

Run the full mock report:

```bash
python3 examples/06_generate_weekly_report.py --mock
```

## Suggested Report Sections

```text
DTC Brand Competitor Monitoring Report

1. Weekly Summary
2. Competitor Activity
3. Top Performing Posts and Reels
4. Content Theme Analysis
5. Hashtag Trends
6. Creator / Influencer Mentions
7. Recommended Content Ideas
8. Raw Metrics
```

## Questions The Report Should Answer

### 1. What Did Competitors Post?

Track:

- number of posts
- number of Reels
- number of carousels
- content themes
- publishing frequency

### 2. Which Content Performed Best?

Rank content by:

- likes
- comments
- engagement rate
- content type
- account size

### 3. Which Themes Repeated?

Look for themes like:

- product demo
- user review
- before and after
- founder story
- lifestyle scene
- giveaway
- creator collaboration
- new product drop

### 4. Which Hashtags Appeared Repeatedly?

Track:

- brand hashtags
- category hashtags
- content format hashtags
- campaign hashtags
- seasonal hashtags

### 5. Are There Creator Collaboration Signals?

Look for:

- creator mentions
- tagged creators
- repeated creator names
- captions referencing collaborations
- content formats that look like UGC or influencer content

## Example Brand Summary

```text
This week, competitor activity was concentrated around short Reels and UGC-style product demonstrations.

Brand A posted fewer times but had the strongest engagement rate. Their highest-performing Reel used a simple product demo format with a short caption and three category hashtags.

Brand B posted more frequently but had lower average engagement.

Brand C showed signs of creator collaboration, with multiple posts mentioning the same creator account.

Suggested next steps:

1. Test one product demo Reel.
2. Create a UGC-style review post.
3. Monitor Brand C's creator mentions for two more weeks.
```

## Production Notes

For recurring monitoring, decide:

- how many competitors to track
- how often to generate reports
- whether reports should be weekly or monthly
- whether results should be exported to CSV, HTML, or a dashboard
- whether the workflow should run manually or on a schedule

Related docs:

```text
docs/production/cost-control.md
docs/production/deployment.md
docs/production/observability.md
```

## What Not To Do

Do not use this workflow for:

- fake engagement
- automated social actions
- private account monitoring
- collecting private contact information
- bulk outreach
- spam workflows

This workflow is intended for public content analysis and brand reporting.
