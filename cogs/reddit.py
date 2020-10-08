"""
Fetch pictures from subreddits
"""

# IMPORTS - external
from discord.ext import commands
import random
import praw

# IMPORTS - internal
from __main__ import REDDIT_CLIENT_ID
from __main__ import REDDIT_CLIENT_SECRET
from __main__ import REDDIT_CLIENT_USERAGENT


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
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                             client_secret=REDDIT_CLIENT_SECRET,
                             user_agent=REDDIT_CLIENT_USERAGENT)

        posts = reddit.subreddit(sub).hot()
        rand_post = random.randint(1, 100)
        # Make sure you're not sending a pinned post
        for i in range(0, rand_post):
            post = next(x for x in posts if not x.stickied)

        await ctx.send(f"> '{post.title}' by {post.author.name}")
        await ctx.send(post.url)


# COG ENDING
def setup(bot):
    bot.add_cog(Reddit(bot))
