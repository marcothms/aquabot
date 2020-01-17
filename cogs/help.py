#
# Cog for a custom Help Command
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#

# IMPORTS
import discord
from discord.ext import commands

# COG INIT
class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(
            name="aquabot"
            description="Prints a short help for new users"
            )
    async def aquabot(self, ctx):

        await ctx.send("""
                I'm the usele... divine AquaBot!\n
                If you need help, try using the `help` command!\n
                """)


# COG ENDING
def setup(bot):
    bot.add_cog(HelpCog(bot))
