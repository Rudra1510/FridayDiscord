import os
import time
import datetime

import discord
from discord.ext import commands
from discord.ext import tasks

from Functions.Internet import *


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 796011920141320192:
            BackupChannel = self.bot.get_channel(842390320057942028)
            await BackupChannel.send(f"{message.author}:{message.content}")

        if message.author.id != 529251441504681994:
            return

        if "youtu" in message.content.lower():
            try:
                File = Download().YouTube(message.content)
                await message.author.send(file=discord.File(File))
                time.sleep(1)
                os.remove(File)
            except Exception as e:
                await message.author.send(f'Code: Message.youtube() | Error: {type(e).__name__}')

        elif "reddit.com" in message.content.lower():
            try:
                await message.author.send(Download().RedGifs(Download().Reddit(message.content.lower())))
            except Exception as e:
                await message.author.send(f'Code: Message.reddit() | Error: {type(e).__name__}')

        elif "twitter.com" in message.content.lower():
            try:
                File = Download().Twitter(message.content)
                await message.author.send(file=discord.File(File))
                time.sleep(1)
                os.remove(File)
            except Exception as e:
                await message.author.send(f'Code: Message.twitter() | Error: {type(e).__name__}')

        elif "incestflix.com/watch" in message.content.lower():
            try:
                await message.author.send(Download().IncestflixWatch(message.content.lower()))
            except Exception as e:
                await message.author.send(f'Code: Message.IncestflixWatch() | Error: {type(e).__name__}')

        elif "incestflix.com" in message.content.lower():
            try:
                try:
                    Num = [int(word) for word in message.content.lower(
                    ).split() if word.isdigit()][0]
                except IndexError:
                    Num = 5

                Data = Download().IncestFlix(message.content, Num)

                Titles = Data[0]
                Contents = Data[1]
                Images = Data[2]

                for i in range(len(Titles)):
                    embed = discord.Embed(
                        color=0xff0000, timestamp=datetime.datetime.now())
                    embed.add_field(
                        name=Titles[i], value=Contents[i], inline=False)
                    embed.set_image(url=Images[i])
                    embed.set_footer(text=os.path.basename(__file__))
                    await message.author.send(embed=embed)
                    time.sleep(1)
            except Exception as e:
                await message.author.send(f'Code: Message.Incestflix() | Error: {type(e).__name__}')


def setup(bot):
    bot.add_cog(Message(bot))
