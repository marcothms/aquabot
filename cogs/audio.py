"""
Play some audio samples
"""

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from asyncio import Lock


class Player:
    lock = Lock()

    async def __aenter__(self):
        await self.__class__.lock.acquire()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.__class__.lock.release()

    @staticmethod
    async def play(vc, audio_source):
        vc.play(audio_source)
        while vc.is_playing():
            await asyncio.sleep(0.1)
        await vc.disconnect()


class Audio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def connect(bot: Bot, voice_channel: VoiceChannel) -> VoiceClient:
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

    def parse(query):
        memes = {"schokobons": "https://www.youtube.com/watch?v=qX7V3EVr1BA"}
        try:
            return memes[query]
        except KeyError as e:
            return None

    @commands.command(name="play")
    async def play(self, ctx, query):

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        uri = parse(query)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            song_info = ydl.extract_info(uri, download=False)
            audio_stream = song_info["formats"][0]["url"]

        audio_source = FFmpegPCMAudio(audio_stream)
        async with self.lock as player:
            vc = await connect(self.bot, member.voice.channel)
            await player.play(vc, audio_source)


def setup(bot):
    bot.add_cog(Audio(bot))
