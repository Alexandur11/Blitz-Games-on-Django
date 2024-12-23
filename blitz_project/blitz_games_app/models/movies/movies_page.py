
from django.db import models
from django.conf import settings
import requests

from .series_db import Series
from .movies_db import Movie
class MoviesPage(models.Model):
    class Meta:
        app_label = 'blitz_games_app'

    def __str__(self):
        return self.title


    def imdb_data(self):
        rapid_api_key = getattr(settings, 'RAPID_API_KEY', None)  # Use getattr to safely access settings
        movies_url = 'https://imdb236.p.rapidapi.com/imdb/top250-movies'
        series_url = 'https://imdb236.p.rapidapi.com/imdb/top250-tv'

        if rapid_api_key is None:
            print("RAPID_API_KEY not set in settings.")
            return

        headers = {
            "x-rapidapi-key": rapid_api_key,
            "x-rapidapi-host": "imdb236.p.rapidapi.com"
        }

        series_response = requests.get(series_url, headers=headers)
        movie_response = requests.get(movies_url,headers=headers)

        for x in series_response.json():
            print(x)
            Series(**x).save()

        for x in movie_response.json():
            print(x)
            Movie(**x).save()

