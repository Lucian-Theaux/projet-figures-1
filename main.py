
#* Projet réalisé par :
#* Roméo HUYNH
#* Lucian THÉAUX 
#* Nathan EUDELIN

#* Ici nous importons les librairies Python importantes pour le programmes, donc NSI_UI pour l'interface interactive et Turtle pour la partie graphique et dessin
from nsi_ui import *
from turtle import *
from math import *

#* ------------------- PROGRAMMES DE ROMÉO HUYNH ------------------- *#

def The_Cat():                  #On commence la définition de la fonction qui dessine "The_Cat"             
    speed(get_int(speed_turtle))
    metric = get_int(metric_slider) #On précise que metric est une variable globale
    
    up()                        #On lève le crayon pour ne pas dessiner en se déplaçant
    goto(400-metric*2.5,400-metric*2)                   #On déplace la tortue à la position (0,metric)
    down()                      #On baisse le crayon pour dessiner
    
    fillcolor("black")          #On choisit la couleur de remplissage
    begin_fill()                #On commence le remplissage
    setheading(180)             #On oriente la tortue vers la gauche
    circle(metric,90)                #On dessine un quart de cercle de rayon metric
    setheading(0)               #On oriente la tortue vers la droite
    fd(metric*2+metric*(1/1.8))                     #On avance de manière proportionnelle 
    circle(metric,90)                #On dessine un quart de cercle de rayon metric
    end_fill()                  #On termine le remplissage de cette partie
    begin_fill()
    circle(metric,90)
    fd(metric*2+metric*(1/1.8))
    setheading(270)             #On oriente la tortue vers le bas
    circle(metric,90)
    fd(metric*2)
    end_fill()
    backward((metric*3)-(1.5*metric))     #On recule (plus simple qu de faire setheading(180) et fd) de la longueur du chat (3foismetric) moins la longueur de la tête (1.3foismetric)
    setheading(90)
    # """Ici on dessine la tête du chat"""
    begin_fill()
    fd(metric*2.3)                   #ici on avance de 2.3fois metric pour la hauteur de la tête + de la partie supérieur du corps qui vaut metric de hauteur
    left(90)
    circle((1/3)*(metric*1.5),90)    #On dessine une oreille proportionelle (1/3 de la largeur de la tête)
    right(90)
    fd((1/3)*(metric*1.5))           #On avance de la largeur entre les oreilles (1/3 de la largeur de la tête)
    right(90)
    circle((1/3)*(metric*1.5),90)    #Deuxième oreille
    left(90)
    fd(metric*1.3)    
    end_fill()                  #On termine le remplissage de la tête

def The_perroquet():             #On commence la définition de la fonction qui dessine "The_perroquet"
    speed(get_int(speed_turtle))
    metric = get_int(metric_slider)                 #On précise que metric est une variable globale
    metric2=metric*(3.35/2)                    #Création d'une deumetricième variable metric2 pour que le perroquet ait un taille proportionelle au chat
    
    up()
    goto(-400+metric2*2,-400)       #On déplace la tortue à la position (-(metric2),0)
    down()
    
    fillcolor("black")
    """on commence la forme principale du perroquet en noir (le corps/l'ombre/le derrière en noir)"""
    begin_fill()
    setheading (90)
    circle(metric2,90)
    setheading(180)
    setheading(0)
    fd(metric2)
    setheading(90)
    circle(metric2,270)
    fd(metric2)
    end_fill()
    """On dessine la partie blanche du perroquet (=les yeumetric)"""
    backward(metric2)
    setheading(90)
    fd((metric2)*2)
    setheading(180)
    fillcolor("white")          #On change la couleur de remplissage en blanc pour les yeux
    begin_fill()
    circle((metric2)/2,180)          #On dessine un demi cercle pour l'œil gauche 2fois plus petit que la taille du cercle du corps noir du perroquet
    end_fill()
    setheading(90)
    fd((metric2)/2+(metric2/7))           #Une fois la partie blanche de l'œil dessinée, on avance pour se placer au bon endroit pour dessiner la pupille noir
    fillcolor("black")          #On remet la couleur de remplissage en noir pour la pupille
    begin_fill()
    circle((metric2)/7)              #On dessine la pupille grâce à un cercle que l'on va remplir (+facile circle que dot pour l'emplacement du début de tracage)
    end_fill()

