""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction init_mat(m, n) qui construit et renvoie une matrice d’entiers initialisée
    à la matrice nulle et de dimension m x n.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction init_mat.
    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.
"""

def init_mat(a, b):
    matrix = [[0]*b for i in range(a)]
    return matrix

print(init_mat(2, 3))
print(init_mat(4, 2))
# Résultat attendu pour init_mat(2, 3) : [[0, 0, 0], [0, 0, 0]]
# Résultat attendu pour init_mat(4, 2) : [[0, 0], [0, 0], [0, 0], [0, 0]]

############ Pour mémo: Mauvaise matrice Vs Bonne matrice ############
"""
n = 3
mauvaise_mat = [[0]*n]*n # 3 fois la même ligne !
mauvaise_mat[1][1] = 666 # pour checker l'erreur
bonne_mat = [[0]*n for i in range(n)]
bonne_mat[1][1] = 666 # pour checker l'erreur

print(mauvaise_mat) # le print montre l'erreur
print(bonne_mat) # le print montre qu'il n'y a pas d'erreur
"""