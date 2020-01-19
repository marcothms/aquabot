#
# This Cog adds some utility commands
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#

# IMPORTS
import discord
from discord.ext import commands

# COG INIT
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="invitelink", aliases=["invite"])
    async def invite_link(self, ctx):
        """
        Sends the server's invitelink to chat
        """

        # TODO fetch this from config so more servers are supported
        link = "Here is our invite link: https://discordapp.com/invite/HbYfyJT"
        await ctx.send(link)

# COG ENDING
def setup(bot):
    bot.add_cog(Utility(bot))
