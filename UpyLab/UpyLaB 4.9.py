"""
Nous vous demandons d’écrire une fonction catalan(n),
où n est un nombre entier positif ou nul,
qui renvoie la valeur du n-ième nombre de Catalan.
c(n)= (2n)! / (n+1)! * n!
"""
from math import factorial


def catalan(n):
    res = factorial(2 * n) / (factorial(n + 1) * factorial(n))
    return int(res)


print(catalan(5))
