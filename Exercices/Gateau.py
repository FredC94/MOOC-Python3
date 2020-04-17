"""Auteur: Thierry Massart
   Date : 5 décembre 2017
   But du programme : calcule les ingrédients nécessaires
   pour préparer de la mousse au chocolat pour n personnes
   Entrée: n (nombre de personnes)
   Sorties: nombre d'oeufs,
            quantité en gramme de chocolat,
            nombre de sachets de sucre vanillé
"""
n = int(input("nombre de personnes : "))     # entrée: nombre de personnes
print("nombre d'oeufs : ", int(3 * n / 4)) # calcule et affiche les résultats
print("quantité de chocolat en grammes : ", int(100 * n / 4))
print("quantité de sucre_vanillé : ", max(int(n / 4), 1))