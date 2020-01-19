#
# A Cog that add some general commands
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#

# IMPORTS - external
import discord
from discord.ext import commands

# COG INIT
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="about")
    async def about(self, ctx):
        """
        Prints some information about myself
        """
        embed = discord.Embed(colour=discord.Colour.blue())

        embed.add_field(name="test", value="test2")

        embed.set_footer(text="footer", icon_url="img/avatar.png")
        

        await ctx.send(embed=embed)



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
    bot.add_cog(General(bot))