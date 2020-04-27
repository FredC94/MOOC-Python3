""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction valeurs(dico) qui doit fournir, à partir du dictionnaire donné en paramètre,
    une liste des valeurs du dictionnaire triées selon leur clé.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction valeurs.
    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.

    Vous pourrez supposer que les clés du dictionnaire sont des chaînes de caractères.
"""

def valeurs(dico):
    liste = [] # on crée la liste
    for key in sorted(dico): # on parcours les clés (par ordre alphabétique) passées dans dico
        liste.append(dico[key]) # puis on ajoute à la liste les valeurs
    return liste


print(valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'}))
# retourne :
# ['un', 'trois', 'deux']

print(valeurs({'Bernadette': ['Luc', 'Michel', 'Jules'], 'Catherine': ['Jean'], 'Michel': ['Luc'], 'Germaine': ['Catherine'], 'Jules': ['Bernadette'], 'Jean': ['Germaine'], 'Luc': []}))
# retourne :
# [['Luc', 'Michel', 'Jules'], ['Jean'], ['Catherine'], ['Germaine'], ['Bernadette'], [], ['Luc']]