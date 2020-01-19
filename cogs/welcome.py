#
# A Cog thats deals with welcoming new users etc.
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#

# IMPORTS
import discord
from discord.ext import commands

# COG INIT
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Greets new users joining your server
        """
        channel = member.guild.system_channel
        text = f"Welcome {member.mention} to our useless Discord!"
        if channel is not None:
            await channel.send(text)


    @commands.command(name="hello")
    async def hello(self, ctx):

        await ctx.send(f"Hello {ctx.author.mention}!")

# COG ENDING
def setup(bot):
    bot.add_cog(Welcome(bot))