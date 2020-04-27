def histogram(s):
    """Renvoie le dictionnaire des lettres dans s
       avec leur fréquence."""
    d = {}
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def invert_dict(d):
    """Renvoie le dictionnaire inversé de d."""
    inv = {}
    for k in d:
        val = d[k]
        if val not in inv:
            inv[val] = [k]
        else:
            inv[val].append(k)
    return inv

d = histogram('evenement')
inv_d = invert_dict(d)
print(inv_d)   # imprime {1: ['m', 't', 'v'], 2: ['n'], 4: ['e']}