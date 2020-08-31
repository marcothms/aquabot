"""
Fetch pictures from subreddits
"""

# IMPORTS - external
import discord
from discord.ext import commands
import random
import praw

# IMPORTS - internal
from __main__ import reddit_client_id
from __main__ import reddit_client_secret
from __main__ import reddit_client_useragent

# COG INIT
class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="reddit")
    async def reddit(self, ctx, sub: str):
        """
        Send a post from a subreddit to chat
        """
        reddit = praw.Reddit(client_id=reddit_client_id,
                             client_secret=reddit_client_secret,
                             user_agent=reddit_client_useragent)

        posts = reddit.subreddit(sub).hot()
        rand_post = random.randint(1, 100)
        # Make sure you're not sending a pinned post
        for i in range(0, rand_post):
            selected_post = next(x for x in posts if not x.stickied)

        await ctx.send(selected_post.url)

# COG ENDING
def setup(bot):
    bot.add_cog(Reddit(bot))
