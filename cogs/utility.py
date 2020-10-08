"""
Some (more or less) handy utility
"""

from discord.ext import commands
import random


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="invitelink", aliases=["invite"])
    async def invite_link(self, ctx, age=60*10, uses=100):
        """
        Sends the server's invitelink to chat
        """
        #age = 60 * 10
        #uses = 100
        unique = True

        channel = ctx.message.channel
        link = await channel.create_invite(
                max_age = age,
                max_uses = uses,
                unique = unique,
                reason = "Created by AquaBot")

        link_embed = discord.Embed(color=discord.Colour.blue())
        link_embed.add_field(
                name="Here's an invite to our server:",
                value=link,
                inline=True)
        link_embed.set_footer(
                text=f"Age: {age}, Uses: {uses}",
                icon_url=ctx.me.avatar_url
                )

        await ctx.send(embed=link_embed)


    @commands.command(name="pat")
    @commands.guild_only()
    async def pat(self, ctx, target: str):
        """
        Let's you pat a selected user
        """
        author = ctx.message.author
        if target is None:
            response = "No one to pat..."
        else:
            response = f"{target} got pat by {author.mention}"

        await ctx.send(response)


def setup(bot):
    bot.add_cog(Utility(bot))
