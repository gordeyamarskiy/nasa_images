import telegram
import os
import random
from time import sleep
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    delay = os.environ["PUBLICATION_DELAY"]
    bot = telegram.Bot(token=tg_token)
    while True:
        try:
            filesindir = os.listdir(os.environ["IMAGES"])
            random.shuffle(filesindir)
            for file in filesindir:
                filepath = os.path.join(os.environ["IMAGES"], file)
                with open(filepath, "rb") as f:
                    bot.send_photo(chat_id=tg_chat_id, photo=f)
                sleep(delay)
        except ConnectionError:
            print("Ошибка соединения, повторная попытка через 20 секунд")
            sleep(20)
            

if __name__ == "__main__":
    main()
