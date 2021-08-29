"""
Data = {
    "AbusiveInput": [
        "chod",
        "chut",
        "lod",
        "laud",
        "bhos",
        "love day",
        "bosd",
        "gand",
        "ghant",
        "gant",
        "land",
        "bp",
        "xxx",
        "sex",
        "porn",
        "ghap",
        "gap",
        "dofa",
        "bol",
        "rand",
        "bob",
        "boob",
        "fuck",
        "fcuk",
    ],
    "AbusiveOutput": [
        "Fakir",
        "C#0DU",
        "B#0SD1N@",
        "G@NDU",
        "L0DU",
        "T0P@",
        "D@F0D",
    ]}
"""


import os
import re
import bs4
import time
import json
import random
import img2pdf
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
}
Cata = {
    "am": {"Base": "AnalMom", "Color": 15243988},
    "bb": {"Base": "BBCParadise", "Color": 16761856},
    "bm": {"Base": "BadMilfs", "Color": 15679592},
    "dc": {"Base": "DadCrush", "Color": 16725631},
    "ds": {"Base": "DaughterSwap", "Color": 39385},
    "fs": {"Base": "FamilyStrokes", "Color": 3830853},
    "ff": {"Base": "FreeUseFantasy", "Color": 16761856},
    "fm": {"Base": "FreeUseMilf", "Color": 0xFFC400},
    "ms": {"Base": "MomSwap", "Color": 0x00D387},
    "md": {"Base": "MYLFDOM", "Color": 16731942},
    "pm": {"Base": "PervMom", "Color": 13698310},
    "pn": {"Base": "PervNana", "Color": 13698310},
    "sl": {"Base": "ShoplyfterMYLF", "Color": 14486850},
    "si": {"Base": "SisLovesMe", "Color": 15745132},
    "ss": {"Base": "SisSwap", "Color": 0xF456E9},
    "tt": {"Base": "TeamSkeetTube", "Color": 636990},
    "zz": {"Base": "Brazzers", "Color": 14725667},
    "tr": {"Base": "TeamSkeetTubeRandom", "Color": 636990},
}
Uata = {
    "AnalMom": 15243988,
    "BBCParadise": 16761856,
    "BadMilfs": 15679592,
    "Brazzers": 14725667,
    "DadCrush": 16725631,
    "DaughterSwap": 39385,
    "FamilyStrokes": 3830853,
    "FreeUseFantasy": 16761856,
    "FreeUseMilf": 0xFFC400,
    "MomSwap": 0x00D387,
    "MYLFDOM": 16731942,
    "PervMom": 13698310,
    "PervNana": 13698310,
    "ShoplyfterMYLF": 14486850,
    "SisLovesMe": 15745132,
    "SisSwap": 0xF456E9,
    "TeamSkeetTube": 636990,
    "TeamSkeetTubeRandom": 636990,
}
TeamSkeetSites = [
    "AnalMom",
    "BBCParadise",
    "BadMilfs",
    "DadCrush",
    "DaughterSwap",
    "FamilyStrokes",
    "FreeUseFantasy",
    "FreeUseMilf",
    "MomSwap",
    "MYLFDOM",
    "PervMom",
    "PervNana",
    "ShoplyfterMYLF",
    "SisLovesMe",
    "SisSwap",
    "TeamSkeetTube",
]
ThresholdValues = [
    "Ass For Pass",
    "Car Trouble",
    "Makeout Tips For Mom",
    "Sabotaging Stepdad's Relationship",
    "Extra Love From Stepdaughters",
    "Big Bet",
    "Home Alone with Step Bro",
    "The Good Ol' Days",
    "No Tramps Allowed",
    "Leather And Lust",
    "A Stepson's Wet Dream",
    "Staying with Nana",
    "Case No. 6615370 - Anti-Masker Thief",
    "Comforting My Stepsis",
    "Getting Lucky With Stepsis",
    "Case No. 7906147",
]
RandomSites = ["Brazzers", "TeamSkeetTubeRandom"]


