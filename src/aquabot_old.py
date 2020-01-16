#################################
### AquaBot created by MarcMK ###
###      Project started      ###
###       on 17.09.2019       ###
###      Aqua Best Girl!      ###
#################################

##############
### IMPORT ###
##############

import discord
import logging
import random
from discord.ext import commands
from discord.utils import get

# https://github.com/Giphy/giphy-python-client#installation--usage
# pip install giphy_client
import giphy_client
from giphy_client.rest import ApiException

# ffmpeg - still unused
# youtube_dl - still unused

##############
### TOKENS ###
##############

GIPHY_API_KEY = ""
BOT_TOKEN = ""

####################
### INITIALIZERS ###
####################

bot = commands.Bot(command_prefix = ".")
prefix = "."
token = BOT_TOKEN
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
    name = f"Hentai | {prefix}aquabot"
    activity = discord.Activity(name=name, type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)
    print(f"AquaBot is ready!\n")

@bot.event
async def on_member_join(member):
    text = 'Welcome {} to our Discord! I am the usele... divine AquaBot!'.format(member.mention)
    channel = bot.get_channel(541637988120133634)
    await channel.send(text)

############
### HELP ###
############

@bot.command(aliases=["aquabot"])
async def help(ctx):
    embed_help = discord.Embed(colour = discord.Colour.blue())

    text = f"All commands were split up into these categories.\n For furter explanation, use e.g. `{prefix}commands general`\n"
    embed_help.add_field(name="I'm the usele... divine AquaBot!", value=text, inline=False)

    embed_help.add_field(name="• General", value="Guess what...", inline=True)
    embed_help.add_field(name="• Media", value="Sounds, GIFS, ...", inline=True)
    embed_help.add_field(name="• Axisbot", value="Praaaay!", inline=True)
    embed_help.add_field(name="• Waifu", value="Best Girl Stuff", inline=True)
    embed_help.add_field(name="• Steam", value="Configs, Profiles, ...", inline=True)
    embed_help.add_field(name="• Support", value="Need even more help?", inline=True)

    link = "https://external-preview.redd.it/9n8rYQUzOck_C54YtzXt8qOFW_rY71-AZZHljtj14qw.jpg?auto=webp&s=aad1bc4546806bc435da29e4502e10442f298f2f"
    embed_help.set_footer(text="AquaBot made by MarcMK.", icon_url=link)
    await ctx.send(embed=embed_help)

### COMMANDS ###

@bot.command(aliases=["command"])
async def commands(ctx, command):
    command_list = ["general", "media", "axisbot", "waifu", "steam", "support"]
    if command in command_list:
        embed_commands = discord.Embed(colour = discord.Colour.blue())

        general = f"`{prefix}aquabot`\n`{prefix}useless`\n`{prefix}pat [@target]`\n`{prefix}invitelink`\n`{prefix}boost`\n`{prefix}senpainoticeme`\n`{prefix}maddlesticks`\n`{prefix}flame [target_name]`\n"

        media = f"`{prefix}gif [tag]`\n`{prefix}listgif`\n`{prefix}join`\n`{prefix}leave`\n`{prefix}play [file]`\n"

        axisbot = f"`{prefix}axisbot `\n`{prefix}pray`\n"

        waifu = f"`{prefix}waifuwar [waifu] [waifu]`\n`{prefix}waifupicture`\n"

        steam = f"`{prefix}steam [name]`\n`{prefix}steamid [id]`\n`{prefix}marcconfig`\n"

        support = "`WIP!`"

        if command == "general":
            text_val = general
        elif command == "media":
            text_val = media
        elif command == "axisbot":
            text_val = axisbot
        elif command == "waifu":
            text_val = waifu
        elif command == "steam":
            text_val = steam
        else:
            text_val = support

        embed_commands.add_field(name=f"Here are all commands from `{command}`\nPro tip: Argument `list` shows all possible arguments from a command.", value=text_val, inline=True)
        await ctx.send(embed=embed_commands)
    else:
        await ctx.send("> Categorie not found!")

########################
### GENERAL COMMANDS ###
########################

