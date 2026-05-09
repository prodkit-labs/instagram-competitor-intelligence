import argparse
import csv
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

if load_dotenv:
    load_dotenv(ROOT / ".env")

from src.providers.factory import get_provider


def parser(description):
    arg_parser = argparse.ArgumentParser(description=description)
    arg_parser.add_argument("--mock", action="store_true", help="Use local sample data")
    arg_parser.add_argument(
        "--accounts",
        default=str(ROOT / "data/sample_accounts.csv"),
        help="CSV file with a username column",
    )
    arg_parser.add_argument(
        "--limit", type=int, default=12, help="Media items per account"
    )
    return arg_parser


def load_usernames(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [row["username"] for row in reader if row.get("username")]


def load_profiles_and_media(use_mock=False, accounts_path=None, limit=12):
    provider = get_provider(use_mock=use_mock)
    usernames = load_usernames(accounts_path or ROOT / "data/sample_accounts.csv")
    profiles = [provider.get_profile(username) for username in usernames]
    media = []
    for username in usernames:
        media.extend(provider.get_recent_media(username, limit=limit))
    return profiles, media
