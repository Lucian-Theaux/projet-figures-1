# coding=utf-8
# from nsi_ui import *

###### * Liste de pensée pour plus tard * ######



from turtle import *
speed(0)

setup(800,800)

#! Constantes à ne pas changer pour maintenir les symbol dans leur bonne forme
circle_radius = 0.65
metric_slider = 100

def maison():
    # metric = get_int(metric_slider)
    global metric_slider
    metric = metric_slider
    setheading(0)

    begin_fill()
    forward(metric*1.9)
    circle(metric*0.32, 90)

    left(45)
    for i in range(4):
        forward(metric*0.44)
        left(90)
        forward(metric*0.44)
        right(90)
    
    left(135)
    circle(metric*0.32, 90)
    end_fill()

    up()
    forward(metric*1.9)
    circle(metric*0.32, 90)
    forward(metric*1.6)
    circle(metric*0.32, 90)
    down()

    begin_fill()
    forward(metric*1.9)
    circle(metric*0.32, 90)

    left(45)
    for i in range(4):
        forward(metric*0.44)
        left(90)
        forward(metric*0.44)
        right(90)
    
    left(135)
    circle(metric*0.32, 90)
    end_fill()

    up()
    forward(metric*1.85)
    circle(metric*0.32, 90)
    forward(metric*1.6)
    left(135)
    forward(metric*0.45)
    right(45)
    down()

    for i in range(3):
        begin_fill()
        forward(metric*0.31)
        left(135)
        forward(metric*0.44)
        left(90)
        forward(metric*0.44)
        left(135)
        forward(metric*0.31)
        end_fill()
        left(90)
        forward(metric*0.32)
        right(90)
    
    up()
    forward(metric*1.87)
    right(90)
    forward(metric*0.96)
    left(90)
    down()

    for i in range(3):
        begin_fill()
        forward(metric*0.31)
        left(135)
        forward(metric*0.44)
        left(90)
        forward(metric*0.44)
        left(135)
        forward(metric*0.31)
        end_fill()
        left(90)
        forward(metric*0.32)
        right(90)
    
    up()
    right(90)
    forward(metric*0.96)
    right(90)
    forward(metric*1.87)
    right(180)
    forward(metric*0.33)
    left(90)
    down()

    begin_fill()
    forward(metric*0.32)
    right(45)
    forward(metric*0.44)
    right(45)
    forward(metric*0.61)
    right(45)
    forward(metric*0.44)
    right(45)
    forward(metric*0.32)
    right(90)
    forward(metric*0.62)
    right(90)
    forward(metric*0.32)
    left(45)
    forward(metric*0.44)
    left(135)
    forward(metric*0.64)
    right(90)
    forward(metric*0.32)
    end_fill()



    


    


    

def hirondelle():
    metric = get_int(metric_slider)
    setheading(0)
    fillcolor('black')
    begin_fill()
    forward(metric*0.60)
    left(116)
    forward(metric*0.34)
    right(117)
    forward(metric*0.46)
    left(117)
    forward(metric*0.67)
    left(63)
    forward(metric*0.15)
    left(117)
    forward(metric*0.34)
    right(117)
    forward(metric*0.16)
    right(62)
    forward(metric*0.32)
    left(126)
    forward(metric*0.32)
    right(63)
    forward(metric*0.16)
    right(118)
    forward(metric*0.34)
    left(117)
    forward(metric*0.15)
    left(63)
    forward(metric*0.67)
    left(117)
    forward(metric*0.46)
    right(117)
    forward(metric*0.34)
    end_fill()

    up()
    left(117)
    forward(metric*0.30)
    left(90)
    forward(metric*0.89)
    down()

    begin_fill()
    circle(metric*0.15, 90)
    left(90)
    circle(metric*0.15, 180)
    left(90)
    circle(metric*0.15, 90)
    end_fill()

    up()
    left(180)
    forward(metric*0.12)
    down()

    begin_fill()
    circle(metric*0.15, 90)
    left(90)
    circle(metric*0.15, 180)
    left(90)
    circle(metric*0.15, 90)
    end_fill()

def poissons():
    metric = get_int(metric_slider)
    setheading(0)

    begin_fill()
    left(90)
    circle(metric*0.63, 90)
    left(90)
    circle(metric*0.63, 90)
    forward(metric*0.63)
    forward(metric*0.32)
    right(90)
    forward(metric*0.32)
    left(90)
    circle(metric*0.32, 90)
    right(90)
    circle(metric*0.63, 90)
    left(90)
    forward(metric*0.63)
    right(90)
    circle(metric*0.32, 90)
    left(90)
    forward(metric*0.32)
    right(90)
    forward(metric*0.32)
    circle(metric*0.63, 90)
    right(90)
    circle(metric*0.63, 90)
    left(90)
    circle(metric*0.63, 90)
    end_fill()

    up()
    setheading(0)
    forward(metric*1.26)
    right(90)
    forward(metric*0.63)
    setheading(180)
    down()

    begin_fill()
    left(90)
    circle(metric*0.63, 90)
    left(90)
    circle(metric*0.63, 90)
    forward(metric*0.63)
    forward(metric*0.32)
    right(90)
    forward(metric*0.32)
    left(90)
    circle(metric*0.32, 90)
    right(90)
    circle(metric*0.63, 90)
    left(90)
    forward(metric*0.63)
    right(90)
    circle(metric*0.32, 90)
    left(90)
    forward(metric*0.32)
    right(90)
    forward(metric*0.32)
    circle(metric*0.63, 90)
    right(90)
    circle(metric*0.63, 90)
    left(90)
    circle(metric*0.63, 90)
    end_fill()

maison()

# button('Hirondelle', hirondelle)
# button('Poissons',poissons)
# button('Maison',maison)
# metric_slider = slider('Metric', 0, 100,)

mainloop()