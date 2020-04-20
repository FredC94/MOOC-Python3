""" Auteur: Frédéric Castel
    Date : Mars 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
   Écrire un programme qui imprime la valeur du volume d’une sphère de rayon r, float lu en entrée.
   On rappelle que le volume d’une sphère de rayon r est donné par la formule : 4/3 * Pi * r^3

Consignes:
   Il n’est pas demandé de tester si la valeur lue en entrée est bien positive ou nulle.

   Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
   En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non float(input("Entrer un nombre : ")) par exemple),
   ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res) par exemple).

"""
import math
r = float(input())
print ((4 / 3) * math.pi * (r ** 3))