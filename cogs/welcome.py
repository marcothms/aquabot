"""
Welcoming new users etc.
"""

import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Greets new users joining your server
        """
        channel = member.guild.system_channel
        text = f"Welcome {member.mention} to our Discord!"
        if channel is not None:
            await channel.send(text)

    @commands.command(name="hello")
    async def hello(self, ctx):
        """
        Sends a simple reply to the user
        """
        await ctx.send(f"Hello {ctx.author.mention}!")


def setup(bot):
    bot.add_cog(Welcome(bot))
