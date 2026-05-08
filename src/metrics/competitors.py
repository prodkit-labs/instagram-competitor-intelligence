from collections import Counter, defaultdict

from src.metrics.engagement import engagement_rate
from src.metrics.hashtags import extract_hashtags


def compare_competitors(profiles, media_items):
    by_username = {profile["username"]: profile for profile in profiles}
    grouped = defaultdict(list)
    for item in media_items:
        grouped[item["username"]].append(item)

    rows = []
    for username, profile in by_username.items():
        media = grouped.get(username, [])
        total_likes = sum(int(item.get("like_count") or 0) for item in media)
        total_comments = sum(int(item.get("comment_count") or 0) for item in media)
        avg_er = 0.0
        if media:
            avg_er = sum(engagement_rate(item, profile.get("follower_count", 0)) for item in media) / len(media)

        hashtags = Counter()
        for item in media:
            hashtags.update(extract_hashtags(item.get("caption", "")))

        rows.append(
            {
                "username": username,
                "full_name": profile.get("full_name", username),
                "follower_count": profile.get("follower_count", 0),
                "media_count_sample": len(media),
                "total_likes": total_likes,
                "total_comments": total_comments,
                "average_engagement_rate": avg_er,
                "top_hashtags": ", ".join(tag for tag, _ in hashtags.most_common(5)),
            }
        )
    return sorted(rows, key=lambda row: row["average_engagement_rate"], reverse=True)

