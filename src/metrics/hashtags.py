import re
from collections import Counter

HASHTAG_RE = re.compile(r"(?<!\w)#([\w_]+)", re.UNICODE)
MENTION_RE = re.compile(r"(?<!\w)@([A-Za-z0-9_.]+)")


def extract_hashtags(text):
    return [match.group(1).lower() for match in HASHTAG_RE.finditer(text or "")]


def extract_mentions(text):
    return [
        match.group(1).lower().rstrip("._") for match in MENTION_RE.finditer(text or "")
    ]


def hashtag_counts(media_items):
    counter = Counter()
    for item in media_items:
        counter.update(extract_hashtags(item.get("caption", "")))
    return counter


def mention_counts(media_items):
    counter = Counter()
    for item in media_items:
        counter.update(extract_mentions(item.get("caption", "")))
    return counter
