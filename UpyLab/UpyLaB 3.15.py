"""
Écrire un programme qui teste si, pour une configuration donnée, un écureuil va ou non atteindre la noisette.
Il reçoit deux valeurs entières en entrée, une valeur saut et une valeur position_cible, toutes deux entre 1 et 99.
"""
saut = int(input())
position_courante = saut
noisette = int(input())
for i in range(0, position_courante, saut):
    # Continuer la boucle tant que l'écureuil n'a pas atteint la noisette...
    while position_courante != noisette:
        print(position_courante)
        position_courante = position_courante + saut
        if position_courante % 100 > 0:
            position_courante = position_courante % 100
        elif position_courante % 100 == 0:
            print(i)
            print("Pas trouvé")
            break
    if position_courante % 100 != 0:
        print("Cible atteinte")
