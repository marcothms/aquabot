"""
Jikan is an unofficial API to access data from MyAnimeList
https://jikanpy.readthedocs.io/en/latest/
"""

import discord
from discord.ext import commands
from jikanpy import Jikan

jikan = Jikan()

class Jikan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group(name="anime")
    async def anime(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.invoke(self.bot.get_command("help"), query="anime")


    @anime.command(name="query")
    async def query(self, ctx, *query: str):
        """
        Query some information about an anime
        """
        search = jikan.search("anime", query)
        results = search.get("results")

        top = results[0]  # get top result

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_thumbnail(url=top.get("image_url"))

        embed.add_field(name="Title", value=top.get("title"), inline=True)
        embed.add_field(name="URL", value=f'[MAL]({top.get("url")})', inline=True)
        embed.add_field(name="Episodes", value=top.get("episodes"), inline=True)
        embed.add_field(name="Airing", value=top.get("airing"), inline=True)
        embed.add_field(name="Synopsis", value=top.get("synopsis"), inline=True)

        await ctx.send(embed=embed)


    @commands.group(name="manga")
    async def manga(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.invoke(self.bot.get_command("help"), query="manga")


    @commands.group(name="character", aliases=["char"])
    async def character(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.invoke(self.bot.get_command("help"), query="character")


def setup(bot):
    bot.add_cog(Jikan(bot))
