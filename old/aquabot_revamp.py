#################################
### AquaBot created by MarcMK ###
###      Project started      ###
###       on 17.09.2019       ###
###      Aqua Best Girl!      ###
#################################

# This project uses discordpy
# https://discordpy.readthedocs.io/en/latest/intro.html

###############
### IMPORTS ###
###############

import discord
from discord.ext import commands
from discord.utils import get

import logging
import random
import os.path

# https://github.com/Giphy/giphy-python-client#installation--usage
# pip install giphy_client
import giphy_client
from giphy_client.rest import ApiException

# ffmpeg - still unused
# youtube_dl - still unused

#################
### CONSTANTS ###
#################

BOT_TOKEN = ""
GIPHY_API_TOKEN = ""

COMMAND_PREFIX = "."

####################
### INITIALIZERS ###
####################

bot = commands.Bot(command_prefix = ".")
bot.remove_command("help")
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.CRITICAL)

##############
### EVENTS ###
##############

@bot.event
async def on_ready():
    name = f"Hentai | {COMMAND_PREFIX}aquabot"
    activity = discord.Activity(name=name, type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    print(f"AquaBot is ready!\n")

# TODO don't use hardcoded channel id
@bot.event
async def on_member_join(member):
    text = f"Welcome {member.mention} to our Discord! I am the usele... divine AquaBot!"
    channel = bot.get_channel(541637988120133634)
    await channel.send(text)

############
### HELP ###
############

@bot.command(aliases=["aquabot"])
async def help(ctx):
    embed_help = discord.Embed(colour = discord.Colour.blue())
    text = f"""
    All commands were split up into these categories.\n
    For furter explanation, use e.g. `{COMMAND_PREFIX}commands general`\n
    """

    embed_help.add_field(name="I'm the usele... divine AquaBot!", value=text, inline=False)

    # All inline=true, so the arrangement is responsive
    embed_help.add_field(name="• General", value="Guess what...", inline=True)
    embed_help.add_field(name="• Media", value="Sounds, GIFS, ...", inline=True)
    embed_help.add_field(name="• Axisbot", value="Praaaay!", inline=True)
    embed_help.add_field(name="• Waifu", value="Best Girl Stuff", inline=True)
    embed_help.add_field(name="• Steam", value="Configs, Profiles, ...", inline=True)
    embed_help.add_field(name="• Support", value="Need even more help?", inline=True)

    link = "https://external-preview.redd.it/9n8rYQUzOck_C54YtzXt8qOFW_rY71-AZZHljtj14qw.jpg?auto=webp&s=aad1bc4546806bc435da29e4502e10442f298f2f"
    embed_help.set_footer(text="AquaBot made by MarcMK.", icon_url=link)
    await ctx.send(embed=embed_help)

@bot.command()
async def commands(ctx, command):
    # All available command-groups
    command_list = [
        "general",
        "media",
        "axisbot",
        "waifu",
        "steam",
        "support"
        ]

    if command in command_list:
        embed_commands = discord.Embed(colour = discord.Colour.blue())

        general = f"""
        `{COMMAND_PREFIX}aquabot`\n
        `{COMMAND_PREFIX}useless`\n
        `{COMMAND_PREFIX}pat [@target]`\n
        `{COMMAND_PREFIX}invitelink`\n
        `{COMMAND_PREFIX}boost`\n
        `{COMMAND_PREFIX}senpainoticeme`\n
        `{COMMAND_PREFIX}maddlesticks`\n
        `{COMMAND_PREFIX}flame [@target_name]`\n
        """

        media = f"""
        `{COMMAND_PREFIX}gif [tag]`\n
        `{COMMAND_PREFIX}listgif`\n
        `{COMMAND_PREFIX}join`\n
        `{COMMAND_PREFIX}leave`\n
        `{COMMAND_PREFIX}play [file]`\n
        """

        axisbot = f"""
        `{COMMAND_PREFIX}axisbot`\n
        `{COMMAND_PREFIX}pray`\n
        """

        waifu = f"""
        `{COMMAND_PREFIX}waifuwar [waifu] [waifu]`\n
        `{COMMAND_PREFIX}waifupicture`\n
        """

        steam = f"""
        `{COMMAND_PREFIX}steam [name]`\n
        `{COMMAND_PREFIX}steamid [id]`\n
        `{COMMAND_PREFIX}marcconfig`\n
        """

        support = "`WIP!`"

        name = f"""
        Here are all commands from `{command}`\n
        Pro tip: The argument `list` shows all possible arguments from a command.
        """

        # TODO does value=command work here?
        embed_commands.add_field(name=name, value=command, inline=True)

        await ctx.send(embed=embed_commands)

    else:
        await ctx.send("> Categorie not found!")

########################
### GENERAL COMMANDS ###
########################

# Prints a random string to the text-channel
@bot.command()
async def useless(ctx):
    responses = [
        "I'm not useless!",
        "You're useless!",
        "Megumin is more useless!"
        ]
    await ctx.send(f"> {random.choice(responses)}")

# Pats the specified user
@bot.command()
async def pat(ctx, target):
    if target == "noel" or target == "Noel":
        await ctx.send("> NNN-GYAAAAAAA!")
    else:
        response = f"{ctx.message.author.mention} has patted {target}"
        await ctx.send(response)

# Sends Discord Invitelink to Channel
@bot.command(aliases=["invitelink"])
async def invite_link(ctx):
    response = "Here is our invite link: https://discordapp.com/invite/HbYfyJT"
    await ctx.send(f"> {response}")

# Prints an Issei reference

@bot.command()
async def boost(ctx):
    response = """
    BOOST! BOOST! BOOST! 🐲🐉\n
    Wait, this isn't my text...
    """
    await ctx.send(f">>> {response}")

@bot.command()
async def senpainoticeme(ctx):
    file = "./pictures/lorgst.png"
    file_exists = os.path.isfile(file)
    if file_exists:
        await ctx.send(file=discord.File(file))
    else:
        await ctx.send("Error opening the file! Maybe it doesn't exist?")

@bot.command()
async def maddlesticks(ctx):
    file = "./pictures/fiddlesticksmarc.png"
    file_exists = os.path.isfile(file)
    if file_exists:
        await ctx.send(file=discord.File(file))
    else:
        await ctx.send("Error opening the file! Maybe it doesn't exist?")

# Flames a player
@bot.command()
async def flame(ctx, username):
    insult_list = [
        "is useless!",
        "is worthless!"
        ]
    response = f"{username} {random.choice(insult_list)}"
    await ctx.send(f"> {response}")

######################
### Media Commands ###
######################
