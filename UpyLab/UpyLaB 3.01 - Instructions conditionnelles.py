""" Auteur: Frédéric Castel
    Date : Mars 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur, 
    imprime cette valeur (le programme n’imprime rien dans le cas contraire).

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.

    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) 
    par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat:", res) par exemple).
"""
a = int(input())
b = int(input())
c = int(input())

if a == b :
    print(a)
elif b == c:
    print(b)
elif a == c:
    print(c)
