"""
AquaBot created by Marc.

This project uses discordpy:
https://discordpy.readthedocs.io/en/latest/intro.html
"""

# IMPORTS - external
import discord
from discord.ext import commands
import logging

# IMPORTS - internal
import loadconfig

# LOGGING
logger = logging.getLogger("discord")
# https://docs.python.org/3/library/logging.html#levels
logger.setlevel(logging.INFO)
handler = logging.FileHandler(
        filename="discord_%(asctime)s.log",
        encoding="utf-8",
        mode="w"
        )
handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
        )
logger.addHandler(handler)

# SOME DATA THAT CAN BE USED LATER
metadata = {
        "name": f"{bot.user.name} - {bot.user.id}",
        "admin": f"{self.bot.AppInfo.owner}",
        "prefix": f"{loadconfig.__token__}",
        "discordpy_version": f"{discord.__version__}",
        "python_version": f"{platform.python_version}",
        "os": f"{platform.system()} {platform.release()} {platform.version()}"
}

# INIT THE BOT
bot = commands.Bot(
    command_prefix=loadconfig.__prefix__,
    description="Holy Goddess Aqua!"
    )

# LOAD COGS SPECIFIED IN 'config/cogs.py'
for cog in loadconfig.__cogs__:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f"ERROR: {type(e).__name__} - {e}")
    else:
        print(f"SUCCESS: Loaded {cog}")

# BOT STARTING EVENT
@bot.event
async def on_ready():
    """
    This prints some information about the bot, while starting up

    Inspired by:
    https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
    """

    startup = f"""
    Bot Name: {metadata["name"]}\n
    Admin: {metadata["admin"]}\n
    Command Prefix: {metadata["prefix"]}\n
    discord.py Version: {metadata["discordpy_version"]}\n
    python Version: {metadata["python_version"]}\n
    OS: {metadata["os"]}\n
    """
    print(startup)

    status = f"Hentai | {loadconfig.__prefix__}aquabot"
    activity = discord.Activity(name=status, type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

    print(f"AquaBot is ready!\n")

# START BOT
bot.run(
        loadconfig.__token__,
        bot=True,
        reconnect=True
        )
