""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction print_mat(M) qui reçoit une matrice M en paramètre et affiche son contenu.
    Les éléments d’une même ligne de la matrice seront affichés sur une même ligne, et séparés par une espace,
    les éléments de la ligne suivante étant affichés sur une nouvelle ligne.

Consignes:
    Important : Afin de permettre à UpyLaB de tester votre fonction, votre code contiendra également,
    après le code de la définition de la fonction print_mat, les instructions suivantes :
        ma_matrice = eval(input())
        print_mat(ma_matrice)

    Si la matrice vide [] est passée en argument , la fonction affiche une ligne vide.
    Dans cet exercice, la présence d’espaces en fin de ligne ne sera pas sanctionnée.
    Par contre, veillez à ce qu’il n’y ait pas de ligne supplémentaire.
"""

def print_mat(matrice):
    for liste in matrice:
        res=""
        for elem in liste:
            res = res + str(elem)
        print(res)



ma_matrice = eval(input())  # input: [['H','E','L','L','O'],['W','O','R','L','D']]
print_mat(ma_matrice)

