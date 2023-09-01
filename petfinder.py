import requests
import os
import random

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET = os.environ['PETFINDER_SECRET']


def get_oauth_token():
    resp = requests.get("https://api.petfinder.com/v2/oauth2/token",
                        params={"client_id": PETFINDER_API_KEY,
                                "client_secret": PETFINDER_SECRET})
    data = resp.json()

    return data["access_token"]


TOKEN = get_oauth_token()


def get_random_pet():
    random_index = random.randint(0, 99)

    resp = requests.get("https://api.petfinder.com/v2/animals?limit=100",
                        headers={f"Authorization": "Bearer {TOKEN}"})
    data = resp.json()

    name = data["animals"][random_index]["name"]
    age = data["animals"][random_index]["age"]
    photo_url = data["animals"][random_index]["primary_photo_cropped"]["small"]

    return {"name": name, "age": age, "photo_url": photo_url}
