from datetime import date

from src.metrics.hashtags import hashtag_counts, mention_counts


def pct(value):
    return f"{value * 100:.2f}%"


def render_markdown_report(
    profiles, enriched_media, competitor_rows, top_media, period=None
):
    period = period or "Sample period"
    hashtags = hashtag_counts(enriched_media).most_common(10)
    mentions = mention_counts(enriched_media).most_common(10)
    reels = [item for item in enriched_media if item.get("media_type") == "reel"]

    lines = [
        "# Weekly Instagram Competitor Report",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Period: {period}",
        "",
        "## Summary",
        "",
        f"- Tracked {len(profiles)} competitor accounts.",
        f"- Analyzed {len(enriched_media)} public posts and Reels.",
        f"- Reels in sample: {len(reels)}.",
        (
            f"- Top hashtag: #{hashtags[0][0]} ({hashtags[0][1]} mentions)."
            if hashtags
            else "- No hashtags found."
        ),
        "",
        "## Competitor Snapshot",
        "",
        "| Competitor | Followers | Sample Posts | Avg Engagement | Top Hashtags |",
        "| --- | ---: | ---: | ---: | --- |",
    ]

    for row in competitor_rows:
        lines.append(
            "| @{username} | {followers:,} | {posts} | {er} | {tags} |".format(
                username=row["username"],
                followers=row["follower_count"],
                posts=row["media_count_sample"],
                er=pct(row["average_engagement_rate"]),
                tags=row["top_hashtags"] or "-",
            )
        )

    lines.extend(
        [
            "",
            "## Top Performing Posts And Reels",
            "",
            "| Rank | Account | Type | Engagement | Likes | Comments | Caption |",
            "| ---: | --- | --- | ---: | ---: | ---: | --- |",
        ]
    )

    for index, item in enumerate(top_media, start=1):
        caption = (item.get("caption") or "").replace("\n", " ")
        if len(caption) > 90:
            caption = caption[:87] + "..."
        lines.append(
            "| {rank} | @{username} | {kind} | {er} | {likes:,} | {comments:,} | {caption} |".format(
                rank=index,
                username=item["username"],
                kind=item.get("media_type", "post"),
                er=pct(item.get("engagement_rate", 0)),
                likes=int(item.get("like_count") or 0),
                comments=int(item.get("comment_count") or 0),
                caption=caption or "-",
            )
        )

    lines.extend(["", "## Hashtag Trends", ""])
    for tag, count in hashtags:
        lines.append(f"- `#{tag}` appeared {count} times.")

    lines.extend(["", "## Creator And Brand Mentions", ""])
    if mentions:
        for mention, count in mentions:
            lines.append(f"- `@{mention}` appeared {count} times.")
    else:
        lines.append("- No creator mentions found in the sample captions.")

    lines.extend(
        [
            "",
            "## Recommended Actions",
            "",
            "1. Study the highest-engagement Reels and identify repeatable content formats.",
            "2. Test a UGC or creator-collaboration post if creator mentions appear frequently.",
            "3. Reuse promising hashtag clusters in a controlled content test.",
            "4. Track the same accounts weekly to build trend history instead of judging from one snapshot.",
            "",
            "## Notes",
            "",
            "This sample uses public data and mock fixtures by default. Replace the provider when using a production data source.",
        ]
    )
    return "\n".join(lines) + "\n"
