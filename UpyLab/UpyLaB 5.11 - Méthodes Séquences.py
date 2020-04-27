""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.

    On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots.
    Par exemple, l’intersection de « programme » et « grammaire » est « gramm ».

    Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.

    Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v.
    Par exemple, intersection('bbaacc', 'aabb') renvoie 'bb'.

Exemples:
    intersection('programme', 'grammaire') doit retourner: 'gramm'
    intersection('salut', 'merci') doit retourner: ''
    intersection('merci', 'adieu') doit retourner: 'e'

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction intersection.

    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.
"""

def intersection(v, w):
    len_v = len(v)
    # print('### ', v, w)
    for size in range(len_v, 0, -1):
        # print(' -- Par taille', size)
        for i in range(len_v - size + 1):
            extrait = v[i:i + size]
            # print('   - Extrait', extrait)
            if extrait in w:
                return extrait
    return ''


intersection('programme', 'grammaire')
