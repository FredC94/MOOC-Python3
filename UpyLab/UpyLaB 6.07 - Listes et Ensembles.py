""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction prime_odd_numbers(numbers) qui reçoit une liste de nombres et qui renvoie un couple d’ensembles contenant
    respectivement les nombres premiers présents dans la liste et les nombres impairs.

    Pour cela, nous vous demandons d’écrire deux fonctions annexes qui seront appelées dans le corps de la fonction prime_odd_numbers :
        la fonction even(max_nb) qui renvoie l’ensemble des nombres naturels pairs inférieurs ou égaux à max_nb
        la fonction prime_numbers(max_nb) qui renvoie l’ensemble des nombres premiers inférieurs ou égaux à max_nb.

Exemples:
    prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18])
    retourne, à l’ordre près, : ({2, 5, 11, 13, 17}, {1, 5, 11, 9, 13, 15, 17})
    
    prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18])
    retourne, à l’ordre près, : (set(), {1, 9, 15, 21})

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement des fonctions.

    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.
"""

def prime_numbers(max_nb):
    liste=set()
    for n in range(2, max_nb+1):
        c=1
        for i in range(2, int(n**(1/2))+1):
            if n%i==0:
                c=0
        if c or n==2:
            liste.add(n)
    return liste
 
def even(max_nb):
    liste=set()
    for i in range((max_nb+2)//2):
        liste.add(2*i)
    return liste

def prime_odd_numbers(numbers):
    ensemble1 = set()
    ensemble2 = set()
    max_nb = max(numbers)
    l1, l2 = prime_numbers(max_nb), even(max_nb)
    for i in numbers:
        if i in l1:
            ensemble1.add(i)
        if i not in l2:
            ensemble2.add(i)
    return ensemble1, ensemble2


prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18])
# retourne, à l’ordre près, : ({2, 5, 11, 13, 17}, {1, 5, 11, 9, 13, 15, 17})

prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18])
# retourne, à l’ordre près, : (set(), {1, 9, 15, 21})

prime_odd_numbers([1, 7, 13, 19, 25, 31, 37, 43, 49, 55, 61, 67, 73, 79, 85, 91, 97])
# doit retourner ({97, 67, 37, 7, 73, 43, 13, 79, 19, 61, 31}, {1, 97, 67, 37, 7, 73, 43, 13, 79, 49, 19, 85, 55, 25, 91, 61, 31})



