""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui calcule la taille moyenne (en nombre de salariés) des Petites et Moyennes Entreprises de la région.

    Les tailles seront données en entrée, chacune sur sa propre ligne, et la fin des données sera signalée par la valeur sentinelle -1.
    Cette valeur n’est pas à comptabiliser pour le calcul de la moyenne, mais indique que l’ensemble des valeurs a été donné.

    Après l’entrée de cette valeur sentinelle -1, le programme affiche la valeur de la moyenne arithmétique calculée.

    On suppose que la suite des tailles contient toujours au moins un élément avant la valeur sentinelle -1,
    et que toutes ces valeurs sont positives ou nulles.

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.

    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) par exemple), 
    ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat:", res) par exemple).
"""

x = 0
z = 0
den = 0
while x != -1:
    z = z + x
    x = int(input())
    den = den + 1
print(z / (den-1))


