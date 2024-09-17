from fastapi import APIRouter

from .utils import download_blob_into_memory, list_blobs

photography_router = APIRouter()


@photography_router.get("/photography")
async def photography():
    blobs = list_blobs()

    download_blob_into_memory()

    return {"message": "Photography...", "blobs": blobs}
