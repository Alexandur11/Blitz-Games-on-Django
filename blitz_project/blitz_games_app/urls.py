
from django.urls import path
from .views import home_page, music_page, movies_page, tv_shows_page

urlpatterns = [
    path('', home_page, name='home_page'),  # Root URL to the home_page view
    path('guess_the_song', music_page, name='music_page'),
    path('guess_the_tv_show_rating',tv_shows_page, name='series_page'),
    path('guess_the_movie_rating',movies_page, name='movies_page')
]
