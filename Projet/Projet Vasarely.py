""" Auteur: Frédéric Castel 
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Enoncé:
    Il vous est demandé de réaliser un programme en Python produisant des tableaux d’art optique comme représentés
    par les figures sur la page ci-dessous avec différentes couleurs et déformations :
    http://upylab.ulb.ac.be/pub/Galerie_des_oeuvres_session1_2019.html

    Ces tableaux représentent des pavages hexagonaux, vus d’en haut, formés avec des losanges de couleurs différentes, déformés par une boule. 
    Votre programme utilisera le module turtle, présenté au module 2 de ce cours, pour peindre vos tableaux.

Consignes: (extrait)
    Nous travaillons avec des coordonnées et distances telles que manipulées par les différentes fonctions de turtle (up, begin_fill, goto, …). 
    En particulier nous demandons de tracer, avec turtle, la vue de dessus d'une figure en 3 dimensions et donc de manipuler
    tantôt des coordonnées en 3 dimensions sous forme de triplet (x, y, z), tantôt en 2 dimensions sous forme de couple (x, y). 
"""
import turtle
import math

def hexagone(point, longueur, col, centre, rayon):
    """  
* le point point sous forme d’un triple (tuple de trois composantes) donnant la valeur des trois coordonnées 
du centre avant déformation de l’hexagone à peindre,
* la distance (avant déformation) longueur entre le centre et n’importe quel sommet de l’hexagone,
* le tuple col contenant les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les hexagones.
* le point centre sous forme de triple (c_x, c_y, c_z) qui donne le centre de la sphère de déformation,
* le rayon de la sphère de déformation.
"""
inf_gauche = int(input("Point en bas à gauche du cadre: "))
sup_droit = int(input("Point en haut à droite du cadre:  "))
longueur = int(input("Longueur coté de l'hexagone: "))

col1 = str(input("Quelle couleur #1 ? "))
col2 = str(input("Quelle couleur #2 ? "))
col3 = str(input("Quelle couleur #3 ? "))
col = (col1, col2, col3)

c_x = int(input("Coordonnée X du centre du cercle: "))
c_y = int(input("Coordonnée Y du centre du cercle: "))
c_z = int(input("Coordonnée Z du centre du cercle: "))
centre = (c_x, c_y, c_z)  # tuple des 3 coordonnées

rayon = int(input("Rayon du cercle de déformation"))

pavage(inf_gauche, sup_droit, longueur, col, centre, rayon)

def deformation(point, centre, rayon):
    """renvoie le point sans le modifier"""
    return point

def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
