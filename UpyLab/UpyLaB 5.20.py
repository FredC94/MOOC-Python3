"""
Écrire une fonction nouveaux_heros dont le but consiste à remplacer les héros d'une histoire.
La fonction acceptera deux paramètres :
    le premier sera une chaîne de caractères précisant le nom du fichier contenant l'histoire initiale ;
    le deuxième sera une chaîne de caractères précisant le nom du fichier dans lequel sera sauvegardée l'histoire modifiée comme précisé ci-dessous.

Exemple:
Sachant que le fichier histoire_1.txt contient le texte :
    Si Pierre est le fils de Paul, et si Paul est le frère de Jacqueline, qui est Pierre pour Jacqueline ?

après l'appel suivant de la fonction :
    nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")

le fichier dont le nom est nouvelle_histoire_1.txt doit contenir le texte :
    Si Paul est le fils de Tom, et si Tom est le frère de Mathilde, qui est Paul pour Mathilde ?

Conseils
    Pour tester votre fonction, assurez-vous de copier le fichier à lire dans le répertoire courant (ou de passer comme argument le chemin complet vers le fichier).
    L’utilisation de la méthode replace sur les chaînes de caractères va s’avérer très utile. Mais attention à Paul qui se trouve à la fois dans les anciens héros et les nouveaux. Une façon de procéder pourrait consister à remplacer, provisoirement, la chaîne "Paul" par une autre valeur (attention toutefois à ce que cette valeur provisoire ne soit pas elle-même présente dans le texte).

"""


def nouveaux_heros(story, new_story):
    with open(story, 'r', encoding='utf-8') as entree:
        filedata = entree.read()
        filedata = filedata.replace('Jacqueline', 'Mathilde').replace('Paul', 'Tom').replace('Pierre', 'Paul')
        with open(new_story, 'w', encoding='utf-8') as sortie:
            sortie.write(filedata)

nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")
nouveaux_heros("histoire_2.txt", "nouvelle_histoire_2.txt")


