from Imports import *


async def Respond(Target, Payload, Send=False, Embed=False):
    async with Target.typing():
        await asyncio.sleep(round(len(Payload) * 0.01))
    if Send:
        if Embed:
            return await Target.send(embed=Payload)
        return await Target.send(Payload)
    elif Send == False:
        if Embed:
            return await Target.reply(embed=Payload)
        return await Target.reply(Payload)


async def Role(ctx, Check=["Admin", "Developer"]):
    Roles = [Role.name for Role in ctx.author.roles]
    RolesInt = len(set(Roles).intersection(Check))
    if RolesInt < 1:
        await ctx.message.add_reaction("\u274C")  # Wrong
        Payload = f"Unauthorized Access Denied."
        Current = await Respond(ctx, Payload)
        await asyncio.sleep(3)
        await Current.delete()
        await ctx.message.delete()
        return None
    else:
        return True


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
                Payload = f"Message.youtube(): {type(e).__name__}"
                await message.author.send(Payload)

        elif "twitter.com" in message.content.lower():
            try:
                File = Download().Twitter(message.content)
                await message.author.send(file=discord.File(File))
                time.sleep(1)
                os.remove(File)
            except Exception as e:
                Payload = f"Message.twitter(): {type(e).__name__}"
                await message.author.send(Payload)

        elif "reddit.com" in message.content.lower():
            try:
                Payload = Download().RedGifs(Download().Reddit(message.content.lower()))
            except Exception as e:
                Payload = f"Message.reddit(): {type(e).__name__}"
            finally:
                await message.author.send(Payload)

        elif (
            "redgifs.com" in message.content.lower()
            or "gyfcat.com" in message.content.lower()
        ):
            try:
                Payload = Download().RedGifs(message.content.lower())
            except Exception as e:
                Payload = f"Message.redgifs(): {type(e).__name__}"
            finally:
                await message.author.send(Payload)

        elif "incestflix.com/watch" in message.content.lower():
            try:
                Payload = Download().IncestflixWatch(message.content.lower())
            except Exception as e:
                Payload = f"Message.IncestflixWatch(): {type(e).__name__}"
            finally:
                await message.author.send(Payload)

        elif "incestflix.com" in message.content.lower():
            try:
                try:
                    Mess = message.content.lower().split()
                    Num = [int(word) for word in Mess if word.isdigit()][0]
                except IndexError:
                    Num = 5

                Data = Download().IncestFlix(message.content, Num)

                Titles = Data[0]
                Contents = Data[1]
                Images = Data[2]

                for i in range(len(Titles)):
                    Timestamp = datetime.datetime.now()
                    embed = discord.Embed(color=0xFF0000, timestamp=Timestamp)
                    embed.add_field(name=Titles[i], value=Contents[i], inline=False)
                    embed.set_image(url=Images[i])
                    embed.set_footer(text=os.path.basename(__file__))
                    await message.author.send(embed=embed)
                    time.sleep(1)
            except Exception as e:
                Payload = f"Message.Incestflix(): {type(e).__name__}"
                await message.author.send(Payload)


