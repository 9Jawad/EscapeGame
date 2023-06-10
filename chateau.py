"""
Projet 2, Escape Game
Auteur : Jawad Cherkaoui
Date : 7 novembre 2022
Entrée : les flèches du clavier
Sorties : affichage du labyrinthe (le plan)
But : Un petit jeu du type jeu d’évasion (escape game)
      dans lequel le joueur commande au clavier les déplacements
      d’un personnage au sein d’un « château » représenté en plan.
      Le château est constitué de cases vides (pièces, couloirs),
      de murs, de portes, que le personnage ne pourra franchir qu’en répondant
      à des questions, d’objets à ramasser, qui l’aideront à trouver les réponses
      à ces questions et de la case de sortie / quête du château.
      Le but du jeu est d’atteindre cette dernière.
"""

import CONFIGS as cfg  # importation d'un fichier python
import turtle as t     # importation du module graphique


DECALAGE_OBJET = 20
DECALAGE_TEXTE = 25
DECALAGE_CERCLE = 0.5


# PARTIE 1 : Affichage du Labyrinthe -----------------------------------------------------------------------------------

def lire_matrice(fichier):
    """
    Entrée : Fichier texte du plan du chateau
    sortie : Matrice
    but : Transforme le fichier du plan du chateau en une matrice (liste de liste).
    """
    with open(fichier) as f:
        matrice = [[int(colonne) for colonne in ligne.split()] for ligne in f]
        return matrice


def calculer_pas(matrice):
    """
    Entrée : Matrice
    sortie : Pas
    but : Calcule la dimension à donner aux cases pour que le plan
          tienne dans la zone de la fenêtre turtle que nous avons définie.
    """
    lignes = len(matrice)
    col = len(matrice[0])
    x = abs(cfg.ZONE_PLAN_MINI[0] - cfg.ZONE_PLAN_MAXI[0])  # calcul du delta x
    y = abs(cfg.ZONE_PLAN_MINI[1] - cfg.ZONE_PLAN_MAXI[1])  # calcul du delta y
    pas = min((x / col), (y / lignes))
    return pas


def coordonnees(case, pas):
    """
    Entrées : Case (tuple d'un élément de la matrice), pas
    sorti : Dimension d'un carré
    but : Calcule les coordonnées en pixels turtle du coin inférieur gauche d’une case définie par ses coordonnées.
    """
    lignes = len(open(cfg.fichier_plan).readlines())
    x, y = case[0], case[1]
    dimension = (cfg.ZONE_PLAN_MINI[0] + (y * pas)), \
                (cfg.ZONE_PLAN_MINI[0] + ((lignes - x) * pas))
    return dimension


def tracer_carre(dimension):
    """
    Entrée : Dimension d'un carré
    sorti : /
    but : Trace un carré dans le module graphique dont la dimension en pixels turtle est donnée en argument.
    """
    pas = calculer_pas(lire_matrice(cfg.fichier_plan))
    t.pencolor(cfg.COULEUR_CASES)
    t.penup()
    t.goto(dimension)  # va à la position indiquer
    t.pendown()
    for i in range(4):  # trace un carré
        t.forward(pas)
        t.left(360 / 4)


def tracer_case(case, couleur, pas):
    """
    Entrées : Case, couleur, pas
    sortie : /
    but : Tracer un carré d’une certaine couleur et taille à un certain endroit dans le module graphique.
    """
    t.color(couleur)  # attribution d'une couleur
    t.begin_fill()  # commence le remplissage
    tracer_carre(coordonnees(case, pas))  # appel à la fonction "coordonnees()"
    t.end_fill()  # fin du remplissage


def afficher_plan(matrice):
    """
    Entrée : Matrice
    sortie : /
    bur :  Pour chaque élément ligne/colonne de la matrice de cet élément ligne,
           tracer une case à l’emplacement correspondant, dans une couleur correspondant à ce que dit la matrice.
    """
    pas = calculer_pas(matrice)
    couleur = None
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            case = (i, j)
            carct = matrice[i][j]  # valeur d'un élément de la matrice selon sa ligne et sa cologne
            if carct == 0:                 # selon la valeur de l'élément de la matrice, une couleur est attribuée
                couleur = cfg.COULEURS[0]
            elif carct == 1:
                couleur = cfg.COULEURS[1]
            elif carct == 2:
                couleur = cfg.COULEURS[2]
            elif carct == 3:
                couleur = cfg.COULEURS[3]
            elif carct == 4:
                couleur = cfg.COULEURS[4]
            t.hideturtle()
            t.tracer(0)     # fonction utilisée pour activer ou désactiver l'animation
            tracer_case(case, couleur, pas)
            t.update()      # affiche le plan du chateau élément par élément
    t.getcanvas().postscript(file="chateau.eps")  # crée un fichier canvas du plan du chateau


