""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    On considère une liste qui décrit une séquence t. Chaque élément de cette liste est un tuple de deux composantes :
    le nombre de répétitions successives de l’élément x dans la séquence t, et l’élément x lui-même.

    Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".

    Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme
    d’une nouvelle liste.

Exemples:
    decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
    doit retourner: [1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction decompresse.
    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.

    Essayez d’utiliser une compréhension de liste pour cet exercice.
"""

def decompresse(t):
    liste = []
    x = 0
    for y in range(len(t)):
        for i in range(t[x][0]):
            liste.append(t[x][1])
        x = x + 1
    return liste


decompresse([(4, 1), (2, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
# [1, 1, 1, 1, 2, 2, 'test', 'test', 3, 3, 3, 'bonjour']
