from common import load_profiles_and_media, parser
from src.metrics.engagement import enrich_media_with_engagement, rank_media

args = parser("Rank top posts and Reels by engagement").parse_args()
profiles, media = load_profiles_and_media(args.mock, args.accounts, args.limit)
profiles_by_username = {profile["username"]: profile for profile in profiles}
enriched = enrich_media_with_engagement(media, profiles_by_username)

for item in rank_media(enriched, key="engagement_rate", limit=10):
    print(
        "@{username:16} {kind:8} engagement={er:.2%} likes={likes:,} comments={comments:,}".format(
            username=item["username"],
            kind=item.get("media_type", "post"),
            er=item.get("engagement_rate", 0),
            likes=int(item.get("like_count") or 0),
            comments=int(item.get("comment_count") or 0),
        )
    )