class Dash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.Whitelist = [
            529251441504681994,
        ]

    async def Dash(self, Target, Color, Data):
        Titles = Data[0][::-1]
        Pornstars = Data[1][::-1]
        Links = Data[2][::-1]
        Daftsexs = Data[3][::-1]
        Biqles = Data[4][::-1]
        Images = Data[5][::-1]
        Videos = Data[6][::-1]

        for i in range(len(Titles)):
            Timestamp = datetime.datetime.now()
            Links = f"{Links[i]}\n{Daftsexs[i]}\n{Biqles[i]}"
            Var = [Titles[i], Pornstars[i]]
            embed = discord.Embed(colour=Color, timestamp=Timestamp)
            embed.add_field(name=Var[0], value=Var[1], inline=False)
            embed.add_field(name="Links", value=Links, inline=False)
            embed.set_image(url=Images[i])
            embed.set_footer(text=os.path.basename(__file__))
            await Target.send(embed=embed)
            await Target.send(Videos[i])

    async def Sending(self, ctx, Category, Number):
        Base = Cata[Category]["Base"]
        Color = Cata[Category]["Color"]
        Data = Get(Base, Number)

        if type(Data) != list:
            await ctx.message.add_reaction("\u274C")  # Wrong
            await Respond(ctx, Data)

        else:
            await ctx.message.add_reaction("\u2705")  # Right
            await self.Dash(ctx.author, Color, Data)

    @commands.command()
    async def DB(self, ctx, Function=None, Key=None, Value=None):
        if not await Role(ctx):
            return ctx.message.delete()

        try:
            Functions = ["delete", "pull", "push"]
            HelpMessage = (
                f"```.DB <Function> <Key> <Value=None>\nFunction={str(Functions)}```"
            )

            if Function == None or Key == None:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

            if Function.lower() not in Functions:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

            if Function.lower() == "pull":
                Payload = DB().Pull(Key)
                if Payload == None:
                    await ctx.message.add_reaction("\u274C")  # Wrong
                    Payload = f"No key found as [**{Key}**]"
                    return await Respond(ctx, Payload)
                else:
                    await ctx.message.add_reaction("\u2705")  # Right
                    return await Respond(ctx, Payload)

            elif Function.lower() == "push":
                DB().Push(Key, Value)
                await ctx.message.add_reaction("\u2705")  # Right
                return await Respond(ctx, f"Added: \n{Key}:{Value}")

            elif Function.lower() == "delete":
                DB().Delete(Key)
                await ctx.message.add_reaction("\u2705")  # Right
                return await Respond(ctx, f"Deleted: {Key}")

        except Exception as e:
            Payload = f"Dash.DB(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
            return await Respond(ctx, Payload)

    @commands.command()
    async def post(self, ctx, Category="", Number=""):
        if ctx.author.id not in self.Whitelist:
            return await ctx.message.delete()

        HelpMessage = f"```.post <Category=None> <Number=1>\nCategory = [{', '.join([_ for _ in Cata])}]```"

        try:
            if Number.isdigit():
                Number = int(Number)

            if type(Number) != int:
                Number = 1
            elif Number > 100:
                Number = 100

            if Category.lower() == "all":
                for Var in Cata:
                    await self.Sending(ctx, Var, Number)
            elif Category.lower() in Cata:
                return await self.Sending(ctx, Category.lower(), Number)
            else:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

        except Exception as e:
            await ctx.message.add_reaction("\u274C")  # Wrong
            Payload = f"Dash.post(): {type(e).__name__}"
            return await Respond(ctx, Payload)

    @commands.command()
    async def loop(self, ctx, Function=""):
        if ctx.author.id not in self.Whitelist:
            return await ctx.message.delete()

        HelpMessage = (
            f"```.loop <Function>\nFunction = ['start', 'stop', 'restart', 'status']```"
        )

        try:
            Loop = self.Update

            if Function.lower() == "start":
                if Loop.is_running() == True:
                    await ctx.message.add_reaction("\u274C")  # Wrong
                    return await Respond(ctx, f"Dash.Update(): Already running.")
                else:
                    await ctx.message.add_reaction("\u2705")  # Right
                    return Loop.start()

            elif Function.lower() == "stop":
                if Loop.is_running() == False:
                    await ctx.message.add_reaction("\u274C")  # Wrong
                    return await Respond(ctx, f"Dash.Update(): Already at standby.")
                else:
                    await ctx.message.add_reaction("\u2705")  # Right
                    return Loop.stop()

            elif Function.lower() == "restart":
                await ctx.message.add_reaction("\u2705")  # Right
                return Loop.restart()

            elif Function.lower() == "status":
                await ctx.message.add_reaction("\u2705")  # Right
                return await Respond(
                    ctx, f"Dash.Update(): Loop.is_running = {Loop.is_running()}"
                )

            else:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

        except Exception as e:
            await ctx.message.add_reaction("\u274C")  # Wrong
            Payload = f"Dash.loop(): {type(e).__name__}"
            return await Respond(ctx, Payload)

    @tasks.loop(hours=1, reconnect=False)
    async def Update(self):
        Admin = await self.bot.fetch_user(529251441504681994)
        Logs = self.bot.get_channel(843016447839567912)

        try:
            start = time.time()
            Inspected = await Inspect()
            for i, Status in enumerate(Inspected):
                if Status > 0:
                    Base = TeamSkeetSites[i]
                    Color = Uata[Base]
                    Data = Get(Base, Status)

                    if type(Data) != list:
                        await Respond(Admin, Data, True, False)

                    else:
                        await self.Dash(Admin, Color, Data)

            Payload = f"Dash.Update(): Done in {round(time.time() - start)} seconds."
            await Logs.send(Payload)
            await Respond(Logs, Payload, True, False)

        except Exception as e:
            await Respond(Admin, f"Dash.Update(): {type(e).__name__}", True)


def setup(bot):
    bot.add_cog(Dash(bot))
    bot.add_cog(Message(bot))
