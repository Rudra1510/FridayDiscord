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
import shutil
import random
import img2pdf
import requests
import replitdb
import youtube_dl
import pyshorteners
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


class Other:
    def __init__(self):
        pass

    def Shorten(self, Link):
        return pyshorteners.Shortener().tinyurl.short(Link)


class Download:
    def YouTube(self, Text):
        AudioPref = {
            "outtmpl": "Data/%(title)s.%(ext)s",
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        VideoPref = {
            "outtmpl": "Data/%(title)s.%(ext)s",
            "merge-output-format": "mp4",
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]",
        }

        Texts = Text.split()

        if len(Texts) > 1:
            for T in Texts:
                if "youtu" in T:
                    Link = T
                    break
        else:
            Link = Text
            Options = AudioPref

        if "mp3" in Text or "audio" in Text:
            Options = AudioPref
        elif "vid" in Text:
            Options = VideoPref
        else:
            Options = AudioPref

        with youtube_dl.YoutubeDL(Options) as Cursor:
            InfoDict = Cursor.extract_info(Link, download=False)
            Title = (
                InfoDict["title"]
                .replace('"', "")
                .replace("'", "")
                .replace("|", "-")
                .replace("?", "#")
            )
            FileName = f"{Title}.mp4"
            Options["outtmpl"] = "Data/" + FileName
        with youtube_dl.YoutubeDL(Options) as Downloader:
            Downloader.download([Link])

        for File in os.listdir("Data"):
            if Title in File:
                return File.replace(" ", "%20")

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

    def Twitter(self, url):
        op = webdriver.ChromeOptions()
        op.add_argument("--no-sandbox")
        op.add_argument("--disable-dev-shm-usage")

        with webdriver.Chrome(chrome_options=op) as driver:
            driver.implicitly_wait(10)
            driver.get("https://twipix.co/dash/")

            driver.find_element_by_class_name("input--style-4").send_keys(url)
            driver.find_element_by_xpath('//*[@id="theme"]/option[2]').click()
            driver.find_element_by_xpath(
                "/html/body/div/div/div/div/form/div[3]/div/div/div/label[1]"
            ).click()
            time.sleep(1)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div/div/div/div/form/div[6]/button"
            ).click()
            time.sleep(1)
            Image = driver.find_element_by_xpath(
                "/html/body/div/div/div/div/form/img"
            ).get_attribute("src")

        import base64

        ImageBytes = bytes(str(Image).replace("data:;base64,", ""), encoding="utf-8")
        RawImage = base64.decodestring(ImageBytes)
        with open("Tweet.jpeg", "wb") as OutputImage:
            OutputImage.write(RawImage)

        return "Tweet.jpeg"

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


class DB:
    def __init__(self):
        self.File = "Bot/Functions/Data.json"
        with open(self.File, "r") as f:
            self.Data = json.loads(f.read())

    def Pull(self, Key):
        return self.Data[Key]

    def Push(self, Key, Value):
        self.Data[Key] = Value
        with open(self.File, "w") as f:
            json.dump(self.Data, f)

    def Delete(self, Key):
        del self.Data[Key]
        with open(self.File, "w") as f:
            json.dump(self.Data, f)

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
            Descriptions
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

        Stored = DB().Pull(Base)

        for i in range(len(Titles)):
            if Stored == Titles[i]:
                DB().Push(Base, Titles[0])
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
