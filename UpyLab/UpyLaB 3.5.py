#Écrire un programme qui lit en entrée deux nombres entiers strictement positifs
#et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.

nbr1 = int(input())
nbr2 = int(input())
if nbr1 % nbr2 == 0:
    print("False")
elif nbr1 < nbr2:
    print("False")
else:
    print("True")
