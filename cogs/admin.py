#
# A Cog that add admin command, usable within the Discord Client
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#
# "load", "unload", "reload"
# https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
#

# IMPORTS
import discord
from discord.ext import commands

# COG INIT
class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    # used as "load cogs.COGNAME"
    @commands.command(name="load", hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    # used as "unload cogs.COGNAME"
    @commands.command(name="unload", hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    # used as "reload cogs.COGNAME"
    @commands.command(name="reload", hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


# COG ENDING
def setup(bot):
    bot.add_cog(AdminCog(bot))
