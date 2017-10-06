from turtle import *

def vorbereiten():
    reset()
    up()
    setx(-200)
    sety(50)
    down()


def kurve(laenge,tiefe):
    if tiefe==1:
        forward(laenge)
    else:
        kurve(laenge*0.25,tiefe-1)
        left(90)
        kurve(laenge*0.25,tiefe-1)
        right(90)
        kurve(laenge*0.25,tiefe-1)
        right(90)
        kurve(laenge*0.5,tiefe-1)
        left(90)
        kurve(laenge*0.25,tiefe-1)
        left(90)
        kurve(laenge*0.25,tiefe-1)
        right(90)
        kurve(laenge*0.25,tiefe-1)

speed('fastest')
vorbereiten()
kurve(400, 3)

