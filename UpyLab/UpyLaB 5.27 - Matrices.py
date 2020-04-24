""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction symetrie_horizontale(A) qui reçoit une matrice carrée A (de taille {n}\times{n}) et qui renvoie l’image
    de A par symétrie horizontale par rapport à la ligne du milieu : la première ligne devenant la dernière, la seconde,
    l’avant-dernière, etc.

Exemples:
    symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) doit retourner: [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    symetrie_horizontale([['a', 'b'], ['c', 'd']]) doit retourner: [['c', 'd'], ['a', 'b']]
    symetrie_horizontale([]) doit retourner: []

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction symetrie_horizontale. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Vous pourrez supposer que les matrices passées en argument sont bien carrées (même nombre de lignes et de colonnes).
"""

def symetrie_horizontale(A):
    liste = []
    indice = (len(A) - 1)
    if A == []:
        return []
    for i in range(indice, -1, -1):
        liste.append(A[i])
    return liste


symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# doit retourner : [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

