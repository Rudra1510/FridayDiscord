from Imports import *


nest_asyncio.apply()

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


class Fun(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    def GetGiphy(self, Query, Rating):
        ApiKey = os.environ["GiphyToken"]
        ApiInstance = giphy_client.DefaultApi()

        try:
            ApiResponse = ApiInstance.gifs_search_get(
                ApiKey, q=Query, limit=25, rating=Rating
            )
            Image = random.choice(list(ApiResponse.data))
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
            Image = None
        finally:
            return Image

    async def Fun(self, ctx, User, Base):
        try:
            if not User:
                User = ctx.author

            if Base == "kiss" or Base == "punch":
                End = "es"
            else:
                End = "s"

            Query = random.choice([Base, f"{Base}{End}"])
            if ctx.channel.is_nsfw():
                Image = self.GetGiphy(Query, "r")
            else:
                Image = self.GetGiphy(Query, "pg-13")

            Payload = discord.Embed(
                title=f"**{ctx.author} {Base}{End} {User}.**", color=ctx.author.color
            )
            Payload.set_image(url=f"https://media.giphy.com/media/{Image.id}/giphy.gif")

            await ctx.message.add_reaction("\u2705")  # Right

        except Exception as e:
            Payload = discord.Embed(
                title="Fun.Fun()",
                description=type(e).__name__,
                color=ctx.author.color,
            )
            await ctx.message.add_reaction("\u274C")  # Wrong

        finally:
            SentMessage = await Respond(ctx, Payload, False, True)
            await SentMessage.add_reaction("\U0001F923")  # LOL

    @commands.command()
    async def slap(self, ctx, *, User: discord.Member = None):
        await self.Fun(ctx, User, "slap")

    @commands.command()
    async def kick(self, ctx, *, User: discord.Member = None):
        await self.Fun(ctx, User, "kick")

    @commands.command()
    async def hug(self, ctx, *, User: discord.Member = None):
        await self.Fun(ctx, User, "hug")

    @commands.command()
    async def punch(self, ctx, *, User: discord.Member = None):
        await self.Fun(ctx, User, "punch")

    @commands.command()
    async def kiss(self, ctx, *, User: discord.Member = None):
        await self.Fun(ctx, User, "kiss")

    @commands.command()
    async def gif(self, ctx, *, Query):
        try:
            if ctx.channel.is_nsfw():
                Image = self.GetGiphy(Query, "r")
            else:
                Image = self.GetGiphy(Query, "pg-13")

            Payload = discord.Embed().set_image(
                url=f"https://media.giphy.com/media/{Image.id}/giphy.gif"
            )

            await ctx.message.add_reaction("\u2705")  # Right

        except Exception as e:
            Payload = discord.Embed(
                title="Fun.gif()",
                description=type(e).__name__,
                color=ctx.author.color,
            )
            await ctx.message.add_reaction("\u274C")  # Wrong

        finally:
            await Respond(ctx, Payload, False, True)


class Random(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def number(self, ctx, start: int = 1, stop: int = 10):
        try:
            Payload = random.randint(start, stop)
            await ctx.message.add_reaction("\u2705")  # Right
        except Exception as e:
            Payload = f"Random.number(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
        finally:
            await Respond(ctx, Payload)

    @commands.command()
    async def dice(self, ctx, NumberOfDice: int = 1):
        try:
            Payload = ", ".join(
                [str(random.randint(1, 6)) for i in range(NumberOfDice)]
            )
            await ctx.message.add_reaction("\u2705")  # Right
        except Exception as e:
            Payload = f"Random.dice(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
        finally:
            await Respond(ctx, Payload)

    @commands.command()
    async def letter(self, ctx):
        try:
            Payload = random.choice([Letter for Letter in "abcdefghijklmnopqrstuvwxyz"])
            await ctx.message.add_reaction("\u2705")  # Right
        except Exception as e:
            Payload = f"Random.letter(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
        finally:
            await Respond(ctx, Payload)

    @commands.command()
    async def quote(self, ctx):
        try:
            r = requests.get("https://api.quotable.io/random")
            Payload = r.json()["content"] + "\n    **-" + r.json()["author"] + "**"
            await ctx.message.add_reaction("\u2705")  # Right
        except Exception as e:
            Payload = f"Random.quote(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
        finally:
            await Respond(ctx, Payload)


class Utility(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    async def ping(self, ctx):
        try:
            Payload = f"Pong {round(self.Bot.latency,2)}"
            await ctx.message.add_reaction("\U0001F3D3")  # PingPong
        except Exception as e:
            Payload = f"Utility.ping(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
        finally:
            await Respond(ctx, Payload)

    @commands.command()
    async def cover(self, ctx, Iteration=1):
        Payload = ("```" + " " * 10 + "\n " * 100 + "\n```" )* Iteration
        return await Respond(ctx, Payload, True, False)

    @commands.command()
    async def test(self, ctx):
        Emojis = [
            "\U0001F44C",  # Ok Hand
            "\u274C",  # Wrong
            "\u2705",  # Right
        ]
        return await ctx.message.add_reaction("\U0001F44C")  # Okay Hand Sign

    @commands.command()
    async def shorten(self, ctx, Link=None):
        try:
            Payload = Other().Shorten(Link)
            await ctx.message.add_reaction("\u2705")  # Right
            await ctx.message.delete()
        except Exception as e:
            Payload = f"Utility.shorten(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
        finally:
            await Respond(ctx, Payload, True)

    @commands.command()
    async def search(self, ctx, Number="", *, Query=""):
        try:
            if Number.isdigit():
                Number = int(Number)
            else:
                Query = Number + " " + Query
                Number = 3

            await ctx.message.add_reaction("\u2705")  # Right

            Results = "\n".join([result for result in search(Query, stop=Number)])
            Payload = discord.Embed(
                title="\U0001F50D " + Query, description=Results, color=ctx.author.color
            ).set_thumbnail(url=str(ctx.guild.icon_url))

        except Exception as e:
            Payload = discord.Embed(
                title="Utility.search()",
                description=type(e).__name__,
                color=ctx.author.color,
            )
            await ctx.message.add_reaction("\u274C")  # Wrong

        finally:
            await Respond(ctx, Payload, False, True)

    @commands.command()
    async def yttrim(self, ctx, URL=None, Start=None, Stop=None):
        HelpMessage = "```.yttrim <URL> <Start> <Stop>\nTime is only vaild in seconds as of now.```"
        IncorrectArgs = "**Incorrect Arguments.**\n```.yttrim <URL> <Start> <Stop>\nTime is only vaild in seconds as of now.```"

        if URL == None or Start == None or Stop == None:
            return await Respond(ctx, HelpMessage, False, False)

        if "https://" not in URL or "youtu" not in URL:
            return await Respond(ctx, HelpMessage, False, False)

        StartRE = re.search(r"(\d\d):(\d\d)", Start)
        StopRE = re.search(r"(\d\d):(\d\d)", Stop)
        if StartRE != None or StopRE != None:
            Start = StartRE[1] * 60 + StartRE[2]
            Stop = StopRE[1] * 60 + StopRE[2]

        VideoPref = {
            "outtmpl": "Data/%(title)s.%(ext)s",
        }

        with youtube_dl.YoutubeDL(VideoPref) as Cursor:
            InfoDict = Cursor.extract_info(URL, download=False)
            Duration = InfoDict["duration"]
            Title = (
                InfoDict["title"].replace('"', "").replace("'", "").replace("|", "-")
            )
            FileName = f"{Title}.{InfoDict['ext']}"
            VideoPref["outtmpl"] = "Data/" + FileName

        try:
            if type(int(Start)) != int or type(int(Stop)) != int:
                return await Respond(ctx, IncorrectArgs, False, False)
        except ValueError:
            return await Respond(ctx, IncorrectArgs, False, False)

        Start, Stop = int(Start), int(Stop)

        if Start > Stop:
            return await (ctx, IncorrectArgs + "\n**Start>Stop**")

        elif Start > Duration or Stop > Duration:
            return await (ctx, IncorrectArgs + "\n**Start or Stop > Duration**")

        # If everything is perfect
        FileName = Download().YouTube(URL + " vid").replace("%20", " ")
        TrimFileName = "Trim - " + FileName
        TrimFile = "Data/Trim - " + FileName
        File = "Data/" + FileName
        with VideoFileClip(filename=File) as Clip:
            Clip = Clip.subclip(Start, Stop)
            Clip.write_videofile(TrimFile)
        os.remove(File)

        Payload = Host + TrimFileName.replace(" ", "%20")
        return await Respond(ctx, Payload, False, False)


class Information(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(aliases=["si"])
    async def serverinfo(self, ctx):
        try:
            Server = str(ctx.guild.name)
            Description = "It's space to hang-out with friends."
            Owner = "<@529251441504681994>"
            MemberCount = str(ctx.guild.member_count)
            ChannelCount = len(ctx.guild.channels)
            Icon = str(ctx.guild.icon_url)

            Payload = discord.Embed(
                title=Server, description=Description, color=ctx.author.color
            )
            Payload.set_thumbnail(url=Icon)
            Payload.add_field(name="Owner", value=Owner, inline=True)
            Payload.add_field(name="Member Count", value=MemberCount, inline=True)
            Payload.add_field(name="Channel Count", value=ChannelCount, inline=True)
            Payload.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

            await ctx.message.add_reaction("\u2705")  # Right

        except Exception as e:
            Payload = discord.Embed(
                title="Information.serverinfo()",
                description=type(e).__name__,
                color=ctx.author.color,
            )
            await ctx.message.add_reaction("\u274C")  # Wrong

        finally:
            await Respond(ctx, Payload, False, True)

    @commands.command(aliases=["ui"])
    async def userinfo(self, ctx, *, User: discord.Member = None):
        try:
            if User is None:
                User = ctx.author

            Title = User.display_name
            Color = User.color
            Icon = User.avatar_url
            Joined = User.joined_at.strftime("%d %b, %Y")
            Reg = User.created_at.strftime("%d %b, %Y")

            Payload = discord.Embed(title=Title, color=Color)
            Payload.set_thumbnail(url=Icon)
            Payload.add_field(name="Joined", value=Joined, inline=True)
            Payload.add_field(name="Registered", value=Reg, inline=True)
            if len(User.roles) > 1:
                RoleString = " ".join([Role.mention for Role in User.roles][1:])
                Roles = f"Roles [{len(User.roles) - 1}]"
                Payload.add_field(
                    name=Roles,
                    value=RoleString,
                    inline=True,
                )

            await ctx.message.add_reaction("\u2705")  # Right

        except Exception as e:
            Payload = discord.Embed(
                title="Information.userinfo()",
                description=type(e).__name__,
                color=ctx.author.color,
            )
            await ctx.message.add_reaction("\u274C")  # Wrong

        finally:
            await Respond(ctx, Payload, False, True)

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, *, User: discord.Member = None):
        try:
            if User is None:
                User = ctx.author
            Payload = discord.Embed(title=User.display_name, color=User.color)
            Payload.set_image(url=User.avatar_url)
            await ctx.message.add_reaction("\u2705")  # Right
        except Exception as e:
            Payload = discord.Embed(
                title="Information.avatar()",
                description=type(e).__name__,
                color=ctx.author.color,
            )
            await ctx.message.add_reaction("\u274C")  # Wrong
        finally:
            await Respond(ctx, Payload, False, True)


def setup(Bot):
    Bot.add_cog(Fun(Bot))
    Bot.add_cog(Random(Bot))
    Bot.add_cog(Utility(Bot))
    Bot.add_cog(Information(Bot))