# PARTIE 2 : Gestion du déplacement dans le chateau --------------------------------------------------------------------


def deplacer_gauche():
    """
    Entrée : /
    Sortie : /
    But : Déclenche le traitement requis chaque fois que la touche clavier correspondante est enfoncée.
    """
    t.onkeypress(None, "Left")  # Désactive la touche Left
    mouvement = (0, -1)  # traitement associé à la flèche gauche appuyée par le joueur
    global position_dep, matrice_dep
    deplacer(matrice_dep, position_dep, mouvement)
    t.onkeypress(deplacer_gauche, "Left")  # Réassocie la touche Left à la fonction "deplacer_gauche()"


def deplacer_droite():
    """
    Entrée : /
    Sortie : /
    But : Déclenche le traitement requis chaque fois que la touche clavier correspondante est enfoncée.
    """
    t.onkeypress(None, "Right")
    mouvement = (0, 1)
    global position_dep, matrice_dep
    deplacer(matrice_dep, position_dep, mouvement)
    t.onkeypress(deplacer_droite, "Right")


def deplacer_haut():
    """
    Entrée : /
    Sortie : /
    But : Déclenche le traitement requis chaque fois que la touche clavier correspondante est enfoncée.
    """
    t.onkeypress(None, "Up")
    mouvement = (-1, 0)
    global position_dep, matrice_dep
    deplacer(matrice_dep, position_dep, mouvement)
    t.onkeypress(deplacer_haut, "Up")


def deplacer_bas():
    """
    Entrée : /
    Sortie : /
    But : Déclenche le traitement requis chaque fois que la touche clavier correspondante est enfoncée.
    """
    t.onkeypress(None, "Down")
    mouvement = (1, 0)
    global position_dep, matrice_dep
    deplacer(matrice_dep, position_dep, mouvement)
    t.onkeypress(deplacer_bas, "Down")


def creer_dictionnaire_des_objets(fichier_des_objets):
    """
    Entrée : Fichier texte
    Sortie : Dictionnaire
    But : Transforme un fichier texte en dictionnaire.
    """
    fichier = open(fichier_des_objets, encoding='utf-8')
    dico = {}
    for lignes in fichier:
        lignes = lignes.strip()
        a, b = eval(lignes)     # transforme ici la chaîne de caractère en tuple
        dico[a] = b             # associe la variable "a" (clé du dictionnaire)
    return dico                 # à la valeur de la variable "b"


def ramasser_objet(matrice, position, mouvement):
    """
    Entrée : Matrice, position, mouvement
    Sortie : /
    But : Faire disparaître l'objet de la case (à la fois dans le plan et à l’affichage),
          qui devra donc prendre la couleur des cases vides.
          Le personnage avancera sur la case demandée.
          Une annonce du type « Vous avez trouvé : objet en question »
          s’affichera dans le bandeau d’affichage des annonces.
          L’objet s’ajoutera à l’inventaire des objets collectés affiché dans la colonne d’affichage de l’inventaire.
    """
    global position_dep, matrice_dep, position_inv
    dico_objets = creer_dictionnaire_des_objets(cfg.fichier_objets)
    tracer_case(position, cfg.COULEUR_VUE, calculer_pas(matrice))   # case de l'ancienne position change de couleur
    deplacement = position[0] + mouvement[0], position[1] + mouvement[1]    # calcule le déplacement
    position_dep = deplacement                                              # à partir du mouvement et de la position
    matrice_dep[deplacement[0]][deplacement[1]] = 0
    tracer_case(deplacement, cfg.COULEUR_CASES, calculer_pas(matrice))   # case de l'objet
                                                                         # prend la couleur d'une case vide
    # affichage du personnage après le déplacement :
    t.penup()
    t.goto(coordonnees((deplacement[0] - DECALAGE_CERCLE, deplacement[1] + DECALAGE_CERCLE), calculer_pas(matrice)))
    t.pendown()
    t.dot(calculer_pas(matrice) * cfg.RATIO_PERSONNAGE, cfg.COULEUR_PERSONNAGE)

    # affichage d'un objet dans l'inventaire :
    t.penup()
    position_inv = (position_inv[0], position_inv[1] - DECALAGE_OBJET)
    t.goto(position_inv)
    t.pendown()
    t.color('black')
    t.write(dico_objets[deplacement], font=('Arial', 10, 'bold'))

    # affichage d'un objet dans l'annonce :
    annonce.clear()
    annonce.penup()
    annonce.goto(cfg.POINT_AFFICHAGE_ANNONCES[0], cfg.POINT_AFFICHAGE_ANNONCES[1] - DECALAGE_TEXTE)
    annonce.pendown()
    annonce.color('black')
    annonce.write("Vous avez trouvé un objet : " + dico_objets[deplacement], font=('Arial', 17, 'bold'))


