#!/usr/bin/python3

# Developer : Hamdy Abou El Anein

from easygui import *
import sys

def Main_loop():
    global pic
    if pic == 0:
        start()
    if pic <= 99:
        pic = pic + 1
        image = ("./Pictures/")+str(pic)+str(".png")
        msg = ("The 99 Names of Allah\n\n")+str("Name number ")+str(pic)
        choices = ["Begin","Previous","Next"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Next":
            Main_loop()
        elif reply == "Previous":
            pic = pic -2
            Main_loop()
        elif reply == None:
            sys.exit(0)
        elif reply == "Begin":
            pic = 1
            start()
        else:
            Main_loop()

    if pic == 100:
        image = ("./Pictures/")+str(pic)+str(".png")
        msg = ("The 99 Names of Allah\n\n")+str("Name number ")+str(pic)
        choices = ["Previous","Begin", "Exit"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Previous":
            pic = pic -2
            Main_loop()
        elif reply == "Begin":
            pic = 1
            start()
        elif reply == "Exit":
            sys.exit(0)
        elif reply == None:
            sys.exit(0)
        else:
            Main_loop()

def start():
    global pic
    pic = 1
    image = ("./Pictures/")+str(pic)+str(".png")
    msg = ("The 99 Names of Allah\n\n")+str("Name number ")+str(pic)
    choices = ["Next"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Next":
        Main_loop()
    elif reply == None:
        sys.exit(0)
    else:
        Main_loop()

start()