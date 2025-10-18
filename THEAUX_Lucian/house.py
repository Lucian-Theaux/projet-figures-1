# coding=utf-8
# from nsi_ui import *

#* Liste de pensée pour plus tard
#? Pourquoi y'a un écart entre le dernier pique du sapin et la pique de haut
#TODO Créer des formules pour calculer


from turtle import *
speed(0)

setup(800,800)

#! Métrique utilisé pour pouvoir adapté la taille du symbol
metric = 30
circle_radius = 0.65

#* Début de la formation du symbol

#* Bas de la figure avec dent
begin_fill()

fd(4*metric)
circle(circle_radius*metric,90)
left(45)
for i in range(4):
    forward(0.93*metric)
    left(90)
    forward(0.93*metric)
    right(90)
setheading(270)
circle(circle_radius*metric,90)
end_fill()

#* Déplacement vers la partie haute 
up()
fd(4*metric)
circle(circle_radius*metric,90)
fd(3.34*metric)
down()

#* Création de la partie haute
begin_fill()
circle(circle_radius*metric,90)
fd(4*metric)
circle(circle_radius*metric,90)
left(45)
for i in range(4):
    forward(0.93*metric)
    left(90)
    forward(0.93*metric)
    right(90)
end_fill()

#* Déplacement vers le premier pique
up()
setheading(90)
circle(circle_radius*metric,90)
fd(4*metric)
circle(circle_radius*metric,90)
fd(3.34*metric)

#* Déplacement vers le haut de la pique avec une orientation vers la droite
left(135)
fd(0.93*metric)
down()

for i in range(3):
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


mainloop()