# Feishu / Lark Integration Guide

Feishu / Lark can be used as a lightweight reporting workspace for teams, agencies, and cross-border operators.

This guide focuses on manual and semi-automated report delivery.

## Best For

- Chinese cross-border ecommerce teams
- social media agencies
- internal operations teams
- client-facing weekly reports
- collaborative report review

## Recommended Workspace Structure

```text
Instagram Competitor Intelligence
|-- Competitor Database
|-- Weekly Reports
|-- Top Reels Table
|-- Hashtag Trends
|-- Creator Mentions
`-- Content Ideas
```

## Document: Weekly Report

Suggested sections:

```text
1. Executive Summary
2. Competitor Snapshot
3. Top Posts and Reels
4. Hashtag Trends
5. Creator / Brand Mentions
6. Recommended Actions
7. Raw Data
```

## Table: Competitor Database

| Field | Description |
| --- | --- |
| Brand | Competitor name |
| Username | Instagram username |
| Category | Direct / aspirational / fast-growing |
| Priority | High / Medium / Low |
| Notes | Analyst notes |

## Table: Top Reels

| Field | Description |
| --- | --- |
| Rank | Ranking |
| Account | Competitor account |
| Theme | Content theme |
| Engagement Rate | Public-data metric |
| Link | Public content URL |
| Takeaway | What to learn |

## Table: Hashtag Trends

| Field | Description |
| --- | --- |
| Hashtag | Hashtag |
| Frequency | Count |
| Related Accounts | Competitors using it |
| Theme | Content theme |
| Notes | Analyst notes |

## Manual Workflow

```text
1. Run the mock or provider-backed report workflow.
2. Generate Markdown / HTML report.
3. Export CSV metrics.
4. Copy the executive summary into Feishu.
5. Import CSV into Feishu tables.
6. Share the report with the team or client.
```

## Semi-Automated Workflow

A semi-automated setup may include:

```text
GitHub Actions
        ->
generated Markdown / HTML / CSV
        ->
manual review
        ->
Feishu report doc
        ->
team or client sharing
```

## Future Automation Ideas

Possible future improvements:

- Feishu webhook notification
- Feishu document creation API
- scheduled report delivery
- automatic CSV import
- report approval workflow

## Delivery Notes

For client-facing reports:

- review all recommendations before sending
- avoid including private data
- avoid unverified partnership claims
- include public links only when appropriate
- keep the executive summary short
