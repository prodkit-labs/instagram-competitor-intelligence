# Production Provider Comparison

Use mock data first. Choose a real provider only when you need fresh public Instagram data for recurring reports, dashboards, or client-facing workflows.

This project supports mock data for local testing. For production workflows, you will need a reliable public-data provider or your own compatible data source.

## Decision Order

1. Run the mock workflow locally.
2. Define the public accounts and report cadence.
3. Estimate request volume and retry behavior.
4. Compare provider options against your workflow.
5. Start with a small account list before scheduling recurring jobs.

## Options

| Option | Best for | Pros | Cons |
| --- | --- | --- | --- |
| Mock fixtures | Learning and local demos | Free, no API key | Not live data |
| Bring your own provider | Teams with existing approved data access | Full control | Requires implementation and maintenance |
| Managed Instagram public-data API | Production reports | Faster setup, fewer moving parts | Ongoing API cost and provider dependency |
| Self-hosted collection infrastructure | Advanced teams | More operational control | More operational complexity and compliance responsibility |

## Included Adapter: HikerAPI

This repo includes a HikerAPI adapter in `src/providers/hikerapi.py`. It is one possible provider for public Instagram data, not a required dependency.

Use it when you want to:

- refresh competitor reports weekly or daily
- monitor real public brand accounts
- export recent posts and Reels data
- avoid maintaining your own data collection layer

HikerAPI: https://hikerapi.com/p/ha4fn2v5

Disclosure: Some product links in this section may be affiliate links. If you buy through them, I may earn a commission at no extra cost to you. Recommendations only appear where they are directly relevant to the production workflow, and the open-source path remains documented.

General disclosure: `../commercial-disclosure.md`.

## Bring Your Own Provider

Implement `src/providers/base.py` if you already have an approved data source.

Required methods:

- `get_profile(username)`
- `get_recent_media(username, limit=12)`

Return dictionaries matching the mock fixture shape in `data/sample_profiles.json` and `data/sample_media.json`.

## What Not To Do

- Do not collect Instagram credentials.
- Do not target private accounts.
- Do not automate follows, likes, comments, DMs, or fake engagement.
- Do not claim official affiliation with Instagram, Meta, or a data provider.
- Do not scale a provider-backed workflow before estimating cost and failure handling.
