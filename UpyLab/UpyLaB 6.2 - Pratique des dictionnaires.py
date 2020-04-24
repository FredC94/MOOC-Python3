""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Enoncé:
    Écrire une fonction calcul_prix(produits, catalogue) où :
        produits est un dictionnaire contenant, comme clés, les produits souhaités par Monsieur Germain et comme valeurs associées, 
        la quantité désirée de chacun d’entre eux, catalogue est un dictionnaire contenant tous les produits du magasin avec leur prix associé.

    La fonction retourne le montant total des achats de Monsieur Germain.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction calcul_prix. Le code que vous soumettez à UpyLaB 
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Vous pourrez supposer que les arguments passés à la fonction sont du bon type, et que les produits souhaités par Monsieur Germain 
    figurent bien dans le catalogue du magasin.
"""

def calcul_prix(produits, catalogue):
    somme = 0
    for i, p in enumerate(produits):
        somme += produits[p] * catalogue[p]
    return somme


calc = calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
            {"brocoli":1.50, "bouteilles d'eau":1, "bière":2, "savon":2.50, "mouchoirs":0.80})
# doit retourner: 13.0
print(calc)