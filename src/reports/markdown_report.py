from datetime import date

from src.metrics.hashtags import hashtag_counts, mention_counts


def pct(value):
    return f"{value * 100:.2f}%"


def count_word(count):
    return "time" if count == 1 else "times"


def recommended_actions(enriched_media, hashtags, mentions):
    actions = []
    total = len(enriched_media)
    reels = [item for item in enriched_media if item.get("media_type") == "reel"]
    if total and reels:
        actions.append(
            f"Prioritize Reels analysis because Reels represent {len(reels)} of {total} analyzed media records."
        )
    elif total:
        actions.append(
            f"Compare content formats across all {total} analyzed media records before choosing a testing theme."
        )

    if hashtags:
        top_tags = ", ".join(f"#{tag}" for tag, _ in hashtags[:3])
        actions.append(
            f"Test content themes around {top_tags} because they appear most often in the sample."
        )

    repeated_mentions = [mention for mention, count in mentions if count > 1]
    if repeated_mentions:
        top_mentions = ", ".join(f"@{mention}" for mention in repeated_mentions[:3])
        actions.append(
            f"Continue monitoring {top_mentions} because they appear multiple times in competitor captions."
        )
    else:
        actions.append(
            "Track creator mentions weekly to identify repeated collaborations instead of judging from one snapshot."
        )

    actions.append(
        "Review the highest-engagement posts and turn the strongest formats into a controlled content test."
    )
    return actions


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
        "- Sample data is fictional and does not represent actual brand metrics.",
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
        lines.append(f"- `#{tag}` appeared {count} {count_word(count)}.")

    lines.extend(["", "## Creator And Brand Mentions", ""])
    if mentions:
        for mention, count in mentions:
            lines.append(f"- `@{mention}` appeared {count} {count_word(count)}.")
    else:
        lines.append("- No creator mentions found in the sample captions.")

    actions = recommended_actions(enriched_media, hashtags, mentions)
    lines.extend(
        [
            "",
            "## Recommended Actions",
            "",
            *[f"{index}. {action}" for index, action in enumerate(actions, start=1)],
            "",
            "## Notes",
            "",
            "This sample uses fictional public-style data by default. Replace the provider when using a production data source.",
        ]
    )
    return "\n".join(lines) + "\n"
