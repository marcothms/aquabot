"""
Send spicy memes to chat
"""

import discord
from discord.ext import commands
import random

import memes


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="meme")
    async def meme(self, ctx, meme: str):
        """
        Sends a spicy meme to the chat
        """
        query = meme.capitalize()

        if query == "List":
            meme_list = ""
            for key in memes.__memes_list__.keys():
                if not meme_list:
                    meme_list = meme_list + key
                else:
                    meme_list = meme_list + ", " + key

            await ctx.send(f"Currently listed memes: `{meme_list}`")
        else:
            try:
                meme = random.choice(memes.__memes_list__[query])
                await ctx.send(meme)
            except KeyError as e:
                await ctx.send("Meme not found in database")


def setup(bot):
    bot.add_cog(Meme(bot))
