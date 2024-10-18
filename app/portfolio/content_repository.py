import datetime
from enum import Enum

from cachetools import TTLCache, cached
from google.auth import default
from google.auth.transport import requests
from google.cloud import storage
from google.cloud.storage import Blob
from pydantic import BaseModel

FILM_PHOTOGRAPHY_BUCKET = "rex-photography-portfolio"

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
        try:
            self.credentials, self.project_id = default()
            self.client = storage.Client(self.project_id)

        except Exception as e:
            raise PermissionError("failed to create Google Storage Client") from e

    # TODO: have to make this compatible with local too somehow
    def _generate_signed_url(self, blob: Blob) -> str:
        """https://stackoverflow.com/questions/73918501/why-my-cloud-run-instance-is-using-the-default-service-account-instead-of-my-ded"""
        # Perform a refresh token with a request to generate a token (Else, it's None)
        r = requests.Request()
        self.credentials.refresh(r)

        return blob.generate_signed_url(
            service_account_email=self.credentials.service_account_email,
            access_token=self.credentials.token,
            method="GET",
            expiration=datetime.timedelta(minutes=TTL_MINUTES),
        )

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
                    url=self._generate_signed_url(blob),
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
            url=self._generate_signed_url(blob),
        )
