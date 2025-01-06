"""
Views Documentation
===================

This module contains Django views for handling various endpoints related to movies, TV shows, and music.
Each view interacts with the database models and services to provide data or render templates.

Views:
------
- random_movie(request): Returns a JSON response with details of a randomly selected movie.
- random_show(request): Returns a JSON response with details of a randomly selected TV show.
- random_song(request): Returns a JSON response with a random song's artist, title, and verse.
- home_page(request): Renders the home page.
- movies_page(request): Renders a movie page with a randomly selected movie.
- tv_shows_page(request): Renders a TV shows page with a randomly selected TV show.
- music_page(request): Renders a music page with a randomly selected artist.
"""

import random
from django.http import JsonResponse
from django.shortcuts import render
from .models import Movie, Series, Artists
from .services.music_service import MusicService

# Initialize the MusicService instance
MS = MusicService()

# Fetch all database objects for reuse
artists = Artists.objects.all()
movies = Movie.objects.all()
shows = Series.objects.all()


def random_movie(request):
    """
    Returns a JSON response with details of a randomly selected movie.

    Parameters:
    -----------
    - request: The HTTP request object.

    Returns:
    --------
    JsonResponse: A JSON object containing movie details:
        - title
        - image
        - year
        - content_rating
        - votes
        - description
        - average_rating
    """
    movie = random.choice(movies)
    data = {
        'title': movie.title,
        'image': movie.primaryImage,
        'year': movie.startYear,
        'content_rating': movie.contentRating,
        'votes': movie.numVotes,
        'description': movie.description,
        'average_rating': movie.averageRating
    }
    return JsonResponse(data)


def random_show(request):
    """
    Returns a JSON response with details of a randomly selected TV show.

    Parameters:
    -----------
    - request: The HTTP request object.

    Returns:
    --------
    JsonResponse: A JSON object containing TV show details:
        - title
        - image
        - year
        - content_rating
        - votes
        - description
        - average_rating
    """
    show = random.choice(shows)
    data = {
        'title': show.title,
        'image': show.primaryImage,
        'year': show.startYear,
        'content_rating': show.contentRating,
        'votes': show.numVotes,
        'description': show.description,
        'average_rating': show.averageRating
    }
    return JsonResponse(data)


def random_song(request):
    """
    Returns a JSON response with a random song's details.

    Parameters:
    -----------
    - request: The HTTP request object.

    Returns:
    --------
    JsonResponse: A JSON object containing song details:
        - artist
        - song
        - verse
    """
    MS.quiz_preparation(artists)
    data = {
        'artist': MS.artist,
        'song': MS.song_title,
        'verse': MS.quiz_verse
    }
    return JsonResponse(data)


def home_page(request):
    """
    Renders the home page.

    Parameters:
    -----------
    - request: The HTTP request object.

    Returns:
    --------
    HttpResponse: Renders the `home_page.html` template.
    """
    return render(request, 'home_page.html', {})


def movies_page(request):
    """
    Renders a movie page with a randomly selected movie.

    Parameters:
    -----------
    - request: The HTTP request object.

    Returns:
    --------
    HttpResponse: Renders the `movie_page.html` template with context:
        - random_movie: A randomly selected movie object.
    """
    movie = random.choice(movies)
    return render(request, 'movie_page.html', {'random_movie': movie})


def tv_shows_page(request):
    """
    Renders a TV shows page with a randomly selected TV show.

    Parameters:
    -----------
    - request: The HTTP request object.

    Returns:
    --------
    HttpResponse: Renders the `series_page.html` template with context:
        - random_tv_show: A randomly selected TV show object.
    """
    random_tv_show = random.choice(shows)
    return render(request, 'series_page.html', {'random_tv_show': random_tv_show})


def music_page(request):
    """
    Renders a music page with a randomly selected artist.

    Parameters:
    -----------
    - request: The HTTP request object.

    Returns:
    --------
    HttpResponse: Renders the `music_page.html` template with context:
        - artist: A randomly selected artist object.
        - text: Currently set to None.
    """
    artist = random.choice(artists)
    return render(request, 'music_page.html', {'artist': artist, 'text': None})
