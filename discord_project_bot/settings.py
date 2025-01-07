import discord
from discord.ext import commands
import requests

def check_django_connection():
    try:
        # Attempt to connect to Django via 127.0.0.1
        response = requests.get('http://127.0.0.1:8000/random_movie')
        response.raise_for_status()
        return 'http://127.0.0.1:8000/'
    except requests.exceptions.RequestException:
        # If the connection fails, fallback to Django service in Docker
        return 'http://django:8000/'

# Server
django_server = check_django_connection()

# Discord
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
