# from nsi_ui import *
from turtle import *
speed(0)

setup(800,800)

#! Métrique utilisé pour pouvoir adapté la taille du symbol
metric = 50

#* Début de la formation du symbol

begin_fill()

fd(4*metric)
for i in range(metric):
    forward(1)
    left(90/metric)
left(45)
for i in range(4):
    forward(0.93*metric)
    left(90)
    forward(0.93*metric)
    right(90)
setheading(270)
for i in range(metric):
    forward(1)
    left(90/metric)
end_fill()

up()
fd(4*metric)
for i in range(metric):
    forward(1)
    left(90/metric)
fd(3.34*metric)
down()

begin_fill()
for i in range(metric):
    forward(1)
    left(90/metric)
fd(4*metric)
for i in range(metric):
    forward(1)
    left(90/metric)
left(45)
for i in range(4):
    forward(0.93*metric)
    left(90)
    forward(0.93*metric)
    right(90)
end_fill()

up()
setheading(90)
for i in range(metric):
    forward(1)
    left(90/metric)
fd(4*metric)
for i in range(metric):
    forward(1)
    left(90/metric)
fd(3.34*metric)

left(135)
fd(0.93*metric)
down()
setheading(0)

begin_fill()
fd(0.65*metric)
left(135)
forward(0.93*metric)
left(90)
forward(0.93*metric)
left(135)
fd(0.65*metric)
end_fill()

left(90)
fd(0.65*metric)

setheading(0)

begin_fill()
fd(0.65*metric)
left(135)
forward(0.93*metric)
left(90)
forward(0.93*metric)
left(135)
fd(0.65*metric)
end_fill()

left(90)
fd(0.65*metric)

setheading(0)

begin_fill()
fd(0.65*metric)
left(135)
forward(0.93*metric)
left(90)
forward(0.93*metric)
left(135)
fd(0.65*metric)
end_fill()

mainloop()