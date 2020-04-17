# Auteur: Frédéric CASTEL (Mars/Avril 2020)
"""
Exercices:
Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs triée par ordre croissant
et comme deuxième paramètre un entier relatif n, et qui renvoie une liste correspondant à la liste reçue,
mais dans laquelle le nombre n a été inséré à la bonne place.

Consignes:
La liste donnée en paramètre ne doit pas être modifiée par votre fonction.
Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers,
mais si le deuxième paramètre n’est pas du bon type, la fonction retourne None.
"""


def my_insert(entier, nb):
    if type(nb) == int:
        liste = list(entier)
        liste.append(nb)
        liste.sort()
        return liste
    else:
        return None


my_insert([1, 3, 5], 1.5)
my_insert([1, 5, 78], -1)
my_insert([1, 3, 5], 4)
