""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction booléenne bonne_planete(diametre) qui reçoit en paramètre un nombre représentant le diamètre, en mètres,
    d'une planète candidate. La fonction retourne la valeur True ou False selon que la planète convient ou non.

    Écrire ensuite un programme qui lit un diamètre depuis l'entrée et affiche 

        la chaîne de caractères "Bonne planète" si le résultat de l'appel à la fonction bonne_planete est True
        la chaîne de caractères "Trop petite" sinon

Exemples:
500 affiche: "Bonne planète"
10 affiche: "Trop petite"

Consignes:
    Dans cet exercice, il vous est demandé d’écrire une fonction, puis un programme appelant cette fonction.
    Notez qu’UpyLaB testera ces deux points, en exécutant le programme entier mais aussi en appelant directement la fonction
    avec les arguments de son choix.

    Nous rappelons que l'aire d'une sphère, solide auquel est assimilée une planète pour les besoins de l'exercice,
    s'obtient par le calcul π * d2 où d désigne le diamètre de la sphère.
"""

import math

def bonne_planete(diametre):
    aire = math.pi * (diametre ** 2)
    if aire >= 50000:
        return True
    else:
        return False

x = int(input())

if bonne_planete(x) == True:
    print("Bonne planète")
else:
    print("Trop petite")

