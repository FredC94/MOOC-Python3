""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Voici le début d’une suite logique inventée par John Horton Conway (et connue donc sous le nom de suite de Conway).
        1
        1 1
        2 1
        1 2 1 1
        1 1 1 2 2 1
        3 1 2 2 1 1
    Chaque ligne, à partir de la deuxième, décrit la précédente :
        la première ligne, 1, est formée de un “1”, d’où la deuxième ligne : 1 1 ;
        la troisième ligne décrit la deuxième ligne, où l’on voit deux “1”, d’où 2 1 ;
        la quatrième ligne décrit la troisième ligne, où l’on voit un “2” et un “1”, d’où 1 2 1 1 ;
        et ainsi de suite.

    Écrire une fonction next_line(line) qui reçoit une liste d’entiers décrivant une ligne de cette suite,
    et qui retourne la liste correspondant à la ligne suivante.

Exemples:
    next_line([1, 2, 1, 1]) doit retourner: [1, 1, 1, 2, 2, 1]
    next_line([1]) doit retourner: [1, 1]
    next_line([]) doit retourner: [1]

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction next_line.Le code que vous soumettez à UpyLaB
    doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Notez que l’appel next_line([]) sur la liste vide retourne par convention la liste [1].
"""

def next_line(line):
    if line == []:
        return [1]
    count = 0
    val = line[0]
    res = ""
    liste = []
    for n in line:
        if n == val:
            count += 1
        else:
            liste.append(count)
            liste.append(val)            
            count = 1
            val = n
    liste.append(count)
    liste.append(val)
    return liste


print(next_line([2, 1])) # doit retourner: [1, 2, 1, 1]
print(next_line([1, 1, 1, 2, 2, 1])) # doit retourner: [3, 1, 2, 2, 1, 1]
print(next_line([1, 2, 1, 1])) # doit retourner: [1, 1, 1, 2, 2, 1]

