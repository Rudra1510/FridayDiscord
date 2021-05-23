'''
#Teamskeet
    SisLovesMe
    FamilyStrokes
    PervMom
    FosterTapes
    Shoplyfter
    BFFS
    DaughterSwap
    DadCrush
    Submissived
    Thickumz
    NotMyGrandPa
    FreeUseFantasy
    PervDoctor

#MYLF
    PervMom
    PervNana
    ShoplyfterMYLF
    FosterTapes
    MYLFDOM
    BBCParadise
    BadMilfs
    AnalMom
    MomSwap

#Selected
    
    #Running

        SisLovesMe     sis --- si
        FamilyStrokes  fs
        PervMom        pm
        DaughterSwap   ds
        AnalMom        am
        FreeUseFantasy fuf --- fu
    
    #To Add

        DadCrush       dc
        PervNana       pn
        ShoplyfterMYLF sl
        MYLFDOM        md
        BBCParadise    bb
        BadMilfs       bm
        
        #Not Supported Yet
            Submissived    su
            MomSwap        ms
            PervDoctor     pd

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
'''


import os
import bs4
import random
import platform
import requests
import youtube_dl
import time
import pyshorteners

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0', }
Cata = {
    'am': {'Base': 'AnalMom', 'Color': 15243988},
    'bb': {'Base': 'BBCParadise', 'Color': 16761856},
    'bm': {'Base': 'BadMilfs', 'Color': 15679592},
    'dc': {'Base': 'DadCrush', 'Color': 16725631},
    'ds': {'Base': 'DaughterSwap', 'Color': 39385},
    'ff': {'Base': 'FreeUseFantasy', 'Color': 16761856},
    'fs': {'Base': 'FamilyStrokes', 'Color': 3830853},
    'md': {'Base': 'MYLFDOM', 'Color': 16731942},
    'pm': {'Base': 'PervMom', 'Color': 13698310},
    'pn': {'Base': 'PervNana', 'Color': 13698310},
    'si': {'Base': 'SisLovesMe', 'Color': 15745132},
    'sl': {'Base': 'ShoplyfterMYLF', 'Color': 14486850},
    'tr': {'Base': 'TeamSkeetTubeRandom', 'Color': 636990},
    'zz': {'Base': 'Brazzers', 'Color': 14725667},
    'tt': {'Base': 'TeamSkeetTube', 'Color': 636990},
}
Uata = {
    'AnalMom': 15243988,
    'BBCParadise': 16761856,
    'BadMilfs': 15679592,
    'Brazzers': 14725667,
    'DadCrush': 16725631,
    'DaughterSwap': 39385,
    'FamilyStrokes': 3830853,
    'FreeUseFantasy': 16761856,
    'MYLFDOM': 16731942,
    'PervMom': 13698310,
    'PervNana': 13698310,
    'ShoplyfterMYLF': 14486850,
    'SisLovesMe': 15745132,
    'TeamSkeetTubeRandom': 636990,
    'TeamSkeetTube': 636990,
}
TeamSkeetSites = [
    'AnalMom',
    'BBCParadise',
    'BadMilfs',
    'DadCrush',
    'DaughterSwap',
    'FamilyStrokes',
    'FreeUseFantasy',
    'MYLFDOM',
    'PervMom',
    'PervNana',
    'ShoplyfterMYLF',
    'SisLovesMe',
    'TeamSkeetTube',
]
RandomSites = [
    "Brazzers",
    "TeamSkeetTubeRandom"
]


class Other:
    def __init__(self):
        pass

    def Shorten(self, Link):
        return pyshorteners.Shortener().tinyurl.short(Link)


