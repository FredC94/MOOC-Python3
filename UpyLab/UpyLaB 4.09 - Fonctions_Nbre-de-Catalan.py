""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    En mathématiques, et plus particulièrement en combinatoire, les nombres de Catalan forment une suite d’entiers naturels
    utilisée dans divers problèmes de dénombrement.

    Ils sont nommés ainsi en l’honneur du mathématicien belge Eugène Charles Catalan (1814-1894).

    Les dix premiers nombres de Catalan (pour n de 0 à 9) sont : 
        1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862.

    Le nombre de Catalan d’indice n, appelé n-ième nombre de Catalan, est défini par : c(n)= (2n)! / (n+1)! * n!
    
    Nous vous demandons d’écrire une fonction catalan(n), où n est un nombre entier positif ou nul,
    qui renvoie la valeur du  n-ième nombre de Catalan.    

Exemples:
    catalan(5) doit retourner 42 
    catalan(0) doit retourner 1

Consignes:
    Il n’est pas demandé que la fonction catalan teste le type du paramètre reçu.
    
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de paramètres.
    Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction pour vérifier que celle-ci n'effectue
    aucun print. Ensuite différents tests de votre fonction seront effectués par UpyLaB.

    Votre fonction doit renvoyer une valeur entière.

    Rappelons aussi que si une fonction est demandée, UpyLaB va tester à la fois que les résultats envoyés par cette fonction
    sont corrects et qu’ils ont le bon type.
"""

from math import factorial


def catalan(n):
    res = factorial(2 * n) / (factorial(n + 1) * factorial(n))
    return int(res)


print(catalan(5))
