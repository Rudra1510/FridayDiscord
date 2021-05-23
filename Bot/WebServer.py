from flask import Flask
from threading import Thread

App = Flask('')


@App.route('/')
def Home():
    return "<01000010><01100001><01100010><01111001>"


def Run():
    App.run(host="0.0.0.0", port=8080)


def StayAwake():
    t = Thread(target=Run)
    t.start()
