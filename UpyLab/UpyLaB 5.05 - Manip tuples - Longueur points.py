""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction longueur(*points) qui reçoit en paramètres un nombre arbitraire de points (tuples de deux composantes),
    et retourne la longueur de la ligne brisée correspondante.

    Cette longueur se calcule en additionnant les longueurs des segments formés par deux points consécutifs.

Exemples:
    longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)) doit retourner :2.0
    longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)) doit retourner (approximativement) :7.1122677042334645

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction longueur. Le code que vous soumettez à UpyLaB doit donc comporter
    uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Pour simplifier, on supposera qu’il y aura toujours au moins deux points passés en paramètre lors des appels à la fonction longueur.

    Il est conseillé d’utiliser la fonction distance_points définie lors de l’exercice précédent.
"""

from math import sqrt


def longueur(*points):
    def distance_points(point1, point2):
        x1, y1 = point1
        x2, y2 = point2

        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    i = 1
    long = 0
    while len(points) > i:
        long = long + distance_points(points[i - 1], points[i])
        i = i + 1
    return long

print(longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)))
