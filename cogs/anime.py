"""
Some anime-related commands
"""

# IMPORTS - external
from discord.ext import commands
import random

# IMPORTS - internal
import loaddata


# COG INIT
class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="animepic")
    async def animemedia(self, ctx):
        """
        Sends a random Anime gif or picture
        """

        media_type = random.choice(loaddata.__media_anime__)
        media = random.choice(media_type)
        await ctx.send(media)

    @commands.command(name="waifupic")
    async def waifumedia(self, ctx, name: str):
        """
        Sends a random picture or gif of an Anime girl
        """
        girl = name.capitalize()

        if girl == "List":
            girl_list = ""
            for key in loaddata.__media_girl__.keys():
                if not girl_list:
                    girl_list = girl_list + key
                else:
                    girl_list = girl_list + ", " + key

            await ctx.send(f"Currently listed girls: `{girl_list}`")

        else:
            try:
                media = random.choice(loaddata.__media_girl__[girl])
                await ctx.send(media)
            except KeyError:
                text = (
                        f"Girl `{girl}` not found in database!\n"
                        "It probably sucks...")
                await ctx.send(text)


# COG ENDING
def setup(bot):
    bot.add_cog(Anime(bot))
