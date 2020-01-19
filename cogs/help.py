#
# Cog for a custom Help Command
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#

# IMPORTS - exter
import discord
from discord.ext import commands

# COG INIT
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command( name="aquabot")
    async def aquabot(self, ctx):
        """
        Sends a short help for new users
        """
        response = """
        I'm the usele... divine AquaBot!
        If you need help, try using the `help` command!
        """

        await ctx.send(response)


# COG ENDING
def setup(bot):
    bot.add_cog(Help(bot))