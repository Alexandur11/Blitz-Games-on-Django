import requests
from settings import django_server
from utils import *
import random


latest_cinematic_data = {}
latest_song_artist = {}


def setup(bot):
    """Load all commands and events into the bot."""

    @bot.event
    async def on_ready():
        print(f"Bot is logged in as {bot.user}")

    @bot.command(name='song')
    async def song_lyrics(ctx):

        """Sends a small verse from a song. """

        try:
            global latest_song_artist
            latest_song_artist = requests.get(f'{django_server}random_song').json()
            await ctx.send(
                f"Year: {latest_song_artist['verse']}")
        except Exception as e:
            await ctx.send(f"An error occurred while fetching song details: {e}")

    @bot.command(name='artist')
    async def song_artist(ctx):

        """
            Sends all details about an artist.
            Caches the artist data for later use in other commands.
        """

        if latest_song_artist:
            await ctx.send(f"Artist: {latest_song_artist['artist']}\n"
                           f"Song: {latest_song_artist['song']}")
        else:
            await ctx.send(
                "No movie data available! Please use the `!movie` command first."
            )
        latest_song_artist.clear()

    @bot.command(name='cinematic')
    async def cinematic_details(ctx):
        """
            Sends all details about a random show or movie except the average rating.
            Caches the data for later use in other commands.
        """

        try:
            global latest_cinematic_data
            cinematic_type = random.choice(['random_show','random_movie'])
            latest_show_data = requests.get(f'{django_server}/{cinematic_type}').json()
            await ctx.send(
                f"Movie Title: {latest_show_data['title']}\n"
                f"Image URL: {latest_show_data['image']}\n"
                f"Year: {latest_show_data['year']}\n"
                f"Content Rating: {latest_show_data['content_rating']}\n"
                f"Description: {latest_show_data['description']}"
            )
        except Exception as e:
            await ctx.send(f"An error occurred while fetching series details: {e}")

    @bot.command(name='rating')
    async def cinematic_rating(ctx):
        """
               Sends the rating of the latest fetched show.
               Uses cached data from the last `!tr` command.
               """

        if latest_cinematic_data:
            await ctx.send(f"Title: {latest_cinematic_data['title']}\n"
                           f"Rating: {latest_cinematic_data['average_rating']}")
        else:
            await ctx.send(
                "No Cinematic data available!"
            )
        latest_cinematic_data.clear()

    @bot.command()
    async def guess(ctx,guess:str):
        if not latest_song_artist or not latest_cinematic_data:
            return

        user_guess = None

        if latest_song_artist:
            user_guess = compare_musical_guess(guess=guess,song_data=latest_song_artist)
            response = song_artist() if user_guess else 'You guessed wrong'
            await ctx.send(response)
        else:
            user_guess = compare_rating_guess(guess=guess,the_truth=latest_cinematic_data['average_rating'])
            response = cinematic_rating() if user_guess else 'You guessed wrong'
            await ctx.send(response)

        if user_guess:
            latest_song_artist.clear()
            latest_cinematic_data.clear()





