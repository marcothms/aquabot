"""
Some general commands:
    - about

https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
"""

# IMPORTS - external
import discord
from discord.ext import commands
import platform

# IMPORTS - internal
import loadconfig

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
        embed.set_thumbnail(url=ctx.me.avatar_url)
        embed.set_image(url=ctx.me.avatar_url)

        embed.add_field(name="Owner", value=self.bot.AppInfo.owner, inline=True)
        embed.add_field(name="Command Prefix", value=loadconfig.__prefix__, inline=True)
        embed.add_field(name="Discord.py Version", value=discord.__version__, inline=True)
        embed.add_field(name="Python Version", value=platform.python_version(), inline=True)
        embed.add_field(name="OS", value=f"{platform.system()} {platform.release()} {platform.version()}", inline=True)

        footer_text = (
            "This Bot is an OpenSource project by Marc and can be found "
            "on github.com/CramMK/aquabot")
        embed.set_footer(text=footer_text, icon_url=loadconfig.__avatar__)

        await ctx.send(embed=embed)


# COG ENDING
def setup(bot):
    bot.add_cog(General(bot))
