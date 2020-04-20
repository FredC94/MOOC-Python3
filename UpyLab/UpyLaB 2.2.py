""" Auteur: Frédéric Castel
    Date : Mars 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui imprime (donc grâce à la fonction print) la moyenne arithmétique de deux nombres
    de type float lus en entrée (c'est-à-dire grâce à des appels à la fonction input) .
    On rappelle que la moyenne arithmétique de deux nombres a et b est égale à {a+b}/{2}.

Consignes
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.

    En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non float(input("Entrer un nombre : ")) par exemple),
    ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res) par exemple).
"""
a = float(input())
b = float(input())
res = (a + b) / 2
print(res)