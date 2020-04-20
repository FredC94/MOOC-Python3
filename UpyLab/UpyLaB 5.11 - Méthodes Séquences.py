"""
Exercices:
Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.
On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots. Par exemple,
l’intersection de « programme » et « grammaire » est « gramm ».

Consignes:
Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.
Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v.
Par exemple, intersection('bbaacc', 'aabb') renvoie 'bb'.
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
