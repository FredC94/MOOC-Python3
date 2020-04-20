#Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b} (la racine carrée du produit de a par b)
# de deux nombres positifs a et b de type float lus en entrée.
#Si au moins un de ces nombres est strictement négatif, le programme imprime le texte « Erreur ».

import math
a = float(input())
b = float(input())
if a < 0 or b < 0:
    print("Erreur")
else:
    print(math.sqrt(a * b))