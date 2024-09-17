import io

from google.cloud import storage
from PIL import Image


def list_blobs() -> list:
    """Lists all the blobs in the bucket."""
    bucket_name = "rex-test-1"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    bs = []
    for b in blobs:
        print(b)
        bs.append(b.name)

    return bs


def download_blob_into_memory():
    """Downloads a blob into memory."""
    bucket_name = "rex-test-1"

    blob_name = "fredmortagne_background.jpg"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(blob_name)
    contents = blob.download_as_bytes()

    imageStream = io.BytesIO(contents)
    picture = Image.open(imageStream)
    picture.show()
    print(picture.format)


if __name__ == "__main__":
    download_blob_into_memory()
