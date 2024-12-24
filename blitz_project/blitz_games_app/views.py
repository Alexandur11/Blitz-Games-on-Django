import random

from django.shortcuts import render

from .models import Movie,Series
from .utilities.utilities import *


def home_page(request):
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
    j_cole = 69
    songs = recursive_collection(j_cole,1)
    songs_list = []
    for x in songs:
        if x:
            songs_list.extend(x)

    print(songs_list)



    return render(request, 'home_page.html', {})
