""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    On représente un brin d’ADN par une chaîne de caractères dont les caractères sont parmi les quatre suivants :
    'A' (Adénine), 'C' (Cytosine), 'G' (Guanine) et 'T' (Thymine).

    Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui retourne True si cette chaîne de caractères
    n'est pas vide et peut représenter un brin d’ADN, False sinon.

Exemples:
    est_adn("ATGGT") doit retourner: True
    est_adn("ISA") doit retourner: False
    est_adn("CTaG") doit retourner: False

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction est_adn. Le code que vous soumettez à UpyLaB doit donc comporter
    uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Vous pouvez supposer que l’argument passé à la fonction sera toujours une chaîne de caractères ;
    notez que l'appel de la fonction sur une chaîne vide doit retourner False .
"""

def est_adn(adn):
    liste = ["A", "C", "G", "T"]
    liste_adn = list(adn)  # je split l'argument pour pouvoir boucler sur chacun des termes et/
    # et vérifier si il est présent dans la liste
    if len(liste_adn) == 0:
        return False
    for c in liste_adn:
        if c not in liste:
            return False
    return True


est_adn('')