#useless
@bot.command()
async def useless(ctx):
    responses = ["I'm not useless!","You're useless!","Megumin is more useless!"]
    await ctx.send(f"> {random.choice(responses)}")

#BOOST BOOST BOOST
@bot.command()
async def boost(ctx):
    text1 = "BOOST! BOOST! BOOST! 🐲🐉"
    text2 = "Wait, this isn't my text..."
    await ctx.send(f">>> {text1} \n {text2}")

#pat
@bot.command()
async def pat(ctx, target_name):
    if target_name == "noel":
        await ctx.send("> NNN-GYAAAAAAA!")
    elif target_name == "Noel":
        await ctx.send("> NNN-GYAAAAAAA!")
    else:
        author = ctx.message.author
        text = '{} has head-patted {}!'.format(author.mention, target_name)
        await ctx.send(text)

@bot.command()
async def senpainoticeme(ctx):
    await ctx.send(file=discord.File("./pictures/lorgst.png"))

@bot.command()
async def maddlesticks(ctx):
    await ctx.send(file=discord.File("./pictures/fiddlesticksmarc.png"))

#Send Discord Invitelink to Channel
@bot.command(aliases=["invitelink"])
async def invite_link(ctx):
    await ctx.send("> Here is our invite link: https://discordapp.com/invite/HbYfyJT")

#Flames a player
@bot.command()
async def flame(ctx, user_name):
    insult_list = ["is useless!", "is worthless!"]
    insult = random.choice(insult_list)
    await ctx.send(f"> {user_name} {insult}")

######################
### Media Commands ###
######################

### GIPHY INITS / FUNCTIONS ###

#https://github.com/Giphy/giphy-python-client#installation--usage

api_key = GIPHY_API_KEY
api_instance = giphy_client.DefaultApi()
limit = 25
offset = 0
lang = "en"
fmt = "json"

async def gif_search_init(searchterm):
    try:
        api_response_search = api_instance.gifs_search_get(
        api_key,
        searchterm,
        limit=limit,
        offset=offset,
        lang=lang,
        fmt=fmt)
        gif_list = list(api_response_search.data)
        gif = random.choices(gif_list)
        return gif[0].url
    except ApiException as exception:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % exception)
        await channel

### GIPHY COMMANDS ###

@bot.command(aliases=["g"])
async def gif(ctx, searchterm):
    gif = await gif_search_init(searchterm)
    await ctx.send(gif)

@bot.command(aliases=["listgif"])
async def gif_list(ctx):
    embed_gif_list = discord.Embed(colour = discord.Colour.blue())
    gifs = f"`{prefix}konosubagif`\n`{prefix}megumingif`\n`{prefix}remgif`"
    embed_gif_list.add_field(name="Try one of these:", value=gifs, inline=True)
    await ctx.send(embed=embed_gif_list)

@bot.command(aliases=["konosubagif"])
async def gif_konosuba(ctx):
    gif = await gif_search_init("konosuba")
    await ctx.send(gif)

@bot.command(aliases=["megumingif"])
async def gif_megumin(ctx):
    gif = await gif_search_init("megumin")
    await ctx.send(gif)

@bot.command(aliases=["remgif"])
async def gif_rem(ctx):
    gif = await gif_search_init("rem re:zero")
    await ctx.send(gif)

### SOUND SETUP ###

@bot.command(aliases=["j"])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        await channel.connect()
        await ctx.send("> Joined!")

@bot.command(aliases=["l", "quit"])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    await voice.disconnect()
    await ctx.send("> Left!")

#@bot.command()
#async def play(ctx, url):
#    guild = ctx.message.guild
#    voice = get(bot.voice_clients, guild=ctx.guild)
#    player = await voice.create_ytdl_player(url)
#    player.start()

### SOUND CLIPS ###

