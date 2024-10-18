from fastapi import APIRouter

from ..content_repository import ContentRepository

photography_router = APIRouter()

content_repo = ContentRepository()


@photography_router.get("/photography/{album}")
async def get_album(album: str):
    return content_repo.get_album(album)


@photography_router.get("/photography/{album}/{image}")
async def get_photograph(album: str, image: str):
    return content_repo.get_image(album, image)
