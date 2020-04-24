""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
    La première donnée lue ne fait pas partie des valeurs à sommer.
    Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :

        si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;

        si elle est négative, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée par le caractère "F" signifiant que la liste est terminée.

Consignes:
    Ne mettez pas d'argument dans les input :
        data = input() et pas
        data = input("Donnée suivante :") par exemple ;
    Le résultat doit juste faire l’objet d’un print(res) sans texte supplémentaire (pas de print("résultat =", res) par exemple).
"""

lst = []
num = int(input())
if num >=0:
    for n in range(num):
        numbers = int(input())
        lst.append(numbers)
    print(sum(lst))
elif num < 0:
    somme = 0
    numbers = 0
    while numbers != 'F':
        numbers = input()
        if numbers == 'F':
            print(int(somme))
        else:
            somme = int(numbers) + somme