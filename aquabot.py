"""
AquaBot created by Marc.

This project uses discordpy:
https://discordpy.readthedocs.io/en/latest/intro.html
"""

# IMPORTS - external
import discord
from discord.ext import commands
import logging
from datetime import datetime
import platform
import random

# IMPORTS - internal
import loadconfig

# LOGGING
logger = logging.getLogger("discord")
# https://docs.python.org/3/library/logging.html#levels
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
        filename="logs/discord-{%Y-%m-%d_%H-%M}.log".format(datetime.now()),
        encoding="utf-8",
        mode="w")
handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

# INIT THE BOT
bot = commands.Bot(
        command_prefix=loadconfig.__prefix__,
        description="Holy Goddess Aqua!")

# LOAD COGS SPECIFIED IN 'config/cogs.py'
for cog in loadconfig.__cogs__:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f"ERROR: {type(e).__name__} - {e}")
    else:
        print(f"SUCCESS: Loaded {cog}")

# ACTIVITY
async def activity():
    while True: # Infinite Loop
        new_activity = random.choice(loadconfig.__activity__)
        status = f"{new_activity[1]} | {loadconfig.__prefix__}aquabot"
        activity = discord.Activity(name=status, type=new_activity[0])
        await bot.change_presence(activity=activity)
        await asyncio.sleep(10) # Time in minutes

# BOT STARTING EVENT
@bot.event
async def on_ready():
    """
    This prints some information about the bot, while starting up

    Inspired by:
    https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
    """
    bot.AppInfo = await bot.application_info()

    startup = f"""
    Bot Name: {bot.user.name} - {bot.user.id}\n
    Owner: {bot.AppInfo.owner}\n
    Command Prefix: {loadconfig.__prefix__}\n
    discord.py Version: {discord.__version__}\n
    python Version: {platform.python_version()}\n
    OS: {platform.system()} {platform.release()} {platform.version()}\n
    """
    print(startup)

    activity_loop = asyncio.ensure_future(activity())

    print(f"AquaBot is ready!\n")

# START BOT
bot.run(
        loadconfig.__token__,
        bot=True,
        reconnect=True)