def The_Snake():                          #On commence la définition de la fonction qui dessine "The_Snake"
    speed(get_int(speed_turtle))             
    metric = get_int(metric_slider) 
    metric3=metric*(3.35/4)               #Création d'une troisième variable metric3 pour que le serpent ait un taille proportionelle à la hauteur du chat
    metricy=0                        #Variable pour le déplacement horizontal du serpent
    orientation_cercle1=180     #Variables pour l'orientation des cercles (180° soit l'orientation vers la gauche)
    orientation_cercle2=0                        #On initialise orentation_cercle2 qui représente 0° soit l'orientation vers la droite
    sens_cercle1=metric*(3.35/4)               #Rayon des cercles du serpent, variable pour l'instant égale à metric3 mais qui va representer l'opposé de metric3 lors du deumetricieme passage dans la boucle
    sens_cercle2=metric                        #Rayon des yeumetric du serpent, variable pour l'instant égale à metric mais qui va representer l'opposé de metric lors du deumetricieme passage dans la boucle
    
    up()                                    #On lève le crayon pour ne pas dessiner en se déplaçant
    goto(400-metric*2.5,-400)                   #On déplace la tortue à la position (0,metric)
    down()  
    
    for i in range(2):          #On fait une boucle pour dessiner les deumetric serpents (gauche et droite)
        fillcolor("black")
        """On commence à desssiner Le serpent de gauche"""
        begin_fill()
        setheading(90)
        fd(metric3)                  #On avance de metric3 pour se placer au bon endroit pour dessiner le premier quart de cercle
        setheading(orientation_cercle1)          #On oriente la tortue vers la gauche ou la droite en fonction de la valeur de orientation_cercle1
        circle(sens_cercle1,90)           #On dessine un quart de cercle de rayon sens_cercle1
        setheading(orientation_cercle2)          #On oriente la tortue vers la droite ou la gauche en fonction de la valeur de orientation_cercle2
        fd(metric3)
        circle(sens_cercle1,180)
        setheading(90)
        fd(metric3)
        setheading(orientation_cercle1)
        circle(sens_cercle1,180)
        setheading(90)
        fd(metric3)
        setheading(orientation_cercle2)
        circle(sens_cercle1,180)
        fd(metric3)
        setheading(270)
        circle(sens_cercle1,90)
        end_fill()
        setheading(90)
        fd((metric)*(6/10))          #On avance pour se placer au bon endroit pour dessiner les yeux
        fillcolor("white")
        """Dans cette partie on dessine les yeux du serpent"""
        begin_fill()
        circle(sens_cercle2*(1/10))       #On dessine le cercle blanc de l'œil avec un rayon proportionelle au rayon de la tête du serpent
        end_fill()
        """!Partie très importante de la fonction The_Snake! Ici on inverse les variables pour dessiner le serpent de droite de façon symétrique au serpent de gauche"""
        variable_tampon=orientation_cercle1                 #On utilise une variable temporaire variable_tampon pour échanger les valeurs de orientation_cercle1 et orientation_cercle2 (elle prend la valeur de orientation_cercle1)
        orientation_cercle1=orientation_cercle2             #orientation_cercle1 prend la valeur de orientation_cercle2
        orientation_cercle2=variable_tampon                 #orientation_cercle2 prend la valeur de varaible_tampon(donc la valeur initiale de orientation_cercle1)
        sens_cercle1=-sens_cercle1                  #On inverse le signe de sens_cercle1 pour que les cercles soient dessinés dans l'autre sens(antihoraire/horraire)
        sens_cercle2=-sens_cercle2                  #On inverse le signe de sens_cercle2 pour que les yeux(=cercle) soient dessinés dans l'autre sens(antihoraire/horraire)
        
        up()
        setheading(0)
        fd(metric3)
        right(90)
        fd((metric3*3)+((metric)*(6/10)))
        left(90)
        fd(metric3)
        down()
    
    fillcolor('black')                 


