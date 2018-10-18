
from turtle import forward, left, right, width, color, clearscreen
from turtle import setx, sety, speed, up, down
from random import randint


def zeichne_flocke(groesse):
    """
    Funktion, wird hier definiert
    und weiter unten verwendet.
    """
    for i in range(6):
        forward(groesse)
        left(60)
        forward(groesse / 2)
        left(180)
        forward(groesse / 2)
        left(60)
        forward(groesse / 2)
        left(180)
        forward(groesse / 2)
        right(120)
        forward(groesse / 2)
        left(180)
        forward(groesse * 1.5)
        left(120)


# Hauptprogramm
clearscreen()
color("lightblue")
width(3)
speed(20)

for i in range(10):
    # Stift an zufällige Position setzen
    up()
    setx(randint(-250, 250))
    sety(randint(-200, 200))
    down()
    # Flocke in zufälliger Größe zeichnen
    groesse = randint(10, 30)
    zeichne_flocke(groesse)

