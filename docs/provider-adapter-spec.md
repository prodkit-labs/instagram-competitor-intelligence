# Provider Adapter Specification

This project separates reporting logic from data provider logic.

Provider adapters make it possible to:

- run with mock data
- use the included HikerAPI adapter
- bring your own approved data source
- keep reports and metrics provider-neutral

## Interface

Adapters implement `InstagramDataProvider` from `src/providers/base.py`.

```python
class InstagramDataProvider:
    def get_profile(self, username):
        """Return a public profile dictionary for a username."""

    def get_recent_media(self, username, limit=12):
        """Return recent public media dictionaries for a username."""
```

## Required Methods

### `get_profile(username)`

Returns one normalized profile record.

Expected fields:

- `username`
- `full_name`
- `follower_count`
- `following_count`
- `media_count`
- `biography`
- `is_verified`
- `profile_url`

Provider adapters may include an optional `raw` object for debugging or advanced mapping.

### `get_recent_media(username, limit=12)`

Returns a list of normalized media records.

Expected fields:

- `username`
- `media_id`
- `media_type`
- `caption`
- `like_count`
- `comment_count`
- `play_count`
- `taken_at`
- `permalink`

## Provider Selection

Provider selection lives in `src/providers/factory.py`.

The current selection flow is:

```text
--mock flag or INSTAGRAM_DATA_PROVIDER=mock -> MockInstagramProvider
INSTAGRAM_DATA_PROVIDER=hikerapi -> HikerAPIProvider
```

Unsupported provider names raise a `ValueError`.

## Adding A New Provider

1. Create a new provider file in `src/providers/`.
2. Implement `InstagramDataProvider`.
3. Normalize provider responses to the data model in `docs/data-model.md`.
4. Add provider selection logic in `src/providers/factory.py`.
5. Add environment variables to `.env.example` if needed.
6. Test with one public account before scheduling recurring jobs.

## Adapter Guidelines

- Keep API keys in environment variables or secrets.
- Normalize data inside the adapter, not inside report code.
- Return empty strings or zero values for missing optional metrics.
- Preserve raw provider payloads only when useful for debugging.
- Do not collect Instagram passwords or private account data.
- Do not add automation features for follows, likes, comments, or DMs.

## Testing A Provider Adapter

Start with:

```bash
python3 -m compileall examples src
python3 examples/01_get_profile.py
python3 examples/02_get_recent_media.py
python3 examples/06_generate_weekly_report.py
```

Use mock data first, then switch to a provider-backed run after credentials and provider limits are understood.
