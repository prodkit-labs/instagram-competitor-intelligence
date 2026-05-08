import csv

from common import ROOT, load_profiles_and_media, parser
from src.metrics.engagement import enrich_media_with_engagement

args = parser("Export media metrics to CSV").parse_args()
profiles, media = load_profiles_and_media(args.mock, args.accounts, args.limit)
profiles_by_username = {profile["username"]: profile for profile in profiles}
enriched = enrich_media_with_engagement(media, profiles_by_username)

output = ROOT / "reports/media_metrics.csv"
output.parent.mkdir(exist_ok=True)

fields = [
    "username",
    "media_id",
    "media_type",
    "like_count",
    "comment_count",
    "play_count",
    "follower_count",
    "engagement_rate",
    "taken_at",
    "permalink",
]
with output.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    for item in enriched:
        writer.writerow({field: item.get(field) for field in fields})

print(f"Wrote {output}")
