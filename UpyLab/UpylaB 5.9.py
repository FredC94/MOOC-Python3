def anagrammes(v, w):
    if len(v) != len(w):
        return False
    liste_1 = sorted(v)
    liste_2 = sorted(w)
    if liste_1 == liste_2:
        return True
    else:
        return False


anagrammes('chien', 'niche')
