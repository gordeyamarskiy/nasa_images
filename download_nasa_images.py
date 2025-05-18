import requests
from urllib.parse import urlparse, unquote
import os
from download_image import download_image
from dotenv import load_dotenv

def split_resolution(url):
    unquote_url = unquote(url)
    parse = urlparse(unquote_url)
    resolution = os.path.splitext(parse.path)[1]
    return resolution

def download_nasa_images(api):
    nasa_url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api, "count": 30}
    responce = requests.get(nasa_url, params=params)
    responce.raise_for_status()
    nasa_images = responce.json()
    for number, nasa_image in enumerate(nasa_images):
        if nasa_image.get("media_type") == "image":
            nasa_link_image = nasa_image.get("hdurl") or nasa_image.get("url")
        print(nasa_link_image)
        nasa_resolution = split_resolution(nasa_link_image)
        download_image(nasa_link_image, f'nasa_apod_{number}{nasa_resolution}')

def main():
    load_dotenv()
    api =  os.environ["NASA_API_KEY"]
    download_nasa_images(api)

if __name__=="__main__":
    main()