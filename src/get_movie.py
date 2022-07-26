## Import statements
from dotenv import load_dotenv
import requests
import json
import random
import os
# from pprint import pprint

load_dotenv()

## Function to render the movie_name from the rest api
def get_movie_name(difficulty):
    if difficulty == "1":
        page = 1
    elif difficulty == "2":
        page = 3
    elif difficulty == "3":
        page = 5
    else:
        print("Invalid level..! Default to Easy")
        page = 2
    BASE_URL = "https://api.themoviedb.org/3/discover/movie"
    params_dict = {
        "api_key": os.environ.get("API_KEY"),       # Your api_key
        "language": "en-IN", 
        "sort_by": "popularity.desc",
        "primary_release_year": 2020,
        "page": page
    }
    response = requests.get(BASE_URL, params=params_dict)
    result = json.loads(response.text)["results"]
    movie_name = random.choice(result)["title"]
    return movie_name.upper()

if __name__ == "__main__":
    print(get_movie_name(difficulty="3"))