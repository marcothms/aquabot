"""
This framework can be used to create new Cogs, remember to add them in the config
"""

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
