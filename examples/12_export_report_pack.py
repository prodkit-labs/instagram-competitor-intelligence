import csv

from common import ROOT, load_profiles_and_media, parser
from src.metrics.competitors import compare_competitors
from src.metrics.engagement import enrich_media_with_engagement, rank_media
from src.metrics.hashtags import (
    extract_hashtags,
    extract_mentions,
    hashtag_counts,
    mention_counts,
)


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def joined(values):
    return ", ".join(str(value) for value in values if value)


def media_account_map(media_items, extractor):
    grouped = {}
    for item in media_items:
        for value in extractor(item.get("caption", "")):
            grouped.setdefault(value, set()).add(item["username"])
    return grouped


def top_matching_media(media_items, value, extractor):
    matches = [
        item for item in media_items if value in set(extractor(item.get("caption", "")))
    ]
    ranked = rank_media(matches, key="engagement_rate", limit=1)
    return ranked[0] if ranked else {}


args = parser("Export a multi-file report pack for spreadsheets and team tools").parse_args()
profiles, media = load_profiles_and_media(args.mock, args.accounts, args.limit)
profiles_by_username = {profile["username"]: profile for profile in profiles}
enriched = enrich_media_with_engagement(media, profiles_by_username)
competitors = compare_competitors(profiles, media)
top_media = rank_media(enriched, key="engagement_rate", limit=10)
top_reels = rank_media(enriched, key="engagement_rate", limit=10, media_type="reel")
hashtags = hashtag_counts(enriched)
mentions = mention_counts(enriched)
hashtag_accounts = media_account_map(enriched, extract_hashtags)
mention_accounts = media_account_map(enriched, extract_mentions)

output_dir = ROOT / "reports/export"

profile_rows = []
for profile in profiles:
    competitor = next(
        (row for row in competitors if row["username"] == profile["username"]),
        {},
    )
    profile_rows.append(
        {
            "username": profile["username"],
            "full_name": profile.get("full_name", profile["username"]),
            "follower_count": profile.get("follower_count", 0),
            "following_count": profile.get("following_count", 0),
            "media_count": profile.get("media_count", 0),
            "sample_media_count": competitor.get("media_count_sample", 0),
            "average_engagement_rate": competitor.get("average_engagement_rate", 0),
            "biography": profile.get("biography", ""),
            "is_verified": profile.get("is_verified", False),
            "profile_url": profile.get("profile_url", ""),
        }
    )

media_rows = [
    {
        "username": item.get("username"),
        "media_id": item.get("media_id"),
        "media_type": item.get("media_type"),
        "caption": item.get("caption"),
        "like_count": item.get("like_count"),
        "comment_count": item.get("comment_count"),
        "play_count": item.get("play_count"),
        "follower_count": item.get("follower_count"),
        "engagement_rate": item.get("engagement_rate"),
        "taken_at": item.get("taken_at"),
        "permalink": item.get("permalink"),
    }
    for item in enriched
]

top_reel_rows = []
for rank, item in enumerate(top_reels, start=1):
    top_reel_rows.append(
        {
            "rank": rank,
            "username": item.get("username"),
            "media_id": item.get("media_id"),
            "caption": item.get("caption"),
            "like_count": item.get("like_count"),
            "comment_count": item.get("comment_count"),
            "play_count": item.get("play_count"),
            "follower_count": item.get("follower_count"),
            "engagement_rate": item.get("engagement_rate"),
            "taken_at": item.get("taken_at"),
            "permalink": item.get("permalink"),
        }
    )

hashtag_rows = []
for rank, (tag, frequency) in enumerate(hashtags.most_common(25), start=1):
    top_item = top_matching_media(enriched, tag, extract_hashtags)
    hashtag_rows.append(
        {
            "rank": rank,
            "hashtag": tag,
            "frequency": frequency,
            "related_accounts": joined(sorted(hashtag_accounts.get(tag, []))),
            "top_media_id": top_item.get("media_id", ""),
            "top_media_permalink": top_item.get("permalink", ""),
        }
    )

mention_rows = []
for rank, (mention, frequency) in enumerate(mentions.most_common(25), start=1):
    top_item = top_matching_media(enriched, mention, extract_mentions)
    mention_rows.append(
        {
            "rank": rank,
            "mention": mention,
            "frequency": frequency,
            "mentioned_by": joined(sorted(mention_accounts.get(mention, []))),
            "top_media_id": top_item.get("media_id", ""),
            "top_media_permalink": top_item.get("permalink", ""),
        }
    )

top_competitor = competitors[0] if competitors else {}
top_item = top_media[0] if top_media else {}
top_hashtag = hashtags.most_common(1)[0][0] if hashtags else ""
top_mention = mentions.most_common(1)[0][0] if mentions else ""
weekly_summary_rows = [
    {
        "account_count": len(profiles),
        "media_count": len(enriched),
        "reel_count": len(
            [item for item in enriched if item.get("media_type") == "reel"]
        ),
        "top_account": top_competitor.get("username", ""),
        "top_account_average_engagement_rate": top_competitor.get(
            "average_engagement_rate", ""
        ),
        "top_media_id": top_item.get("media_id", ""),
        "top_media_engagement_rate": top_item.get("engagement_rate", ""),
        "top_hashtag": top_hashtag,
        "top_mention": top_mention,
        "note": "Sample fixture data is fictional when run with --mock.",
    }
]

write_csv(
    output_dir / "profiles.csv",
    [
        "username",
        "full_name",
        "follower_count",
        "following_count",
        "media_count",
        "sample_media_count",
        "average_engagement_rate",
        "biography",
        "is_verified",
        "profile_url",
    ],
    profile_rows,
)
write_csv(
    output_dir / "media_metrics.csv",
    [
        "username",
        "media_id",
        "media_type",
        "caption",
        "like_count",
        "comment_count",
        "play_count",
        "follower_count",
        "engagement_rate",
        "taken_at",
        "permalink",
    ],
    media_rows,
)
write_csv(
    output_dir / "top_reels.csv",
    [
        "rank",
        "username",
        "media_id",
        "caption",
        "like_count",
        "comment_count",
        "play_count",
        "follower_count",
        "engagement_rate",
        "taken_at",
        "permalink",
    ],
    top_reel_rows,
)
write_csv(
    output_dir / "hashtag_trends.csv",
    [
        "rank",
        "hashtag",
        "frequency",
        "related_accounts",
        "top_media_id",
        "top_media_permalink",
    ],
    hashtag_rows,
)
write_csv(
    output_dir / "creator_mentions.csv",
    [
        "rank",
        "mention",
        "frequency",
        "mentioned_by",
        "top_media_id",
        "top_media_permalink",
    ],
    mention_rows,
)
write_csv(
    output_dir / "weekly_summary.csv",
    [
        "account_count",
        "media_count",
        "reel_count",
        "top_account",
        "top_account_average_engagement_rate",
        "top_media_id",
        "top_media_engagement_rate",
        "top_hashtag",
        "top_mention",
        "note",
    ],
    weekly_summary_rows,
)

for path in sorted(output_dir.glob("*.csv")):
    print(f"Wrote {path}")
