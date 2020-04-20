# Auteur: Frédéric CASTEL (Mars/Avril 2020)
"""
Exercices:
L’exercice est le même que le précédent(Upylab 5.12), mais ici, si les paramètres ont le type attendu,
la fonction modifie la liste en place et ne retourne rien.

Consignes:
Si les paramètres ne sont pas valides, une erreur se produit à l’exécution.
"""


def my_insert(liste, nb):
    assert type(nb) == int
    assert type(nb) != str
    liste.append(nb)
    liste.sort()


my_insert([1, 3, 5], 1.5)
my_insert([1, 5, 78], -1)
my_insert([1, 8, 26], a)