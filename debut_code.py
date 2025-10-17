from nsi_ui import*
from turtle import*

setup(1000,800)
speed(0)
title("Projet de Roméo!!")

def The_Cat():
    up()
    goto(0,0)
    down()
    global Champ_taille
    x=100
    begin_fill()
    setheading(180)
    circle(x,90)
    setheading(0)
    fd(x*2)
    circle(x,90)
    end_fill()
    begin_fill()
    circle(x,90)
    fd(x*2)
    setheading(270)
    circle(x,90)
    fd(x*2)
    end_fill()
    backward((x*3)-(1.3*x))
    setheading(90)
    begin_fill()
    fd(x*2.3)
    setheading(180)
    circle((1/3)*(x*1.3),90)
    setheading(180)
    fd((1/3)*(x*1.3))
    setheading(90)
    circle((1/3)*(x*1.3),90)
    setheading(270)
    fd(x*1.3)    
    end_fill()
    hideturtle()


def The_peroquet():
    up()
    goto(0,0)
    down()
    global Champ_taille
    x=100   
    begin_fill()


def figure2():
    backward(50)
button("Chat", The_Cat)
button("Peroquet", The_peroquet)
Champ_taille=entry("La taille de la figure: ")


mainloop()