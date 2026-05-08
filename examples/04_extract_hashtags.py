from common import load_profiles_and_media, parser
from src.metrics.hashtags import hashtag_counts

args = parser("Extract and rank hashtags from captions").parse_args()
_, media = load_profiles_and_media(args.mock, args.accounts, args.limit)

for tag, count in hashtag_counts(media).most_common(20):
    print(f"#{tag}: {count}")
