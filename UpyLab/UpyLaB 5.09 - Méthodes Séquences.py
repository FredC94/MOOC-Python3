""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True si les mots v et w sont des anagrammes.

Exemples:
    anagrammes('marion', 'romina')doit retourner: True
    anagrammes('bonjour', 'jour')doit retourner: False
    anagrammes('pate', 'patte')doit retourner: False

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction anagrammes. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Votre code ne doit pas tester si les mots existent bien dans un quelconque dictionnaire.

    Pour simplifier, on supposera que tout mot est une anagramme de lui-même (par exemple, anagrammes('jour', 'jour') renvoie True),
    et on ne considèrera que des mots écrits en minuscule.
    Par ailleurs, il n’est pas demandé que votre fonction teste si les mots sont recensés dans un dictionnaire quelconque.
"""

def anagrammes(v, w):
    if len(v) != len(w):
        return False
    liste_1 = sorted(v)
    liste_2 = sorted(w)
    if liste_1 == liste_2:
        return True
    else:
        return False

anagrammes('chien', 'niche')
