"""
Auteur: Frédéric CASTEL
Date : Avril 2020
"""


def distance_mots(mot_1, mot_2):
    res = 0
    for i in range(len(mot_1)):
        if id(mot_1[i]) != id(mot_2[i]):
            res = res + 1
    return res


distance_mots("lire", "bise")