from Imports import *

Host = "https://FridayDiscord.rudra1510.repl.co/"


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
    try:
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
    except AttributeError:
        Whitelist = [529251441504681994, 858998113453080577]
        if ctx.author.id in Whitelist:
            return True
        else:
            await ctx.message.add_reaction("\u274C")  # Wrong
            Payload = f"Unauthorized Access Denied."
            Current = await Respond(ctx, Payload)
            await asyncio.sleep(3)
            await Current.delete()
            await ctx.message.delete()
            return None
    except Exception as e:
        await ctx.message.add_reaction("\u274C")  # Wrong
        Payload = f"Roles(): {type(e).__name__}"
        Current = await Respond(ctx, Payload)
        await asyncio.sleep(3)
        await Current.delete()
        await ctx.message.delete()
        return None


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 796011920141320192:
            BackupChannel = self.bot.get_channel(842390320057942028)
            await BackupChannel.send(f"{message.author}:{message.content}")

        if "youtu" in message.content.lower():
            try:
                File = Download().YouTube(message.content)
                await message.author.send(f"{Host}{File}")
            except Exception as e:
                Payload = f"Message.youtube(): {type(e).__name__}"
                await message.author.send(Payload)

        if message.author.id not in [529251441504681994, 858998113453080577]:
            return

        if "twitter.com" in message.content.lower():
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

        elif "allporncomic.com" in message.content.lower():
            if "pdf" in message.content.lower():
                Data = Download().AllPC(message.content.split()[0], True)
                await message.author.send(f"{Host}{Data}")

            else:
                Data = Download().AllPC(message.content.lower(), False)
                Length = len(Data)
                for _ in Data:
                    await message.channel.send(_)
                Payload = f"**Type ||.purge {Length+1}|| to clear this.**"
                await message.channel.send(Payload)

        elif "hdporncomics.com" in message.content.lower():
            if "pdf" in message.content.lower():
                Data = Download().HDPC(message.content.split()[0], True)
                await message.author.send(f"{Host}{Data}")

            else:
                Data = Download().HDPC(message.content.lower(), False)
                Length = len(Data)
                for _ in Data:
                    await message.channel.send(_)
                await message.channel.send(
                    f"**Type ||.purge {Length+1}|| to clear this.**"
                )


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
            NoArg = ["list", "json"]
            OneArg = ["pull", "delete"]
            TwoArg = ["push"]
            Functions = NoArg + OneArg + TwoArg
            HelpMessage = (
                f"```.DB <Function> <Key> <Value>\n-----\nFunction={str(Functions)}```"
            )

            if Function == None:  # or Key == None:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

            elif Function.lower() not in Functions:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

            elif Function.lower() in Functions:
                if Function.lower() in NoArg:
                    if Function.lower() == "list":
                        String = DB().List()
                        Payload = discord.Embed(
                            title="Database", description=String, color=ctx.author.color
                        )
                        await ctx.message.add_reaction("\u2705")  # Right
                        return await Respond(ctx, Payload, False, True)

                    elif Function.lower() == "json":
                        Payload = f"```JSON\n{DB().Data}```"
                        await ctx.message.add_reaction("\u2705")  # Right
                        return await Respond(ctx, Payload, True, False)

                elif Function.lower() in OneArg:
                    if Key == None:
                        await ctx.message.add_reaction("\u274C")  # Wrong
                        return await Respond(ctx, HelpMessage)
                    else:
                        if Function.lower() == "pull":
                            Payload = DB().Pull(Key)
                            if Payload == None:
                                await ctx.message.add_reaction("\u274C")  # Wrong
                                Payload = f"No key found as [**{Key}**]"
                                return await Respond(ctx, Payload)
                            else:
                                await ctx.message.add_reaction("\u2705")  # Right
                                return await Respond(ctx, Payload)

                        elif Function.lower() == "delete":
                            DB().Delete(Key)
                            await ctx.message.add_reaction("\u2705")  # Right
                            return await Respond(ctx, f"Deleted: {Key}")

                elif Function.lower() in TwoArg:
                    if Key == None or Value == None:
                        await ctx.message.add_reaction("\u274C")  # Wrong
                        return await Respond(ctx, HelpMessage)
                    else:
                        if Function.lower() == "push":
                            DB().Push(Key, Value)
                            await ctx.message.add_reaction("\u2705")  # Right
                            return await Respond(ctx, f"Added: \n{Key}:{Value}")

        except Exception as e:
            Payload = f"Dash.DB(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
            return await Respond(ctx, Payload)

    @commands.command()
    async def data(self, ctx, Function=None, File=None):
        if not await Role(ctx):
            return ctx.message.delete()

        try:
            Functions = ["deletea", "deletef", "list", "link"]
            HelpMessage = f"```.Data <Function> <File=None>\n-----\nFunction ={str(Functions)}\n<File> is only usable for deletef command.```"

            if Function == None:  # or Key == None:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

            elif Function.lower() not in Functions:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

            elif Function.lower() == "deletea":
                await ctx.message.add_reaction("\u2705")  # Right

                RawData = os.listdir("Data")
                DataLength = len(RawData)
                DataString = "\n".join(RawData)
                Payload = f"```Deleted {DataLength} Files from the Data folder. Named as:\n{DataString}\n------```"

                RawData.remove("Empty.txt")
                for File in RawData:
                    os.remove("Data/" + File)

                return await Respond(ctx, Payload, False, False)

            elif Function.lower() == "deletef":
                RawData = os.listdir("Data")
                DataLength = len(RawData)
                DataString = "\n".join(RawData)
                Payload1 = f"```There are {DataLength} Files in the Data folder. Please use any one of this file as an argument for deletef function:\n{DataString}\n------```"

                if File == None:
                    await ctx.message.add_reaction("\u274C")  # Wrong
                    return await Respond(ctx, HelpMessage, False, False)
                elif File not in RawData:
                    await ctx.message.add_reaction("\u274C")  # Wrong
                    return await Respond(ctx, Payload1, False, False)
                elif File in RawData:
                    await ctx.message.add_reaction("\u2705")  # Right
                    Payload2 = f"```Deleted: {File}```"
                    os.remove(File)
                    await Respond(ctx, Payload2, False, False)

            elif Function.lower() == "list":
                await ctx.message.add_reaction("\u2705")  # Right

                RawData = os.listdir("Data")
                DataLength = len(RawData)
                DataString = "\n".join(RawData)
                Payload = f"```There are {DataLength} Files in the Data folder. Named as:\n{DataString}\n------```"

                return await Respond(ctx, Payload, False, False)

            elif Function.lower() == "link":
                await ctx.message.add_reaction("\u2705")  # Right

                RawData = os.listdir("Data")
                DataLength = len(RawData)
                DataString = "\n".join(
                    [Host + File.replace(" ", "%20") for File in RawData]
                )
                Payload = f"There are {DataLength} Files in the Data folder. Here are the links:\n{DataString}\n------"

                return await Respond(ctx, Payload, False, False)

        except Exception as e:
            Payload = f"Dash.Data(): {type(e).__name__}"
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
            Payload = (
                "Dash.Update(): Started.\n[This Message will be edited when completed.]"
            )
            Current = await Respond(Logs, Payload, True, False)
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

            Payload = f"Dash.Update(): **{sum(Inspected)} Updates** in {round(time.time() - start)} seconds."
            await Current.edit(content=Payload)

        except Exception as e:
            await Respond(Admin, f"Dash.Update(): {type(e).__name__}", True)

    @commands.command()
    async def SDDE(self, ctx):
        Data = {
            "330": [
                "SDDE-330 Continuous Morning Sex Life And Cooking, Washing, Sexual Desire For 10 Sons",
                "https://pornimg.xyz/2020/0318/1sdde330pl.jpg",
            ],
            "343": [
                'SDDE-343 Homemaker Service "always Fuck"',
                "https://pornimg.xyz/2020/0402/1sdde343pl.jpg",
            ],
            "352": [
                "SDDE-352 Every Morning, Mom Hisa-dai Continuous Sex With 10 Sons While The Busy Housework (47)",
                "https://pornimg.xyz/2018/1124/1sdde352pl.jpg",
            ],
            "360": [
                "SDDE-360 Oma \u25cb Co Housekeeper Booty",
                "https://pornimg.xyz/2020/0420/1sdde360pl.jpg",
            ],
            "372": [
                'SDDE-372 Sperm Empty Morning Life In The "eldest Daughter, Second Daughter, Third Daughter, Four F-five Woman Lok Woman Mother Sexual Desire Processing My Role Of" Seven Consecutive Sex',
                "https://pornimg.xyz/2020/0429/1sdde372pl.jpg",
            ],
            "389": [
                "SDDE-389 Oma Nice Bottom Crew Pies Hospitality Cowgirl \u25cf Co Commuter Train",
                "https://pornimg.xyz/2021/0124/1sdde389pl.jpg",
            ],
            "416": [
                "SDDE-416 Continuous And Cooking, Washing, Sexual Desire Processing 10 Sons Sex Morning Life Tall Angrily Milk Mom Hen",
                "https://pornimg.xyz/2020/0531/1sdde416pl.jpg",
            ],
            "450": [
                "SDDE-450 Continuous And Cooking, Washing And Sexual Desire Processing 10 Sons SEX Morning Life Unequaled Masegaki Vs Gyarumama Hen AIKA",
                "https://pornimg.xyz/2020/0626/1sdde450pl.jpg",
            ],
            "457": [
                "SDDE-457 Man Who Can Stop Time Was Real!~ Happy That Her Proud Of The Guys \u201cIn O\u2019sleeping\u201d Saddle Defeated!Hen ~",
                "https://pornimg.xyz/2020/0707/1sdde457pl.jpg",
            ],
            "511": [
                "SDDE-511 Cooking \u00b7 Washing \u00b7 Libido Treatment 10 Son And Continuous Creampie Morning Living (38)",
                "https://pornimg.xyz/2017/1013/1sdde511pl.jpg",
            ],
            "526": [
                "SDDE-526 Cooking \u00b7 Washing \u00b7 Libido Processing Son & Relatives 15 Consecutive Sex Morning Life New Year Happy New Year Happy Incest Incest Today Ko (43) Kubo Kyoko",
                "https://pornimg.xyz/2018/0117/1sdde526pl.jpg",
            ],
            "564": [
                "SDDE-564 Cooking \u00b7 Laundry \u00b7 Libido Treatment 9 Sons, Husband And Consecutive Sex Morning Life Naho (38) Nagaho Yamaguchi",
                "https://pornimg.xyz/2018/1227/1sdde564pl.jpg",
            ],
            "582": [
                "SDDE-582 Emergency Lifesaving (immediately Fuck) Sexual Intercourse Center",
                "https://pornimg.xyz/2019/0513/1sdde582pl.jpg",
            ],
            "589": [
                "SDDE-589 Cooking, Laundry, Libido Processing 9 Sons, Husband And Continuous Sex Morning Life Saki Kato (34)",
                "https://pornimg.xyz/2019/0715/1sdde589pl.jpg",
            ],
            "596": [
                "SDDE-596 Hospitality In \u201cUniform, Underwear, Naked\u201d Oma \u25cb Co Airlines 11 Deca Ass Flight",
                "https://pornimg.xyz/2019/1124/1sdde596pl.jpg",
            ],
            "602": [
                "SDDE-602 A Single Woman In A Family Full Of Men Daily Life With 10 Brothers While Doing Busy Chores Everyday Mirei Nitta",
                "https://pornimg.xyz/2020/0108/1sdde602pl.jpg",
            ],
            "605": [
                "SDDE-605 Daddy Mom Do Your Best! With A Slimy Lotion, Your Friend\u2019s Family Will Endure The Championship! Total 9 Cum Shots!",
                "https://pornimg.xyz/2019/1212/1sdde605pl.jpg",
            ],
            "631": [
                "SDDE-631 (Super Popular!) Cooking, Cleaning, Sex These 7 Big Families Will Take Care Of Those Needs And Transcend Time To Gather Here!! Consecutive Sex In The Morning 7 Titles 70 Ejaculations 240-Minute Special!",
                "https://pornimg.xyz/2020/0819/1sdde00631pl.jpg",
            ],
            "636": [
                "SDDE-636 Cooking / Washing / Sexual Desire Processing 10 Continuous Sex With My Son Morning Life Maiko Ayase (48)",
                "https://pornimg.xyz/2021/0205/1sdde636pl.jpg",
            ],
            "638": [
                "SDDE-638 Tobizio! EVENING NEWS Female Ana Who Reads The Manuscript Calmly Even If She Keeps Squirting And Incontinence During The Production",
                "https://pornimg.xyz/2021/0312/1sdde638pl.jpg",
            ],
            "643": [
                "SDDE-643 In-Flight Sexual Services: Uniform, Lingerie, Or Totally Nude 13 \u2013 Pussy Spread Wide For Cowgirl \u2013 Black Pantyhose Version",
                "https://pornimg.xyz/2021/0203/1sdde00643pl.jpg",
            ],
        }

        for _ in Data:
            Title, Image = Data[_][0], Data[_][1]
            Payload = discord.Embed(
                title=f"SDDE {_}", description=Title, color=ctx.author.color
            ).set_image(url=Image)
            await Respond(ctx, Payload, True, True)


def setup(bot):
    bot.add_cog(Dash(bot))
    bot.add_cog(Message(bot))
