
from django.urls import path
from .views import home_page,music_page,movies_page

urlpatterns = [
    path('', home_page, name='home_page'),  # Root URL to the home_page view
    path('music_game', music_page, name='music_page'),
    path('movies_game',movies_page, name='movies_page')
]
