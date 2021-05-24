"""
Play some audio clips
"""

from asyncio import Lock
from discord import FFmpegPCMAudio
from discord import VoiceClient, VoiceChannel
from discord.ext import commands
import asyncio
import discord
import youtube_dl


class Player:
    lock = Lock()

    async def __aenter__(self):
        await self.__class__.lock.acquire()
        return self


    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.__class__.lock.release()


    @staticmethod
    async def connect(bot, voice_channel):
        """
        Let's the bot join a VC
        """
        assert isinstance(voice_channel, VoiceChannel)
        if bot.voice_clients:
            vc: VoiceClient = bot.voice_clients[0]
            if vc.channel.id != voice_channel.id:
                await vc.move_to(voice_channel)
        else:
            await voice_channel.connect()
        vc: VoiceClient = bot.voice_clients[0]
        assert isinstance(vc, VoiceClient)
        await asyncio.sleep(0.3)
        return vc


    @staticmethod
    async def disconnect(vc):
        await vc.disconnect()


    @staticmethod
    async def play(vc, audio_source):
        vc.play(audio_source)
        while vc.is_playing():
            await asyncio.sleep(0.1)


class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    def parse(self, query):
        """
        Parse a request into an uri
        """
        # TODO: maybe put this into a db?
        clips = {"schokobons": "https://www.youtube.com/watch?v=qX7V3EVr1BA",
                 "raus": "https://youtu.be/_e1cWuQ8WQw"}
        try:
            return clips[query]
        except KeyError:
            return None


    @commands.command(name="dc")
    async def disconnect(self, ctx):
        """
        Disconnect from audio
        """
        await Player.disconnect(self.bot.voice_clients[0])


    @commands.command(name="play")
    async def play(self, ctx, query):
        """
        Play an audio clip
        - schokobons
        - raus
        """

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        await ctx.trigger_typing()
        uri = self.parse(query)
        if uri:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                song_info = ydl.extract_info(uri, download=False)
                audio_stream = song_info["formats"][0]["url"]

            audio_source = FFmpegPCMAudio(audio_stream)
            async with Player() as player:
                vc = await player.connect(self.bot, ctx.author.voice.channel)
                await player.play(vc, audio_source)
            await ctx.send(f"Playing: {uri}")
        else:
            await ctx.send(f"Clip '{query}' not found")


def setup(bot):
    bot.add_cog(Audio(bot))