@bot.command(aliases=["p"])
async def play(ctx, file_name):
    voice = get(bot.voice_clients, guild=ctx.guild)
    channel = ctx.message.author.voice.channel

    if file_name == "list":
        embed_help_chat = discord.Embed(colour = discord.Colour.blue())
        titles = open("sounds/AAAlist.txt", encoding="utf-8").read()
        embed_help_chat.add_field(name="Try one of these:", value=titles, inline=True)
        await ctx.send(embed=embed_help_chat)
    else:
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            await channel.connect()
            await ctx.send("> Joined!")
        location = "sounds/"
        ending = ".mp3"
        player = f"{location}{file_name}{ending}"
        voice = get(bot.voice_clients, guild=ctx.guild)
        voice.play(discord.FFmpegPCMAudio(player))
        voice.source.volume = 0.005

#########################
### AXIS BOT COMMANDS ###
#########################

#Main Command > needs more features
@bot.command()
async def axisbot(ctx):
    link = "> https://www.reddit.com/r/AquaSama/"
    gif_link = "> https://media.giphy.com/media/yiqkf0clPXvAk/giphy.gif"
    text = f"I see you're interested into the Axis Order? Come join us here: {link}"
    await ctx.send(gif_link)
    await ctx.send(text)

#Pray Function > Database? > Leveling System?
@bot.command()
async def pray(ctx):
    text = "> {0.mention} has prayed for the usel... divine Water Goddess Aqua!"
    await ctx.send(text.format(ctx.message.author))

######################
### WAIFU COMMANDS ###
######################

#Waifu Comparison
@bot.command(aliases=["waifuwar"])
async def waifu_war(ctx, waifu1, waifu2):
    waifu_list = [waifu1, waifu2]
    random1 = random.choice(waifu_list)
    if random1 == waifu1:
        random2 = waifu2
    else:
        random2 = waifu1
        text_list = ["is clearly superior to", "is waaaay better than"]
        text = random.choice(text_list)
        await ctx.send(f"> {random1} {text} {random2}!")

#Waifu Pictures
@bot.command(aliases=["waifupicture", "waifupic"])
async def waifu_picture(ctx, waifu):
    waifu_list = ["aqua", "akeno", "rem", "megumin"]
    if waifu in waifu_list:
        await ctx.send(file=discord.File(f"./pictures/{waifu}.jpg"))
    else:
        await ctx.send("> Your Waifu either sucks or is non-existent, so no picture will be send.")

######################
### STEAM COMMANDS ###
######################

#Send Steam Profiles with predefined Name
@bot.command(aliases=["steam"])
async def steam_profiles_name(ctx, name):
    embed = discord.Embed(colour = discord.Colour.blue())

    profile_list = ["marc", "lorgst", "chikmalo", "jaron", "max"]
    if name in profile_list:
        profile_link = "https://ecosia.org"
        embed.add_field(name=f"Profile from `{name}`", value=profile_link, inline=True)
    elif name == "list":
        list = "`marc`\n`marc_smurf`\n`lorgst`\n`chikmalo`\n`jaron`\n`max`\n"
        embed.add_field(name="Available Profiles:", value=list, inline=True)
    else:
        embed.add_field(name="Steamprofile", value="Error.", inline=False)

    await ctx.send(embed=embed)

#Send Steam Profiles with ID
@bot.command(aliases=["steamid"])
async def steam_profiles_id(ctx, id):
    link = "https://steamcommunity.com/id/"
    output = f"{link}{id}"
    await ctx.send(output)

#Send my CS:GO Config to Channel
@bot.command(aliases=["marcconfig"])
async def marc_csgo_config(ctx):
    await ctx.send("Last updated on 19.09.2019:")
    with open("docs/marcexec.cfg", "rb") as fp:
        await ctx.send(file=discord.File(fp, "marcexec.cfg"))

#####################
### TEST PURPOSES ###
#####################

#send a pic
#@bot.command()
#async def fetchaqua(ctx):
#    FunctionExecuted(ctx.message.author, ctx.command)
#    await ctx.send(file=discord.File("./pictures/aqua.jpg"))
#
#read a file
#@bot.command()
#async def fetchtext(ctx):
#    FunctionExecuted(ctx.message.author, ctx.command)
#    text = open("docs/test.txt", encoding="utf-8").read()
#    await ctx.send(text)

###############
### RUN BOT ###
###############

bot.run(token)
