""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur.
    Chaque manche va consister en :

        la génération (pseudo) aléatoire d’un nombre entre 0 et 2 compris, à l’aide de la fonction randint du module random, qui va représenter le coup de l’ordinateur (0 valant Pierre, 1, Feuille et 2, Ciseaux) ;
        la lecture en entrée (input) d’une valeur entière entre 0 et 2 compris qui représente le coup du joueur ;
        l’affichage du résultat sous une des formes :
            coup_o bat coup_j : points
            coup_o est battu par coup_j : points
            coup_o annule coup_j : points
        où
            coup_o et coup_j sont respectivement le coup de l’ordinateur et du joueur : "Pierre" s’il a joué 0, "Feuille" s’il a joué 1 et "Ciseaux" s’il a joué 2.
            points donne le résultat des manches jusqu’à présent sachant que le compteur points part de zéro, et est incrémenté de un
            chaque fois que le joueur gagne une manche, et décrémenté de un chaque fois que l’ordinateur gagne une manche
            (les match nuls ne modifiant pas le compteur points).

À la fin des cinq manches, votre programme affichera : Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou strictement positif.

Consignes:
    Dans cet exercice, il vous est demandé d’écrire un programme contenant des fonctions.
    
    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veillez à n’imprimer que le résultat attendu
    en respectant majuscules et minuscules et en veillant à n’avoir qu’une espace entre les mots et signes et aucune espace supplémentaire
    en fin de ligne. En particulier, il ne faut rien écrire à l’intérieur des appels à input (int(input()) et non int(input("Entrer un nombre : ")) par exemple),
    ni ajouter du texte supplémentaire dans ce qui est imprimé (print(points) et non print("résultat :",points) par exemple).
"""

def pierre_feuille_ciseaux():
    import random

    s = int(input())
    random.seed(s)
    point = 0

    def affichage_manche(point):
        if point < 0:
            print("Perdu")
        elif point == 0:
            print("Nul")
        else:
            print("Gagné")

    def affichage_bat(result, joueur, ordi, point):
        def rename(name):
            if name == 0:
                name = "Pierre"
            elif name == 1:
                name = "Feuille"
            elif name == 2:
                name = "Ciseaux"
            return name

        joueur = rename(joueur)
        ordi = rename(ordi)

        if result > 0:
            print(ordi, "est battu par", joueur, ":", point)
        elif result == 0:
            print(ordi, "annule", joueur, ":", point)
        else:
            print(ordi, "bat", joueur, ":", point)

    def bat(joueur, ordi):

        PIERRE = 0
        FEUILLE = 1
        CISEAUX = 2

        if joueur == PIERRE and ordi == FEUILLE:
            point = 1
        elif joueur == FEUILLE and ordi == CISEAUX:
            point = 1
        elif joueur == CISEAUX and ordi == PIERRE:
            point = 1
        elif joueur == PIERRE and ordi == CISEAUX:
            point = -1
        elif joueur == FEUILLE and ordi == PIERRE:
            point = -1
        elif joueur == CISEAUX and ordi == FEUILLE:
            point = -1
        else:
            point = 0

        return point

    for i in range(5):
        coup_j = int(input())
        coup_o = random.randint(0, 2)

        result = bat(coup_o, coup_j)
        point += result
        affichage_bat(result, coup_j, coup_o, point)
    affichage_manche(point)


pierre_feuille_ciseaux()
