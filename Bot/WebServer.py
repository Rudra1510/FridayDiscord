from flask import Flask
from threading import Thread

App = Flask("")


@App.route("/")
def Home():
    return "<01000110><01110010><01101001><01100100><01100001><01111001>"


def Run():
    App.run(host="0.0.0.0", port=8080)


def StayAwake():
    t = Thread(target=Run)
    t.start()
