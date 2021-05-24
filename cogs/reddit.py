"""
Fetch pictures from subreddits
"""

from discord.ext import commands
import discord
import praw
import random

from __main__ import REDDIT_CLIENT_ID
from __main__ import REDDIT_CLIENT_SECRET
from __main__ import REDDIT_CLIENT_USERAGENT


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @staticmethod
    def find_post(posts):
        rand_post = random.randint(1, 100)
        # Make sure you're not sending a pinned post
        for i in range(0, rand_post):
            submission = next(post for post in posts if not post.stickied)
        return submission
        
    async def output(self, ctx, submission):
        output = f"'{submission.title}' by {submission.author.name} - 🔼 {submission.score}"
        if submission.over_18:
            if not ctx.channel.is_nsfw():
                await ctx.send("The post is marked as NSFW, but your channel isn't!")
                return
            else:
                output = f"❗ NSFW ❗ " + output

        await ctx.send(output)
        await ctx.send(submission.url)


    @commands.command(name="reddit")
    async def reddit(self, ctx, sub: str, sorting="hot", time_filter="all"):
        """
        Send a post from a subreddit to chat. Timefilters: all, day, hour, month, week, year
        """
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                             client_secret=REDDIT_CLIENT_SECRET,
                             user_agent=REDDIT_CLIENT_USERAGENT,
                             check_for_async=False)

        try:
            reddit.subreddits.search_by_name(sub, exact=True)
        except:
            await ctx.send(f"Subreddit '{sub}' not found!")

        if sorting == "hot":
            posts = reddit.subreddit(sub).hot()
        elif sorting == "top":
            posts = reddit.subreddit(sub).top(time_filter)
        elif sorting == "new":
            posts = reddit.subreddit(sub).new()
        else:
            await ctx.send(f"Invalid Argument: {sorting}")
            return

        await ctx.trigger_typing()
        submission = self.find_post(posts)
        await self.output(ctx, submission)


def setup(bot):
    bot.add_cog(Reddit(bot))