class DashFunctions:
    def Reddit(self, URL):
        cookies = {"over18": "1"}
        headers = {"User-Agent": "Mozilla/5.0"}

        r = requests.get(url=URL, headers=headers, cookies=cookies)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        Articles = soup.find_all("a")
        for Artilcle in Articles:
            Source = Artilcle["href"]
            if "redgifs.com" in Source:
                return Source
            elif "gyfcat.com" in Source:
                return Source.replace("gyfcat.com", "redgifs.com/watch")

    def RedGifs(self, URL):
        if "gyfcat.com" in URL:
            URL = URL.replace("gyfcat.com", "redgifs.com/watch")

        op = webdriver.ChromeOptions()
        op.add_argument("--no-sandbox")
        op.add_argument("--disable-dev-shm-usage")
        op.add_argument("--headless")

        with webdriver.Chrome(chrome_options=op) as Driver:
            Driver.get(URL)
            WebDriverWait(Driver, 10).until(
                presence_of_element_located((By.TAG_NAME, "source"))
            )
            r = Driver.page_source

        Term = URL.split("/")[-1]
        soup = bs4.BeautifulSoup(r, "html.parser")
        sources = soup.find_all("source")
        for source in sources:
            try:
                found = source["src"]
                if Term in found.lower():
                    return found.replace("-mobile", "")
            except KeyError:
                pass

    def IncestFlix(self, URL, Num=5):
        Tag1 = URL.split(",")[1].strip().replace(" ", "-")

        try:
            Tag2 = URL.split(",")[2].strip().replace(" ", "-")
            DataUrl = f"http://www.incestflix.com/tag/{Tag1}/and/{Tag2}"
        except IndexError:
            Tag2 = None
            DataUrl = f"http://www.incestflix.com/tag/{Tag1}/"

        Titles, Contents, Images = [], [], []

        Var = int(Num / 10) + 2

        for i in range(1, Var):
            NDataUrl = DataUrl + f"/page/{i}"
            r = requests.get(url=NDataUrl, headers=headers).content
            soup = bs4.BeautifulSoup(r, "html.parser")
            Articles = soup.find_all("a", id="videolink")

            if len(Articles) < 10:
                break

            for Artilce in Articles:
                Link = Artilce["href"]
                Pornstar = (
                    Artilce.find("div", {"class": "text-heading"})
                    .text.split(" - ")[0]
                    .replace("[60fps] ", "")
                    .strip()
                )
                Video = bs4.BeautifulSoup(
                    requests.get(url=Link, headers=headers).content, "html.parser"
                ).find("source")["src"]
                Contents.append(f"{Pornstar}\n\n{Link}\n{Video}")

                Titles.append(
                    Artilce.find("div", {"class": "text-heading"})
                    .text.split(" - ")[1]
                    .strip()
                )
                Images.append(
                    Artilce.find("div", {"class": "img-overflow"})["style"]
                    .split("(")[1]
                    .split(")")[0]
                )

        return [Titles[:Num], Contents[:Num], Images[:Num]]

    def IncestflixWatch(self, URL):
        return bs4.BeautifulSoup(
            requests.get(url=URL, headers=headers).content, "html.parser"
        ).find("source")["src"]

    async def AllPC(self, Message):
        StartTime = time.time()

        URLRE = re.search(r"https://allporncomic.com/porncomic/(.*)/(.*)/", Message)
        if URLRE.group(2) != "":
            URL = (
                f"https://allporncomic.com/porncomic/{URLRE.group(1)}/{URLRE.group(2)}/"
            )
            Soup = bs4.BeautifulSoup(
                requests.get(URL, headers=headers).content, "html.parser"
            )
            Wrapper = Soup.find("div", attrs={"class": "reading-content"})
            Images = [Image["data-src"].strip() for Image in Wrapper.find_all("img")]
            FileName = f"{URLRE.group(1).replace('-',' ').title()} - {URLRE.group(2).replace('-',' ').title()}.pdf"
        elif URLRE.group(2) == "":
            URL = f"https://allporncomic.com/porncomic/{URLRE.group(1)}/"
            Soup = bs4.BeautifulSoup(
                requests.get(URL, headers=headers).content, "html.parser"
            )
            Chapters = [
                Article["href"]
                for Article in Soup.find_all("a")[1:]
                if URL in Article["href"]
            ][2:][::-1]
            Images = []
            for Chapter in Chapters:
                Soup = bs4.BeautifulSoup(
                    requests.get(Chapter, headers=headers).content, "html.parser"
                )
                Wrapper = Soup.find("div", attrs={"class": "reading-content"})
                Images.append(
                    [Image["data-src"].strip() for Image in Wrapper.find_all("img")]
                )

            FileName = f"{URLRE.group(1).replace('-',' ').title()}.pdf"

        Data = [requests.get(Image).content for Image in Images]
        with open(f"Data/{FileName}", "wb") as f:
            f.write(img2pdf.convert(Data))

        TotalTime = round(time.time() - StartTime)
        Length = len(Images)
        Results = f"Processed {Length} Images in {TotalTime} seconds. Rate: {round(TotalTime/Length)} seconds per Image."

        return f"{FileName.replace(' ','%20')}\n{Results}"

    async def HDPC(self, Message):
        StartTime = time.time()

        URL = re.search(r"https://hdporncomics.com/(.*)/", Message).group(1)
        URL = f"https://hdporncomics.com/{URL}/"
        Soup = bs4.BeautifulSoup(
            requests.get(URL, headers=headers).content, "html.parser"
        )
        Wrapper = Soup.find_all("a", attrs={"itemprop": "contentUrl"})
        Title = Soup.find("h1").text.replace(" comic porn", "").strip().title()
        ImageLinks = [Var["href"] for Var in Wrapper]
        Images = [requests.get(Image).content for Image in ImageLinks]
        with open(f"Data/{Title}.pdf", "wb") as F:
            F.write(img2pdf.convert(Images))

        TotalTime = round(time.time() - StartTime)
        Length = len(Images)
        Results = f"Processed {Length} Images in {TotalTime} seconds. Rate: {round(TotalTime/Length)} seconds per Image."

        return f"{Title.replace(' ','%20')}.pdf\n{Results}"

    async def NHentai(self, Message):
        StartTime = time.time()

        URLRE = re.search(r"https://nhentai.net/g/(.*)/", Message)
        URL = f"https://nhentai.net/g/{URLRE.group(1)}/"

        HomeSoup = bs4.BeautifulSoup(
            requests.get(URL.split()[0]).content, "html.parser"
        )
        Section = HomeSoup.find("div", attrs={"id": "info"}).find("section")
        Length = [
            int(Division.find("span", attrs={"class": "name"}).text.strip())
            for Division in Section
            if "Pages:" in Division.text
        ][0]
        Title = HomeSoup.find("h1", attrs={"class": "title"}).text.replace("|", "")

        ImageSoup = bs4.BeautifulSoup(requests.get(URL + "1/").content, "html.parser")
        ImageLinkRaw = (
            ImageSoup.find("section", attrs={"id": "image-container"})
            .find("a")
            .find("img")["src"]
        )

        reCursor = re.match(
            r"https://i.nhentai.net/galleries/(.*)/(\d).(.*)", ImageLinkRaw
        )
        LinkTemplate = f"https://i.nhentai.net/galleries/{reCursor.group(1)}/%s.{reCursor.group(3)}"
        ImageLinks = [LinkTemplate % str(i) for i in range(1, Length + 1)]
        ImageContents = [requests.get(ImageLink).content for ImageLink in ImageLinks]

        FileName = f"{Title}.pdf"
        if os.path.isfile(f"Data/{FileName}"):
            os.remove(f"Data/{FileName}")
        with open(f"Data/{FileName}", "wb") as F:
            F.write(img2pdf.convert(ImageContents))

        TotalTime = round(time.time() - StartTime)
        Results = f"Processed {Length} Images in {TotalTime} seconds. Rate: {round(TotalTime/Length)} seconds per Image."
        return f"{FileName.replace(' ', '%20')}\n{Results}"


