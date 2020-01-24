"""
Make Aqua be able to join voice channel and play audio:
    - join
    - leave
    - play

https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
https://stackoverflow.com/questions/56031159/discord-py-rewrite-what-is-the-source-for-youtubedl-to-play-music
"""

# IMPORTS
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import os
import youtube_dl

# COG INIT
class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# COG BODY
    @commands.command(name="join", aliases=["j"])
    @commands.guild_only()
    async def join(self, ctx):
        """
        Tries to join the author's current voice channel
        """
        channel = ctx.message.author.voice.channel
        if not channel:
            ctx.send("You're not connected to a voice channel!")
            return

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
            await ctx.send(f"`Moved to {channel}!`")
        else:
            voice = await channel.connect()
            await ctx.send(f"`Joined {channel}!`")


    @commands.command(name="leave", aliases=["quit, l"])
    @commands.guild_only()
    async def leave(self, ctx):
        """
        Leaves the voice channel, if connected
        """
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"`Left {channel}!`")
        else:
            await ctx.send("I'm not connected to a channel!")


    @commands.command(name="play", aliases=["p"])
    @commands.guild_only()
    async def play(self, ctx, url: str):
        """
        Plays music from YT link specifies
        """
        # TODO
        try:
            if os.path.isfile("song.mp3"):
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current song to end or use the `stop`command")
            return

        voice = get(bot.voice_clients, guild=ctx.guild)
        youtube_dl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YouTubeDL(youtube_dl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        voice.volume=25
        voice.is_playing()


# COG ENDING
def setup(bot):
    bot.add_cog(Voice(bot))
