""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui lit une valeur flottante x en entrée et imprime une approximation de sin(x)

    Cette approximation sera obtenue en additionnant successivement les différents termes de la série jusqu’à ce que la valeur du terme
    devienne inférieure (en valeur absolue) à une constante \epsilon que l’on fixera à 10^{-6}.

Consignes:
    Nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et nonfloat(input("Entrer un nombre : "))
    par exemple), ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res) par exemple).

Conseils:
    Dans cet exercice, notre programme doit calculer une approximation du sinus d’un nombre mais il ne faut pas utiliser la fonction sin du module math.
    Pour éviter de calculer explicitement la valeur des factorielles, on pourra chercher à exprimer chacun des termes en fonction du précédent.
    Notez bien que les exposants de x ne sont que les nombres impairs, et que le signe alterne entre + et -. 
"""

from math import factorial

x = float(input())
index = 3  # premier entier
exp = 2  # on commence par le signe +
terme = 10
temp = 0

while abs(terme) > 10e-6:
    terme = ((-1) ** exp) * (((x) ** index) / factorial(index))
    temp = terme + temp
    index = index + 2  # incrément de +2 pour changer l'entier dans la boucle
    exp = exp + 1  # incrément de +1 pour changer de signe à chaque tour de boucle
print(x - temp)