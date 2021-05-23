import os
import time
import datetime

import discord
from discord.ext import commands
from discord.ext import tasks

from Functions.Internet import *


class Dash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Whitelist = [
            529251441504681994,
        ]

    @commands.command()
    async def short(self, ctx, Link=None):
        HelpMessage = f".short <Link>"
        try:
            if "Direct Message" in str(ctx.channel):
                Reciever = ctx.author
            else:
                Reciever = ctx.channel

            if not Link:
                await Reciever.send(HelpMessage)
            else:
                await Reciever.send(Other().Shorten(Link))

        except Exception as e:
            await self.bot.get_channel(843016447839567912).send(
                f"Code: Dash.short() | Error: {type(e).__name__}"
            )

    @commands.command()
    async def post(self, ctx, Category="", Number=""):
        if ctx.author.id not in self.Whitelist:
            return

        HelpMessage = f".post <Category=None> <Number=1>\nCategory = [{', '.join([_ for _ in Cata])}]"

        try:
            if Number.isdigit():
                Number = int(Number)

            if type(Number) != int:
                Number = 1
            elif Number > 100:
                Number = 100

            if Category.lower() == "all":
                for Var in Cata:
                    Base = Cata[Var]["Base"]
                    Color = Cata[Var]["Color"]
                    Data = Get(Base, Number)

                    if type(Data) != list:
                        await ctx.author.send(Data)

                    else:
                        Titles = Data[0][::-1]
                        Pornstars = Data[1][::-1]
                        Links = Data[2][::-1]
                        Daftsexs = Data[3][::-1]
                        Biqles = Data[4][::-1]
                        Images = Data[5][::-1]
                        Videos = Data[6][::-1]

                        for i in range(len(Titles)):
                            embed = discord.Embed(
                                colour=Color, timestamp=datetime.datetime.now()
                            )
                            embed.add_field(
                                name=Titles[i], value=Pornstars[i], inline=False
                            )
                            embed.add_field(
                                name="Links",
                                value=f"{Links[i]}\n{Daftsexs[i]}\n{Biqles[i]}",
                                inline=False,
                            )
                            embed.set_image(url=Images[i])
                            embed.set_footer(text=os.path.basename(__file__))
                            await ctx.author.send(embed=embed)
                            await ctx.author.send(Videos[i])

            elif Category.lower() in Cata:
                Base = Cata[Category.lower()]["Base"]
                Color = Cata[Category.lower()]["Color"]
                Data = Get(Base, Number)

                if type(Data) != list:
                    await ctx.author.send(Data)

                else:
                    Titles = Data[0][::-1]
                    Pornstars = Data[1][::-1]
                    Links = Data[2][::-1]
                    Daftsexs = Data[3][::-1]
                    Biqles = Data[4][::-1]
                    Images = Data[5][::-1]
                    Videos = Data[6][::-1]

                    for i in range(len(Titles)):
                        embed_var = discord.Embed(
                            colour=Color, timestamp=datetime.datetime.now()
                        )
                        embed_var.add_field(
                            name=Titles[i], value=Pornstars[i], inline=False
                        )
                        embed_var.add_field(
                            name="Links",
                            value=f"{Links[i]}\n{Daftsexs[i]}\n{Biqles[i]}",
                            inline=False,
                        )
                        embed_var.set_image(url=Images[i])
                        embed_var.set_footer(text=os.path.basename(__file__))
                        await ctx.author.send(embed=embed_var)
                        await ctx.author.send(Videos[i])

            else:
                await ctx.author.send(HelpMessage)

        except Exception as e:
            await self.bot.get_channel(843016447839567912).send(
                f"Code: Dash.post() | Error: {type(e).__name__}"
            )
            await ctx.author.send(f"Code: Dash.post() | Error: {type(e).__name__}")

    @commands.command()
    async def loop(self, ctx, Function=""):
        if ctx.author.id not in self.Whitelist:
            return

        HelpMessage = (
            f".loop <Function>\nFunction = ['start', 'stop', 'restart', 'status']"
        )

        try:
            Loop = self.Update

            if Function.lower() == "start":
                if Loop.is_running() == True:
                    await ctx.author.send(f"Dash.Update() is already running.")
                else:
                    await ctx.author.send(f"Sure, starting Dash.Update().")
                    Loop.start()

            elif Function.lower() == "stop":
                if Loop.is_running() == False:
                    await ctx.author.send(f"Dash.Update() is already at standby.")
                else:
                    await ctx.author.send(f"Sure, deactivating Dash.Update().")
                    Loop.stop()

            elif Function.lower() == "restart":
                await ctx.author.send("As you wish.")
                Loop.restart()

            elif Function.lower() == "status":
                await ctx.author.send(f"Loop Running Status is {Loop.is_running()}")

            else:
                await ctx.author.send(HelpMessage)

        except Exception as e:
            await self.bot.get_channel(843016447839567912).send(
                f"Code: Dash.loop() | Error: {type(e).__name__}"
            )
            await ctx.author.send(f"Code: Dash.loop() | Error: {type(e).__name__}")

    @tasks.loop(hours=1, reconnect=False)
    async def Update(self):
        Admin = await self.bot.fetch_user(529251441504681994)

        try:
            await self.bot.get_channel(843016447839567912).send(
                f"Dash.Update(): Started!"
            )
            Inspected = Inspect()
            for i, Status in enumerate(Inspected):
                if Status > 0:
                    Base = TeamSkeetSites[i]
                    Color = Uata[Base]
                    Data = Get(Base, Status)

                    if type(Data) != list:
                        await Admin.send(Data)

                    else:
                        Titles = Data[0][::-1]
                        Pornstars = Data[1][::-1]
                        Links = Data[2][::-1]
                        Daftsexs = Data[3][::-1]
                        Biqles = Data[4][::-1]
                        Images = Data[5][::-1]
                        Videos = Data[6][::-1]

                        for i in range(len(Titles)):
                            embed = discord.Embed(
                                colour=Color, timestamp=datetime.datetime.now()
                            )
                            embed.add_field(
                                name=Titles[i], value=Pornstars[i], inline=False
                            )
                            embed.add_field(
                                name="Links",
                                value=f"{Links[i]}\n{Daftsexs[i]}\n{Biqles[i]}",
                                inline=False,
                            )
                            embed.set_image(url=Images[i])
                            embed.set_footer(text=os.path.basename(__file__))
                            await Admin.send(embed=embed)
                            await Admin.send(Videos[i])
                            time.sleep(1)

            await self.bot.get_channel(843016447839567912).send(
                f"Dash.Update(): Stopped!"
            )

        except Exception as e:
            await self.bot.get_channel(843016447839567912).send(
                f"Code: Dash.Update() | Error: {type(e).__name__}"
            )
            await Admin.send(f"Code: Dash.Update() | Error: {type(e).__name__}")


def setup(bot):
    bot.add_cog(Dash(bot))
