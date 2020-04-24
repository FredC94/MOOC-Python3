""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction distance_points() qui reçoit en paramètres deux tuples de deux composantes représentant les coordonnées de deux points
    et qui retourne la distance euclidienne séparant ces deux points.

    Pour rappel, la distance euclidienne entre les points (x_1, y_1) et (x_2, y_2) se calcule grâce à la formule :
        sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)

    où, si a désigne un nombre positif, \sqrt{a} désigne la racine carrée de a et correspond à a^{\frac{1}{2}}.

Exemples:
    distance_points((1.0, 1.0), (2.0, 1.0)) doit retourner : 1.0
    distance_points((-1.0, 0.5), (2.0, 1.0)) doit retourner (approximativement) : 3.0413812651491097

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction distance_points. Le code que vous soumettez à UpyLaB doit donc comporter
    uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Il n’est pas demandé que la fonction distance_points teste le type des paramètres reçus.
"""

from math import sqrt


def distance_points(x, y):
    # res = sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)
    res = sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    return float(res)


print(distance_points((-4, 3), (3.1, 4.1)))
print(distance_points((-2.0, 2.5), (-1.5, 1.0)))
print(distance_points((1.0, 1.0), (2.0, 1.0)))
print(distance_points((-1.0, 0.5), (2.0, 1.0)))
print(distance_points((-2.5, 1.0), (-1.5, 4.0)))
