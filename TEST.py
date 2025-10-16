from turtle import*
#bgcolor('Fuchsia')
#fillcolor()
#dot(100)
#up()
#goto(-200,-200)
#down()

#circle(100)
setup(1000,800)
speed(0)

"""Ici on essaye de faire le quadrillage de fond"""
def quadrillage():
    x=-500
    y=400
    carreau_size=0
    carreau_size1=0
    for i in range(17):
        up()
        goto(x,y-carreau_size)
        down()
        goto(-x,y-carreau_size)
        carreau_size=carreau_size+50
    for i in range(21):
        x1=-500
        y1=400
        up()
        goto(x1+carreau_size1,y1)
        down()
        goto(x1+carreau_size1,(-y1))
        carreau_size1=carreau_size1+50
    up()
    goto(-25,-25)
    down()

quadrillage()


def f():
    setheading(90)
    fd(50)


def a():
    setheading(270)
    fd(50)


def b():
    setheading(180)
    fd(50)


def c():
    setheading(0)
    fd(50)


onkey(f, "Up")
onkey(a,"Down")
onkey(b,"Left")
onkey(c,"Right")

listen()
mainloop()