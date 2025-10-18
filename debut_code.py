from nsi_ui import*
from turtle import*

setup(1000,800)
speed(0)
title("Projet de Roméo!!")

x=100

def The_Cat():
    global x
    up()
    goto(0,0+x)
    down()
    global Champ_taille
    fillcolor("black")
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
    global x
    x2=x*1.5
    up()
    goto(0-x2,0)
    down()
    global Champ_taille  
    fillcolor("black")
    begin_fill()
    setheading (90)
    circle(x2,90)
    setheading(180)
    setheading(0)
    fd(x2)
    setheading(90)
    circle(x2,270)
    fd(x2)
    end_fill()
    backward(x2)
    setheading(90)
    fd((x2)*2)
    setheading(180)
    fillcolor("white")
    begin_fill()
    circle((x2)/2,180)
    end_fill()
    setheading(90)
    fd((x2)/2+(x2/7))
    fillcolor("black")
    begin_fill()
    circle((x2)/7)
    end_fill()






def figure2():
    backward(50)
button("Chat", The_Cat)
button("Peroquet", The_peroquet)
Champ_taille=entry("La taille de la figure: ")


mainloop()
