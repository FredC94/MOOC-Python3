def histogram(s):
    """Renvoie le dictionnaire des lettres dans s
       avec leur fréquence."""
    d = {}
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def get_keys(d, value):
    """Renvoie la liste des clés de d ayant la valeur value."""
    t = []
    for k in d:
        if d[k] == value:
            t.append(k)
    return t

d = histogram('evenement')
print(get_keys(d,4))  # imprime ['e']
print(get_keys(d,1))  # imprime ['v', 'm', 't']