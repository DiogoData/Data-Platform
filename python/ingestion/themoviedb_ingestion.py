from libs import ingestion
from libs import api_connector

api = api_connector.API("https://api.themoviedb.org/3/discover")
ingestor = ingestion.Ingestor()

tables = [
    "movie",
    "tv"
]
for table in tables:
    api.generic_get_themoviedb(table, ingestor)