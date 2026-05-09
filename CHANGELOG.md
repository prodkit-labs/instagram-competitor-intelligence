# Changelog

## v0.5.0 - Report Pack Exporter

Added a multi-file CSV report-pack exporter for spreadsheet and team-workspace workflows.

New recipe:

- `examples/12_export_report_pack.py`

Generated files:

- `reports/export/profiles.csv`
- `reports/export/media_metrics.csv`
- `reports/export/top_reels.csv`
- `reports/export/hashtag_trends.csv`
- `reports/export/creator_mentions.csv`
- `reports/export/weekly_summary.csv`

Documentation updates:

- CSV export guide now documents both the existing single-file export and the report-pack exporter.
- Google Sheets and Feishu / Lark guides now point to the report-pack workflow.

## v0.4.1 - Quality Fix Pack

Quality fixes:

- Added `.env` loading for examples through `python-dotenv`.
- Replaced real-brand sample data with fictional demo brands.
- Hardened HikerAPI media response parsing and caption handling.
- Added per-run HikerAPI profile caching to avoid duplicate profile lookups.
- Updated README roadmap to reflect completed templates and integrations.
- Added a CI workflow for compile, mock report, CSV export, and cost-estimator checks.
- Clarified the current CSV output and future report-pack export direction.

## v0.4.0 - Templates & Integration Pack

Added reusable report templates and integration guides for turning workflow outputs into client-ready and team-ready deliverables.

New templates:

- agency weekly report
- DTC brand report
- Reels breakdown template
- hashtag trend template
- creator mention research template
- executive summary template
- service delivery checklist

New integration guides:

- CSV export
- Google Sheets
- Notion
- Feishu / Lark
- email reports

This release helps users move from running examples to delivering reports, organizing outputs, and building lightweight reporting workflows for teams or clients.

## v0.3.0 - Use Case Pack

Added practical use-case documentation for different reporting workflows:

- agency client reports
- DTC brand monitoring
- Reels content research
- hashtag trend tracking
- creator mention research
- weekly report automation

This release helps users map the starter project to real-world public-data reporting workflows before adding new product features.

## v0.2.0 - Trust & Documentation Pack

Added:

- privacy and data-use notes
- troubleshooting guide
- metrics documentation
- data model documentation
- provider adapter specification
- architecture overview

## v0.1.0 - Mock Report Workflow

Initial public starter for Instagram competitor intelligence workflows.

Includes:

- mock data workflow
- weekly Markdown / HTML report generator
- Reels and post engagement ranking
- hashtag trend extraction
- creator mention extraction
- CSV export
- GitHub Actions scheduled report example
- production provider comparison docs
- cost-control notes
- deployment and observability notes
- benchmark evidence rules
- commercial disclosure policy
- issue templates
