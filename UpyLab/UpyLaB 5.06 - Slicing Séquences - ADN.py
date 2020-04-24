""" Auteur = Frédéric Castel
    Date : Avril 2020
    Projet : MOOC Python 3 - France Université Numérique

Objectif:
    Écrire une fonction transcription_arn(brin) qui reçoit une chaîne de caractères en paramètre, correspondant à un brin d'ADN,
    et qui retourne une chaîne de caractère correspondant à la transcription ARN de ce brin.

    Nous rappelons qu'un brin d'ADN peut être modélisé par une chaîne de caractères, dont les caractères sont pris parmi les quatre suivants:
    'A'(Adénine), 'C' (Cytosine),'G' (Guanine) et 'T' (Thymine).
    La transcription en ARN se traduit par le remplacement des nucléotides de Thymine par des nucléotides d'Uracile,
    que l'on représenterapar le caractère 'U'.

Exemples:
    transcription_arn('AGTCTTACCGATCCAT') doit retourner: 'AGUCUUACCGAUCCAU'

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction transcription_arn. Le code que vous soumettez à UpyLaB doit donc comporter
    uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à print.

    Il n'est pas demandé que la fonction teste le type de l'argument passé ; vous pouvez supposer qu'il s'agira d'une chaîne de caractères valide.
"""

def transcription_arn(brin):
    liste = ""
    for i in range(len(brin)):
        adn = 'AGUC'
        if brin[i] not in adn:
            lettre = 'U'
            liste = liste + lettre
        else:
            lettre = brin[i]
            liste = liste + lettre
    return liste


transcription_arn('AGTCTTACCGATCCAT')