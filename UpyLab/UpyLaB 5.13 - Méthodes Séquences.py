""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    L’exercice est le même que le précédent (5.12), mais ici, si les paramètres ont le type attendu,
    la fonction modifie la liste en place et ne retourne rien. Si les paramètres ne sont pas valides,
    une erreur se produit à l’exécution.

Exemples:
    l = [1, 3, 5]
    my_insert(l, 4)
    print(l)

    doit afficher : [1, 3, 4, 5]

    l = [1, 3, 5]
    my_insert(l, 'a')
    print(l)

    doit provoquer une exception Python, par exemple : AssertionError

Consignes:
    Attention, le code que vous soumettez à UpyLaB ne doit contenir que la définition de la fonction.
    N’y déclarez donc pas de variable l, ni n’y faites d’appel à print comme dans les exemples ci-dessus.

    Pour tester le type des paramètres, vous pouvez utiliser les verbes assert, type ou isinstance.

            l’instruction assert condition laisse continuer l’exécution du code si la condition évaluée est vraie,
            mais provoque une erreur (appelée exception en Python) si la condition est fausse.

            type(v) donne le type de v.

            isinstance(v, typ) teste si v est de type typ. 
"""

def my_insert(liste, nb):
    assert type(nb) == int
    assert type(nb) != str
    liste.append(nb)
    liste.sort()


my_insert([1, 3, 5], 1.5)
my_insert([1, 5, 78], -1)
my_insert([1, 8, 26], a)