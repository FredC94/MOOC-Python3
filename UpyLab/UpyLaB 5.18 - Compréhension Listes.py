""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction my_filter qui reçoit une liste lst et une fonction booléenne f en paramètres et
    renvoie une nouvelle liste constituée des éléments de lst pour lesquels la fonction f renvoie True.

Exemples:
    my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int))
    doit retourner: [666, 42]

    my_filter([-2, 0, 4, -5, -6], lambda x : x < 0)
    doit retourner: [-2, -5, -6]

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_filter.
    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.

    On rappelle qu’une fonction booléenne est une fonction qui retourne True ou False.

    Essayez d’utiliser une compréhension de liste pour cet exercice.
"""


def my_filter(lst, f):
    res = []
    for elem in lst:
        if f(elem):  # if f(elem) == True:
            res.append(elem)
    return res


my_filter(['a', 2, 'toc', 3, '5'], lambda e: isinstance(e, int))
my_filter([-2, 0, 4, -5, -6], lambda x: x < 0)

"""
******** voir également (compréhension de liste) *************

def my_filter(lst, f):
    t = [elem for elem in lst if f(elem) == True]
    return t
"""
