import json

import requests

# resp = requests.get("http://127.0.0.1:8000/photography/album_1/001167720002%20Large.jpeg")
resp = requests.get("http://127.0.0.1:8000/photography/album_1")

print(resp.json())

# print(json.dumps(resp.json(), indent=2))
