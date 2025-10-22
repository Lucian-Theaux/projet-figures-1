from nsi_ui import *
from turtle import *
from math import *

def loup(cote):
    fillcolor()          
    begin_fill()
    backward(cote*0.34)
    left(90)
    forward(cote*1.04)
    left(225)
    forward(cote*0.98)
    left(135)
    forward(cote*0.69)
    right(135)
    forward(cote*1.45)
    left(45)
    forward(cote*1.03)
    left(90)
    circle(cote*1.02,-90)
    right(45)
    forward(cote*0.98)
    right(135)
    forward(cote*2.4)
    right(90)
    forward(cote*0.7)
    right(45)
    forward(cote*0.47)
    left(135)
    forward(cote*0.34)
    right(135)
    forward(cote*0.47)
    left(135)
    forward(cote*0.34)
    right(135)
    forward(cote*0.47)
    up()
    right(45)
    forward(cote*0.86) 
    down() 
    circle(cote*-0.17,360) 
    end_fill()
    up()
    forward(cote*1.2)
    left(90)
    forward(cote*0.33)
    down()
    begin_fill()
    circle(cote*0.35,90)
    right(180)
    circle(cote*0.35,90)
    left(180)
    circle(cote*0.35,90)
    left(180)
    circle(cote*0.35,90)
    end_fill()


    
    
    
    
    



   

loup(100)


mainloop()
