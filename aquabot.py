"""
  __ _  __ _ _   _  __ _| |__   ___ | |_ 
 / _` |/ _` | | | |/ _` | '_ \ / _ \| __|
| (_| | (_| | |_| | (_| | |_) | (_) | |_ 
 \__,_|\__, |\__,_|\__,_|_.__/ \___/ \__|
          |_|                            

by MarcMK

This project uses discordpy: https://discordpy.readthedocs.io/en/latest/intro.html
"""

import discord
from discord.ext import commands
import logging
import platform
import os

# Environment
PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']
REDDIT_CLIENT_ID = os.environ['REDDIT_CLIENT_ID']
REDDIT_CLIENT_SECRET = os.environ['REDDIT_CLIENT_SECRET']
REDDIT_CLIENT_USERAGENT = os.environ['REDDIT_CLIENT_USERAGENT']
AVATAR = "https://i.redd.it/0uajctrps9u41.jpg"

# Logger
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="/logs/discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

# Bot declaration
bot = commands.Bot(command_prefix=PREFIX, description="Holy Goddess Aqua!")

# Preloaded Cogs
cogs = ["cogs.admin",
        "cogs.audio",
        "cogs.help",
        "cogs.jikan",
        "cogs.meme",
        "cogs.reddit",
        "cogs.utility"]

for cog in cogs:
    try:
        bot.load_extension(cog)
    except Exception as e:
        print(f"ERROR: {type(e).__name__} - {e}")
    else:
        print(f"SUCCESS: Loaded {cog}")

# Start Bot
@bot.event
async def on_ready():
    bot.AppInfo = await bot.application_info()

    startup = f"""
    Bot Name: {bot.user.name} - {bot.user.id}\n
    Owner: {bot.AppInfo.owner}\n
    Command Prefix: {PREFIX}\n
    discord.py Version: {discord.__version__}\n
    python Version: {platform.python_version()}\n
    """
    print(startup)

    activity_name = f"with water | {PREFIX}aquabot"
    activity = discord.Activity(name=activity_name, type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)

    print("AquaBot is ready!\n")

bot.run(TOKEN,
        bot=True,
        reconnect=True)
