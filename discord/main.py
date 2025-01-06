import os
from discord.settings import bot
from discord.commands import setup


# Call the setup process
setup(bot)

# Run the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
