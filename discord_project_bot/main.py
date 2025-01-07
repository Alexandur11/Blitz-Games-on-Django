import os
from dotenv import load_dotenv
from commands import setup
from settings import bot

load_dotenv()
setup(bot)

# Run the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
