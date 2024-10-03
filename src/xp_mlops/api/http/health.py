from http import HTTPStatus
from typing import Tuple
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health() -> Tuple[str, int]:
    return "OK", HTTPStatus.OK
