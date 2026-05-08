import os

from src.providers.mock import MockInstagramProvider


def get_provider(use_mock=False):
    provider = os.getenv("INSTAGRAM_DATA_PROVIDER", "mock").lower()
    if use_mock or provider == "mock":
        return MockInstagramProvider()
    if provider == "hikerapi":
        from src.providers.hikerapi import HikerAPIProvider

        return HikerAPIProvider()
    raise ValueError(f"Unsupported provider: {provider}")
