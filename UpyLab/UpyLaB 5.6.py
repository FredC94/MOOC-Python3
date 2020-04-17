"""
Écrire une fonction transcription_arn(brin) qui reçoit une chaîne de caractères en paramètre, correspondant à un brin d'ADN,
et qui retourne une chaîne de caractère correspondant à la transcription ARN de ce brin.
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