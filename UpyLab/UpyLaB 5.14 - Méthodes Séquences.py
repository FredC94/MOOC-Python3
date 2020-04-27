""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Nous pouvons définir la distance entre deux mots de même longueur (c’est-à-dire 
    ayant le même nombre de lettres) mot_1 et mot_2 comme le nombre minimum de fois où 
    il faut modifier une lettre de mot_1 pour obtenir mot_2 (distance de Hamming).

    Par exemple, les mots « lire » et « bise » sont à une distance de 2, puisqu’il faut changer 
    le “l” et le “r” du mot « lire » pour obtenir « bise ».

    Écrire une fonction distance_mots(mot_1, mot_2) qui retourne la distance entre deux mots.

    Vous pouvez supposer que les deux mots sont de même longueur, et sont écrits sans accents.

Exemples:
    distance_mots("lire", "bise") doit retourner: 2
    distance_mots("Python", "Python") doit retourner: 0
    distance_mots("merci", "adieu") doit retourner: 5

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction distance_mots.

    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.  
"""


def distance_mots(mot_1, mot_2):
    res = 0
    for i in range(len(mot_1)):
        if id(mot_1[i]) != id(mot_2[i]):
            res = res + 1
    return res


distance_mots("lire", "bise")