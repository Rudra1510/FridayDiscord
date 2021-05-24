# import os
# print(os.getenv("REPLIT_DB_URL"))
import replitdb


class DB:
    def __init__(self):
        self.client = replitdb.Client()

    def Pull(self, Key):
        return self.client.view(Key)

    def Push(self, Key, Value):
        self.client.set_dict({Key: Value})


print(replitdb.Client().all)

TeamSkeetSites = [
    "AnalMom",
    "BBCParadise",
    "BadMilfs",
    "DadCrush",
    "DaughterSwap",
    "FamilyStrokes",
    "FreeUseFantasy",
    "MYLFDOM",
    "PervMom",
    "PervNana",
    "ShoplyfterMYLF",
    "SisLovesMe",
    "TeamSkeetTube",
]
Values = [
    "Peeper Gives Me Good Anal",
    "BBC Birthday",
    "We're Sharing You, Honey",
    "Bratty Behavior",
    "Stepdaughter Up!",
    "Meeting the Stepbro",
    "The Coolest Stepdad",
    "Cougar Bangs The Bully",
    "Confiscate this!",
    "Comforting My Nana",
    "Case No. 6615368 - She's Ready For It",
    "Stepsis Can't Get Enough",
    "Tik Tok Thots",
]

for i, Site in enumerate(TeamSkeetSites):
    DB().Push(Site, Values[i])

for Site in TeamSkeetSites:
    try:
        print(DB().Pull(Site))
    except KeyError:
        print(f"Database for :{Site}, does not exist.")
