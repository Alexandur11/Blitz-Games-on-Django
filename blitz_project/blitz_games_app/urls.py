
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),  # Root URL to the home_page view
    path('guess_the_song', views.music_page, name='music_page'),
    path('guess_the_tv_show_rating',views.tv_shows_page, name='series_page'),
    path('guess_the_movie_rating',views.movies_page, name='movies_page'),
    path('random_movie',views.random_movie,name='random_movie'),
    path('random_show',views.random_show,name='random_show'),
    path('random_song',views.random_song,name='random_song'),
]
