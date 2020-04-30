""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction placer_pion(couleur, colonne, grille) où :
        couleur est la couleur du pion, qui peut être soit 'R' (rouge), soit 'J' (jaune),
        colonne est l’indice de la colonne où le joueur souhaite placer le pion (allant de 0 à 6),
        grille est la grille de jeu sous forme de matrice.

    Cette matrice contient donc six listes de lignes contenant chacune sept éléments.
    La ligne à l’indice 0 représente le bas du jeu.
    Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.
    Cette fonction placera un pion dans la grille du jeu et renverra un couple de valeurs :
        si le placement est possible, la valeur booléenne True et la grille modifiée,
        sinon, la valeur booléenne False et la grille non modifiée.

Exemples:

    placer_pion("R", 3, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V']])

    doit retourner :

    (True, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'V', 'V', 'V', 'V']])

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction placer_pion. Le code que vous soumettez à UpyLaB doit
    donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Vous pourrez supposer que les arguments passés à la fonction seront valides.

    Il n’est pas demandé de vérifier si la grille contient un alignement gagnant.
"""

def placer_pion(couleur, colonne, grille):
    for ligne in range(6):
        if grille[ligne][colonne] == 'V':
            grille[ligne][colonne] = couleur
            return True, grille
    return False, grille



print(placer_pion('J', 2, [['R', 'V', 'J', 'J', 'V', 'R', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'], 
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'], 
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'], 
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))
"""
                (True, [['R', 'V', 'J', 'J', 'V', 'R', 'V'],
                        ['V', 'V', 'J', 'V', 'V', 'V', 'V'], 
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'], 
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'], 
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'], 
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V']])    
"""        
placer_pion("R", 3, [['V', 'V', 'V', 'J', 'V', 'V', 'V'], # True
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'V', 'V', 'V']])

placer_pion("J", 4, [['J', 'J', 'J', 'J', 'R', 'R', 'R'], # False
                     ['R', 'R', 'R', 'R', 'R', 'V', 'V'],
                     ['J', 'J', 'J', 'J', 'J', 'V', 'V'],
                     ['V', 'R', 'J', 'R', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'J', 'V', 'V'],
                     ['V', 'V', 'V', 'V', 'R', 'V', 'V']])