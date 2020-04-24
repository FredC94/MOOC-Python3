""" Auteur: Frédéric Castel
    Date : Mars 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b} (la racine carrée du produit de a par b) 
    de deux nombres positifs a et b de type float lus en entrée.

    Si au moins un de ces nombres est strictement négatif, le programme imprime le texte « Erreur ».

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.

    En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non float(input("Entrer un nombre : ")) par exemple), 
    ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat:", res) par exemple).
"""

import math
a = float(input())
b = float(input())
if a < 0 or b < 0:
    print("Erreur")
else:
    print(math.sqrt(a * b))