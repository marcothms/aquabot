"""
A simple reminder option
"""

# IMPORTS
from discord.ext import commands


# COG INIT
class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY


# COG ENDING
def setup(bot):
    bot.add_cog(Reminder(bot))
