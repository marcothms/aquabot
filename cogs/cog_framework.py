#
# foo
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#

# IMPORTS
import discord
from discord.ext import commands

# COG INIT
class Foo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY

# COG ENDING
def setup(bot):
    bot.add_cog(Foo(bot))