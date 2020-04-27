""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b,
    et qui renvoie une liste contenant les m premières puissances de b, c’est-à-dire une liste contenant
    les nombres allant de b^0 à b^{m - 1}.

    Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None.

Exemples:
    my_pow(3, 5.0) doit retourner: [1.0, 5.0, 25.0]
    my_pow(3.0, 5.0) doit retourner: None
    my_pow('a', 'b') doit retourner: None

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction my_pow.

    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.
"""

def my_pow(m, b):  # ou m est un entier et b est un float
    if (type(m) != int or type(b) == str) or (m == 1 and type(b) == int):
        return None
    res = [b ** exp for exp in range(0, m)]
    return res


# OK
my_pow(0, 1.9)

# None
my_pow(1, 4)
my_pow('a', 'b')
my_pow(3.0, 5.0)
my_pow(1.0, 5.0)


