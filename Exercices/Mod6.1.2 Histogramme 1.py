def histogram(s):
    """Renvoie le dictionnaire des lettres dans s avec leur fréquence"""
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

h = histogram('brontosaurus')
print(h)