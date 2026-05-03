from datetime import datetime, timezone
from typing import Optional
from model.tag import Tag, TagIn

_fake_db: dict[str, Tag] = {}


def create(tag_data: TagIn) -> Tag:

    new_tag = Tag(
        tag=tag_data.tag,
        created=datetime.now(timezone.utc),
        secret=f"Secret metadata for {tag_data.tag}",
    )

    _fake_db[new_tag.tag] = new_tag
    return new_tag


def get(tag_str: str) -> Optional[Tag]:
    return _fake_db.get(tag_str)
