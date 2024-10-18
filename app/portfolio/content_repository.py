import datetime
from enum import Enum

from cachetools import TTLCache, cached
from google.cloud import storage
from pydantic import BaseModel

FILM_PHOTOGRAPHY_BUCKET = "rex-photography-portfolio"
# FILM_PHOTOGRAPHY_BUCKET = "rex-test-1"

TTL_MINUTES = 60


class Size(Enum):
    SMALL = "small"
    LARGE = "large"
    ORIGINAL = "original"


class Image(BaseModel):
    path: str
    url: str


class Album(BaseModel):
    name: str
    path: str
    images: list[Image]


class ContentRepository:
    """Repository for fetching photographs from"""

    def __init__(self):
        self.client = storage.Client(project="ultra-path-385820")

    @cached(cache=TTLCache(maxsize=1024, ttl=datetime.timedelta(minutes=TTL_MINUTES), timer=datetime.datetime.now))
    def get_album(self, album_name: str, size: Size = Size.SMALL) -> Album:
        blobs: list[storage.Blob] = self.client.list_blobs(
            FILM_PHOTOGRAPHY_BUCKET, prefix=f"{album_name}/{size.value}/"
        )

        images = []
        for blob in blobs:
            # Skip Folders
            if blob.name[-1] == "/":
                continue

            images.append(
                Image(
                    path=f"{FILM_PHOTOGRAPHY_BUCKET}/{blob.name}",
                    url=blob.generate_signed_url(
                        version="v4",
                        expiration=datetime.timedelta(minutes=TTL_MINUTES),
                        method="GET",
                    ),
                )
            )

        return Album(
            name=album_name,
            path=f"{FILM_PHOTOGRAPHY_BUCKET}/{album_name}",
            images=images,
        )

    @cached(cache=TTLCache(maxsize=1024, ttl=datetime.timedelta(minutes=TTL_MINUTES), timer=datetime.datetime.now))
    def get_image(self, album_name: str, image_name: str, size: Size = Size.LARGE) -> Image:
        bucket = self.client.get_bucket(FILM_PHOTOGRAPHY_BUCKET)
        blob = bucket.get_blob(f"{album_name}/{size.value}/{image_name}")
        return Image(
            path=f"{FILM_PHOTOGRAPHY_BUCKET}/{blob.name}",
            url=blob.generate_signed_url(
                version="v4",
                expiration=datetime.timedelta(minutes=TTL_MINUTES),
                method="GET",
            ),
        )
