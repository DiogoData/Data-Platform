import os
import requests
from datetime import datetime
import json

def get_token():
	from dotenv import load_dotenv
	load_dotenv()
	token = os.getenv('TOKEN_TMDB')
	if not token:
		raise RuntimeError('TOKEN_TMDB nao foi encontrado no arquivo .env')
	return token

def get_movie(token):
    languages = ["en-US"]

    url = "https://api.themoviedb.org/3/discover/movie"
    url = "https://api.themoviedb.org/3/discover/movie?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": f'Bearer {token}',
    }

    response = requests.get(url, headers=headers)

    print(response.content)

    # for language in languages:
    #     response = requests.get(url, headers=headers)
    #     total_pages = response.json()["total_pages"]
    #     print(total_pages)

get_movie(get_token())  