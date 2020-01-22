#
# A Cog that add admin command, usable within the Discord Client
#
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
#
# "load", "unload", "reload"
# https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
#
"""
Admin commands, that can be used from within the chat

https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html

"load", "unload", "reload"
https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
"""

# IMPORTS
import discord
from discord.ext import commands

# COG INIT
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="load", hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """
        Used as 'load cogs.COGNAME'
        """
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    @commands.command(name="unload", hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """
        Used as 'unload cogs.COGNAME' 
        """
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    @commands.command(name="reload", hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """
        Used as 'reload cogs.COGNAME'
        """
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


# COG ENDING
def setup(bot):
    bot.add_cog(Admin(bot))