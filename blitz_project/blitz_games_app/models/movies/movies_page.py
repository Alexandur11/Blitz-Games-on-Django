
from django.db import models
from django.conf import settings
import requests

class MoviesPage(models.Model):
    app_label = 'blitz_games_app'
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

    def imdb_data(self):
        url = "https://imdb236.p.rapidapi.com/imdb/types"
        rapid_api_key = getattr(settings, 'RAPID_API_KEY', None)  # Use getattr to safely access settings

        if rapid_api_key is None:
            print("RAPID_API_KEY not set in settings.")
            return

        headers = {
            "x-rapidapi-key": rapid_api_key,
            "x-rapidapi-host": "imdb236.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        print(response.json())
