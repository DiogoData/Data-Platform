import os
import requests
from datetime import datetime
import json
import ingestion
import api_connector
# from python.ingestion import ingestion
# from python.ingestion import api_connector


# def get_movie(token, ingestor):

api = api_connector.API("https://api.themoviedb.org/3/discover")
ingestor = ingestion.Ingestor()

# api.generic_get_themoviedb("movie", ingestor)
api.generic_get_themoviedb("tv", ingestor)