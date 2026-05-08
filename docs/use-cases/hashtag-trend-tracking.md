# Hashtag Trend Tracking Workflow

This use case is for social media managers, content strategists, DTC brands, and agencies that want to understand hashtag patterns across public competitor content.

## Problem

Hashtags are often added manually and inconsistently.

Teams may know which hashtags they use, but they rarely track:

- which hashtags competitors use
- which hashtags appear repeatedly
- which hashtags are tied to high-performing content
- which hashtag groups belong to content themes
- which hashtags are brand-specific, category-specific, or campaign-specific

## Goal

Extract hashtags from public captions and summarize recurring patterns across competitor accounts.

## Workflow

```text
public captions
        ->
hashtag extraction
        ->
frequency count
        ->
account grouping
        ->
theme grouping
        ->
hashtag trend report
```

## Recommended Examples

```text
examples/04_extract_hashtags.py
examples/05_compare_competitors.py
examples/06_generate_weekly_report.py
examples/07_export_csv.py
```

## Suggested Hashtag Categories

### Brand Hashtags

Used by a specific brand or campaign.

```text
#brandname
#brandcommunity
#brandcampaign
```

### Category Hashtags

Used across a market category.

```text
#skincare
#activewear
#homedecor
#petproducts
```

### Content Format Hashtags

Used to describe the content format.

```text
#productdemo
#beforeafter
#ugc
#unboxing
#tutorial
```

### Campaign Or Seasonal Hashtags

Used for time-sensitive activity.

```text
#blackfriday
#holidaygift
#newdrop
#summerlaunch
```

## Suggested Output Table

| Hashtag | Frequency | Related Accounts | Content Theme | Notes |
| --- | ---: | --- | --- | --- |
| #ugc | 18 | @brand_a, @brand_c | User-generated content | Often appears in review-style posts |
| #productdemo | 12 | @brand_b | Product demonstration | Common in Reels |
| #beforeafter | 9 | @brand_a | Transformation content | Performs well in visual formats |

## Useful Questions

A hashtag trend report should help answer:

- Which hashtags appear most often?
- Which competitors use the same hashtags?
- Which hashtags are tied to high-performing posts?
- Which hashtags are generic and possibly low-value?
- Which hashtag groups match content themes?
- Which hashtags should be tested next week?

## Example Summary

```text
This week, hashtag usage concentrated around UGC, product demo, and before/after content.

The hashtag #ugc appeared across 3 competitor accounts and was often attached to higher-performing Reels.

The hashtag #productdemo appeared mostly in short-form video captions.

Brand-specific hashtags were less frequent than category and content-format hashtags.
```

## Recommended Actions

```text
1. Build a small hashtag set around UGC and product demo content.
2. Avoid relying only on generic category hashtags.
3. Track whether high-frequency hashtags are also tied to high engagement.
4. Review hashtag patterns weekly instead of treating hashtag lists as static.
```

## Production Notes

For recurring hashtag tracking:

- keep raw captions
- track hashtags by week
- group hashtags by content theme
- export frequency tables to CSV
- compare hashtag frequency against content performance
- avoid assuming frequency equals effectiveness

Related docs:

```text
docs/metrics.md
docs/data-model.md
docs/production/cost-control.md
```

## Boundary

This workflow analyzes public captions.

It should not be used for:

- private account monitoring
- spam hashtag generation
- automated posting
- fake engagement
- misleading growth claims
