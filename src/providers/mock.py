import json
from pathlib import Path

from src.providers.base import InstagramDataProvider

ROOT = Path(__file__).resolve().parents[2]


class MockInstagramProvider(InstagramDataProvider):
    """Offline provider backed by sample JSON data."""

    def __init__(self):
        self.profiles = self._load_json("data/sample_profiles.json")
        self.media = self._load_json("data/sample_media.json")

    def _load_json(self, path):
        with (ROOT / path).open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def get_profile(self, username):
        for profile in self.profiles:
            if profile["username"].lower() == username.lower():
                return dict(profile)
        raise ValueError(f"No mock profile for username: {username}")

    def get_recent_media(self, username, limit=12):
        rows = [
            dict(item)
            for item in self.media
            if item["username"].lower() == username.lower()
        ]
        return rows[:limit]
