
from django.db import models

class HomePage(models.Model):
    app_label = 'blitz_games_app'
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
