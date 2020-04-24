""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction alea_dice(s) qui génère trois nombres (pseudo) aléatoires à l’aide de la fonction randint du module random,
    représentant trois dés (à six faces avec les valeurs de 1 à 6), et qui renvoie la valeur booléenne True si les dés forment un 421,
    et la valeur booléenne False sinon.

    Le paramètre s de la fonction est un nombre entier, qui sera passé en argument à la fonction random.seed au début du code de la fonction.
    Cela permettra de générer la même suite de nombres aléatoires à chaque appel de la fonction, et ainsi de pouvoir tester son fonctionnement.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction alea_dice. Le code que vous soumettez à UpyLaB doit donc comporter uniquement
    la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.
    
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de paramètres.
    Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction pour vérifier que celle-ci
    n'effectue aucun print. Ensuite différents tests de votre fonction seront effectués par UpyLaB.

    Il n’est pas demandé que la fonction alea_dice teste le type du paramètre reçu.

    N’importe quelle combinaison de trois dés permettant de former le nombre 421 sera acceptée, quel que soit l’ordre de la combinaison.
    Par exemple, les tirages 2, 4, 1 forment bien 421.

    La première instruction de la fonction, après l’import du module random, sera random.seed(s).

    On rappelle que la fonction randint(a, b) retourne un nombre (pseudo) aléatoire compris entre les bornes a et b incluses.
"""

import random

def alea_dice(s):
    random.seed(s)
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    if dice1 in (4, 2, 1) and dice2 in (4, 2, 1) and dice3 in (4, 2, 1):
        # ou if dice1 + dice2 + dice3 == 7
        return True
    else:
        return False

print(alea_dice(25))


"""
Exemple 1
alea_dice(1)

doit retourner :
False

Exemple 2
alea_dice(25)

doit retourner :
True
"""