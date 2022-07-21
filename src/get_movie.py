## Import statements
from dotenv import load_dotenv
import requests
import json
import random
import os
# from pprint import pprint

load_dotenv()

## Function to render the movie_name from the rest api
def get_movie_name():
    BASE_URL = "https://api.themoviedb.org/3/discover/movie"
    params_dict = {
        "api_key": os.environ.get("API_KEY"),
        "language": "en-IN", 
        "sort_by": "popularity.desc",
        "primary_release_year": 2018,
        "page": 1
    }
    response = requests.get(BASE_URL, params=params_dict)
    result = json.loads(response.text)["results"]
    movie_name = random.choice(result)["title"]
    return movie_name.upper()

if __name__ == "__main__":
    print(get_movie_name())