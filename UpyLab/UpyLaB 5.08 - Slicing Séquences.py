""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb et qui renvoie la liste des
    nb premiers nombres premiers.

    Si le paramètre n’est pas du type attendu, ou ne correspond pas à un nombre entier positif ou nul, la fonction renvoie None.

Exemples:
    prime_numbers(4)doit retourner : [2, 3, 5, 7]
    prime_numbers(-2)doit retourner : None

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement une fonction prime_numbers, et non un programme complet.
    Le code que vous soumettez à UpyLaB ne fait donc en particulier aucun appel à input ou à print. Par contre, il est tout à fait possible,
    voire conseillé, de définir une fonction annexe, qui par exemple ici détermine si le nombre passé en paramètre est premier ou non.
    
    On rappelle qu’un nombre premier est un entier naturel qui possède exactement deux diviseurs distincts et positifs, 1 et lui-même.
"""

def prime_numbers(nb):
    if type(nb) != int or nb < 0:
        liste = None
    else:
        k = 2
        liste = []
        while len(liste) < nb:
            test = True
            for j in range(2, k - 1):
                print(j)
                if k % j == 0:
                    test = False
                    break
            if test:
                liste.append(k)
            k += 1
    return liste


print(prime_numbers(10))
