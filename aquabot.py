#################################
###  AquaBot created by Marc  ###
###      Aqua Best Girl!      ###
#################################

# This project uses discordpy
# https://discordpy.readthedocs.io/en/latest/intro.html

# IMPORTS - external
import discord
from discord.ext import commands

# IMPORTS - internal
import loadconfig

# CONSTANTS


# INIT
bot = commands.Bot(
    command_prefix=loadconfig.__prefix__,
    description="Holy Goddess Aqua!"
    )

for cog in loadconfig.__cogs__:
    try:
        bot.load_extension(cog)
    except Exception:
        print(f"Error while trying to load cog {cog}")

# BOT
# https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
@bot.event
async def on_ready():
    print(f"""
        Logged in as: {bot.user.name} - {bot.user.id}\n
        Version: {discord.__version__}\n
        """)

    status = f"Hentai | {loadconfig.__prefix__}aquabot"
    activity = discord.Activity(name=status, type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

    print(f"AquaBot is ready!\n")


bot.run(loadconfig.__token__, bot=True, reconnect=True)