import requests
import os
from dotenv import load_dotenv


def download_image(url, filename, params=None):
    os.makedirs(os.environ["IMAGES"], exist_ok=True)
    response = requests.get(url, params)
    response.raise_for_status()

    with open(os.path.join(os.environ["IMAGES"], filename), "wb") as file:
        file.write(response.content)
