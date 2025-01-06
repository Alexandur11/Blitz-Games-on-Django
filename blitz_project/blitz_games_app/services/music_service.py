"""
MusicService Documentation
==========================

This module provides a `MusicService` class to manage music-based functionalities, including selecting artists,
songs, and specific verses for a quiz game. The class integrates external utilities for parsing song lyrics.

Classes:
--------
MusicService

Methods: -------- - __init__(): Initializes the MusicService class with default attributes. - artist_selector():
Randomly selects an artist's repertoire from a list of artists. - song_selector(): Randomly selects a song from the
selected artist's repertoire. - verse_selector(): Randomly selects a verse from the lyrics of the selected song. -
quiz_preparation(artists): Prepares the music quiz by selecting an artist, song, and verse while retrieving the
song's details."""

import random
from ..utilities.parsing_utilities import *
from ..utilities.utilities import get_song_lyrics


class MusicService:
    """
    A service class for managing music-related functionalities such as artist selection,
    song selection, and verse retrieval for a quiz game.
    """

    def __init__(self):
        """
        Initializes the MusicService class.

        Attributes:
        -----------
        - artists: List of artists to choose from.
        - artists_repertoire: Repertoire of the selected artist.
        - quiz_song: The selected song for the quiz.
        - lyrics: The lyrics of the selected song.
        - song_title: Title of the selected song.
        - artist: The name of the selected artist.
        - quiz_verse: A randomly chosen verse from the selected song's lyrics.
        """
        self.artists = None
        self.artists_repertoire = None
        self.quiz_song = None
        self.lyrics = None
        self.song_title = None
        self.artist = None
        self.quiz_verse = None

    def artist_selector(self):
        """
        Randomly selects an artist's repertoire.

        This method uses the `artists` attribute, which should contain a list of artist objects.
        Each artist object is expected to have a `songs` attribute with song IDs in a comma-separated string.
        The selected artist's repertoire is stored in `artists_repertoire`.
        """
        try:
            artists_songs = [x.songs[1:-1].split(',') for x in self.artists]
            self.artists_repertoire = random.choice(artists_songs)
        except IndexError:
            raise IndexError('No songs for this artist in the database')

    def song_selector(self):
        """
        Randomly selects a song from the selected artist's repertoire.

        This method uses the `artists_repertoire` attribute to select a song and stores
        it in the `quiz_song` attribute.
        """
        self.quiz_song = random.choice(self.artists_repertoire)

    def verse_selector(self):
        """
        Randomly selects a verse from the lyrics of the selected song.

        Returns:
        --------
        str: A randomly chosen verse from the `lyrics` attribute.
        """
        return random.choice(self.lyrics)

    def quiz_preparation(self, artists):
        """
        Prepares the music quiz by selecting an artist, a song, and a quiz verse,
        while retrieving additional details of the selected song.

        Parameters:
        -----------
        - artists (list): A list of artist objects to choose from.

        This method performs the following steps:
        1. Sets the `artists` attribute.
        2. Randomly selects an artist and their repertoire using `artist_selector()`.
        3. Randomly selects a song from the selected repertoire using `song_selector()`.
        4. Fetches and parses the song lyrics.
        5. Randomly selects a verse using `verse_selector()`.
        6. Stores additional details (artist name, song title) in `artist` and `song_title`.

        The method also prints the selected artist, song, and verse for debugging purposes.
        """
        if not artists:
            raise Exception('Not artists inside the database')
        self.artists = artists
        self.artist_selector()
        self.song_selector()
        lyrics_response = get_song_lyrics(self.quiz_song)
        parsed_response = parse_lyrics_response(lyrics_response)

        self.lyrics = parse_song_lyrics(parsed_response['html_content'])
        self.quiz_verse = self.verse_selector()
        self.artist = parsed_response['artist']
        self.song_title = parsed_response['title']
