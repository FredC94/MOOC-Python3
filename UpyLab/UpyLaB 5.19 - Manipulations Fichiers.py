""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction acrostiche qui reçoit en paramètre le nom d’un fichier et qui retourne
    la chaîne de caractères formée par les premières lettres de chaque ligne du fichier.

Exemples:
    Sachant que le fichier Apollinaire.txt contient le texte :

    Mon aimée adorée avant que je m'en aille
    Avant que notre amour triste défaille
    Râle et meure ô m'amie une fois
    Il faut nous promener tous les deux seuls dans les bois
    Alors je m'en irai plus heureux que les rois.

    acrostiche('Apollinaire.txt')
    doit retourner : 'MARIA'

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction acrostiche. Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.
    Les fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :
        https://upylab.ulb.ac.be/pub/data/acro1.txt
        https://upylab.ulb.ac.be/pub/data/acro2.txt
        https://upylab.ulb.ac.be/pub/data/acro3.txt

"""

def acrostiche(file):
    with open(file, encoding="utf-8") as mots:
        res = ""
        for m in mots:
            res = res + m[0]
        return res


print(acrostiche('acro1.txt'))
print(acrostiche('acro2.txt'))
print(acrostiche('acro3.txt'))