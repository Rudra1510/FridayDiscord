import os
from Extension.Dash import Dash
from discord.ext import commands


class System(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot
        self.Whitelist = [
            529251441504681994,
        ]

    @commands.Cog.listener()
    async def on_ready(self):
        await self.Bot.get_channel(843016447839567912).send(f"^-^")
        Dash(self.Bot).Update.start()

    @commands.command()
    async def send(self, ctx, Value, *, Text=""):

        if Value.isdigit():
            if int(Value) > 100:
                Value = 100
            for i in range(int(Value)):
                await ctx.channel.send(Text)
        else:
            await ctx.channel.send(Value + " " + Text)

    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send(f"Pong {self.Bot.latency} :ping_pong:")

    @commands.command()
    async def clear(self, ctx, Value=5):
        await ctx.channel.purge(limit=Value)

    @commands.command()
    async def ext(self, ctx, Function="", Extension=""):
        if ctx.author.id not in self.Whitelist:
            return

        HelpMessage = f".ext <Function> <Extension>\nFunction = [load, unload, reload, list]\nExtension = [{', '.join([filename[:-3] for filename in os.listdir('./baby/Extension')])}]"

        try:
            if Function.strip().lower() == "list":
                await ctx.channel.send(
                    f"Extension = [{', '.join([filename[:-3] for filename in os.listdir('./baby/Extension')])}]"
                )

            if Extension not in [
                filename[:-3] for filename in os.listdir("./baby/Extension")
            ]:
                await ctx.channel.send(HelpMessage)

            if Function.strip().lower() == "load":
                self.Bot.load_extension(f"Extension.{Extension}")
                await ctx.channel.send(f"Extension: {Extension} | Function: Loaded")

            elif Function.strip().lower() == "unload":
                self.Bot.unload_extension(f"Extension.{Extension}")
                await ctx.channel.send(f"Extension: {Extension} | Function: Unloaded")

            elif Function.strip().lower() == "reload":
                self.Bot.reload_extension(f"Extension.{Extension}")
                await ctx.channel.send(f"Extension: {Extension} | Function: Reloaded")

            elif Function.strip().lower() == "list":
                pass

            else:
                await ctx.channel.send(HelpMessage)

        except Exception as e:
            await self.Bot.get_channel(843016447839567912).send(
                f"Code: System.ext() | Error: {type(e).__name__}"
            )


def setup(Bot):
    Bot.add_cog(System(Bot))
