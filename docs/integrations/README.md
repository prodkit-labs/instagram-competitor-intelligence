# Integrations

This directory explains how to move report outputs into common team tools.

The project currently focuses on Markdown, HTML, and CSV-friendly outputs. These can be adapted into spreadsheets, documentation tools, email reports, and team workspaces.

## Integration Index

| Integration | Best For | Status |
| --- | --- | --- |
| CSV Export | Basic data export and spreadsheet workflows | Supported |
| Google Sheets | Team dashboards and manual reporting workflows | Guide |
| Notion | Lightweight content databases and report pages | Guide |
| Feishu / Lark | China-focused teams, agencies, and client reporting | Guide |
| Email Reports | Weekly reporting delivery | Guide |

## Recommended Starting Point

If you are delivering reports manually, start with:

```text
docs/integrations/csv-export.md
```

If you work with Chinese teams or cross-border operations, start with:

```text
docs/integrations/feishu-lark.md
```

If you want a spreadsheet dashboard, start with:

```text
docs/integrations/google-sheets.md
```

## Integration Philosophy

Start simple.

Recommended order:

```text
Markdown / HTML report
        ->
CSV export
        ->
manual spreadsheet import
        ->
team workspace
        ->
scheduled delivery
        ->
API-based automation
```

Do not automate too early.
