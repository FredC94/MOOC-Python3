""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction somme(a, b) qui retourne la somme de deux valeurs entières a et b.
    Par défaut, la valeur de a est 0 et la valeur de b est 1.
    
Exemples:
    somme(24, 18) doit retourner: 42
    somme(4) doit retourner: 5
    somme() doit retourner: 1

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction somme. Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de paramètres.
    Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction pour vérifier que
    celle-ci n'effectue aucun print. Ensuite différents tests de votre fonction seront effectués par UpyLaB.

    Il n’est pas demandé que la fonction somme teste le type des paramètres reçus.
"""

def somme(a=0, b=1):
    if b != 1:
        return a + b
    else:
        return a + 1


print(somme())
