""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction wc(nomFichier) qui ouvre le fichier en question et renvoie un tuple de trois nombres :
        le nombre de caractères (y compris les caractères de retour à la ligne)
        le nombre de mots
        le nombre de lignes.

Consignes:
    Nous définissons ici un mot comme étant une chaîne de caractères alphanumériques, c’est-à-dire répondant True à la méthode isalnum(),
    et maximale, c’est-à-dire entourée d’espaces ou de séparateurs ou de caractères de fin de phrase.
    Les fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :
            https://upylab.ulb.ac.be/pub/data/wc1.txt
            https://upylab.ulb.ac.be/pub/data/Zola.txt
            https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt

    Pour information, le premier fichier contient les caractères a2x!§t5\n (\n désignant le caractère de fin de ligne).
    L’appel de la fonction sur ce fichier retourne donc le tuple (8, 2, 1), les deux mots étant a2x et t5.

    Notez que le fichier le-petit-prince.txt est libre de droit d’auteur sauf en France (voir https://fr.wikipedia.org/wiki/Le_Petit_Prince).
    Si vous habitez en France, vous ne pouvez donc légalement le télécharger, mais aucun souci ailleurs dans le monde.

    Vous pourriez être tenté d’utiliser la méthode split. Ce n’est peut-être pas une très bonne idée, car la liste des séparateurs est ici très longue.
    Par exemple, le fichier pourrait contenir la chaîne "a$€αω$BOjJOurα"
"""

def wc(filename):
    (caracteres, mots, lignes) = (0, 0, 0)
    with open(filename, 'r', encoding='utf-8') as mon_fichier:
        for word in mon_fichier:
            lignes = lignes + 1
            caracteres = caracteres + len(word)
            for i in range(len(word)):
                if word[i].isalnum() and not word[i-1].isalnum():
                    mots = mots + 1
    return caracteres, mots, lignes




print(wc('wc1.txt'))
print(wc('Zola.txt'))
print(wc('le-petit-prince.txt'))
# wc('wc1.txt') doit retourner (8, 2, 1)
# wc('Zola.txt') doit retourner (1356, 219, 1)
# wc('le-petit-prince.txt') doit retourner (82650, 15317, 1550)