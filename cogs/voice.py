"""
Make Aqua be able to join voice channel and play audio:
    - join
    - leave
    - play

https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html
https://stackoverflow.com/questions/56060614/how-to-make-a-discord-bot-play-youtube-audio
"""

# IMPORTS - external
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import os
import glob
import youtube_dl

# IMPORTS - internal
import loadconfig

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
            await ctx.send(f"Moved to {channel}!")
        else:
            voice = await channel.connect()
            await ctx.send(f"Joined {channel}!")


    @commands.command(name="leave", aliases=["quit","disconnect","dc"])
    @commands.guild_only()
    async def leave(self, ctx):
        """
        Leaves the voice channel, if connected
        """
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"Left {channel}!")
            # cleanup
            yt_files = glob.glob("youtube-*")
            for f in yt_files:
                os.remove(f)
        else:
            await ctx.send("I'm not connected to a channel!")

    @commands.command(name="skip")
    @commands.guild_only()
    async def skip(self, ctx):
        """
        Skips the current song: WIP!
        """
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await ctx.send("Skipping...")
        else:
            await ctx.send("I'm not connected to a channel!")


    # Begin of YouTube Player

    @commands.command(name="play", aliases=["p"])
    @commands.guild_only()
    async def play(self, ctx, *query: str):
        """
        Plays music from YouTube
        """
        # concat query tuple into string
        url = " ".join(query)

        # join channel
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not channel:
            ctx.send("You're not connected to a voice channel!")
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            await ctx.send(f"Joined {channel}!")


        youtube_dl.utils.bug_reports_message = lambda: ''
        ytdl_format_options = {
            'format': 'bestaudio/best',
            'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
            'restrictfilenames': True,
            'noplaylist': True,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': True,
            'default_search': 'auto',
            'source_address': '0.0.0.0'
        }
        ffmpeg_options = {
            'options': '-vn'
        }
        ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
        class YTDLSource(discord.PCMVolumeTransformer):
            def __init__(self, source, *, data, volume=0.5):
                super().__init__(source, volume)

                self.data = data

                self.title = data.get('title')
                self.url = data.get('url')

                # Maybe i can make a fancy embed out of this?
                self.uploader = data.get('uploader')
                self.uploader_url = data.get('uploader_url')
                date = data.get('upload_date')
                self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
                self.title = data.get('title')
                self.thumbnail = data.get('thumbnail')
                self.description = data.get('description')
                # self.duration = self.parse_duration(int(data.get('duration')))
                self.tags = data.get('tags')
                self.url = data.get('webpage_url')
                self.views = data.get('view_count')
                self.likes = data.get('like_count')
                self.dislikes = data.get('dislike_count')
                self.stream_url = data.get('url')

            @classmethod
            async def from_url(cls, url, *, loop=None, stream=False):
                loop = loop or asyncio.get_event_loop()
                data = await loop.run_in_executor(
                        None,
                        lambda: ytdl.extract_info(url, download=not stream))

                if 'entries' in data:
                    # take first item from a playlist
                    data = data['entries'][0]

                filename = data['url'] if stream else ytdl.prepare_filename(data)
                return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            voice.play(
                    player,
                    after=lambda e: print('Player error: %s' % e) if e else None)

            player_embed = discord.Embed(colour=discord.Colour.blue())
            player_embed.set_thumbnail(url=player.thumbnail)

            player_embed.add_field(name="Song", value=player.title)
            player_embed.add_field(name="Uploader", value=player.uploader)

        await ctx.send(":musical_note: Now playing: ")
        await ctx.send(embed=player_embed)

    # End of YouTube Player


# COG ENDING
def setup(bot):
    bot.add_cog(Voice(bot))
