""" Auteur: Frédéric Castel
    Date : Mars 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui lit en entrée deux nombres entiers strictement positifs, et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.
    Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.

Consignes:
    Notez qu’il n’est pas demandé de vérifier que les deux nombres en entrée sont strictement positifs. 
    Vous pouvez supposer que ce sera le cas pour toutes les entrées proposées par UpyLaB lors des tests.

    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) 
    par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res) par exemple).
"""

nbr1 = int(input())
nbr2 = int(input())
if nbr1 % nbr2 == 0:
    print("False")
elif nbr1 < nbr2:
    print("False")
else:
    print("True")
