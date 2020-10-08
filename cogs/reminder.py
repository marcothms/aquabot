"""
A simple reminder option
"""

import discord
from discord.ext import commands


class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(Reminder(bot))
