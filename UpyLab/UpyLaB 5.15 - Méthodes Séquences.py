# Auteur: Frédéric CASTEL (Mars/Avril 2020)
"""
Exercices:
nous vous demandons d’écrire une fonction correcteur(mot, liste_mots) où mot est le mot que Joao écrit et liste_mots
est une liste qui contient les mots (ayant la bonne orthographe)que Joao est susceptible d’utiliser.

Consignes:
Cette fonction doit retourner le mot dont l’orthographe a été corrigée.
Exemple, l’appel suivant de la fonction :
correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
doit retourner :
"bonjour"
"""


def correcteur(mot, liste_mots):
    mot_correct = ""
    for mot_bon in liste_mots:
        if len(mot) == len(mot_bon):
            distance = len(mot)
            for i in range(len(mot)):
                if mot[i] == mot_bon[i]:
                    distance = distance - 1
            if distance <= 1:
                mot_correct = mot_bon
                break
    return mot_correct


correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
