from models.movies.movies_db import Movie
movies = Movie.objects.all()  # Fetch all records from the MoviesPage model.

for movie in movies:
    print(movie.title, movie.id, movie.average_rating)
