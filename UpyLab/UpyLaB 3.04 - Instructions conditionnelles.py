""" Auteur: Frédéric Castel
    Date : Mars 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui teste la parité d’un nombre entier lu sur input et imprime:
    True si le nombre est pair, False dans le cas contraire.

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) 
    par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat:", res) par exemple).
"""

chiffre = int(input())
deux = 2
if chiffre % 2 == 0:
    print("True")
else:
    print("False")