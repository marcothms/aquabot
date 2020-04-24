"""
Some anime-related commands:


https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
"""

# IMPORTS - external
import discord
from discord.ext import commands
import random

# IMPORTS - internal
import loadconfig

# COG INIT
class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="animemedia")
    async def animemedia(self, ctx):
        """
        Sends a random Anime gif or picture
        """
        # Choose either a gif or a pic -> config/media.py
        media_type = random.choice(loadconfig.__media_anime__)
        media = random.choice(media_type)
        await ctx.send(media)

    @commands.command(name="animegirl")
    async def girlmedia(self, ctx, query: str):
        """
        Sends a random picture or gif of an Anime girl
        """
        # config/media.py
        girl = query.capitalize()

        if girl == "List":
            girl_list = ""
            for key in loadconfig.__media_girl__.keys():
                if not girl_list:
                    girl_list = girl_list + key
                else:
                    girl_list = girl_list + ", " + key

            await ctx.send(f"Currently listed girls: `{girl_list}`")

        else:
            try:
                media = random.choice(loadconfig.__media_girl__[girl])
                await ctx.send(media)
            except KeyError as error:
                text = (
                        f"Girl `{girl}` not found in database!\n"
                        "It probably sucks...")
                await ctx.send(text)


# COG ENDING
def setup(bot):
    bot.add_cog(Anime(bot))
