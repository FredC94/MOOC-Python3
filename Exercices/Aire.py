""" Auteur: Sébastien Hoarau
    date : juin 2018
    But du programme :
    Le programme suivant calcule la circonférence
    et l’aire d’un disque dont le rayon est donné
    en input
    Entrée: rayon : le rayon du disque
    Sorties: la circonférence du disque
             l'aire du disque
"""

rayon = float(input("Veuillez donner le rayon : "))  # lecture du rayon de mon disque
circ = 2 * 3.14  * rayon                    # calcul de la circonférence
aire = 3.14 * rayon **  2                   # calcul de l'aire
# Affichage des résultats
print("Circonférence : ", circ)
print("Aire          : ", aire)