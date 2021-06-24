from Imports import *


Bot = commands.Bot(command_prefix=".")
App = Flask("")


class WebServer:
    @App.route("/")
    def Home():
        return "<01000110><01110010><01101001><01100100><01100001><01111001>"

    def Run():
        App.run(host="0.0.0.0", port=8080)

    def StayAwake():
        Thread(target=WebServer.Run).start()


for File in os.listdir("./Bot/Extension"):
    if File.endswith(".py"):
        Bot.load_extension(f"Extension.{File[:-3]}")


WebServer.StayAwake()
Bot.run(os.environ["Discord_Bot_Token"])
