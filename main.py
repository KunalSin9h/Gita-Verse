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
        try:
            api.create_tweet(text=hero_text)
        except ConnectionError:
            print(f"on verse: {current_verse_id} ConnectionError Accured, Tweeting again...")
            try:
                api.create_tweet(text=hero_text)
            except:
                print("Fail again!(1)")
            else:
                print(f"Tweet Send on second try for verse {current_verse_id}(1)")
        except:
            print(f"on verse: {current_verse_id} at  create_tweet something went wrong, Retrying again...")
            try:
                api.create_tweet(text=hero_text)
            except:
                print("Fail again!(2)")
            else:
                print(f"Tweet Send on second try for verse {current_verse_id}(2)")
        else:
            print(f"Tweet Send for verse {current_verse_id}")
    else:
        print("Skip tweet due to long text")
    current_verse_id += 1

schedule.every().day.at("06:00").do(tweet_verse)
schedule.every().day.at("12:00").do(tweet_verse)
schedule.every().day.at("18:00").do(tweet_verse)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)