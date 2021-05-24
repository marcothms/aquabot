"""
Admin commands, that can be used within the Discord Client
"""

from discord.ext import commands
import discord

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="load", hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """
        Used as 'load cogs.COGNAME'
        """
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**ERROR:** {type(e).__name__} - {e}')
        else:
            await ctx.send('**SUCCESS**')


    @commands.command(name="unload", hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """
        Used as 'unload cogs.COGNAME'
        """
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**ERROR:** {type(e).__name__} - {e}')
        else:
            await ctx.send('**SUCCESS**')


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
            await ctx.send(f'**ERROR:** {type(e).__name__} - {e}')
        else:
            await ctx.send('**SUCCESS**')


def setup(bot):
    bot.add_cog(Admin(bot))
