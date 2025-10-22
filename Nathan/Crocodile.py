from nsi_ui import *
from turtle import *
from math import *

def crocodile(cote):
    fillcolor()
    begin_fill()
    backward(cote*2.81)
    left(90)
    right(45)
    forward(cote*1.91)
    left(135)
    forward(cote*1.36)
    right(90)
    forward(cote*0.35)
    right(90)
    forward(cote*1.71)
    left(135)
    forward(cote*0.48)
    for i in range(4):
        left(135)
        forward(cote*0.33)
        right(135)
        forward(cote*0.48)
    right(45)
    forward(cote*0.33)
    right(90)
    forward(cote*1.37)
    right(90)
    circle(cote*0.34,-180)
    up()
    right(90)
    backward(cote*0.68)
    forward(cote*0.17)
    down()
    left(90)
    circle(cote*-0.17,360)
    up()
    right(90)
    forward(cote*0.5)
    left(180)
    down()
    circle(cote*0.33,-90)
    right(135)
    forward(cote*0.48)
    right(135)
    for i in range(5):
        forward(cote*0.33)
        left(135)
        forward(cote*0.49)
        right(135)
    end_fill()
    



crocodile(100)
mainloop()


    