import os
from discord.ext import commands
from WebServer import StayAwake

SpaceBot = commands.Bot(command_prefix=".", description="I'm Friday.")

for File in os.listdir("./Bot/Extension"):
    if File.endswith(".py"):
        SpaceBot.load_extension(f"Extension.{File[:-3]}")

StayAwake()

try:
    Token = os.environ["Discord_Bot_Token"]
except KeyError:
    string1 = "Nzk2MDExOTIwMTQxMzIwMTky.X_Rt3g"
    string2 = ".lQnH7kgG4UHXT_0BNjjldEzu-Wk"
    Token = string1 + string2

SpaceBot.run(Token)

# Important Message
"""
The replitdb package uses async/await, which cannot run inside a discord async event.loop
so I've edited the replitdb package files:
    replitdb / __init__.py
        removed asycio.run() from view() and set_dict()
"""
