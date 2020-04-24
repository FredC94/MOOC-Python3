""" Auteur: Frédéric Castel
    Date : Mars 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui lit :
        la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),
        la longueur de l’arête du polyèdre,
    et qui imprime le volume du polyèdre correspondant.

    Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu".

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non float(input("Entrer un nombre : ")) par exemple), 
    ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat:", res) par exemple).
"""

from math import sqrt
lettre = input()
long = float(input())

if lettre == "C":
    print(long ** 3)
elif lettre == "T":
    print((sqrt(2) * (long ** 3)) / 12)
elif lettre == "O":
    print((sqrt(2) * (long ** 3)) / 3)
elif lettre == "D":
    print(((15 + (7 * sqrt(5))) * (long ** 3)) / 4)
elif lettre == "I":
    print(((5 * (3 + sqrt(5))) * (long ** 3)) / 12)
else:
    print("Polyèdre non connu")



