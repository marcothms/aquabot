#
# A Cog that add some general commands
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#

# IMPORTS
import discord
from discord.ext import commands

# COG INIT
class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(
            name="invitelink",
            description="Sends the invite link",
            aliases=["invite"]
            )
    async def invite_link(self, ctx):

        # TODO fetch this from config so more servers are supported
        link = "Here is our invite link: https://discordapp.com/invite/HbYfyJT"
        await ctx.send(link)


    @commands.command(
            name="pat",
            description="Pats the selected user"
            )
    @commands.guild_only()
    async def pat(self, ctx, target: str):

        author = ctx.message.author
        if target is None:
            response = "No one to pat..."
        else if target.capitalize == "Noel":
            response = "NNN-GYAAAA!"
        else:
            response = f"{target.mention} got pat by {author.mention}"

        await ctx.send(response)


# COG ENDING
def setup(bot):
    bot.add_cog(GeneralCog(bot))
