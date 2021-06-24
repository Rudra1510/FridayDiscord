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


class System(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        Game = discord.Game(name=".help")
        Target = self.Bot.get_channel(843016447839567912)
        await self.Bot.change_presence(activity=Game)
        await Respond(Target, "Booting Up.", True)
        # Dash(self.Bot).Update.start()

    @commands.command(aliases=["ext"])
    async def extension(self, ctx, Function="", Extension=""):
        if not await Role(ctx):
            return ctx.message.delete()

        try:
            FileList = [filename[:-3] for filename in os.listdir("./Bot/Extension")]
            HelpMessage = (
                "```.ext <Function> <Extension>"
                + "\nFunction = [load, unload, reload, list]"
                + "\nExtension = "
                + f"[{', '.join(FileList)}]```"
            )

            Function = Function.strip().lower()

            if Function == "list":
                await ctx.message.add_reaction("\u2705")  # Right
                return await Respond(ctx, f"Extension = [{', '.join(FileList)}]", True)

            if Extension == "":
                pass

            elif Extension not in FileList:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage, True)

            if Function == "load":
                self.Bot.load_extension(f"Extension.{Extension}")
                return await ctx.message.add_reaction("\u2705")  # Right

            elif Function == "unload":
                self.Bot.unload_extension(f"Extension.{Extension}")
                return await ctx.message.add_reaction("\u2705")  # Right

            elif Function == "reload":
                self.Bot.reload_extension(f"Extension.{Extension}")
                return await ctx.message.add_reaction("\u2705")  # Right

            elif Function == "list":
                pass

            else:
                await ctx.message.add_reaction("\u274C")  # Wrong
                return await Respond(ctx, HelpMessage)

        except Exception as e:
            await ctx.message.add_reaction("\u274C")  # Wrong
            Payload = f"System.extnesion(): {type(e).__name__}"
            return await Respond(ctx, Payload)


class Management(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command(aliases=["delete", "purge"])
    async def clear(self, ctx, Value=5):
        if not await Role(ctx):
            return ctx.message.delete()

        try:
            await ctx.message.add_reaction("\u2705")  # Right
            await asyncio.sleep(1)
            return await ctx.channel.purge(limit=Value + 1)
        except Exception as e:
            Payload = f"Management.clear(): {type(e).__name__}"
            await ctx.message.add_reaction("\u274C")  # Wrong
            return await Respond(ctx, Payload)

    @commands.command(aliases=["say", "tell"])
    async def send(self, ctx, Variable, *, Text=""):
        if not await Role(ctx):
            return ctx.message.delete()

        try:
            if "<@!" in Variable:
                Target = await self.Bot.fetch_user(
                    int(re.match(r"<@!(.*)>", Variable).group(1))
                )
            else:
                Target = await self.Bot.fetch_user(Variable)

            await ctx.message.add_reaction("\u2705")  # Right
            return await Respond(Target, Text, True)

        except Exception as e:
            try:
                if "<#" in Variable:
                    Target = self.Bot.get_channel(
                        int(re.match(r"<#(.*)>", Variable).group(1))
                    )
                else:
                    Target = self.Bot.get_channel(Variable)

                await ctx.message.add_reaction("\u2705")  # Right
                return await Respond(Target, Text, True)

            except Exception as e:
                try:
                    Target = ctx
                    if Variable.isdigit():
                        if int(Variable) > 100:
                            Variable = 100
                        await ctx.message.add_reaction("\u2705")  # Right
                        for i in range(int(Variable)):
                            await Respond(Target, Text, True)
                    else:
                        Payload = Variable + " " + Text
                        await ctx.message.add_reaction("\u2705")  # Right
                        return await Respond(Target, Payload, True)

                except Exception as e:
                    Payload = f"Management.send(): {type(e).__name__}"
                    await ctx.message.add_reaction("\u274C")  # Wrong
                    await Respond(ctx, Payload)


def setup(Bot):
    Bot.add_cog(System(Bot))
    Bot.add_cog(Management(Bot))
