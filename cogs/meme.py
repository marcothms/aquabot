"""
Send memes to chat
"""

from discord.ext import commands
import discord
import random

import memes


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @staticmethod
    def parse(query):
        """
        Parse a request
        """
        try:
            to_choose = memes.memes[query.capitalize()]
            return random.choice(to_choose)
        except KeyError:
            return None


    @commands.command(name="meme")
    async def meme(self, ctx, query: str):
        """
        Sends a meme
        - marc
        - cenk
        - olli
        """
        meme = self.parse(query)
        if meme:
            await ctx.send(meme)
        else:
            await ctx.send(f"Meme '{query}' not found")


def setup(bot):
    bot.add_cog(Meme(bot))
q
