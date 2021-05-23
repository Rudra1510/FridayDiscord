import os
from discord.ext import commands
from WebServer import StayAwake

SpaceBot = commands.Bot(command_prefix=".")

for File in os.listdir("./Bot/Extension"):
    if File.endswith(".py"):
        SpaceBot.load_extension(f"Extension.{File[:-3]}")

StayAwake()
SpaceBot.run(os.environ["Discord_Bot_Token"])
