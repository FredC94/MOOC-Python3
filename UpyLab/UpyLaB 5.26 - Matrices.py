""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Une matrice M = \{m_{ij}\} de taille {n}\times{n} est dite antisymétrique lorsque, pour toute paire d’indices i, j, on a m_{ij} = - m_{ji}.
    Écrire une fonction booléenne antisymetrique(M) qui teste si la matrice M reçue est antisymétrique.

Exemples:
    antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]) doit retourner: True
    antisymetrique([[0, 1], [1, 0]]) doit retourner: False
    antisymetrique([[1, -2], [2, 1]]) doit retourner: False

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction antisymetrique. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Vous pourrez supposer que les matrices passées en argument sont bien carrées (même nombre de lignes et de colonnes).

    On rappelle qu’une fonction booléenne retourne les valeurs True ou False.

    La fonction retourne True pour la matrice vide.
"""

def antisymetrique(M):
    if M == []:
        return True
    MSize = len(M)     # Extract size of M  (defined by number of rows)
    numCols = len(M[0])  # Extract number of columns
    if not (MSize == numCols):  # If M is non-square
        return False
    i = 0
    while i <= (MSize - 1):
        j = 0
        while j <= (MSize - 1):   # for each entry in ith row/column
            # work through the ith row
            if not (M[i][j] == -M[j][i]):
                return False
            j = j + 1
        i = i + 1   # next row/column
    return True  # Nothing was wrong.
            

antisymetrique([[0, 1], [1, 0]])
# doit retourner :False

antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
# doit retourner : True