class Database:
    def __init__(self):
        self.File = "Data/Data.json"
        with open(self.File, "r") as f:
            self.Data = json.loads(f.read())

    def Pull(self, Key):
        return self.Data[Key]

    def Push(self, Key, Value):
        self.Data[Key] = Value
        with open(self.File, "w") as f:
            json.dump(self.Data, f, indent=4)

    def Delete(self, Key):
        del self.Data[Key]
        with open(self.File, "w") as f:
            json.dump(self.Data, f, indent=4)

    def List(self):
        Keys = [_ for _ in self.Data]
        Values = [self.Pull(Key) for Key in Keys]
        String = "\n".join([f"{K}:{V}" for K, V in zip(Keys, Values)])
        return String


class Parser:
    def TeamSkeet(self, Base, Number=1):
        Soup = bs4.BeautifulSoup(
            requests.get(f"https://www.{Base}.com/movies", headers=headers).content,
            "html.parser",
        )
        Length = len(
            Soup.find_all("div", {"class": "title info update_name text-truncate"})
        )

        if Number > Length:
            Number = Length
        elif Number < 1:
            Number = 1

        Title = [
            T.text.strip()
            for T in Soup.find_all(
                "div", {"class": "title info update_name text-truncate"}
            )
        ]
        Pornstar = [
            PS.text.strip()
            for PS in Soup.find_all("div", {"class": "girlname text-truncate"})
        ]
        Links = [
            f"https://www.{Base}.com" + Anchor.find_all("a")[0]["href"]
            for Anchor in Soup.find_all(
                "div", {"class": "title info update_name text-truncate"}
            )
        ]

        Descriptions = [
            bs4.BeautifulSoup(
                requests.get(url=Link, headers=headers).content, "html.parser"
            )
            .find("p", attrs={"class": "video-description"})
            .text
            for Link in Links[:Number]
        ]

        Images = [
            bs4.BeautifulSoup(
                requests.get(Link, headers=headers).content, "html.parser"
            ).find("stream")["poster"]
            for Link in Links[:Number]
        ]
        Videos = [Image.replace("big.jpg", "small.mp4") for Image in Images]

        Daftsex = ["https://daftsex.com/video/" + T.replace(" ", "%20") for T in Title]
        Biqle = ["https://biqle.com/video/" + T.replace(" ", "%20") for T in Title]

        return [
            Title[:Number],
            Pornstar[:Number],
            Links[:Number],
            Daftsex[:Number],
            Biqle[:Number],
            Images,
            Videos,
            Descriptions,
        ]

    def TeamSkeetTubeRandom(self, Number=1):
        BackEnds = [
            "anal-mom",
            "bad-milfs",
            "bbc-paradise",
            "bffs",
            "dad-crush",
            "daughter-swap",
            "family-strokes",
            "foster-tapes",
            "freeuse-fantasy",
            "full-of-joi",
            "ginger-patch",
            "got-mylf",
            "lone-milf",
            "milf-body",
            "milfty",
            "mom-drips",
            "perv-mom",
            "perv-nana",
            "shoplyfter-mylf",
            "submissived",
            "the-real-workout",
            "thickumz",
        ]
        Categories = [
            f"https://www.teamskeettube.com/video/category/{Back}/" for Back in BackEnds
        ]
        Category = random.choice(Categories)

        for WebPageNo in range(1, 100):
            Link = f"{Category}page/{WebPageNo}/"
            Articles = bs4.BeautifulSoup(
                requests.get(url=Link, headers=headers).content, "html.parser"
            ).find_all("article")
            if len(Articles) != 20:
                LastLength = len(Articles)
                break

        PageNo = random.randint(1, WebPageNo)
        if PageNo != WebPageNo:
            LastLength = 20

        Article = bs4.BeautifulSoup(
            requests.get(url=f"{Category}page/{PageNo}/", headers=headers).content,
            "html.parser",
        ).find_all("article")[random.randint(1, LastLength) - 1]

        Title, Pornstar, Links, Images, Videos = [], [], [], [], []

        for i in range(Number):
            Title.append(Article.text.strip().split(" - ")[1])
            Pornstar.append(Article.text.strip().split(" - ")[0])
            Links.append(Article.find("a")["href"])

            Images.append(Article.find("img")["data-src"])
            try:
                Videos.append(
                    bs4.BeautifulSoup(
                        requests.get(
                            url=Article.find("a")["href"], headers=headers
                        ).content,
                        "html.parser",
                    ).find("source")["src"]
                )
            except Exception as e:
                Videos.append(type(e).__name__)

            Daftsex = [
                f"https://daftsex.com/video/" + T.strip().replace(" ", "%20")
                for T in Title
            ]
            Biqle = [
                f"https://Biqle.com/video/" + T.strip().replace(" ", "%20")
                for T in Title
            ]

        return [Title, Pornstar, Links, Daftsex, Biqle, Images, Videos]

    def TeamSkeetTube(self, Number=1):
        Articles = bs4.BeautifulSoup(
            requests.get(url="https://www.teamskeettube.com/", headers=headers).content,
            "html.parser",
        ).find_all("article")
        Title, Pornstar, Links, Images, Videos = [], [], [], [], []

        for Article in Articles:
            Title.append(Article.text.strip().split(" - ")[1])
            Pornstar.append(Article.text.strip().split(" - ")[0])
            Links.append(Article.find("a")["href"])

            Images.append(Article.find("img")["data-src"].replace("-640x360", ""))
            # Videos.append(
            #     "Error Internet.py|Parser()|TeamSkeetTube()|Videos|Not Scripted")
            try:
                Videos.append(
                    bs4.BeautifulSoup(
                        requests.get(
                            url=Article.find("a")["href"], headers=headers
                        ).content,
                        "html.parser",
                    ).find("source")["src"]
                )
            except Exception as e:
                Videos.append(type(e).__name__)

        Daftsex = [
            f"https://daftsex.com/video/" + T.strip().replace(" ", "%20") for T in Title
        ]
        Biqle = [
            f"https://Biqle.com/video/" + T.strip().replace(" ", "%20") for T in Title
        ]

        return [
            Title[:Number],
            Pornstar[:Number],
            Links[:Number],
            Daftsex[:Number],
            Biqle[:Number],
            Images[:Number],
            Videos[:Number],
        ]

    def Brazzers(self, Number=1):
        Title, Pornstar, Links, Images, Videos = [], [], [], [], []

        for i in range(Number):
            PageNo = random.randint(1, 295)
            RNumber = random.randint(1, 24) - 1

            Soup = bs4.BeautifulSoup(
                requests.get(
                    f"https://www.brazzers.com/videos/page/{PageNo}", headers=headers
                ).content,
                "html.parser",
            )
            FrontSoup = Soup.find_all("div", {"class": "dtkdna-3 cjHUpt"})
            FrontSoupL = [Div for Div in FrontSoup[RNumber]]
            BackSoup = Soup.find_all("a", {"class": "aq1tgu-0 ja-Dbkh"})

            Title.append(FrontSoupL[3].text)
            Pornstar.append(FrontSoupL[0].text)
            Links.append(
                "https://www.brazzers.com"
                + [Link["href"] for Link in BackSoup][RNumber]
            )
            Images.append(
                BackSoup[RNumber].find("img", {"class": "sc-1p8qg4p-3 cortgL"})["src"]
            )
            Videos.append("Error Web.py|Random()|Fetch()|Brazzers|Videos|Not Scripted")

        Daftsex = [
            f"https://daftsex.com/video/" + T.strip().replace(" ", "%20") for T in Title
        ]
        Biqle = [
            f"https://Biqle.com/video/" + T.strip().replace(" ", "%20") for T in Title
        ]

        return [Title, Pornstar, Links, Daftsex, Biqle, Images, Videos]


