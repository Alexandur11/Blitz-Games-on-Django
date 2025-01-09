from bs4 import BeautifulSoup
import logging

"""
Parsing Utilities Documentation
===============================

This module provides utility functions to parse and extract relevant data from song lyrics API responses.
It uses `BeautifulSoup` to process HTML content and retrieve structured information.

Functions:
----------
- parse_lyrics_response(response_data): Parses API response to extract song metadata and HTML content.
- parse_song_lyrics(html_content): Parses HTML content of song lyrics to extract individual verses.
"""


def parse_lyrics_response(response_data):
    """
       Parses the lyrics response data to extract song metadata and HTML content.

       Parameters:
       -----------
       - response_data (dict): A dictionary containing the response data from the lyrics API.

       Returns:
       --------
       dict: A dictionary with the following keys:
           - 'artist' (str): The name of the song's primary artist.
           - 'title' (str): The title of the song.
           - 'html_content' (str): The HTML content of the song's lyrics."""

    try:
        lyrics_data = response_data['lyrics']
        lyrics = lyrics_data['lyrics']
        body = lyrics['body']
        track_data = lyrics_data['tracking_data']

        html_content = body['html']
        song_title = track_data['title']
        artist = track_data['primary_artist']

        return {'artist': artist, 'title': song_title, 'html_content': html_content}
    except (KeyError,TypeError,AttributeError,ValueError) as e:
        logging.exception(e)



def parse_song_lyrics(html_content):
    """
        Parses the HTML content of a song's lyrics to extract individual verses.

        Parameters:
        -----------
        - html_content (str): The HTML content of the song's lyrics.

        Returns: -------- list: A list of song verses extracted from the HTML content. Each verse is represented as a
        set containing the verse text.

        Behavior:
        ---------
        - Extracts all `<a>` tags from the HTML using BeautifulSoup.
        - For each `<a>` tag, retrieves:
            - `data-classification`: Classification metadata (if present, default is 'N/A').
            - `data-id`: ID metadata (if present, default is 'N/A').
            - `lyrics`: The text content of the tag.
        - Logs each verse to the console."""

    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        parsed_data = []

        song_verses = []

        for anchor in soup.find_all('a'):
            data_classification = anchor.get('data-classification', 'N/A')
            data_id = anchor.get('data-id', 'N/A')
            lyrics = anchor.text.strip()

            parsed_data.append({
                "data_id": data_id,
                "data_classification": data_classification,
                "lyrics": lyrics
            })

        for item in parsed_data:
            song_verses.append({item['lyrics']})
        return song_verses
    except (TypeError,ValueError,AttributeError,KeyError) as e:
        logging.exception(e)