""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros et 1 euro.

    Écrire une fonction rendre_monnaie qui reçoit en paramètre un entier prix et cinq valeurs entières x20, x10, x5, x2 et x1,
    qui représentent le nombre de billets ou de pièces de chaque valeur que donne un client pour l’achat d’un objet dont le prix est mentionné.

    La fonction doit renvoyer cinq valeurs, représentant le nombre de billets et pièces de chaque sorte qu’il faut rendre au client,
    dans le même ordre que précédemment. Cette décomposition doit être faite en rendant le plus possible de billets et pièces de grosses valeurs.

    Si la somme d’argent avancée par le client n’est pas suffisante pour effectuer l’achat, la fonction retournera cinq valeurs None.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction rendre_monnaie. Le code que vous soumettez à UpyLaB doit donc comporter
    uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de votre fonction avec le bon nombre de paramètres. 
    Si la fonction existe bien, UpyLaB testera votre fonction : il ajoutera des appels à votre fonction pour vérifier que celle-ci
    n'effectue aucun print. Ensuite différents tests de votre fonction seront effectués par UpyLaB.

    Il n’est pas demandé que la fonction rendre_monnaie teste le type des paramètres reçus.

    On suppose qu’il y a toujours suffisamment de billets et pièces de chaque sorte.

    Pour retourner cinq valeurs, on pourra utiliser l’instruction return res20, res10, res5, res2, res1.
    Cela renvoie un tuple de cinq valeurs (apparaissant entre parenthèses lorsqu’on l’affiche). 
"""

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    liste_valeur_billet = (20, 10, 5, 2, 1)
    n = len(liste_valeur_billet)
    somme = x20 * 20 + x10 * 10 + x5 * 5 + x2 * 2 + x1 * 1
    reste = somme - prix
    if somme <= prix:
        res20 = None
        res10 = None
        res5 = None
        res2 = None
        res1 = None
    else:
        res20 = reste // 20
        reste -= res20 * 20
        res10 = reste // 10
        reste -= res10 * 10
        res5 = reste // 5
        reste -= res5 * 5
        res2 = reste // 2
        reste -= res2 * 2
        res1 = reste // 1
    return res20, res10, res5, res2, res1


print(rendre_monnaie(52, 2, 2, 2, 3, 3))


rendre_monnaie(80, 2, 2, 2, 3, 3)
#doit retourner :
(None, None, None, None, None)

