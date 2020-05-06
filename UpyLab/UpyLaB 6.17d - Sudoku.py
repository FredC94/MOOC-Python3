""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction check_sudoku capable de vérifier si la grille passée en paramètre, sous forme d’une matrice 9 x 9 d’entiers, est une solution au problème du sudoku. La fonction retournera la réponse (True ou False).

    Cette fonction devra utiliser les trois fonctions suivantes (que vous devez aussi définir) :
            check_rows qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie si toutes les lignes sont valides (c’est-à-dire que sur chaque ligne, chaque chiffre apparaît une et une seule fois).

            check_cols qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie si toutes les colonnes sont valides (c’est-à-dire que sur chaque colonne, chaque chiffre apparaît une et une seule fois).

            check_regions qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie si toutes les régions sont valides (c’est-à-dire que dans chaque région, chaque chiffre apparaît une et une seule fois).

Consignes:
    Dans cet exercice, le code que vous soumettez à UpyLaB doit comporter uniquement la définition des fonctions attendues, et ne fait en particulier aucun appel à input ou à print.

    Vous pourrez supposer que la grille passée en paramètre est valide.

    Aucune des fonctions ne doit modifier la grille passée en paramètre.

    Pour vous aider, nous vous proposons de réaliser au préalable les trois exercices intermédiaires qui vont vous permettre d’écrire et de tester les trois fonctions auxiliaires, avant de les utiliser ici.
"""

def check_sudoku(grid):
    if check_rows(grid) != 45:
        return False
    elif check_cols(grid) != 45:
        return False
    elif check_regions(grid) != 45:
        return False
    else:
        return True

# on retourne la somme des valeurs de chaque rangées
def check_rows(grid):
    for line in grid:
        return sum(line)

# on retourne la somme des valeurs de chaque colonnes
def check_cols(grid):
    for line in range(len(grid)):
        somme = 0
        for col in range(len(grid)):
            somme += int(grid[col][line])
        return somme

# on retourne la somme des valeurs de chaque carrés
def check_regions(grid):
    for ligne in range(0, 9, 3):
            for colonne in range(0, 9, 3):
                liste = []
                for l in range(ligne, ligne + 3):
                    for c in range(colonne, colonne + 3): 
                        liste.append(grid[l][c])
            return sum(liste)


print(check_sudoku([[1, 6, 3, 1, 7, 4, 2, 5, 8], # doit retourner False
                    [9, 7, 8, 3, 2, 5, 6, 4, 9], 
                    [2, 5, 4, 6, 8, 9, 7, 3, 1], 
                    [8, 2, 1, 4, 3, 7, 5, 9, 6], 
                    [4, 9, 6, 8, 5, 2, 3, 1, 7], 
                    [7, 3, 5, 9, 6, 1, 8, 2, 4], 
                    [5, 8, 9, 7, 1, 3, 4, 6, 2], 
                    [3, 1, 7, 2, 4, 6, 9, 8, 5], 
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]))


print(check_sudoku([[6, 9, 3, 1, 7, 4, 2, 5, 8], # doit retourner False
                    [1, 7, 8, 3, 2, 5, 6, 4, 9], 
                    [2, 5, 4, 6, 8, 9, 7, 3, 1], 
                    [8, 2, 1, 4, 3, 7, 5, 9, 6], 
                    [4, 9, 6, 8, 5, 2, 3, 1, 7], 
                    [7, 3, 5, 9, 6, 1, 8, 2, 4], 
                    [5, 8, 9, 7, 1, 3, 4, 6, 2], 
                    [3, 1, 7, 2, 4, 6, 9, 8, 5], 
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

print(check_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9], # doit retourner False
                    [2, 3, 4, 5, 6, 7, 8, 9, 1],
                    [3, 4, 5, 6, 7, 8, 9, 1, 2],
                    [4, 5, 6, 7, 8, 9, 1, 2, 3],
                    [5, 6, 7, 8, 9, 1, 2, 3, 4],
                    [6, 7, 8, 9, 1, 2, 3, 4, 5],
                    [7, 8, 9, 1, 2, 3, 4, 5, 6],
                    [8, 9, 1, 2, 3, 4, 5, 6, 7],
                    [9, 1, 2, 3, 4, 5, 6, 7, 8]]))

print(check_sudoku([[9, 6, 3, 1, 7, 4, 2, 5, 8], # doit retourner True
                    [1, 7, 8, 3, 2, 5, 6, 4, 9],
                    [2, 5, 4, 6, 8, 9, 7, 3, 1],
                    [8, 2, 1, 4, 3, 7, 5, 9, 6],
                    [4, 9, 6, 8, 5, 2, 3, 1, 7],
                    [7, 3, 5, 9, 6, 1, 8, 2, 4],
                    [5, 8, 9, 7, 1, 3, 4, 6, 2],
                    [3, 1, 7, 2, 4, 6, 9, 8, 5],
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]))




