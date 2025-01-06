import os
from discord.settings import bot
from discord.commands import setup


setup(bot)
bot.run(os.getenv('DISCORD_BOT_TOKEN'))