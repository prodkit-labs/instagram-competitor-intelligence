from common import load_profiles_and_media, parser
from src.metrics.hashtags import mention_counts


args = parser("Extract creator and brand mentions from captions").parse_args()
_, media = load_profiles_and_media(args.mock, args.accounts, args.limit)

for mention, count in mention_counts(media).most_common(20):
    print(f"@{mention}: {count}")

