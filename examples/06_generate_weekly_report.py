from pathlib import Path

from common import ROOT, load_profiles_and_media, parser
from src.metrics.competitors import compare_competitors
from src.metrics.engagement import enrich_media_with_engagement, rank_media
from src.reports.html_report import markdown_to_simple_html
from src.reports.markdown_report import render_markdown_report

args = parser("Generate a weekly Instagram competitor report").parse_args()
profiles, media = load_profiles_and_media(args.mock, args.accounts, args.limit)
profiles_by_username = {profile["username"]: profile for profile in profiles}
enriched = enrich_media_with_engagement(media, profiles_by_username)
competitors = compare_competitors(profiles, media)
top_media = rank_media(enriched, key="engagement_rate", limit=10)

markdown = render_markdown_report(
    profiles,
    enriched,
    competitors,
    top_media,
    period="2026-05-01 to 2026-05-07",
)
html = markdown_to_simple_html(markdown)

reports_dir = ROOT / "reports"
reports_dir.mkdir(exist_ok=True)
(reports_dir / "sample_weekly_report.md").write_text(markdown, encoding="utf-8")
(reports_dir / "sample_weekly_report.html").write_text(html, encoding="utf-8")

print(f"Wrote {reports_dir / 'sample_weekly_report.md'}")
print(f"Wrote {reports_dir / 'sample_weekly_report.html'}")
