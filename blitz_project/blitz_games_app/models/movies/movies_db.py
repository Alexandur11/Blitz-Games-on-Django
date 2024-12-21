from django.db import models

class Movie(models.Model):
    id = models.CharField(max_length=20, primary_key=True)  # Example: "tt0111161"
    url = models.URLField()
    title = models.CharField(max_length=200)
    primaryImage = models.URLField()  # URL for the movie poster
    description = models.TextField()  # Description of the movie
    startYear = models.PositiveIntegerField()  # Start year, e.g., 1994
    endYear = models.PositiveIntegerField(null=True, blank=True)  # End year, can be nullable for ongoing series or null for movies
    runtimeMinutes = models.PositiveIntegerField()  # Runtime in minutes
    contentRating = models.CharField(max_length=10, null=True, blank=True)  # Content rating like "R"
    averageRating = models.FloatField()  # Average rating, e.g., 9.3
    numVotes = models.PositiveIntegerField()  # Number of votes
    type = models.CharField(max_length=50)  # Type, e.g., "movie"

    def __str__(self):
        return self.title