async def Inspect():
    Inspected = []
    for Base in TeamSkeetSites:

        if Base == "TeamSkeetTube":
            Articles = bs4.BeautifulSoup(
                requests.get(
                    url="https://www.teamskeettube.com/", headers=headers
                ).content,
                "html.parser",
            ).find_all("article")
            Titles = [Article.text.strip().split(" - ")[1] for Article in Articles]

        else:
            Soup = bs4.BeautifulSoup(
                requests.get(f"https://www.{Base}.com/movies", headers=headers).content,
                "html.parser",
            )
            Titles = [
                T.text.strip()
                for T in Soup.find_all(
                    "div", {"class": "title info update_name text-truncate"}
                )
            ]

        Stored = Database().Pull(Base)

        for i in range(len(Titles)):
            if Stored == Titles[i]:
                Database().Push(Base, Titles[0])
                break
        if i + 1 == len(Titles):
            Inspected.append(0)
        else:
            Inspected.append(i)
    return Inspected


def Get(Site, Number=1):
    try:
        if Site == "TeamSkeetTube":
            return Parser().TeamSkeetTube(Number)

        elif Site == "TeamSkeetTubeRandom":
            return Parser().TeamSkeetTubeRandom(Number)

        elif Site == "Brazzers":
            return Parser().Brazzers(Number)

        elif Site in TeamSkeetSites:
            return Parser().TeamSkeet(Site, Number)

    except Exception as e:
        return f"{Site}: {type(e).__name__}"


