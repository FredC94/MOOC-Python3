""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs triée par ordre croissant
    et comme deuxième paramètre un entier relatif n, et qui renvoie une liste correspondant à la liste reçue,
    mais dans laquelle le nombre n a été inséré à la bonne place.

    La liste donnée en paramètre ne doit pas être modifiée par votre fonction.

    Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers, mais si le deuxième paramètre
    n’est pas du bon type, la fonction retourne None.

Exemples:
    my_insert([1, 3, 5], 4) doit retourner: [1, 3, 4, 5]
    my_insert([2, 3, 5], 1) doit retourner: [1, 2, 3, 5]
    my_insert([2, 3, 5], 0.5) doit retourner: None

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_insert.

    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.   
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