def poser_question(matrice, case, mouvement):
    """
    Entrée : Matrice, case, mouvement
    Sortie : /
    But : Pose au joueur la question correspondant à l’emplacement de la porte et le joueur saisie sa réponse.
          Si la réponse est bonne, remplacer la porte par une case vide,
          + afficher dans le bandeau d’annonce que la porte s’ouvre et avancer le personnage.
          Si la réponse est mauvaise, l'annoncer et ne pas déplacer le personnage.
    """
    global position_dep, matrice_dep
    # affichage dans l'annonce que la porte est fermée :
    annonce.clear()
    annonce.penup()
    annonce.goto(cfg.POINT_AFFICHAGE_ANNONCES[0], cfg.POINT_AFFICHAGE_ANNONCES[1] - DECALAGE_TEXTE)
    annonce.pendown()
    annonce.color('black')
    annonce.write("Cette porte est fermée.", font=('Arial', 17, 'bold'))

    position = case

    deplacement = position[0] + mouvement[0], position[1] + mouvement[1]    # calcule le déplacement
    dico_portes = creer_dictionnaire_des_objets(cfg.fichier_questions)      # à partir du mouvement et de la position
    reponse = t.textinput("Question", dico_portes[deplacement][0])     # poser une question et retient la réponse
    t.listen()

    if reponse == dico_portes[deplacement][1]:     # vérifie que la réponse donnée est correcte
        matrice_dep[deplacement[0]][deplacement[1]] = 0
        tracer_case(position, cfg.COULEUR_VUE, calculer_pas(matrice))
        position_dep = deplacement      # retient la nouvelle position
        tracer_case(deplacement, cfg.COULEUR_CASES, calculer_pas(matrice))

        # affichage du personnage dans la case du déplacement :
        t.penup()
        t.goto(coordonnees((deplacement[0] - DECALAGE_CERCLE, deplacement[1] + DECALAGE_CERCLE), calculer_pas(matrice)))
        t.pendown()
        t.dot(calculer_pas(matrice) * cfg.RATIO_PERSONNAGE, cfg.COULEUR_PERSONNAGE)

        # affichage dans l'annonce que la porte s'ouvre :
        annonce.clear()
        annonce.penup()
        annonce.goto(cfg.POINT_AFFICHAGE_ANNONCES[0], cfg.POINT_AFFICHAGE_ANNONCES[1] - DECALAGE_TEXTE)
        annonce.pendown()
        annonce.color('black')
        annonce.write("La porte s'ouvre !", font=('Arial', 17, 'bold'))

    else:
        # affichage dans l'annonce que la réponse donnée est incorrect :
        annonce.clear()
        annonce.penup()
        annonce.goto(cfg.POINT_AFFICHAGE_ANNONCES[0], cfg.POINT_AFFICHAGE_ANNONCES[1] - DECALAGE_TEXTE)
        annonce.pendown()
        annonce.color('black')
        annonce.write("Mauvaise réponse", font=('Arial', 17, 'bold'))


