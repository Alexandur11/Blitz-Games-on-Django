import random

from django.shortcuts import render
from .models.home_page.home_page import HomePage
from .models.movies.movies_db import Movie
from .models.movies.series_db import Series


def home_page(request):
    page = HomePage.objects.first()

    # H = MoviesPage()
    # data = H.imdb_data()
    # # H.get_movies()

    return render(request, 'home_page.html', {})


def movies_page(request):
    movies = Movie.objects.all()
    random_movie = random.choice(movies)
    return render(request, 'movie_page.html', {'random_movie':random_movie})

def tv_shows_page(request):
    tv_shows = Series.objects.all()
    random_tv_show = random.choice(tv_shows)
    return render(request,'series_page.html',{'random_tv_show':random_tv_show})

def music_page(request):
    page = Movie.objects.first()
    return render(request, 'home_page.html', {})
