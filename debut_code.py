from nsi_ui import*
from turtle import*

setup(1000,800)
speed(0)


def figure1():
    begin_fill(color)
    fd(50)

def figure2():
    backward(50)

button("figure1", figure1)
slider("figure2", 0,100)
mainloop()