def deplacer(matrice, position, mouvement):
    """
    Entrée : Matrice, position, mouvement
    Sortie : /
    But : Avance le personnage seulement si le déplacement ne mène pas vers un mur,
          si le déplacement mène vers un objet, la fonction "ramasser_objets()" est appelé,
          si le déplacement mène vers une porte, la fonction "poser_question()" est appelé,
    """
    global position_dep
    deplacement = position[0] + mouvement[0], position[1] + mouvement[1]

    if matrice[deplacement[0]][deplacement[1]] == 0:        # vérifie que le déplacement mène vers une case vide
        tracer_case(position, cfg.COULEUR_VUE, calculer_pas(matrice))

        # affichage du personnage dans la case du déplacement :
        position_dep = deplacement      # retient la nouvelle position
        t.penup()
        t.goto(coordonnees((deplacement[0] - DECALAGE_CERCLE, deplacement[1] + DECALAGE_CERCLE), calculer_pas(matrice)))
        t.pendown()
        t.dot(calculer_pas(matrice) * cfg.RATIO_PERSONNAGE, cfg.COULEUR_PERSONNAGE)

    elif matrice[deplacement[0]][deplacement[1]] == 3:      # vérifie que le déplacement mène vers une porte
        poser_question(matrice, position, mouvement)

    elif matrice[deplacement[0]][deplacement[1]] == 4:      # vérifie que le déplacement mène vers un objet
        ramasser_objet(matrice, position, mouvement)

    elif matrice[deplacement[0]][deplacement[1]] == 2:      # vérifie que le déplacement mène vers la sortie

        # désaffectation des touches, car fin du jeu :
        t.onkeypress(None, "Up")
        t.onkeypress(None, "Down")
        t.onkeypress(None, "Right")
        t.onkeypress(None, "Left")

        tracer_case(position, cfg.COULEUR_VUE, calculer_pas(matrice))
        position_dep = deplacement
        tracer_case(deplacement, cfg.COULEUR_CASES, calculer_pas(matrice))

        # affichage du personnage dans la case du déplacement :
        t.penup()
        t.goto(coordonnees((deplacement[0] - DECALAGE_CERCLE, deplacement[1] + DECALAGE_CERCLE), calculer_pas(matrice)))
        t.pendown()
        t.dot(calculer_pas(matrice) * cfg.RATIO_PERSONNAGE, cfg.COULEUR_PERSONNAGE)

        # affichage dans l'annonce que le jeu est terminé :
        annonce.clear()
        annonce.penup()
        annonce.goto(cfg.POINT_AFFICHAGE_ANNONCES[0], cfg.POINT_AFFICHAGE_ANNONCES[1] - DECALAGE_TEXTE)
        annonce.pendown()
        annonce.color('black')
        annonce.write("Bravo ! Vous avez gagné.", font=('Arial', 25, 'bold'))
        t.done()


# PARTIE 3 : Corps du code ---------------------------------------------------------------------------------------------


# appel de la fonction "afficher_plan()"
afficher_plan(lire_matrice(cfg.fichier_plan))

# valeur global :
position_dep = cfg.POSITION_DEPART
matrice_dep = lire_matrice(cfg.fichier_plan)
position_inv = (cfg.POINT_AFFICHAGE_INVENTAIRE[0], cfg.POINT_AFFICHAGE_INVENTAIRE[1] - DECALAGE_TEXTE)

# Utilisation d'un second turtle :
annonce = t.Turtle()    # permet d'utiliser la fonction "turtle.clear()" sur une partie du code

# Affichage du personnage  en debut de jeu :
t.penup()
t.goto(coordonnees((position_dep[0] - DECALAGE_CERCLE, position_dep[1] + DECALAGE_CERCLE),
                   calculer_pas(lire_matrice(cfg.fichier_plan))))
t.pendown()
t.dot(calculer_pas(lire_matrice(cfg.fichier_plan)) * cfg.RATIO_PERSONNAGE, cfg.COULEUR_PERSONNAGE)

# Affichage de l'annonce en début de jeu :
annonce.clear()
annonce.penup()
annonce.goto(cfg.POINT_AFFICHAGE_ANNONCES[0], cfg.POINT_AFFICHAGE_ANNONCES[1] - DECALAGE_TEXTE)
annonce.pendown()
annonce.color('black')
annonce.write("Vous devez mener le point rouge jusqu'à la sortie jaune.", font=('Arial', 17, 'bold'))

# Affichage de l'inventaire en début de jeu :
t.penup()
t.goto(position_inv)
t.pendown()
t.color('black')
t.write("Inventaire: ", font=('Arial', 15, 'bold'))


t.listen()  # Déclenche l’écoute du clavier
t.onkeypress(deplacer_gauche, "Left")  # Associe à la touche Left une fonction appelée "deplacer_gauche()"
t.onkeypress(deplacer_droite, "Right")
t.onkeypress(deplacer_haut, "Up")
t.onkeypress(deplacer_bas, "Down")
t.mainloop()  # Place le programme en position d’attente d’une action du joueur
