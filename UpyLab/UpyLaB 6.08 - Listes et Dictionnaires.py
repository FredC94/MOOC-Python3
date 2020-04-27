""" Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction store_email(liste_mails) qui reçoit en paramètre une liste d’adresses e-mail et qui renvoie
    un dictionnaire avec comme clés les domaines des adresses e-mail et comme valeurs les listes d’utilisateurs correspondantes,
    triées par ordre croissant (UTF-8).

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction store_email.

    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait
    en particulieraucun appel à input ou à print.   
"""

def store_email(liste_mails):
    dict={} # on crée le dictionnaire vide
    for c in liste_mails:
        # slicing pour ne conserver que le domaine, que l'on affecte à la variable cle
        cle = c[c.find('@')+1:]        
        # slicing pour ne conserver que ce qui précède @ et constitution du dictionnaire
        dict[cle] = dict.get(cle, []) + [c[:c.find('@')]]
    for i in dict:
        dict[i].sort()
    return dict



# L’appel de la fonction suivant :

store_email(["ludo@prof.ur", "andre.colon@stud.ulb",
             "thierry@profs.ulb", "sébastien@prof.ur",
             "eric.ramzi@stud.ur", "bernard@profs.ulb",
             "jean@profs.ulb" ])

#~retourne le dictionnaire :
"""
{ 'prof.ur' : ['ludo', 'sébastien'],
  'stud.ulb' : ['andre.colon'],
  'profs.ulb' : ['bernard', 'jean', 'thierry'],
  'stud.ur' : ['eric.ramzi'] }
"""
