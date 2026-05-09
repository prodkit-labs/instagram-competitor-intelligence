import os

import requests

from src.providers.base import InstagramDataProvider


class HikerAPIProvider(InstagramDataProvider):
    """Provider adapter for HikerAPI public Instagram data endpoints."""

    def __init__(self, api_key=None, base_url="https://api.hikerapi.com"):
        self.api_key = api_key or os.getenv("HIKERAPI_KEY")
        if not self.api_key:
            raise ValueError("HIKERAPI_KEY is required for HikerAPIProvider")
        self.base_url = base_url.rstrip("/")
        self._profile_cache = {}

    def _get(self, path, params):
        response = requests.get(
            f"{self.base_url}{path}",
            params=params,
            headers={"x-access-key": self.api_key},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    def get_profile(self, username):
        if username in self._profile_cache:
            return dict(self._profile_cache[username])

        raw = self._get("/v1/user/by/username", {"username": username})
        if isinstance(raw, dict) and isinstance(raw.get("response"), dict):
            raw = raw["response"]
        if not isinstance(raw, dict):
            raise ValueError(f"Unexpected profile response for {username}")

        profile = {
            "username": raw.get("username", username),
            "full_name": raw.get("full_name") or raw.get("name") or username,
            "follower_count": raw.get("follower_count")
            or raw.get("followers_count")
            or 0,
            "following_count": raw.get("following_count")
            or raw.get("followings_count")
            or 0,
            "media_count": raw.get("media_count") or 0,
            "biography": raw.get("biography") or raw.get("bio") or "",
            "is_verified": bool(raw.get("is_verified", False)),
            "profile_url": f"https://www.instagram.com/{username}/",
            "raw": raw,
        }
        self._profile_cache[username] = profile
        return dict(profile)

    def _media_items(self, raw):
        if isinstance(raw, list):
            return raw
        if isinstance(raw, dict):
            items = raw.get("response") or raw.get("items") or []
            return items if isinstance(items, list) else []
        return []

    def _caption_text(self, item):
        caption = item.get("caption")
        if isinstance(caption, dict):
            return caption.get("text") or item.get("caption_text") or ""
        if isinstance(caption, str):
            return caption
        return item.get("caption_text") or ""

    def get_recent_media(self, username, limit=12):
        profile = self.get_profile(username)
        user_id = profile.get("raw", {}).get("pk") or profile.get("raw", {}).get("id")
        if not user_id:
            raise ValueError(f"Could not resolve user id for {username}")

        raw = self._get("/v1/user/medias/chunk", {"user_id": user_id, "limit": limit})
        items = self._media_items(raw)
        normalized = []
        for item in items[:limit]:
            if not isinstance(item, dict):
                continue
            caption = self._caption_text(item)
            media_type = (
                item.get("media_type_name")
                or item.get("product_type")
                or item.get("media_type")
                or "post"
            )
            code = item.get("code") or item.get("shortcode") or item.get("id")
            normalized.append(
                {
                    "username": username,
                    "media_id": str(item.get("id") or item.get("pk") or code),
                    "media_type": str(media_type).lower(),
                    "caption": caption,
                    "like_count": item.get("like_count") or 0,
                    "comment_count": item.get("comment_count") or 0,
                    "play_count": item.get("play_count") or item.get("view_count"),
                    "taken_at": item.get("taken_at") or item.get("taken_at_ts") or "",
                    "permalink": f"https://www.instagram.com/p/{code}/" if code else "",
                }
            )
        return normalized