#* ------------------- PROGRAMMES DE NATHAN EUDELIN ------------------- *#

def crocodile():                #Définition de la fonction crocodile pour se comprendre que le code du crocodile est le suivant
    metric = 1.3*(get_int(metric_slider)) 
    speed(get_int(speed_turtle))

    up()                                        #On lève le crayon pour ne pas dessiner en se déplaçant
    goto(-400+metric*2.5,400-metric*2.5)                   #On déplace la tortue à la position (0,metric)
    down() 

    setheading(0)
    fillcolor()
    begin_fill()                #On commence le remplissage
    backward(metric*2.81)        #On commence a dessiner le contour
    left(90)
    right(45)
    forward(metric*1.91)
    left(135)
    forward(metric*1.36)
    right(90)
    forward(metric*0.35)
    right(90)
    forward(metric*1.71)
    left(135)
    forward(metric*0.48)
    for i in range(4):          #Création d'une boucle pour les dents du crocodile
        left(135)
        forward(metric*0.33)
        right(135)
        forward(metric*0.48)
    right(45)
    forward(metric*0.33)
    right(90)
    forward(metric*1.37)
    right(90)
    circle(metric*0.34,-180)
    up()
    right(90)
    backward(metric*0.68)
    forward(metric*0.17)
    down()
    left(90)
    circle(metric*-0.17,360)
    up()
    right(90)
    forward(metric*0.5)
    left(180)
    down()
    circle(metric*0.33,-90)
    right(135)
    forward(metric*0.48)
    right(135)
    for i in range(5):
        forward(metric*0.33)
        left(135)
        forward(metric*0.49)
        right(135)
    end_fill()

def lion():         #Définition de la fonction lion pour se comprendre que le code du lion est le suivant
    metric = 1.3*(get_int(metric_slider))
    speed(get_int(speed_turtle))

    up()
    goto(-(metric*1.6), 400-metric*2.5)
    down()

    setheading(0)
    begin_fill()                #On commence le remplissage
    forward(metric*0.73)        #On commence a dessiner le contour
    left(135)
    forward(metric*1.02)
    left(135)
    forward(metric*0.73)
    left(90)
    end_fill()                  #On arrête le remplissage pour éviter les bugs de couleurs
    up()                        #On lève le stylo pour ne pas impacter l'image final
    forward(metric*2.02)
    down()
    begin_fill()
    forward(metric*0.73)
    left(90)
    forward(metric*0.73)
    left(135)
    forward(metric*1.02)
    right(45)
    end_fill()
    up()
    forward(metric*0.67)
    down()
    begin_fill()       #J'ouvre un nouveau remplissage, le défi était vraiment de jongler entre lever/poser le stylo et ouvrir/fermer le remplissage 
    right(45)
    forward(metric*1.96)
    right(45)
    forward(metric*0.35)
    right(135)
    forward(metric*0.5)
    left(45)
    forward(metric*0.36)
    right(90)
    forward(metric*0.68)
    left(90)
    forward(metric*0.33)
    left(45)
    forward(metric*0.98)
    left(135)
    forward(metric*0.71)
    left(135)
    forward(metric*0.98)
    left(45)
    forward(metric*0.33)
    left(90)
    forward(metric*0.68)
    right(90)
    forward(metric*0.36)
    left(45)
    forward(metric*0.5)
    right(135)
    forward(metric*0.35)
    right(45)
    forward(metric*1.96)
    end_fill()
    up()
    right(90)
    forward(metric*1.96)
    right(45)
    forward(metric*1.38)
    down()
    begin_fill()
    right(90)
    forward(metric*0.73)
    right(135)
    forward(metric*1.01)
    right(135)
    forward(metric*0.73)
    right(90)
    end_fill()
    up()
    forward(metric*2.04)
    down()
    begin_fill()
    forward(metric*0.73)
    right(90)
    forward(metric*0.73)
    right(135)
    forward(metric*1.01)
    end_fill()
    up()
    left(135)
    forward(metric*1.04)
    down()
    begin_fill()
    right(135)
    forward(metric*0.51)
    right(135)
    forward(metric*0.71)
    right(135)
    forward(metric*0.51)
    end_fill()
    up()
    right(45)
    forward(metric*1.37)
    down()
    begin_fill()
    right(45)
    forward(metric*0.51)
    right(135)
    forward(metric*0.71)
    right(135)
    forward(metric*0.51)
    end_fill()                  #On arrête le remplissage 

