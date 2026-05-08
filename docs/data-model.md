# Data Model

This document explains the sample data shape used by the workflow.

Provider adapters should normalize provider responses to this shape before passing data into metrics and reports.

## Profile Record

Profile records are stored in `data/sample_profiles.json`.

| Field | Type | Description |
| --- | --- | --- |
| `username` | string | Public account username without `@` |
| `full_name` | string | Display name |
| `follower_count` | integer | Public follower count |
| `following_count` | integer | Public following count |
| `media_count` | integer | Public media count |
| `biography` | string | Public profile biography |
| `is_verified` | boolean | Whether the account is verified |
| `profile_url` | string | Public profile URL |
| `raw` | object | Optional raw provider payload for debugging or custom mapping |

Example:

```json
{
  "username": "glossier",
  "full_name": "Glossier",
  "follower_count": 3200000,
  "following_count": 530,
  "media_count": 5400,
  "biography": "Skincare, makeup, body care and fragrance.",
  "is_verified": true,
  "profile_url": "https://www.instagram.com/glossier/"
}
```

## Media Record

Media records are stored in `data/sample_media.json`.

| Field | Type | Description |
| --- | --- | --- |
| `username` | string | Account that posted the media |
| `media_id` | string | Unique media identifier |
| `media_type` | string | Content type such as `reel`, `carousel`, or `image` |
| `caption` | string | Public caption text |
| `like_count` | integer | Public like count |
| `comment_count` | integer | Public comment count |
| `play_count` | integer or null | Public play/view count when available |
| `taken_at` | string | Publish timestamp or provider timestamp |
| `permalink` | string | Public content URL |

Example:

```json
{
  "username": "glossier",
  "media_id": "glossier_001",
  "media_type": "reel",
  "caption": "A dewy base routine with @creator_maya using Cloud Paint and Futuredew. #grwm #ugc #skincare",
  "like_count": 182000,
  "comment_count": 1850,
  "play_count": 2100000,
  "taken_at": "2026-05-02T14:30:00Z",
  "permalink": "https://www.instagram.com/reel/sample-glossier-001/"
}
```

## Account List

`data/sample_accounts.csv` contains the usernames used by examples.

The recipes expect a `username` column.

## Derived Fields

Metrics may add derived fields such as:

- `follower_count`
- `engagement_rate`
- `top_hashtags`
- `average_engagement_rate`

Derived fields should not be required from provider adapters.

## Report Outputs

The weekly report generator writes:

- `reports/sample_weekly_report.md`
- `reports/sample_weekly_report.html`

CSV export recipes can also produce spreadsheet-friendly metrics from the same normalized data.
