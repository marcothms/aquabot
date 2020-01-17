#################################
###  AquaBot created by Marc  ###
###      Aqua Best Girl!      ###
#################################

# This project uses discordpy
# https://discordpy.readthedocs.io/en/latest/intro.html

# IMPORTS
import discord
from discord.utils import commands

# CONSTANTS
BOT_TOKEN = ""
COMMAND_PREFIX = ""

# INIT
bot = commands.Bot(command_prefix=COMMAND_PREFIX, description="Holy Goddess Aqua!")

inital_extensions = [
        "cogs.admin",
        "cogs.general",
        "cogs.welcome"
        ]

if __name__ == "__main__":
    for extension in inital_extensions:
        bot.load_extension(extension)

# BOT
# https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
@bot.event
async def on_ready():
    print(f"""
        Logged in as: {bot.user.name} - {bot.user.id}\n
        Version: {discord.__version__}\n
        """)

    status = f"Hentai | {COMMAND_PREFIX}aquabot"
    activity = discord.Activity(name=status, type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

    print(f"AquaBot is ready!\n")


bot.run(BOT_TOKEN, bot=True, reconnect=True)
