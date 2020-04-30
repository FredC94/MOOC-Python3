""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction check_rows(grid) qui prend en paramètre une grille sous forme de matrice à deux dimensions
    et vérifie si toutes les lignes sont valides (c’est-à-dire que sur chaque ligne, chaque chiffre apparaît une et une seule fois).
    
Consignes:
    Dans cet exercice, le code que vous soumettez à UpyLaB doit comporter uniquement la définition de la fonction check_rows,
    et ne fait en particulier aucun appel à input ou à print.

    Vous pourrez supposer que la grille passée en paramètre est valide.

    La fonction ne doit pas modifier la grille passée en paramètre.
"""

def check_rows(grid):
    for line in grid:
        somme = sum(line)
        if somme != 45:
            return False
        else:
            return True

check_rows([[9, 6, 3, 1, 7, 4, 2, 5, 8], # retourne True
            [1, 7, 8, 3, 2, 5, 6, 4, 9],
            [2, 5, 4, 6, 8, 9, 7, 3, 1],
            [8, 2, 1, 4, 3, 7, 5, 9, 6],
            [4, 9, 6, 8, 5, 2, 3, 1, 7],
            [7, 3, 5, 9, 6, 1, 8, 2, 4],
            [5, 8, 9, 7, 1, 3, 4, 6, 2],
            [3, 1, 7, 2, 4, 6, 9, 8, 5],
            [6, 4, 2, 5, 9, 8, 1, 7, 3]])