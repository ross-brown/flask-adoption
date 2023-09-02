import requests
import os
import random

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET = os.environ['PETFINDER_SECRET']


def get_oauth_token():
    resp = requests.post("https://api.petfinder.com/v2/oauth2/token",
                        data={"client_id": PETFINDER_API_KEY,
                                "client_secret": PETFINDER_SECRET,
                                "grant_type":"client_credentials"})
    data = resp.json()

    return data["access_token"]



def get_random_pet(token):
    random_index = random.randint(0, 99)

    resp = requests.get("https://api.petfinder.com/v2/animals?limit=100",
                        headers={"Authorization": f"Bearer {token}"})
    data = resp.json()

    name = data["animals"][random_index]["name"]
    age = data["animals"][random_index]["age"]

    if not (data["animals"][random_index]["photos"]):
        photo_url = ''
    else:
        photo_url = data["animals"][random_index]["photos"][0]["small"]

    return {"name": name, "age": age, "photo_url": photo_url}
