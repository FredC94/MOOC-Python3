""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui lit sur input une valeur naturelle n et qui affiche à l’écran un carré de n caractères X (majuscule) de côté.

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input())et non int(input("Entrer un nombre : ")) par exemple).
    
    Il n’est pas demandé de tester si la valeur n est bien positive ou nulle, vous pouvez supposer que ce sera toujours le cas pour les valeurs transmises par UpyLaB.
"""

nbr = int(input())
lettre = "X"
y = 0
while y != nbr:
    print (nbr * lettre)
    y = y + 1