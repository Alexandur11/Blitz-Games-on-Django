from django.db import models


class Movie(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    url = models.URLField()
    title = models.CharField(max_length=200)
    primaryImage = models.URLField()
    description = models.TextField()
    startYear = models.PositiveIntegerField()
    endYear = models.PositiveIntegerField(null=True, blank=True)
    runtimeMinutes = models.PositiveIntegerField()
    contentRating = models.CharField(max_length=10, null=True, blank=True)
    averageRating = models.FloatField()
    numVotes = models.PositiveIntegerField()
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} | {self.url} | {self.primaryImage} | {self.description} " \
               f"| {self.startYear} | {self.contentRating} | {self.averageRating} | {self.numVotes} | {self.type}"


class Series(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    url = models.URLField()
    title = models.CharField(max_length=200)
    primaryImage = models.URLField()
    description = models.TextField()
    startYear = models.PositiveIntegerField()
    endYear = models.PositiveIntegerField(null=True, blank=True)
    totalEpisodes = models.PositiveIntegerField(null=True, blank=True)
    runtimeMinutes = models.PositiveIntegerField(null=True)
    contentRating = models.CharField(max_length=10, null=True, blank=True)
    averageRating = models.FloatField()
    numVotes = models.PositiveIntegerField()
    type = models.CharField(max_length=50, default="tvSeries")

    def __str__(self):
        return f"{self.title} | {self.url} | {self.primaryImage} | {self.description} " \
               f"| {self.startYear} | {self.contentRating} | {self.averageRating} | {self.numVotes} | {self.type}"

class Artists(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    songs = models.TextField()
    image = models.URLField(default='https://img.freepik.com/premium-vector/man-singer-silhouette-man-singing-mic'
                                    '-singer-singing-silhouette-vocalist-singing-microphone_690577-1487.jpg?w=1060')

    def __str__(self):
        return f"{self.id} | {self.songs} | {self.image}"
