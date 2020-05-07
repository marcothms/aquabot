"""
Some help for the users:
    - aquabot

https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
"""

# IMPORTS - external
import discord
from discord.ext import commands

# IMPORTS - internal
import loadconfig

# COG INIT
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="aquabot")
    async def aquabot(self, ctx):
        """
        Sends a short help for new users
        """
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_thumbnail(url=ctx.me.avatar_url)

        embed.add_field(name="Owner", value=self.bot.AppInfo.owner, inline=True)
        embed.add_field(name="Command Prefix", value=loadconfig.__prefix__, inline=True)
        embed.add_field(name="Source Code", value="[GitHub](https://github.com/crammk/aquabot)", inline=True)

        footer_text = "This Bot is a project by MarcMK."
        embed.set_footer(text=footer_text)

        await ctx.send(embed=embed)


# COG ENDING
def setup(bot):
    bot.add_cog(Help(bot))
