""" Auteur: Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction substitue(message, abréviation) qui renvoie une copie de la chaîne de caractères message dans laquelle 
    les mots qui figurent parmi les clés du dictionnaire abréviation sont remplacés par leur signification (valeur).

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction substitue.
    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction,
    et ne fait en particulier aucun appel à input ou à print.
    
    Pour simplifier, on suppose que les mots de la chaîne message sont séparés par des espaces.
    
    Vous pourrez supposer que les arguments passés à la fonction sont du bon type.
"""

def substitue(message, abreviation):
    msg = message.split(" ")
    # msg.remove('to')
    phrase = ''
    for i in msg:
        if i in abreviation:
            phrase = phrase + " " + abreviation[i]
        else:
            phrase = phrase + " " + i
    return phrase.strip()

#~L’appel suivant de la fonction :
sub = substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck',
                                 'N.' : 'Norris',
                                 'cpt' : 'counted',
                                 '2' : 'two times',
                                 'inf' : 'infinity'})

print(sub)
# doit retourner : 'Chuck Norris counted two times to infinity'
