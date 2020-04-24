""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrivez un code qui lit un nombre entier strictement positif n et affiche sur n lignes une table de multiplication de taille  n x n,
    avec, pour i entre 1 et n,  les n premières valeurs multiples de i strictement positives sur la ième ligne.
    
    Ainsi, les n premiers multiples de 1 strictement positifs (0 non compris) sont affichés sur la première ligne, les n premiers multiples de 2 sur la deuxième, et cætera.

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) par exemple),
    et à afficher précisément le résultat demandé.

    Il n'est pas requis que les nombres soient alignés verticalement. Pour cet exercice, UpyLaB ne tiendra pas compte du nombre d'espaces
    séparant les nombres sur chaque ligne, ni de la présence d'espace en fin de ligne.
"""

X = 1
Y = 1
Z = int(input())
for X in range(1,Z+1):
 while Y <= Z:
  print((X * Y), end=' ')
  Y+=1
 print()
 Y=1