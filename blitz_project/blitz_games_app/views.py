
from django.shortcuts import render
from .models.home_page.home_page import HomePage
from .models.movies.movies_page import MoviesPage
from.models.music.music_page import MusicPage

def home_page(request):
    page = HomePage.objects.first()

    H = MoviesPage()
    data = H.imdb_data()
    # H.get_movies()

    return render(request, 'home_page.html', {'page': page})

def movies_page(request):
    page = MoviesPage.objects.first()
    return render(request,'home_page.html',{'page':page})

def music_page(request):
    page = MusicPage.objects.first()
    return render(request,'home_page.html',{'page':page})