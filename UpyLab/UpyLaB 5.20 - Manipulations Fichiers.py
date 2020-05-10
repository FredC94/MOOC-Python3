""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction nouveaux_heros dont le but consiste à remplacer les héros d'une histoire.
    La fonction acceptera deux paramètres :
        le premier sera une chaîne de caractères précisant le nom du fichier contenant l'histoire initiale ;
        le deuxième sera une chaîne de caractères précisant le nom du fichier dans lequel sera sauvegardée
        l'histoire modifiée comme précisé ci-dessous.

Exemple:
    Sachant que le fichier histoire_1.txt contient le texte :
        Si Pierre est le fils de Paul, et si Paul est le frère de Jacqueline, qui est Pierre pour Jacqueline ?

    après l'appel suivant de la fonction :
        nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")

    le fichier dont le nom est nouvelle_histoire_1.txt doit contenir le texte :
        Si Paul est le fils de Tom, et si Tom est le frère de Mathilde, qui est Paul pour Mathilde ?

Consignes
    Vous pouvez supposer que le fichier dont le nom est donné en premier argument existe bien et est au format UTF-8.
    Les fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :
            https://upylab.ulb.ac.be/pub/data/histoire_1.txt
            https://upylab.ulb.ac.be/pub/data/histoire_2.txt
"""

def nouveaux_heros(story, new_story):
    with open(story, 'r', encoding='utf-8') as entree:
        print(len(entree.read().split()))
        filedata = filedata.replace('Jacqueline', 'Mathilde').replace('Paul', 'Tom').replace('Pierre', 'Paul')
        with open(new_story, 'w', encoding='utf-8') as sortie:
            sortie.write(filedata)

nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")
#nouveaux_heros("histoire_2.txt", "nouvelle_histoire_2.txt")


