
import random
from ..utilities.parsing_utilities import *
from ..utilities.utilities import get_song_lyrics

class MusicService:

    def __init__(self):
        self.artists = None
        self.artists_repertoire = None
        self.quiz_song = None
        self.lyrics = None
        self.song_title = None
        self.artist = None
        self.quiz_verse = None

    def artist_selector(self):
        artists_songs = [x.songs[1:-1].split(',') for x in self.artists]
        self.artists_repertoire=random.choice(artists_songs)

    def song_selector(self):
        self.quiz_song = random.choice(self.artists_repertoire)

    def verse_selector(self):
        return random.choice(self.lyrics)

    def quiz_preparation(self,artists):
        self.artists = artists
        self.artist_selector()
        self.song_selector()
        lyrics_response = get_song_lyrics(self.quiz_song)
        parsed_response = parse_lyrics_response(lyrics_response)

        self.lyrics = parse_song_lyrics(parsed_response['html_content'])
        self.quiz_verse = self.verse_selector()
        self.artist = parsed_response['artist']
        self.song_title = parsed_response['title']

        print(f'artist : {self.artist}')
        print(f'song: {self.song_title}')
        print(f'verse: {self.quiz_verse}')

