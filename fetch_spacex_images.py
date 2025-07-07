import requests
from download_image import download_image
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    launch_id = os.environ.get("LAUNCH_ID", "5eb87d47ffd86e000604b38a")
    spacex_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    responce = requests.get(spacex_url)
    responce.raise_for_status()
    spacex_links = responce.json()["links"]["flickr"]["original"]

    for number, link in enumerate(spacex_links):
        download_image(link, f"spacex{number}.jpg")


if __name__ == "__main__":
    main()