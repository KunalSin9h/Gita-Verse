from os import environ as env
from dotenv import load_dotenv
import requests

load_dotenv()  # load credentials from .env file


def get_translations(chapter, verse):
    url = f"https://bhagavad-gita3.p.rapidapi.com/v2/chapters/{chapter}/verses/{verse}/"
    headers = {
        "X-RapidAPI-Key": env["X-RapidAPI-Key"],
        "X-RapidAPI-Host": env["X-RapidAPI-Host"],
    }
    response = requests.request("GET", url, headers=headers)
    response_json = response.json()
    return response_json["translations"]