class Download:
    def YouTube(self, Text):
        AudioPref = {
            'outtmpl': 'baby/Functions/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        VideoPref = {
            'outtmpl': 'baby/Functions/%(title)s.%(ext)s',
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

        if "-a" in Text:
            Options = AudioPref
        elif "-v" in Text:
            Options = VideoPref
        else:
            Options = AudioPref

        with youtube_dl.YoutubeDL(Options) as Downloader:
            Downloader.download([Link])

        for FileName in os.listdir("./baby/Functions"):
            Extension = FileName.split(".")[-1]
            MediaExtensions = ["mp4", "mkv", "webm", "mp3", "m4a"]

            if Extension in MediaExtensions:
                return f"./baby/Functions/{FileName}"

    def Reddit(self, URL):
        cookies = {'over18': '1'}
        headers = {'User-Agent': 'Mozilla/5.0'}

        r = requests.get(url=URL, headers=headers, cookies=cookies)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        Articles = soup.find_all('a')
        for Artilcle in Articles:
            Source = Artilcle['href']
            if 'redgifs.com' in Source:
                return Source

    def RedGifs(self, URL):
        op = webdriver.ChromeOptions()
        op.add_argument('--no-sandbox')
        op.add_argument('--disable-dev-shm-usage')
        # op.add_argument("--headless")

        with webdriver.Chrome(chrome_options=op) as driver:
            driver.get(URL)
            WebDriverWait(driver, 10).until(
                presence_of_element_located((By.TAG_NAME, "source")))
            r = driver.page_source

        soup = bs4.BeautifulSoup(r, "html.parser")
        sources = soup.find_all('source')
        for source in sources:
            try:
                found = source['src']
                if "mobile" not in found:
                    return found
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

        Var = int(Num/10)+2

        for i in range(1, Var):
            NDataUrl = DataUrl + f"/page/{i}"
            r = requests.get(url=NDataUrl, headers=headers).content
            soup = bs4.BeautifulSoup(r, "html.parser")
            Articles = soup.find_all('a', id='videolink')

            if len(Articles) < 10:
                break

            for Artilce in Articles:
                Link = Artilce['href']
                Pornstar = Artilce.find(
                    "div", {"class": "text-heading"}).text.split(' - ')[0].replace("[60fps] ", "").strip()
                Video = bs4.BeautifulSoup(requests.get(
                    url=Link, headers=headers).content, "html.parser").find('source')["src"]
                Contents.append(f"{Pornstar}\n\n{Link}\n{Video}")

                Titles.append(Artilce.find(
                    "div", {"class": "text-heading"}).text.split(' - ')[1].strip())
                Images.append(Artilce.find("div", {"class": "img-overflow"})
                              ["style"].split("(")[1].split(")")[0])

        return [Titles[:Num], Contents[:Num], Images[:Num]]

    def IncestflixWatch(self, URL):
        return bs4.BeautifulSoup(requests.get(
            url=URL, headers=headers).content, "html.parser").find('source')["src"]

    def Twitter(self, url):
        op = webdriver.ChromeOptions()
        op.add_argument('--no-sandbox')
        op.add_argument('--disable-dev-shm-usage')

        with webdriver.Chrome(chrome_options=op) as driver:
            driver.implicitly_wait(10)
            driver.get("https://twipix.co/dash/")

            driver.find_element_by_class_name("input--style-4").send_keys(url)
            driver.find_element_by_xpath('//*[@id="theme"]/option[2]').click()
            driver.find_element_by_xpath(
                '/html/body/div/div/div/div/form/div[3]/div/div/div/label[1]').click()
            time.sleep(1)
            driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div/div/div/div/form/div[6]/button").click()
            time.sleep(1)
            Image = driver.find_element_by_xpath(
                "/html/body/div/div/div/div/form/img").get_attribute('src')

        import base64
        ImageBytes = bytes(str(Image).replace(
            "data:;base64,", ""), encoding='utf-8')
        RawImage = base64.decodestring(ImageBytes)
        with open('Tweet.jpeg', 'wb') as OutputImage:
            OutputImage.write(RawImage)

        return 'Tweet.jpeg'


class DB:

    def __init__(self, Collection):
        self.Collection = Collection
        self.System = platform.uname().system
        self.REPLIT_DB_URL = "https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTgzODg0MTUsImlhdCI6MTYxODI3NjgxNSwiaXNzIjoiY29ubWFuIiwiZGF0YWJhc2VfaWQiOiI4YjFhZGZlNC0wMTE5LTRjZjgtODFhMS1hZWI2ZjZlYmQ4MTcifQ.onuRprfx7YpJmMp3KCrBQwhWPj_SlqY49X4jl36y38lSjVsV85EG8bByfyII46jK9JtTbQijQFDmCFqTg2lwNQ"

    def Pull(self):
        if self.System == 'Linux':
            from replit import db
            return db[self.Collection]

        elif self.System == 'Windows':
            Value = os.popen(
                f"curl {self.REPLIT_DB_URL}/{self.Collection}").read().strip()
            return Value

    def Push(self, Text):
        if self.System == 'Linux':
            from replit import db
            db[self.Collection] = Text

        elif self.System == 'Windows':
            os.system(
                f"curl {self.REPLIT_DB_URL} -d '{self.Collection}'='{Text}'")


class Parser:

    def TeamSkeet(self, Base, Number=1):
        Soup = bs4.BeautifulSoup(requests.get(
            f'https://www.{Base}.com/movies', headers=headers).content, 'html.parser')
        Length = len(Soup.find_all(
            'div', {'class': 'title info update_name text-truncate'}))

        if Number > Length:
            Number = Length
        elif Number < 1:
            Number = 1

        Title = [T.text.strip() for T in Soup.find_all(
            'div', {'class': 'title info update_name text-truncate'})]
        Pornstar = [PS.text.strip() for PS in Soup.find_all(
            'div', {'class': 'girlname text-truncate'})]
        Links = [f'https://www.{Base}.com' + Anchor.find_all('a')[0]['href'] for Anchor in Soup.find_all(
            'div', {'class': 'title info update_name text-truncate'})]

        Images = [bs4.BeautifulSoup(requests.get(Link, headers=headers).content, 'html.parser').find(
            'stream')['poster'] for Link in Links[:Number]]
        Videos = [Image.replace('big.jpg', 'small.mp4') for Image in Images]

        Daftsex = ['https://daftsex.com/video/' +
                   T.replace(' ', '%20') for T in Title]
        Biqle = ['https://biqle.com/video/' +
                 T.replace(' ', '%20') for T in Title]

        return [Title[:Number], Pornstar[:Number], Links[:Number], Daftsex[:Number], Biqle[:Number], Images, Videos]

    def TeamSkeetTubeRandom(self, Number=1):
        Categories = ['https://www.teamskeettube.com/video/category/anal-mom/', 'https://www.teamskeettube.com/video/category/bad-milfs/', 'https://www.teamskeettube.com/video/category/bbc-paradise/', 'https://www.teamskeettube.com/video/category/bffs/', 'https://www.teamskeettube.com/video/category/dad-crush/', 'https://www.teamskeettube.com/video/category/daughter-swap/', 'https://www.teamskeettube.com/video/category/family-strokes/', 'https://www.teamskeettube.com/video/category/foster-tapes/', 'https://www.teamskeettube.com/video/category/ginger-patch/',
                      'https://www.teamskeettube.com/video/category/got-mylf/', 'https://www.teamskeettube.com/video/category/milf-body/', 'https://www.teamskeettube.com/video/category/milfty/', 'https://www.teamskeettube.com/video/category/mom-drips/', 'https://www.teamskeettube.com/video/category/perv-mom/', 'https://www.teamskeettube.com/video/category/perv-nana//', 'https://www.teamskeettube.com/video/category/shoplyfter-mylf/', 'https://www.teamskeettube.com/video/category/submissived/', 'https://www.teamskeettube.com/video/category/the-real-workout/', 'https://www.teamskeettube.com/video/category/thickumz/']
        Category = random.choice(Categories)

        for WebPageNo in range(1, 100):
            Link = f'{Category}page/{WebPageNo}/'
            Articles = bs4.BeautifulSoup(requests.get(
                url=Link, headers=headers).content, 'html.parser').find_all('article')
            if len(Articles) != 20:
                LastLength = len(Articles)
                break

        PageNo = random.randint(1, WebPageNo)
        if PageNo != WebPageNo:
            LastLength = 20

        Article = bs4.BeautifulSoup(requests.get(
            url=f'{Category}page/{PageNo}/', headers=headers).content, 'html.parser').find_all('article')[random.randint(1, LastLength) - 1]

        Title, Pornstar, Links, Images, Videos = [], [], [], [], []

        for i in range(Number):
            Title.append(Article.text.strip().split(' - ')[1])
            Pornstar.append(Article.text.strip().split(' - ')[0])
            Links.append(Article.find('a')['href'])

            Images.append(Article.find('img')['data-src'])
            try:
                Videos.append(bs4.BeautifulSoup(requests.get(
                    url=Article.find('a')['href'], headers=headers).content, 'html.parser').find('source')['src'])
            except Exception as e:
                Videos.append(type(e).__name__)

            Daftsex = [f'https://daftsex.com/video/' + T.strip().replace(' ', '%20')
                       for T in Title]
            Biqle = [f'https://Biqle.com/video/' + T.strip().replace(' ', '%20')
                     for T in Title]

        return [Title, Pornstar, Links, Daftsex, Biqle, Images, Videos]

    def TeamSkeetTube(self, Number=1):
        Articles = bs4.BeautifulSoup(requests.get(
            url='https://www.teamskeettube.com/', headers=headers).content, 'html.parser').find_all('article')
        Title, Pornstar, Links, Images, Videos = [], [], [], [], []

        for Article in Articles:
            Title.append(Article.text.strip().split(' - ')[1])
            Pornstar.append(Article.text.strip().split(' - ')[0])
            Links.append(Article.find('a')['href'])

            Images.append(Article.find('img')[
                          'data-src'].replace("-640x360", ""))
            # Videos.append(
            #     "Error Internet.py|Parser()|TeamSkeetTube()|Videos|Not Scripted")
            try:
                Videos.append(bs4.BeautifulSoup(requests.get(
                    url=Article.find('a')['href'], headers=headers).content, 'html.parser').find('source')['src'])
            except Exception as e:
                Videos.append(type(e).__name__)

            Daftsex = [f'https://daftsex.com/video/' + T.strip().replace(' ', '%20')
                       for T in Title]
            Biqle = [f'https://Biqle.com/video/' + T.strip().replace(' ', '%20')
                     for T in Title]

        return [Title[:Number], Pornstar[:Number], Links[:Number], Daftsex[:Number], Biqle[:Number], Images[:Number], Videos[:Number]]

    def Brazzers(self, Number=1):
        Title, Pornstar, Links, Images, Videos = [], [], [], [], []

        for i in range(Number):
            PageNo = random.randint(1, 295)
            RNumber = random.randint(1, 24) - 1

            Soup = bs4.BeautifulSoup(requests.get(
                f'https://www.brazzers.com/videos/page/{PageNo}', headers=headers).content, 'html.parser')
            FrontSoup = Soup.find_all('div', {"class": "dtkdna-3 cjHUpt"})
            FrontSoupL = [Div for Div in FrontSoup[RNumber]]
            BackSoup = Soup.find_all('a', {'class': 'aq1tgu-0 ja-Dbkh'})

            Title.append(FrontSoupL[3].text)
            Pornstar.append(FrontSoupL[0].text)
            Links.append('https://www.brazzers.com' +
                         [Link['href'] for Link in BackSoup][RNumber])
            Images.append(BackSoup[RNumber].find(
                'img', {'class': 'sc-1p8qg4p-3 cortgL'})["src"])
            Videos.append(
                "Error Web.py|Random()|Fetch()|Brazzers|Videos|Not Scripted")

        Daftsex = [f'https://daftsex.com/video/' + T.strip().replace(' ', '%20')
                   for T in Title]
        Biqle = [f'https://Biqle.com/video/' + T.strip().replace(' ', '%20')
                 for T in Title]

        return [Title, Pornstar, Links, Daftsex, Biqle, Images, Videos]


def Inspect():
    Inspected = []
    for Base in TeamSkeetSites:

        if Base == 'TeamSkeetTube':
            Articles = bs4.BeautifulSoup(requests.get(
                url='https://www.teamskeettube.com/', headers=headers).content, 'html.parser').find_all('article')
            Titles = [Article.text.strip().split(' - ')[1]
                      for Article in Articles]

        else:
            Soup = bs4.BeautifulSoup(requests.get(
                f'https://www.{Base}.com/movies', headers=headers).content, 'html.parser')
            Titles = [T.text.strip() for T in Soup.find_all(
                'div', {'class': 'title info update_name text-truncate'})]

        Stored = DB(Base).Pull().strip('"')

        for i in range(len(Titles)):
            if Stored == Titles[i]:
                DB(Base).Push(Titles[0])
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
        return (f'File :{os.path.basename(__file__)} | Error :{type(e).__name__}')
