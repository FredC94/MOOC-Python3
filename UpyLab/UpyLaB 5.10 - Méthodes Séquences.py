""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction dupliques qui reçoit une séquence en paramètre.

    La fonction doit renvoyer la valeur booléenne True si la séquence passée en paramètre contient des éléments dupliqués
    et la valeur booléenne False sinon.

Exemples:
    dupliques([1, 2, 3, 4]) doit retourner: False
    dupliques(['a', 'b', 'c', 'a']) doit retourner: True
    dupliques('abcda') doit retourner: True

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction dupliques.

    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.

    Il n'est pas demandé que la fonction teste le type de l'argument passé ; vous pouvez supposer qu'il sera valide.
"""

def dupliques(seq):
    for elem in seq:
        if seq.count(elem) > 1:
            return True
    return False


dupliques(['a', 'b', 'c', 'a'])
dupliques(['a', 'b', 'c'])
