import discord
from discord.ext import commands
from dotenv import load_dotenv


# Env Variables
env_path = '/Users/aleksandardaskalov/PycharmProjects/Blitz-Games-on-Django/blitz_project/.env'
env_var = load_dotenv(env_path)

# Server
django_server = 'http://127.0.0.1:8000/'


# Discord
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)