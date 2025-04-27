import requests
from download_image import download_image

def fetch_spacex_last_launch():
    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    responce = requests.get(spacex_url)
    responce.raise_for_status()
    spacex_links = responce.json()["links"]["flickr"]["original"]

    for number, link in enumerate(spacex_links):
        download_image(link, f'spacex{number}.jpg')

def main():
    fetch_spacex_last_launch()

if __name__=="__main__":
    main()