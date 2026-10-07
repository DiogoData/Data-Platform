import os
from datetime import datetime
import requests
import json

class API:
    def __init__(self, url_base):
        self.url_base = url_base

    def generic_get_themoviedb(self, endpoint, ingestor):
        languages = ["pt-BR"]

        url = f"{self.url_base}/{endpoint}"
        token = get_dotenv('TOKEN_TMDB')

        headers = {
        "accept": "application/json",
        "Authorization": f'Bearer {token}',
        }

        ingestor.set_table(schema="themoviedb", table=endpoint)

        for language in languages:
            response = requests.get(url, headers=headers, params={"language":language})
            total_pages = response.json()["total_pages"]
            for page in range(1,total_pages + 1):
                params = {
                "page": page,
                "language": language
                }
                response = requests.get(url, headers=headers, params=params)
                ingestor.save_to_bronze(json.dumps(response.json()), "json")

def get_dotenv(id):
    from dotenv import load_dotenv
    load_dotenv()
    token = os.getenv(id)
    if not token:
        raise RuntimeError('TOKEN_TMDB nao foi encontrado no arquivo .env')
    return token