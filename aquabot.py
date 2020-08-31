"""
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄
 █       █       █  █ █  █       █  ▄    █       █       █
 █   ▄   █   ▄   █  █ █  █   ▄   █ █▄█   █   ▄   █▄     ▄█
 █  █▄█  █  █ █  █  █▄█  █  █▄█  █       █  █ █  █ █   █
 █       █  █▄█  █       █       █  ▄   ██  █▄█  █ █   █
 █   ▄   █      ██       █   ▄   █ █▄█   █       █ █   █
 █▄▄█ █▄▄█▄▄▄▄██▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█ █▄▄▄█

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
import asyncio
import sys
import os

# SET VARS
prefix = os.environ['PREFIX']
token = os.environ['TOKEN']
reddit_client_id = os.environ['REDDIT_CLIENT_ID']
reddit_client_secret = os.environ['REDDIT_CLIENT_SECRET']
reddit_client_useragent = os.environ['REDDIT_CLIENT_USERAGENT']

avatar = "https://i.redd.it/0uajctrps9u41.jpg"

# LOGGING
logger = logging.getLogger("discord")

logger.setLevel(logging.INFO)
handler = logging.FileHandler(
        filename="logs/discord.log",
        encoding="utf-8",
        mode="w")
handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

# INIT
bot = commands.Bot(
        command_prefix=prefix,
        description="Holy Goddess Aqua!")

# LOAD COGS
cogs = [
        "cogs.admin",
        "cogs.anime",
        "cogs.help",
        "cogs.meme",
        "cogs.music",
        "cogs.reddit",
        "cogs.utility",
        "cogs.welcome"
        ]

for cog in cogs:
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
    """
    bot.AppInfo = await bot.application_info()

    startup = f"""
    Bot Name: {bot.user.name} - {bot.user.id}\n
    Owner: {bot.AppInfo.owner}\n
    Command Prefix: {prefix}\n
    discord.py Version: {discord.__version__}\n
    python Version: {platform.python_version()}\n
    OS: {platform.system()} {platform.release()} {platform.version()}\n
    """
    print(startup)

    name = f"with water | {prefix}aquabot"
    activity = discord.Activity(name=name, type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)

    print(f"AquaBot is ready!\n")

# START BOT
bot.run(
        token,
        bot=True,
        reconnect=True)
