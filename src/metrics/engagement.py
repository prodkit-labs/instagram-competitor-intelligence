def engagement_rate(media, follower_count):
    if not follower_count:
        return 0.0
    interactions = int(media.get("like_count") or 0) + int(media.get("comment_count") or 0)
    return interactions / follower_count


def enrich_media_with_engagement(media_items, profiles_by_username):
    enriched = []
    for item in media_items:
        profile = profiles_by_username.get(item["username"], {})
        row = dict(item)
        row["follower_count"] = profile.get("follower_count", 0)
        row["engagement_rate"] = engagement_rate(row, row["follower_count"])
        enriched.append(row)
    return enriched


def rank_media(media_items, key="engagement_rate", limit=10, media_type=None):
    rows = media_items
    if media_type:
        rows = [row for row in rows if row.get("media_type") == media_type]
    return sorted(rows, key=lambda row: row.get(key) or 0, reverse=True)[:limit]

