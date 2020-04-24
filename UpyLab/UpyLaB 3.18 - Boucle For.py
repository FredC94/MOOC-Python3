""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui lit un nombre entier strictement positif n et imprime une pyramide de chiffres de hauteur n (sur n lignes complètes,
    c'est-à-dire toutes terminées par une fin de ligne).
        La première ligne imprime un “1” (au milieu de la pyramide).
        La ligne i commence par le chiffre i % 10 et tant que l’on n’est pas au milieu, le chiffre suivant a la valeur suivante ((i+1) % 10).
        Après le milieu de la ligne, les chiffres vont en décroissant modulo 10 (symétriquement au début de la ligne).

Notons qu’à la dernière ligne, aucune espace n’est imprimée avant d’écrire les chiffres 0123....

Consignes:
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu.
    En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) par exemple),
    ni ajouter du texte dans ce qui est imprimé.

Conseils:
    Pour tester votre code, UpyLaB va l’exécuter plusieurs fois en lui fournissant à chaque test des nombres différents en entrée.
    Il vérifiera alors que le résultat affiché par votre code correspond à ce qui est attendu.
    N’hésitez donc pas à tester votre code en l’exécutant plusieurs fois dans PyCharm avec des valeurs différentes en entrée y compris supérieure à 10.
"""

N=int(input())
for i in range(1,N+1):
    for j in range(N,i,-1):
        print(" ", end='')
    for k in range(1,i+1):
        if i == 1:
            print(i%10, end='')
        else:
            print(i%10, end='')
            i=i+1
    for q in range(i-1,0,-1):
        if (i != j):
            i=i-1
            if i == j == k == q == N:
                break
            else:
                print((i-1)%10,end="")
    print()
