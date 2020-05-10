"""
On se propose d'écrire une moulinette qui annote un fichier avec des nombres de lignes, de mots et de caractères.

Le but de l'exercice est d'écrire une fonction comptage :

    qui prenne en argument un nom de fichier d'entrée (on suppose qu'il existe) et un nom de fichier de sortie (on suppose qu'on a le droit de l'écrire) ;
    le fichier d'entrée est supposé encodé en UTF-8 ;
    le fichier d'entrée est laissé intact ;
    pour chaque ligne en entrée, le fichier de sortie comporte une ligne qui donne le numéro de ligne, le nombre de mots (séparés par des espaces), le nombre de caractères (y compris la fin de ligne), et la ligne d'origine.
"""

def comptage(in_filename, out_filename):
    with open(in_filename, encoding='utf-8') as entree:
        with open(out_filename, 'w', encoding='utf-8') as sortie:
            lineno = 1
            for ligne in entree:
                nb_mots = len(ligne.split())
                nb_car = len(ligne)
                sortie.write(f"{lineno}:{nb_mots}:{nb_car}:{ligne}")
                lineno += 1


comptage('entree.txt', 'sortie.txt')
