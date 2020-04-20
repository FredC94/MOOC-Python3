# Auteur: Frédéric CASTEL (Mars/Avril 2020)
"""
Exercices:
Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme d’une nouvelle liste.
L’appel suivant de la fonction :
decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
doit retourner :
[1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']

Consignes:
Il n’est demandé ici que de définir la fonction. Mais pour tester son fonctionnement dans PyCharm, pensez à ajouter du code
qui l’appelle et teste son résultat, sur plusieurs valeurs, comme print(decompresse([(1,'He'), (2, 'l'), (1,'o')]) par exemple.
"""


def decompresse(t):
    liste = []
    x = 0
    for y in range(len(t)):
        for i in range(t[x][0]):
            liste.append(t[x][1])
        x = x + 1
    return liste


decompresse([(4, 1), (2, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
# [1, 1, 1, 1, 2, 2, 'test', 'test', 3, 3, 3, 'bonjour']
