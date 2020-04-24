""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction fibo(n) qui reçoit un nombre entier n et qui renvoie la valeur du nombre de Fibonacci F_n.

    On rappelle que :
        F_0 vaut 0 ;
        F_1 vaut 1 ;
        F_{i + 1} vaut F_i + F_{i-1} pour i > 0 ;
        F_i vaut None pour i < 0.

    Ensuite, écrire un programme qui lit une valeur entière strictement positive x et affiche le résultat de fibo(i)
    pour i allant de 0 compris à x non compris, avec chaque valeur sur sa propre ligne.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire une fonction, puis un programme appelant cette fonction.
    Notez qu’UpyLaB testera ces deux points, en exécutant le programme entier mais aussi en appelant directement la fonction avec les arguments de son choix.
    
    Plus précisément UpyLaB testera d'abord l'existence d'une définition fibo avec le bon nombre de paramètres.
    Si la fonction existe bien, UpyLaB testera votre programme en ajoutant un appel à la fonction fibo pour vérifier que celle-ci n'effectue aucun print.
    C'est en effet à votre programme d'effectuer le print demandé. Ensuite différents tests de votre programme complet et de la fonction seront effectués par UpyLaB.

    Il n’est pas demandé que la fonction fibo teste le type du paramètre reçu.

    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input())et non int(input("Entrer un nombre : ")) par exemple),
    ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res) par exemple).

    Par ailleurs, la fonction fibo est demandée; UpyLaB va valider qu’en appelant la fonction indépendamment du reste de votre code,
    les résultats envoyés par votre fonction sont corrects et ont le bon type.
"""

def fibo(n):
    if n < 0:
        return None
    temp = 1
    v = 0
    for i in range(n):
        v = v + temp  # ou v += temp
        temp = v - temp  # or à ce stade v = v + temp, il faut donc soustraire temp
    return v


x = int(input())
for i in range(x):
    print(fibo(i))

"""
Exemple:
Avec la donnée lue suivante :

5

le résultat à imprimer vaudra donc

0
1
1
2
3
"""