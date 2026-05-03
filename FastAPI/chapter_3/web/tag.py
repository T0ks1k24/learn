from fastapi import APIRouter, HTTPException
from typing import Any
from model.tag import TagIn, TagOut
import service.tag as service

router = APIRouter()


@router.post("/")
def create(tag_in: TagIn) -> Any:
    tag = service.create(tag_in)
    return tag


@router.get("/{tag_str}", response_model=TagOut)
def get_one(tag_str: str) -> Any:
    tag = service.get(tag_str)

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    return tag
