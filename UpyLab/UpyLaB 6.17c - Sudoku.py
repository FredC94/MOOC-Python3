""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
  Écrire une fonction check_regions qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie
  si toutes les régions sont valides (c’est-à-dire que dans chaque région, chaque chiffre apparaît une et une seule fois).

Consignes:
  Dans cet exercice, le code que vous soumettez à UpyLaB doit comporter uniquement la définition de la fonction check_regions,
  et ne fait en particulier aucun appel à input ou à print.

  Vous pourrez supposer que la grille passée en paramètre est valide.

  La fonction ne doit pas modifier la grille passée en paramètre.
"""

def check_regions(grid):
  for ligne in range(0, 9, 3):
    for colonne in range(0, 9, 3):
      liste = []
      for l in range(ligne, ligne + 3):
        for c in range(colonne, colonne + 3): 
          liste.append(grid[l][c])
      if sum(liste) != 45:
      # On peut aussi comparer la longueur de la liste (contenant potentiellement des objets dupliqués)...
      # ...à la longeur de l'ensemble de la liste (pas d'objets dupliqués dans un ensemble)
      # if len(liste) != len(set(liste)):
        return False
  return True

print(check_regions([[6, 9, 3, 1, 7, 4, 2, 5, 8], # doit retourner False, mais marche pas
                    [1, 7, 8, 3, 2, 5, 6, 4, 9], 
                    [2, 5, 4, 6, 8, 9, 7, 3, 1], 
                    [8, 2, 1, 4, 3, 7, 5, 9, 6], 
                    [4, 9, 6, 8, 5, 2, 3, 1, 7], 
                    [7, 3, 5, 9, 6, 1, 8, 2, 4], 
                    [5, 8, 9, 7, 1, 3, 4, 6, 2], 
                    [3, 1, 7, 2, 4, 6, 9, 8, 5], 
                    [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

print(check_regions([[1, 2, 3, 4, 5, 6, 7, 8, 9], # retourne False
                  [2, 3, 4, 5, 6, 7, 8, 9, 1],
                  [3, 4, 5, 6, 7, 8, 9, 1, 2],
                  [4, 5, 6, 7, 8, 9, 1, 2, 3],
                  [5, 6, 7, 8, 9, 1, 2, 3, 4],
                  [6, 7, 8, 9, 1, 2, 3, 4, 5],
                  [7, 8, 9, 1, 2, 3, 4, 5, 6],
                  [8, 9, 1, 2, 3, 4, 5, 6, 7],
                  [9, 1, 2, 3, 4, 5, 6, 7, 8]]))
                  
print(check_regions([[9, 6, 3, 1, 7, 4, 2, 5, 8], # retourne True
                    [1, 7, 8, 3, 2, 5, 6, 4, 9],
                  [2, 5, 4, 6, 8, 9, 7, 3, 1],
                  [8, 2, 1, 4, 3, 7, 5, 9, 6],
                  [4, 9, 6, 8, 5, 2, 3, 1, 7],
                  [7, 3, 5, 9, 6, 1, 8, 2, 4],
                  [5, 8, 9, 7, 1, 3, 4, 6, 2],
                  [3, 1, 7, 2, 4, 6, 9, 8, 5],
                  [6, 4, 2, 5, 9, 8, 1, 7, 3]]))

