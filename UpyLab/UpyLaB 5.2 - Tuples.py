"""
Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui retourne
True si cette chaîne de caractères n'est pas vide et peut représenter un brin d’ADN, False sinon.
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
