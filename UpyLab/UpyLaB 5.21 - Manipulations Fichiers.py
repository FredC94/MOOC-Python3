""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction liste_des_mots qui reçoit en paramètre le nom d’un fichier texte,
    que la fonction doit ouvrir, et qui renvoie la liste des mots contenus dans le fichier.

Consignes:
    On peut supposer que le fichier est présent et dans le bon format en encodage UTF-8.
    Les mots dans la liste seront écrits en minuscule et triés dans l’ordre donné par la codification UTF-8
    (en utilisant la méthode sort par exemple), les accents n’étant pas gérés de façon spécifique
    (« a » et « à » sont deux mots différents).
    Un même mot ne peut pas se trouver deux fois dans la liste.
    Dans le fichier source, les mots peuvent être séparés par des caractères blancs habituels
    (caractère espace, tabulation, passage à la ligne), ou par n’importe quel caractère parmi les suivants :

        - ' " ? ! : ; . , * = ( ) 1 2 3 4 5 6 7 8 9 0

    Certains des fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :
            https://upylab.ulb.ac.be/pub/data/Zola.txt
            https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt

    Notez que le fichier le-petit-prince.txt est libre de droit d’auteur sauf en France
    (voir https://fr.wikipedia.org/wiki/Le_Petit_Prince).
    Si vous habitez en France, vous ne pouvez donc légalement le télécharger, mais aucun souci ailleurs dans le monde.
"""

def liste_des_mots(filename):
    # constitution des 2 listes (vides)
    liste_temp = []
    liste = []
    for mots in open(filename, encoding="utf-8"): # on liste tous les mots du fichier passé en argument
        for i in range(len(mots)): # on boucle sur la longueur du mot 
            if not mots[i].isalpha(): # si la lettre n'est pas un terme alphabétique
                mots = mots.replace(mots[i], " ") # on remplace la lettre du mot par une chaîne vide (espace)

        # puis on split chaque mot que l'on additionne à la liste temporaire à chaque tour de boucle
        liste_temp = liste_temp + mots.split()
        print(liste_temp) 

    for mots in liste_temp: # on boucle sur chaque mots de la liste temporaire
        mots = mots.lower() # on convertit le mot en minuscule
        if mots not in liste: # si le mot n'est pas dans la liste définitive (supprime les doublons)...
            liste.append(mots) # ...on ajoute le mot à la liste 
    liste.sort() # fin de boucle, on classe les mots par ordre alphabétique

    return liste # ... et on retourne la liste
        
(liste_des_mots("Zola.txt")) 
# print(liste_des_mots("Zola.txt"))

