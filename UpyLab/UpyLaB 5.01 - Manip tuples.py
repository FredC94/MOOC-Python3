""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction signature qui reçoit un paramètre identite. Ce paramètre est un couple (tuple de deux composantes)
    dont la première composante représente un nom et la seconde un prénom.

    Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace.

Exemples:
    signature(('de Saint-Exupéry', 'Antoine')) doit retourner : 'Antoine de Saint-Exupéry'

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction signature. Le code que vous soumettez à UpyLaB doit donc comporter
    uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Vous pouvez supposer que l’argument passé à la fonction est valide (couple de deux chaînes de caractères).
"""

def signature(identite):
    res = identite[-1] + " " + identite[0]
    return res


print(signature(('Hoarau', 'Sébastien')))

