""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Enoncé:
Écrire une fonction substitue(message, abréviation) qui renvoie une copie de la chaîne de caractères message dans laquelle 
les mots qui figurent parmi les clés du dictionnaire abréviation sont remplacés par leur signification (valeur).

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction substitue. Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.
    Pour simplifier, on suppose que les mots de la chaîne message sont séparés par des espaces.
    Vous pourrez supposer que les arguments passés à la fonction sont du bon type.
"""
def construction_dict_amis(personnes):
    dic = {}
    for prenom1, prenom2 in personnes:
        if prenom1 not in dic:
            dic[prenom1] = {prenom2}
        else:
            dic[prenom1].add(prenom2)
        if prenom2 not in dic:
            dic[prenom2] = set()
    return dic

# L’appel suivant de la fonction :
c1 = construction_dict_amis([('Quidam', 'Pierre'),
                        ('Thierry', 'Michelle'),
                        ('Thierry', 'Pierre')])

# doit retourner : 
# {'Quidam' : {'Pierre'}, 'Pierre' : set(), 'Thierry' : {'Michelle', 'Pierre'},  'Michelle' : set()}

c2 = construction_dict_amis([('Bernadette', 'Ariane'), 
                        ('Michelle', 'Quidam'), 
                        ('Pierre', 'Pierre'), 
                        ('Bernadette', 'Thierry'), 
                        ('Quidam', 'Thierry'), 
                        ('Quidam', 'Michelle'), 
                        ('Quidam', 'Bernadette'), 
                        ('Pierre', 'Bernadette')]) 
# doit retourner : 
# {'Michelle': {'Quidam'}, 'Bernadette': {'Ariane', 'Thierry'}, 'Quidam': {'Michelle', 'Bernadette', 'Thierry'}, 'Thierry': set(), 'Ariane': set(), 'Pierre': {'Bernadette', 'Pierre'}}

print(c1)
print(c2)