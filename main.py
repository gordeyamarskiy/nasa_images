import telegram
import os
import random
from time import sleep
from dotenv import load_dotenv


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=tg_token)
    while True:
        filesindir = os.listdir("images")
        random.shuffle(filesindir)
        for file in filesindir:
            filepath = os.path.join("images", file)
            with open(filepath, "rb") as f:
                bot.send_photo(chat_id=tg_chat_id, photo=f)
            sleep(5)


if __name__ == "__main__":
    main()