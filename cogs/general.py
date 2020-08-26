"""
Some general commands:

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


# COG ENDING
def setup(bot):
    bot.add_cog(General(bot))
