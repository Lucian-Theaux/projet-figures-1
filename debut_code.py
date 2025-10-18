from nsi_ui import*             #On importe le module nsi_ui qui permet de créer des interfaces graphiques simples
from turtle import*             #On importe le module turtle qui permet de dessiner

setup(1000,800)                 #Ici on set up le fromat de l'écran
speed(0)                        #On définie la vitesse de la tortue à 0 (=elle ne fait pas d'animation, elle trace directement)
title("Projet de Roméo!!")      #On met un titre à la fenêtre
hideturtle()                    #On cache la tortue pour plus l'esthétique (personnellement)

x=100                           #Variable temporaire et global pour la taille des figures

def The_Cat():                  #On commence la définition de la fonction qui dessine "The_Cat"             
    global x                    #On précise que x est une variable globale
    up()                        #On lève le crayon pour ne pas dessiner en se déplaçant
    goto(0,x)                   #On déplace la tortue à la position (0,x)
    down()                      #On baisse le crayon pour dessiner
    fillcolor("black")          #On choisit la couleur de remplissage
    begin_fill()                #On commence le remplissage
    setheading(180)             #On oriente la tortue vers la gauche
    circle(x,90)                #On dessine un quart de cercle de rayon x
    setheading(0)               #On oriente la tortue vers la droite
    fd(x*2)                     #On avance de 2fois x
    circle(x,90)                #On dessine un quart de cercle de rayon x
    end_fill()                  #On termine le remplissage de cette partie
    begin_fill()
    circle(x,90)
    fd(x*2)
    setheading(270)             #On oriente la tortue vers le bas
    circle(x,90)
    fd(x*2)
    end_fill()
    backward((x*3)-(1.3*x))     #On recule (plus simple qu de faire setheading(180) et fd) de la longueur du chat (3foisx) moins la longueur de la tête (1.3foisx)
    setheading(90)
    """Ici on dessine la tête du chat"""
    begin_fill()
    fd(x*2.3)                   #ici on avance de 2.3fois x pour la hauteur de la tête + de la partie supérieur du corps qui vaut x de hauteur
    setheading(180)
    circle((1/3)*(x*1.3),90)    #On dessine une oreille proportionelle (1/3 de la largeur de la tête)
    setheading(180)
    fd((1/3)*(x*1.3))           #On avance de la largeur entre les oreilles (1/3 de la largeur de la tête)
    setheading(90)
    circle((1/3)*(x*1.3),90)    #Deuxième oreille
    setheading(270)
    fd(x*1.3)    
    end_fill()                  #On termine le remplissage de la tête


def The_perroquet():             #On commence la définition de la fonction qui dessine "The_perroquet"
    global x                    #On précise que x est une variable globale
    x2=x*1.5                    #Création d'une deuxième variable x2 pour que le perroquet ait un taille proportionelle au chat
    up()
    goto(-(x2),0)               #On déplace la tortue à la position (-(x2),0)
    down()
    fillcolor("black")
    """on commence la forme principale du perroquet en noir (le corps/l'ombre/le derrière en noir)"""
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
    """On dessine la partie blanche du perroquet (=les yeux)"""
    backward(x2)
    setheading(90)
    fd((x2)*2)
    setheading(180)
    fillcolor("white")          #On change la couleur de remplissage en blanc pour les yeux
    begin_fill()
    circle((x2)/2,180)          #On dessine un demi cercle pour l'œil gauche 2fois plus petit que la taille du cercle du corps noir du perroquet
    end_fill()
    setheading(90)
    fd((x2)/2+(x2/7))           #Une fois la partie blanche de l'œil dessinée, on avance pour se placer au bon endroit pour dessiner la pupille noir
    fillcolor("black")          #On remet la couleur de remplissage en noir pour la pupille
    begin_fill()
    circle((x2)/7)              #On dessine la pupille grâce à un cercle que l'on va remplir (+facile circle que dot pour l'emplacement du début de tracage)
    end_fill()





"""Ici on définit les boutons et l'interface grâce à tkinter via le module nsi_ui"""
button("Chat", The_Cat)                             #Le premier bouton qui dessine le chat
button("Peroquet", The_perroquet)                   #Le deuxième bouton qui dessine le perroquet


mainloop()                                          #Fonction pour garder la fenêtre graphique ouverte 
