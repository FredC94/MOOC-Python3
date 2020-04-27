""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction compteur_lettres(texte) qui renvoie un dictionnaire contenant toutes les lettres 
    de l’alphabet associées à leur nombre d’apparition dans texte.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction compteur_lettres.
    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.

    Les clés du dictionnaire seront les lettres de l’alphabet en minuscule. Si le texte contient des 
    majuscules, celles-ci seront comptabilisées comme la lettre minuscule correspondante.

    Le texte passé en paramètre ne comportera aucun caractère accentué.

    Les espaces et autres caractères de ponctuation doivent être ignorés.
"""

def compteur_lettres(texte):
    mon_dict ={}
    mon_dict.update(dict.fromkeys(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 0))

    for c in texte:
        if c.isalpha():
            mon_dict[c.lower()] = mon_dict[c.lower()] + 1
    return mon_dict

# L’appel de la fonction suivant:
compteur_lettres("Dessine-moi un mouton !")

# retourne:
"""
{'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 2,
 'f': 0, 'g': 0, 'h': 0, 'i': 2, 'j': 0,
 'k': 0, 'l': 0, 'm': 2, 'n': 3, 'o': 3,
 'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 1,
 'u': 2, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
 'z': 0}
"""
