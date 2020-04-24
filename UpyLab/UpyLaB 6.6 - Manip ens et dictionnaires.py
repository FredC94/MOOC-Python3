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
def symetrise_amis(dic, englobe):
    for amis in dic:
        liste=[]
        for i in dic[amis]:
            if i in dic and englobe:
                dic[i].add(amis)
            elif i not in dic or amis not in dic[i]:
                liste.append(i)
        for i in liste:
            dic[amis].remove(i)



d = {'Thierry': {'Michelle', 'Bernadette'},
     'Michelle': {'Thierry'},
     'Bernadette': set()}
symetrise_amis(d, True)

print(d)
# doit afficher, à l’ordre près :

{'Thierry': {'Michelle', 'Bernadette'},
 'Michelle' : {'Thierry'},
 'Bernadette' : {'Thierry'}}

