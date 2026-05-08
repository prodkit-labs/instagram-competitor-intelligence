from common import load_usernames, parser
from src.providers.factory import get_provider

args = parser("Get public profile data for competitor accounts").parse_args()
provider = get_provider(use_mock=args.mock)

for username in load_usernames(args.accounts):
    profile = provider.get_profile(username)
    print(
        "{username:20} followers={followers:,} verified={verified}".format(
            username=profile["username"],
            followers=profile.get("follower_count", 0),
            verified=profile.get("is_verified", False),
        )
    )
