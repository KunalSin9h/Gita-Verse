import pytwitter
from os import environ as env
from dotenv import load_dotenv
from datetime import datetime

from db import get_description

load_dotenv()

api = pytwitter.Api(
    consumer_key=env['API_KEY'],
    consumer_secret=env['API_SEC'],
    access_token=env['ACCESS_KEY'],
    access_secret=env['ACCESS_SEC']
)

current_id = 1
hour_list = [6, 13, 18]
next_hour = 0

if __name__ == "__main__":
    while True:
        current_hour = int(datetime.now().hour)
        if current_hour == hour_list[next_hour]:
            hero_text = get_description(current_id)
            len_hero = len(hero_text)
            if len_hero <= 280:
                api.create_tweet(text=hero_text)
            if current_id == 701:
                break
            current_id += 1
            next_hour = (next_hour + 1)%3

    api.create_tweet(text="Jai Shri Krishna")