def loup():             #Définition de la fonction loup pour se comprendre que le code du loup est le suivant
    metric = 1.3*(get_int(metric_slider))
    speed(get_int(speed_turtle))
    
    up()
    goto(-(metric*1.5), (metric/2))
    down()

    setheading(0)
    fillcolor()             #On choisi la couleur de base: le noir      
    begin_fill()            #On commence le remplissage 
    backward(metric*0.34)       #On commence à dessiner les contours
    left(90)
    forward(metric*1.04)
    left(225)
    forward(metric*0.98)
    left(135)
    forward(metric*0.69)
    right(135)
    forward(metric*1.45)
    left(45)
    forward(metric*1.03)
    left(90)
    circle(metric*1.02,-90)
    right(45)
    forward(metric*0.98)
    right(135)
    forward(metric*2.4)
    right(90)
    forward(metric*0.7)
    right(45)
    forward(metric*0.47)
    left(135)
    forward(metric*0.34)
    right(135)
    forward(metric*0.47)
    left(135)
    forward(metric*0.34)
    right(135)
    forward(metric*0.47)
    up()                    #Je lève le stylo pour ne pas impacter l'image finale et éviter les anomalies 
    right(45)
    forward(metric*0.86) 
    down() 
    circle(metric*-0.17,360)                #Je dessine un cercle pour l'oeil du loup 
    end_fill()                              #Je ferme le remplissage car sinon il y a des problèmes avec les couleurs 
    up()
    forward(metric*1.2)
    left(90)
    forward(metric*0.33)
    down()
    begin_fill()
    circle(metric*0.35,90)
    right(180)
    circle(metric*0.35,90)
    left(180)
    circle(metric*0.35,90)
    left(180)
    circle(metric*0.35,90)
    end_fill()                                  #Fin du remplissage global


#* ------------------- PROGRAMMES DE LUCIAN THÉAUX ------------------- *#

def maison():
    metric = 1.5*(get_int(metric_slider)) #! Définition de la métrique nommée 'metric'
    speed(get_int(speed_turtle))          #! Définition de la vitesse de la tortue avec le slider se trouvant sur la fenêtre de nsi_ui

    up()
    goto(-(metric*1.3), -400)             #* On déplace la maison à son emplacement en bas au centre 
    down()

    setheading(0)                         #* On oriente la tête vers la droite

    begin_fill()                          #* La tortue crée la partie basse avec une boucle for créant 4 piques
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
                                        
    up()                                  #* On déplace la tortue vers la partie haute 
    forward(metric*1.9)
    circle(metric*0.32, 90)
    forward(metric*1.6)
    circle(metric*0.32, 90)
    down()

    begin_fill()                          #* La tortue crée la partie haute avec une boucle for créant 4 piques orienté vers la bas
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

    up()                                   #* La tortue se positionne sur la premiere pique de la partie basse
    forward(metric*1.85)
    circle(metric*0.32, 90)
    forward(metric*1.6)
    left(135)
    forward(metric*0.45)
    right(45)
    down()

    for i in range(3):                     #* La tortue crée une répétition de 3 piques pour créer un sapin 
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
    
    up()                                   #* La tortue se déplace vers la dernière pique de la partie basse
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
    forward(metric*0.63)
    right(90)
    forward(metric*0.31)
    end_fill()

    up()
    right(90)
    forward(metric*0.64)
    right(90)
    forward(metric*0.15)
    left(90)
    down()

    begin_fill()
    circle(metric*0.15,90)
    right(180)
    circle(metric*0.15,90)
    left(180)
    circle(metric*0.15,90)
    left(180)
    circle(metric*0.15,90)
    end_fill()

    up()
    circle(metric*0.15,-90)
    left(180)
    forward(metric*0.32)
    left(90)
    down()

    begin_fill()
    circle(metric*0.15,90)
    right(180)
    circle(metric*0.15,90)
    left(180)
    circle(metric*0.15,90)
    left(180)
    circle(metric*0.15,90)
    end_fill()

    up()
    left(90)
    forward(metric*0.31)
    down()

    begin_fill()
    circle(metric*0.15,90)
    right(180)
    circle(metric*0.15,90)
    left(180)
    circle(metric*0.15,90)
    left(180)
    circle(metric*0.15,90)
    end_fill()

    up()
    left(180)
    forward(metric*0.62)
    left(90)
    forward(metric*0.79)
    down()

    begin_fill()
    circle(metric*0.31, 180)
    left(90)
    forward(metric*0.16)
    right(90)
    circle(metric*0.15, -180)
    right(90)
    forward(metric*0.16)
    end_fill()

    left(180)
    forward(metric*1.2)
    right(90)

    begin_fill()
    circle(metric*0.31, 180)
    left(90)
    forward(metric*0.16)
    right(90)
    circle(metric*0.15, -180)
    right(90)
    forward(metric*0.16)
    end_fill()

