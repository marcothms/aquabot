"""
Some (more or less) handy utility:
    - invitelink
    - pat

https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
"""

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


    @commands.command(name="pat")
    @commands.guild_only()
    async def pat(self, ctx, target: str):
        """
        Let's you pat a selected user
        """
        author = ctx.message.author
        if target is None:
            response = "No one to pat..."
        elif target.capitalize() == "Noel":
            response = "NNN-GYAAAA!"
        else:
            response = f"{target} got pat by {author.mention}"

        await ctx.send(response)


# COG ENDING
def setup(bot):
    bot.add_cog(Utility(bot))
