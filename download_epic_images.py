import requests
from datetime import datetime
from download_image import download_image
import os
from dotenv import load_dotenv


def download_epic_images(api):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {"api_key": api, "count": 30}
    responce = requests.get(url, params=params)
    responce.raise_for_status()
    epic_images = responce.json()
    for epic_image in epic_images:
        epic_date = epic_image["date"]
        epic_date = datetime.fromisoformat(epic_date).strftime("%Y/%m/%d")
        epic_name = epic_image["image"]
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{epic_date}/png/{epic_name}.png?api_key={api}"
        download_image(epic_url, f'{epic_name}.png')

def main():
    load_dotenv()
    api =  os.environ["NASA_API_KEY"]
    download_epic_images(api)

if __name__=="__main__":
    main()