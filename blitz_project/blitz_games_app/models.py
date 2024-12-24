from django.db import models


class Movie(models.Model):
    id = models.CharField(max_length=20, primary_key=True)  # Example: "tt0111161"
    url = models.URLField()
    title = models.CharField(max_length=200)
    primaryImage = models.URLField()  # URL for the movie poster
    description = models.TextField()  # Description of the movie
    startYear = models.PositiveIntegerField()  # Start year, e.g., 1994
    endYear = models.PositiveIntegerField(null=True, blank=True)  # End year, can be nullable for ongoing series or
    # null for movies
    runtimeMinutes = models.PositiveIntegerField()  # Runtime in minutes
    contentRating = models.CharField(max_length=10, null=True, blank=True)  # Content rating like "R"
    averageRating = models.FloatField()  # Average rating, e.g., 9.3
    numVotes = models.PositiveIntegerField()  # Number of votes
    type = models.CharField(max_length=50)  # Type, e.g., "movie"

    def __str__(self):
        return f"{self.title} | {self.url} | {self.primaryImage} | {self.description} " \
               f"| {self.startYear} | {self.contentRating} | {self.averageRating} | {self.numVotes} | {self.type}"


class Series(models.Model):
    id = models.CharField(max_length=20, primary_key=True)  # IMDb ID, e.g., "tt0903747"
    url = models.URLField()  # IMDb URL, e.g., "https://www.imdb.com/title/tt0903747/"
    title = models.CharField(max_length=200)  # Series title, e.g., "Breaking Bad"
    primaryImage = models.URLField()  # URL for the primary image, e.g., poster
    description = models.TextField()  # Short description of the series
    startYear = models.PositiveIntegerField()  # Year the series started, e.g., 2008
    endYear = models.PositiveIntegerField(null=True, blank=True)  # Year the series ended, e.g., 2013 (nullable for ongoing)
    totalEpisodes = models.PositiveIntegerField(null=True, blank=True)  # Total number of episodes, e.g., 62
    runtimeMinutes = models.PositiveIntegerField(null=True)
    contentRating = models.CharField(max_length=10, null=True, blank=True)  # Content rating, e.g., "TV-MA"
    averageRating = models.FloatField()  # Average IMDb rating, e.g., 9.5
    numVotes = models.PositiveIntegerField()  # Number of votes on IMDb, e.g., 2242894
    type = models.CharField(max_length=50, default="tvSeries")  # Type of content, defaulted to "tvSeries"

    def __str__(self):
        return f"{self.title} | {self.url} | {self.primaryImage} | {self.description} " \
               f"| {self.startYear} | {self.contentRating} | {self.averageRating} | {self.numVotes} | {self.type}"
