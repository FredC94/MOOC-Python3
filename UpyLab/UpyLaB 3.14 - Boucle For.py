"""
Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100. Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.
À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :
    « Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais
    « Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais
    « Gagné en n essais ! » : si le nombre secret est trouvé
    « Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.
"""


import random
essais = 5
secret = random.randint(0, 100)
for i in range(secret):
    choix_utilisateur = int(input())
    if secret == choix_utilisateur:
        print("Gagné en", i+1, "essais !")
        break
    elif i == essais:
        print("Perdu ! Le secret était", secret)
    elif secret < choix_utilisateur and i < essais:
        print("Trop grand")
    elif secret > choix_utilisateur and i < essais:
        print("Trop petit")
