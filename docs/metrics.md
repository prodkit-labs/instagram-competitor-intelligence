# Metrics

This project uses simple public-data metrics for reporting workflows.

The goal is not to produce a perfect source of marketing truth. The goal is to create repeatable, explainable signals for competitor research.

## Engagement Rate

The default engagement rate is:

```text
engagement_rate = (like_count + comment_count) / follower_count
```

The implementation lives in `src/metrics/engagement.py`.

## Why This Metric Is Useful

Engagement rate gives a rough way to compare public posts across accounts with different audience sizes.

For example, a post with fewer likes may still be more interesting if it performs strongly relative to the account's follower count.

## Limitations

This metric does not include:

- reach
- impressions
- saves
- shares
- story views
- paid promotion effects
- recommendation ranking
- audience quality
- account age or posting history

Use engagement rate as a directional signal, not as a complete performance truth.

## Ranking Media

The ranking helper sorts enriched media records by a selected key:

```text
rank_media(media_items, key="engagement_rate", limit=10)
```

You can also filter by media type, such as Reels:

```text
rank_media(media_items, media_type="reel")
```

## Hashtag Frequency

Hashtag frequency counts hashtags extracted from captions.

The extractor normalizes hashtags to lowercase and removes the `#` prefix.

Useful questions:

- Which tags repeat across competitors?
- Which tags appear in top-performing content?
- Which product or content themes are recurring?

## Creator Mention Frequency

Creator mentions count public `@username` mentions extracted from captions.

Useful questions:

- Which creators appear repeatedly?
- Which competitors use creator-led content?
- Which posts combine creator mentions and high engagement?

## Competitor Snapshot Metrics

The competitor comparison helper produces:

- username
- full name
- follower count
- sample media count
- total likes
- total comments
- average engagement rate
- top hashtags

These are starter metrics. Adapt them to your own provider fields, customer context, and reporting needs.
