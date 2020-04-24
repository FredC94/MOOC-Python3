""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui lit en entrée une valeur naturelle n et qui affiche à l’écran un triangle supérieur droit formé de X (voir exemples plus bas).

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input())et non int(input("Entrer un nombre : ")) par exemple).

    Il n’est pas demandé de tester si la valeur n est bien positive ou nulle, vous pouvez supposer que ce sera toujours le cas pour les valeurs transmises par UpyLaB.
"""

nbr = int(input())
lettre = "X"
y = 0
z = 0
nbr2 = nbr
print (nbr2 * lettre)
espace = " "
while y != nbr:
#   print ((z * (" ")), nbr2 * lettre)
    print("", nbr2 * lettre, sep=z * espace, end='\n')
    y = y + 1
    z = z + 1
    nbr2 = nbr2 -1


espace = " "
print("", nbr2 * lettre, sep=espace, end='\n')