# ---------------------------------------------------------------------------------------------------

import discord
import datetime
from discord.ext import tasks
from discord.ext import commands

from Global import *


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == True:
            return

        if message.author.id not in Whitelist:
            return

        elif "reddit.com" in message.content.lower():
            try:
                Payload = DashFunctions().RedGifs(
                    DashFunctions().Reddit(message.content.lower())
                )
            except Exception as e:
                Payload = f"Message.reddit(): {type(e).__name__}"
            finally:
                await message.author.send(Payload)

        elif (
            "redgifs.com" in message.content.lower()
            or "gyfcat.com" in message.content.lower()
        ):
            try:
                Payload = DashFunctions().RedGifs(message.content.lower())
            except Exception as e:
                Payload = f"Message.redgifs(): {type(e).__name__}"
            finally:
                await message.author.send(Payload)

        elif "incestflix.com/watch" in message.content.lower():
            try:
                Payload = DashFunctions().IncestflixWatch(message.content.lower())
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

                Data = DashFunctions().IncestFlix(message.content, Num)

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
            Data = await DashFunctions().AllPC(message.content)
            await message.author.send(f"{Host}{Data}")

        elif "hdporncomics.com" in message.content.lower():
            Data = await DashFunctions().HDPC(message.content)
            await message.author.send(f"{Host}{Data}")

        elif "nhentai.net/g/" in message.content.lower():
            Data = await DashFunctions().NHentai(message.content)
            await message.author.send(f"{Host}{Data}")


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
        Descriptions = Data[7][::-1]

        for i in range(len(Titles)):
            Timestamp = datetime.datetime.now()
            LinksSTR = f"{Links[i]}\n{Daftsexs[i]}\n{Biqles[i]}"
            Var = [Titles[i], Pornstars[i]]
            embed = discord.Embed(colour=Color, timestamp=Timestamp)
            embed.add_field(name=Var[0], value=Var[1], inline=False)
            embed.add_field(name="Links", value=LinksSTR, inline=False)
            embed.add_field(name="Description", value=Descriptions[i], inline=False)
            embed.set_image(url=Images[i])
            embed.set_footer(text=os.path.basename(__file__))
            await Target.send(embed=embed)
            await Target.send(Videos[i])

    async def Sending(self, ctx, Category, Number):
        Base = Cata[Category]["Base"]
        Color = Cata[Category]["Color"]
        Data = Get(Base, Number)

        if type(Data) != list:
            await ctx.message.add_reaction(Emoji["Wrong"])
            await Respond(ctx, Data)

        else:
            await ctx.message.add_reaction(Emoji["Right"])
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
                await ctx.message.add_reaction(Emoji["Wrong"])
                return await Respond(ctx, HelpMessage)

            elif Function.lower() not in Functions:
                await ctx.message.add_reaction(Emoji["Wrong"])
                return await Respond(ctx, HelpMessage)

            elif Function.lower() in Functions:
                if Function.lower() in NoArg:
                    if Function.lower() == "list":
                        String = Database().List()
                        Payload = discord.Embed(
                            title="Database", description=String, color=ctx.author.color
                        )
                        await ctx.message.add_reaction(Emoji["Right"])
                        return await Respond(ctx, Payload, False, True)

                    elif Function.lower() == "json":
                        Payload = f"```JSON\n{Database().Data}```"
                        await ctx.message.add_reaction(Emoji["Right"])
                        return await Respond(ctx, Payload, True, False)

                elif Function.lower() in OneArg:
                    if Key == None:
                        await ctx.message.add_reaction(Emoji["Wrong"])
                        return await Respond(ctx, HelpMessage)
                    else:
                        if Function.lower() == "pull":
                            Payload = Database().Pull(Key)
                            if Payload == None:
                                await ctx.message.add_reaction(Emoji["Wrong"])
                                Payload = f"No key found as [**{Key}**]"
                                return await Respond(ctx, Payload)
                            else:
                                await ctx.message.add_reaction(Emoji["Right"])
                                return await Respond(ctx, Payload)

                        elif Function.lower() == "delete":
                            Database().Delete(Key)
                            await ctx.message.add_reaction(Emoji["Right"])
                            return await Respond(ctx, f"Deleted: {Key}")

                elif Function.lower() in TwoArg:
                    if Key == None or Value == None:
                        await ctx.message.add_reaction(Emoji["Wrong"])
                        return await Respond(ctx, HelpMessage)
                    else:
                        if Function.lower() == "push":
                            Database().Push(Key, Value)
                            await ctx.message.add_reaction(Emoji["Right"])
                            return await Respond(ctx, f"Added: \n{Key}:{Value}")

        except Exception as e:
            Payload = f"Dash.DB(): {type(e).__name__}"
            await ctx.message.add_reaction(Emoji["Wrong"])
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
                await ctx.message.add_reaction(Emoji["Wrong"])
                return await Respond(ctx, HelpMessage)

        except Exception as e:
            await ctx.message.add_reaction(Emoji["Wrong"])
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
                    await ctx.message.add_reaction(Emoji["Wrong"])
                    return await Respond(ctx, f"Dash.Update(): Already running.")
                else:
                    await ctx.message.add_reaction(Emoji["Right"])
                    return Loop.start()

            elif Function.lower() == "stop":
                if Loop.is_running() == False:
                    await ctx.message.add_reaction(Emoji["Wrong"])
                    return await Respond(ctx, f"Dash.Update(): Already at standby.")
                else:
                    await ctx.message.add_reaction(Emoji["Right"])
                    return Loop.stop()

            elif Function.lower() == "restart":
                await ctx.message.add_reaction(Emoji["Right"])
                return Loop.restart()

            elif Function.lower() == "status":
                await ctx.message.add_reaction(Emoji["Right"])
                return await Respond(
                    ctx, f"Dash.Update(): Loop.is_running = {Loop.is_running()}"
                )

            else:
                await ctx.message.add_reaction(Emoji["Wrong"])
                return await Respond(ctx, HelpMessage)

        except Exception as e:
            await ctx.message.add_reaction(Emoji["Wrong"])
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
    pass
    # bot.add_cog(Dash(bot))
    # bot.add_cog(Message(bot))
