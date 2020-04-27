""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
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

def top_3_candidats(moyennes):
    mon_tuple = tuple()
    for cle, valeur in sorted(moyennes.items(), reverse=True, key=lambda x: x[1]):
        mon_tuple += ("%s" % cle,)


top = top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33})

# doit retourner : ('Candidat 6', 'Candidat 5', 'Candidat 2')
print(top)
