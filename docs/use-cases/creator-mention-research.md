# Creator Mention Research Workflow

This use case is for influencer marketing teams, brand researchers, agencies, and social media analysts who want to identify public creator and brand mentions in competitor content.

## Problem

Competitor creator activity is often difficult to track manually.

Teams may notice creator collaborations occasionally, but they rarely have a repeatable way to document:

- which creators competitors mention
- which creators appear repeatedly
- which posts include possible collaboration signals
- how creator-related posts perform
- which brands and creators appear together

## Goal

Detect public creator, influencer, and brand mentions from caption-style data and summarize them in a reporting workflow.

## Important Boundary

This workflow is for public mention research.

It is not a contact scraping tool.

It should not be used for:

- collecting private contact information
- scraping emails or phone numbers
- bulk DM outreach
- spam workflows
- private account monitoring
- harassment or aggressive outreach

## Workflow

```text
public captions
        ->
mention extraction
        ->
creator / brand grouping
        ->
related media records
        ->
engagement metrics
        ->
creator mention report
```

## Recommended Examples

```text
examples/09_extract_creator_mentions.py
examples/06_generate_weekly_report.py
examples/07_export_csv.py
```

## Suggested Output Table

| Mention | Mentioned By | Media Type | Engagement Rate | Content Link | Notes |
| --- | --- | --- | ---: | --- | --- |
| @creator_a | @brand_a | Reel | 8.4% | View | Possible creator collaboration |
| @creator_b | @brand_c | Post | 4.1% | View | Repeated mention |
| @brand_partner | @brand_b | Reel | 5.6% | View | Brand collaboration signal |

## Useful Questions

A creator mention report should help answer:

- Which creators are competitors mentioning?
- Are any creators mentioned repeatedly?
- Are creator-related posts performing well?
- Which brands appear together in captions?
- Are there collaboration patterns worth monitoring?
- Should the team keep watching specific creators?

## Example Summary

```text
This week, competitor captions included 7 public creator mentions across 3 accounts.

@creator_a appeared twice in high-engagement Reels from @brand_a.

@creator_b appeared in a lower-performing post but has been mentioned more than once over the last month.

Recommended action:

Continue monitoring @creator_a and @creator_b for future collaboration signals. Do not treat public mentions as confirmed paid partnerships without additional evidence.
```

## Recommended Actions

```text
1. Track repeated creator mentions over time.
2. Compare creator-related content against account averages.
3. Review whether creator mentions are linked to high-performing Reels.
4. Avoid assuming every mention is a paid collaboration.
5. Use findings as research notes, not as private contact data.
```

## Production Notes

If running this workflow repeatedly:

- store mention history by week
- group mentions by competitor account
- distinguish creator mentions from brand mentions
- avoid collecting private contact details
- document uncertainty in report notes
- export mention data to CSV for review

Related docs:

```text
docs/privacy-and-data-use.md
docs/metrics.md
docs/data-model.md
docs/production/observability.md
```

## What Not To Do

Do not use this workflow to:

- collect emails
- scrape private profiles
- send automated DMs
- build spam outreach lists
- imply confirmed partnerships without evidence
- violate platform policies or privacy laws

This workflow is intended for public research notes and competitor reporting.
