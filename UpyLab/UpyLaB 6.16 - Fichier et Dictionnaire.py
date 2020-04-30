""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction file_histogram(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères,
    d’un fichier texte, et qui renvoie un dictionnaire associant à chaque caractère du texte contenu dans ce fichier
    son nombre d’occurrence.

    Écrire une fonction words_by_length(fileName) qui prend en paramètre le nom, sous forme d’une chaîne de caractères,
    d’un fichier texte, et qui renvoie un dictionnaire associant à une longueur l la liste triée (dans l’ordre utf-8 croissant)
    des mots de longueur l présents dans le texte contenu dans le fichier.
    Ces mots seront écrits en minuscules.

Exemples:

    L’appel de la fonction suivant : file_histogram('/pub/data/Zola.txt')
    retourne :
    {'f': 14, 'î': 1, "'": 10, 'v': 15, 'm': 24,
    'N': 1, 'o': 49, 'a': 95, 'h': 13, 'd': 37,
    'é': 21, 'b': 12, 'E': 2, '\n': 1, 'x': 2,
    'y': 3, 'U': 1, 'M': 2, 'u': 50, 'à': 3,
    'e': 168, 'i': 73, ' ': 209, 'r': 64, 'p': 24,
    'D': 3, 's': 105, ',': 35, 't': 82, '-': 1,
    'è': 4, 'g': 16, 'c': 39, '.': 10, '?': 1,
    'L': 1, 'n': 81, 'ç': 1, 'j': 4, 'A': 2,
    'l': 71, 'ô': 1, 'q': 5}

    L’appel de la fonction suivant : words_by_length('/pub/data/Zola.txt')
    retourne :
    {1: ['a', 'c', 'd', 'l', 'n', 's', 'à'],
    2: ['ce', 'de', 'du', 'en', 'et', 'il',
        'la', 'le', 'là', 'sa', 'se', 'si', 'un'],
    3: ['aux', 'des', 'ils', 'les', 'par', 'pas',
        'que', 'qui', 'ses', 'sol', 'une', 'vie'],
    4: ['avec', 'blés', 'ciel', 'dans', 'dont',
        'loin', 'plus', 'pour', 'sous', 'sève',
        'tous', 'voix'],
    5: ['armée', 'astre', 'avril', 'bruit', 'cette',
        'comme', 'coups', 'faire', 'flanc', 'futur',
        'grand', 'haies', 'noire', 'parts', 'pieds',
        'pièce', 'plein', 'terre', 'vives', 'était'],
    6: ['allait', 'arbres', 'autres', 'baiser', 'besoin',
        'cassée', 'champs', 'chaque', 'droite', 'encore',
        'gauche', 'germes', 'gloire', 'grosse', 'herbes',
        'hommes', 'jeunes', 'plaine', 'rauque', 'rayons',
        'rumeur', 'siècle', 'soleil', 'suivre', 'toutes',
        'vertes', 'échine'],
    7: ['bientôt', 'chaleur', 'coulait', 'croyait',
        'fussent', 'germait', 'graines', 'lumière',
        'maheude', 'matinée', 'montait', 'poussée',
        'sillons', 'souffle', 'éclater', 'étaient'],
    8: ['campagne', 'enjambée', 'feuilles', 'jeunesse',
        'obstinés', 'profonds', 'récoltes', 'tapaient', 'épandait'],
    9: ['bourgeons', 'camarades', 'crevaient', 'enfantait', 'enflammés',
        'entendait', 'gerçaient', 'lentement', 'rayonnait'],
    10: ['accompagné', 'betteraves', 'gonflaient', 'maintenant',
        'nourricier', 'poussaient', 'rapprochés', 'rivelaines',
        'ronflement', 'vengeresse', 'échauffant'],
    11: ['débordement', 'germination', 'grandissant', 'jaillissait',
        'reconnaître', 'travaillées', 'ventilateur'],
    12: ['allongeaient', 'chuchotantes', 'continuaient'],
    13: ['distinctement'], 14: ['tressaillaient']}

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement des fonctions.
    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de ces fonctions,
    et ne fait en particulier aucun appel à input ou à print.
    
    Les fichiers utilisés par UpyLaB pour tester votre code sont :
            https://upylab.ulb.ac.be/pub/data/words.txt
            https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt
            https://upylab.ulb.ac.be/pub/data/Zola.txt

    Pour la fonction words_by_length, on supposera qu’un mot est une séquence de caractères alphabétiques.
    La méthode isalpha() pourra être utile.

    Par exemple, la chaîne de caractères 'cat4dog' sera considérée comme formant deux mots : 'cat' et 'dog'.

    Veillez aussi à ce qu’un même mot n’apparaisse pas plusieurs fois dans la même liste.
"""

def file_histogram(fileName):
    mon_dic ={}
    with open(fileName, encoding="utf-8") as mon_fichier:
        for mot in mon_fichier:
            for lettre in mot:
                if lettre in mon_dic:
                    mon_dic[lettre] = mon_dic[lettre] + 1
                else:
                    mon_dic[lettre] = 1
        return mon_dic

def words_by_length(fileName):
    liste_temp = []
    liste =[]
    my_dic ={}
    for mots in open(fileName, encoding="utf-8"):
        for i in range(len(mots)):
            if not mots[i].isalpha():
                mots = mots.replace(mots[i], " ")
        liste_temp = liste_temp + mots.split()

    for mots in liste_temp:
        mots = mots.lower()
        if mots not in liste:
            liste.append(mots)
    liste.sort()

    for mots in liste:
        key = len(mots)
        if key in my_dic:
            my_dic[key].append(mots)
        else:
            my_dic[key] = [mots]
    sorted_dict = {k: my_dic[k] for k in sorted(my_dic)}
    return sorted_dict


print(file_histogram('Zola.txt'))
print(words_by_length('Zola.txt'))