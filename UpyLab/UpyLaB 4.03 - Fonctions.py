""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction booléenne premier(n) qui reçoit un nombre entier positif n et qui renvoie
    True si n est un nombre premier,et False sinon.

    Ensuite, écrire un programme qui lit une valeur entière x et affiche, grâce à des appels à la fonction premier,
    tous les nombres premiers strictement inférieurs à x, chacun sur sa propre ligne.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire une fonction, puis un programme appelant cette fonction.
    Notez qu’UpyLaB testera ces deux points, en exécutant le programme entier mais aussi en appelant directement
    la fonctionavec les arguments de son choix.
    
    Plus précisément UpyLaB testera d'abord l'existence d'une définition de la fonction premier avec le bon nombre de paramètres.
    Si la fonction existe bien, UpyLaB testera un programme qui réalise 2 appels à la fonction et réalise deux print ;
    ceci pour vérifier que celle-ci n'effectue aucun print.  C'est en effet à votre programme d'effectuer les print demandés.
    Ensuite différents tests de votre programme complet et de la fonction seront effectués par UpyLaB.

    Il n’est pas demandé que la fonction premier teste le type du paramètre reçu, ni si sa valeur est bien positive ou nulle.

    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer,
    ou pour les fonctions ne renvoyer, que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) par exemple),
    ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res) par exemple).
"""

from math import sqrt

def premier(n):
    """ renvoie vrai si n est un nombre premier"""
    if n == 2:
        return True
    elif n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


x = int(input())
for i in range(x + 1):
    if premier(i):
        print(i)


"""
Exemple
Avec la donnée lue suivante :

9

le résultat à imprimer vaudra donc

2
3
5
7
"""
