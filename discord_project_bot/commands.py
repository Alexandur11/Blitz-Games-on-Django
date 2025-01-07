import requests
from settings import django_server

latest_movie_data = {}
latest_show_data = {}
song_artist = {}


def setup(bot):
    """Load all commands and events into the bot."""

    @bot.event
    async def on_ready():
        print(f"Bot is logged in as {bot.user}")

    @bot.command(name='song')
    async def song_lyrics(ctx):

        """Sends a small verse from a song. """

        try:
            global song_artist
            song_artist = requests.get(f'{django_server}random_song').json()
            await ctx.send(
                f"Year: {song_artist['verse']}")
        except Exception as e:
            await ctx.send(f"An error occurred while fetching song details: {e}")

    @bot.command(name='artist')
    async def song_artist(ctx):

        """
            Sends all details about an artist.
            Caches the artist data for later use in other commands.
        """

        if song_artist:
            await ctx.send(f"Artist: {song_artist['artist']}\n"
                           f"Song: {song_artist['song']}")
        else:
            await ctx.send(
                "No movie data available! Please use the `!movie` command first."
            )

    @bot.command(name='s')
    async def tv_show_details(ctx):

        """
            Sends all details about a random show except the average rating.
            Caches the show data for later use in other commands.
            """

        try:
            global latest_show_data
            latest_show_data = requests.get(f'{django_server}/random_show').json()
            await ctx.send(
                f"Movie Title: {latest_show_data['title']}\n"
                f"Image URL: {latest_show_data['image']}\n"
                f"Year: {latest_show_data['year']}\n"
                f"Content Rating: {latest_show_data['content_rating']}\n"
                f"Description: {latest_show_data['description']}"
            )
        except Exception as e:
            await ctx.send(f"An error occurred while fetching series details: {e}")

    @bot.command(name='tr')
    async def tv_show_rating(ctx):

        """
           Sends the rating of the latest fetched show.
           Uses cached data from the last `!tr` command.
           """

        if latest_show_data:
            await ctx.send(f"Title: {latest_show_data['title']}\n"
                           f"Rating: {latest_show_data['average_rating']}")
        else:
            await ctx.send(
                "No movie data available! Please use the `!movie` command first."
            )

    @bot.command(name="m")
    async def movie_details(ctx):
        """
        Sends all details about a random movie except the average rating.
        Caches the movie data for later use in other commands.
        """

        try:
            global latest_movie_data
            latest_movie_data = requests.get(f'{django_server}random_movie').json()
            await ctx.send(
                f"Movie Title: {latest_movie_data['title']}\n"
                f"Image URL: {latest_movie_data['image']}\n"
                f"Year: {latest_movie_data['year']}\n"
                f"Content Rating: {latest_movie_data['content_rating']}\n"
                f"Description: {latest_movie_data['description']}"
            )
        except Exception as e:
            await ctx.send(f"An error occurred while fetching movie details: {e}")

    @bot.command(name="mr")
    async def movie_rating(ctx):
        """
        Sends the rating of the latest fetched movie.
        Uses cached data from the last `!movie` command.
        """
        if latest_movie_data:
            await ctx.send(f"Title: {latest_movie_data['title']}\n"
                           f"Rating: {latest_movie_data['average_rating']}")
        else:
            await ctx.send(
                "No movie data available! Please use the `!movie` command first."
            )
