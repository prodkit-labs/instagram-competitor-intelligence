from abc import ABC, abstractmethod


class InstagramDataProvider(ABC):
    """Minimal provider interface used by the recipes."""

    @abstractmethod
    def get_profile(self, username):
        """Return a public profile dictionary for a username."""

    @abstractmethod
    def get_recent_media(self, username, limit=12):
        """Return recent public media dictionaries for a username."""
