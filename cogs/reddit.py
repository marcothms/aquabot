"""
Fetch pictures from subreddits
"""

import discord
from discord.ext import commands
import random
import praw

from __main__ import REDDIT_CLIENT_ID
from __main__ import REDDIT_CLIENT_SECRET
from __main__ import REDDIT_CLIENT_USERAGENT


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="reddit")
    async def reddit(self, ctx, sub: str, sorting="hot", time_filter="all"):
        """
        Send a post from a subreddit to chat. Timefilters: all, day, hour, month, week, year
        """
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                             client_secret=REDDIT_CLIENT_SECRET,
                             user_agent=REDDIT_CLIENT_USERAGENT)

        try:
            if sorting == "hot":
                posts = reddit.subreddit(sub).hot()
            elif sorting == "top":
                posts = reddit.subreddit(sub).top(time_filter)
            elif sorting == "new":
                posts = reddit.subreddit(sub).new()

        except ValueError as e:
            await ctx.send(f"Invalid Argument: {e}")

        # WORKS
        rand_post = random.randint(1, 100)
        # Make sure you're not sending a pinned post
        for i in range(0, rand_post):
            submission = next(x for x in posts if not x.stickied)

        await ctx.send(f"'{submission.title}' by {submission.author.name} - 🔼 {submission.score}")
        await ctx.send(submission.url)


def setup(bot):
    bot.add_cog(Reddit(bot))
