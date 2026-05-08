from common import load_profiles_and_media, parser
from src.metrics.competitors import compare_competitors

args = parser("Compare competitor accounts side by side").parse_args()
profiles, media = load_profiles_and_media(args.mock, args.accounts, args.limit)

for row in compare_competitors(profiles, media):
    print(
        "@{username:16} followers={followers:,} sample_posts={posts} avg_er={er:.2%} top_tags={tags}".format(
            username=row["username"],
            followers=row["follower_count"],
            posts=row["media_count_sample"],
            er=row["average_engagement_rate"],
            tags=row["top_hashtags"],
        )
    )
