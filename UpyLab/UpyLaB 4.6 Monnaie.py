BILLET20 = 20
BILLET10 = 10
BILLET5 = 5
PIECE2 = 2
PIECE1 = 1
def rendre_monnaie(prix, x20, x10, x5, x2, x1):

    somme = x20 * BILLET20 + x10 * BILLET10 + x5 * BILLET5 + x2 * PIECE2 + x1 * PIECE1
    reste = prix - somme
    if prix > somme:
        return None, None, None, None, None
    elif prix == somme:
        return 0, 0, 0, 0, 0
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

##########################################

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

