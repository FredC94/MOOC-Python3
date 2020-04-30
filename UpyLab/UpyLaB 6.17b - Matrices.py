""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction check_cols qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie
    si toutes les colonnes sont valides (c’est-à-dire que sur chaque colonne, chaque chiffre apparaît une et une seule fois).

Consignes:
    Dans cet exercice, le code que vous soumettez à UpyLaB doit comporter uniquement la définition de la fonction check_cols,
    et ne fait en particulier aucun appel à input ou à print.

    Vous pourrez supposer que la grille passée en paramètre est valide.

    La fonction ne doit pas modifier la grille passée en paramètre.
"""

def check_cols(grid):
    for line in range(len(grid)):
        somme = 0
        for col in range(len(grid)):
            somme += int(grid[col][line])
        if somme != 45:
            return False
    return True


check_cols([[9, 6, 3, 1, 7, 4, 2, 5, 8], # retourne True
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 5, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]])

check_cols([[1, 2, 3, 4, 5, 6, 7, 8, 9], # retourne False
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [7, 8, 5, 1, 2, 3, 4, 9, 6],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]])