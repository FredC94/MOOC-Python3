"""
Écrire une fonction duree qui reçoit deux paramètres debut et fin.
Ces derniers sont des couples (tuples de deux composantes) dont la première composante représente une heure et la seconde les minutes.
Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants.
Le résultat sera donné sous la forme d’un tuple (heure, minutes).
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
