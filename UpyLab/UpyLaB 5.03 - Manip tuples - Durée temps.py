""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction duree qui reçoit deux paramètres debut et fin. Ces derniers sont des couples (tuples de deux composantes)
    dont la première composante représente une heure et la seconde les minutes.
    Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. Le résultat sera donné sous la forme d’un tuple(heure, minutes).

Exemples:
    duree ((14, 39), (18, 45)) doit retourner: (4, 6)
    duree ((6, 0), (5, 15)) doit retourner: (23, 15)

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction duree. Le code que vous soumettez à UpyLaB doit donc comporter
    uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Notez que l’appel duree ((6, 0), (5, 15)) retourne le couple (23, 15) et non (0, 45). Le premier argument correspond à l’instant initial
    et le second à l’instant final.
"""

def duree(debut, fin):
    heureD = debut[0]
    heureF = fin[0]
    minuteD = debut[1]
    minuteF = fin[1]
    if (heureD < heureF) and (minuteD < minuteF):
        heure = heureF - heureD
        minute = minuteF - minuteD
        return heure, minute
    elif (heureD < heureF) and (minuteD > minuteF):
        heure = heureF - (heureD + 1)
        minute = (minuteF + 60) - minuteD
        return heure, minute
    elif (heureD > heureF) and (minuteD > minuteF):
        heure = (heureF + 23) - heureD
        minute = (minuteF + 60) - minuteD
        return heure, minute
    elif (heureD > heureF) and (minuteD < minuteF):
        heure = (heureF + 24) - heureD
        minute = minuteF - minuteD
        return heure, minute


print(duree((3, 45), (13, 22)))
print(duree((6, 0), (5, 15)))
