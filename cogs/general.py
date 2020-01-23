"""
Some general commands:
    - about

https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
"""

# IMPORTS - external
import discord
from discord.ext import commands

# IMPORTS - internal
from aquabot import metadata

# COG INIT
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="about")
    async def about(self, ctx):
        """
        Prints some information about myself
        """
        embed = discord.Embed(colour=discord.Colour.blue())

        embed.add_field(name="Bot Name", value=metadata["name"], inline=True)
        embed.add_field(name="Admin", value=metadata["admin"], inline=True)
        embed.add_field(name="Prefix", value=metadata["prefix"], inline=True)
        embed.add_field(name="discord.py Version", value=metadata["discordpy_version"], inline=True)
        embed.add_field(name="python Version", value=metadata["python_version"], inline=True)
        embed.add_field(name="OS", value=metadata["os"], inline=True)

        footer_text = """
        This Bot is an OpenSource project by Marc and can be found on
        github.com/CramMK/aquabot
        """
        embed.set_footer(text=footer_text, icon_url="img/avatar.png")

        await ctx.send(embed=embed)


# COG ENDING
def setup(bot):
    bot.add_cog(General(bot))
