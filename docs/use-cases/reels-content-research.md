# Reels Content Research Workflow

This use case is for social media managers, content strategists, creators, and brand teams that want to study competitor Reels performance.

## Problem

Reels content research is often manual and subjective.

Common problems:

- teams save links without consistent metrics
- high-performing Reels are not compared across accounts
- content themes are not documented
- content ideas are based on memory
- weekly research is hard to repeat

## Goal

Use public-data style inputs to identify top-performing competitor Reels and turn them into a repeatable content research report.

## Workflow

```text
competitor accounts
        ->
recent Reels-style media
        ->
likes and comments
        ->
engagement rate
        ->
ranking
        ->
content theme notes
        ->
content ideas
```

## Recommended Examples

```text
examples/02_get_recent_media.py
examples/03_rank_top_reels.py
examples/04_extract_hashtags.py
examples/06_generate_weekly_report.py
```

## Core Metric

A simple public-data engagement rate can be calculated as:

```text
engagement_rate = (like_count + comment_count) / follower_count
```

This is a directional metric.

It does not include:

- reach
- impressions
- saves
- shares
- watch time
- paid promotion effects

Use it as a practical comparison signal, not a complete performance truth.

## Suggested Reels Research Table

| Field | Description |
| --- | --- |
| Account | Competitor account |
| Reel Link | Public content link |
| Publish Date | When the Reel was posted |
| Likes | Public like count |
| Comments | Public comment count |
| Engagement Rate | Directional public-data metric |
| Content Theme | Main topic or format |
| Hook | Opening idea or first-frame pattern |
| Caption Notes | Caption style and message |
| Hashtags | Extracted hashtags |
| Takeaway | What can be learned |

## Content Themes To Track

Common Reels themes include:

- product demo
- user review
- before and after
- founder story
- behind the scenes
- unboxing
- tutorial
- creator collaboration
- meme / trend adaptation
- lifestyle scene
- offer / promotion
- new product announcement

## Example Research Output

```text
Top Reels this week:

1. @brand_a - Product demo Reel - 8.4% engagement rate
2. @brand_b - UGC review Reel - 6.2% engagement rate
3. @brand_c - Before/after Reel - 5.8% engagement rate

Observed patterns:

- Short product demonstration formats performed well.
- UGC-style captions appeared in multiple top Reels.
- Competitors used fewer hashtags in top-performing Reels than in lower-performing posts.
- Creator collaboration content appeared twice in the top 10.
```

## Recommended Actions

A useful Reels research report should end with content ideas.

Example:

```text
Suggested content tests:

1. Create a 15-second product demo Reel.
2. Test a UGC-style review format.
3. Try a before/after visual comparison.
4. Repurpose top-performing caption structures.
5. Monitor creator collaboration Reels for another week.
```

## Production Notes

If you run this weekly, consider:

- limiting the number of recent media items per account
- storing raw media records
- exporting rankings to CSV
- separating Reels from other media types
- tracking account averages over time
- documenting content themes consistently

Related docs:

```text
docs/metrics.md
docs/data-model.md
docs/production/cost-control.md
```

## Boundary

This workflow is for public Reels-style content research.

It should not be used for:

- downloading private videos
- automating engagement
- reposting copyrighted content without permission
- bulk messaging creators
- claiming official Instagram or Meta affiliation