def hirondelle():
    metric = 1.5*(get_int(metric_slider))
    speed(get_int(speed_turtle))

    up()
    goto(-380, -(metric))
    down()


    setheading(0)
    fillcolor('black')
    begin_fill()
    forward(metric*1.3)
    left(116)
    forward(metric*0.71)
    right(117)
    forward(metric*0.94)
    left(117)
    forward(metric*1.4)
    left(63)
    forward(metric*0.31)
    left(117)
    forward(metric*0.71)
    right(117)
    forward(metric*0.32)
    right(62)
    forward(metric*0.70)
    left(126)
    forward(metric*0.70)
    right(63)
    forward(metric*0.31)
    right(118)
    forward(metric*0.70)
    left(117)
    forward(metric*0.31)
    left(63)
    forward(metric*1.4)
    left(117)
    forward(metric*0.94)
    right(118)
    forward(metric*0.71)
    end_fill()

    up()
    left(117)
    forward(metric*0.60)
    left(90)
    forward(metric*1.95)
    down()

    begin_fill()
    circle(metric*0.3, 90)
    left(90)
    circle(metric*0.3, 180)
    left(90)
    circle(metric*0.3, 90)
    end_fill()

    up()
    left(180)
    forward(metric*0.25)
    down()

    begin_fill()
    circle(metric*0.3, 90)
    left(90)
    circle(metric*0.3, 180)
    left(90)
    circle(metric*0.3, 90)
    end_fill()

def poissons():
    metric = 1.5*(get_int(metric_slider))
    speed(get_int(speed_turtle))

    up()
    goto(400-metric*2, (metric/1.5))
    down()

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

def all_animals():
    crocodile()
    lion()
    The_Cat()
    hirondelle()
    loup()
    poissons()
    The_perroquet()
    maison()
    The_Snake()


title('Projet - n°1 | Animaux')
setup(900,900)


begin_vertical()
label('Roméo HUYNH')
begin_horizontal()
button('Crocodile', crocodile)
button('Lion', lion)
button('Chat', The_Cat)
end_horizontal()
label('Nathan EUDELIN')
begin_horizontal()
button('Hirondelle', hirondelle)
button('Loup', loup)
button('Poissons', poissons)
end_horizontal()
label('Lucian THÉAUX')
begin_horizontal()
button('Perroquet', The_perroquet)
button('Maison', maison)
button('Serpents', The_Snake)
end_horizontal()
metric_slider = slider('Métrique', 0, 100)
speed_turtle = slider('Vitesse', 0, 10)
begin_horizontal()
button('Effacer', clearscreen)
button('One-shot', all_animals)
end_horizontal()
end_vertical()

mainloop()
