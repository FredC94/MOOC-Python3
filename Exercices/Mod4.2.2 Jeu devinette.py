"""
Petit jeu de devinette (version 2)
Auteur: Thierry Massart
Date : 10 octobre 2018
Petit jeu de devinette d'un nombre entier tiré aléatoirement par le programme dans un intervalle donné
Entrée : le nombre proposé par l'utilisateur
Résultat : affiche si le nombre proposé est celui tiré aléatoirement
"""

# importation des modules

import random  # module le tirage des nombres aléatoires

# Définition des constantes globales

VALEUR_MIN = 0  # borne inférieure de l'intervalle
VALEUR_MAX = 5  # borne supérieure de l'intervalle


# Définition des fonctions

def entree_utilisateur(borne_min, borne_max):
    """
    Lecture du nombre entier choisi par l'utilisateur
    dans l'intervalle [borne_min, borne_max]
    Entrées : bornes de l'intervalle
    Résultat : choix de l'utilisateur
    """
    message = "Votre choix de valeur entre {0} et {1} : "
    ok = False  # vrai quand le choix donné est valable
    while not ok:  # répétition tant que le choix n'est pas bon
        choix = int(input(message.format(borne_min, borne_max)))
        ok = (borne_min <= choix and choix <= borne_max)
        if not ok:  # entrée hors de l'intervalle
            print("Hors de l'intervalle ! Donnez une valeur valide")
    return choix


def tirage(borne_min, borne_max):
    """
    Tirage aléatoire d'un entier dans [borne_min, borne_max]
    """
    return random.randint(borne_min, borne_max)


def affichage_resultat(secret, choix_utilisateur):
    """
    Affiche le résultat
    """
    if secret == choix_utilisateur:
        print("gagné !")
    else:
        print("perdu ! La valeur était", secret)


# Code principal

mon_secret = tirage(VALEUR_MIN, VALEUR_MAX)
choix_util = entree_utilisateur(VALEUR_MIN, VALEUR_MAX)
affichage_resultat(mon_secret, choix_util)
