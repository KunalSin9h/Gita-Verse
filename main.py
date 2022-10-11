import pytwitter
from os import environ as env
from dotenv import load_dotenv
import schedule
import time

from db import get_description

load_dotenv()

env['TZ'] = 'Asia/Kolkata'
time.tzset()

api = pytwitter.Api(
    consumer_key=env['API_KEY'],
    consumer_secret=env['API_SEC'],
    access_token=env['ACCESS_KEY'],
    access_secret=env['ACCESS_SEC']
)

current_verse_id = 1

def tweet_verse():
    global current_verse_id
    hero_text = get_description(current_verse_id)
    len_hero = len(hero_text)
    if len_hero <= 280:
        api.create_tweet(text=hero_text)
    current_verse_id += 1

schedule.every().day.at("6:00").do(tweet_verse)
schedule.every().day.at("12:00").do(tweet_verse)
schedule.every().day.at("18:00").do(tweet_verse)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
        if current_verse_id == 702:
            api.create_tweet(text="Jai Shri Krishna.")
            exit()
