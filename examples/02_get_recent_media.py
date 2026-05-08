from common import load_usernames, parser
from src.providers.factory import get_provider


args = parser("Get recent public posts and Reels").parse_args()
provider = get_provider(use_mock=args.mock)

for username in load_usernames(args.accounts):
    print(f"\n@{username}")
    for item in provider.get_recent_media(username, limit=args.limit):
        print(
            "- {kind:8} likes={likes:,} comments={comments:,} {caption}".format(
                kind=item.get("media_type", "post"),
                likes=int(item.get("like_count") or 0),
                comments=int(item.get("comment_count") or 0),
                caption=(item.get("caption") or "")[:80],
            )
        )

