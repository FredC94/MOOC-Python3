def pierre_feuille_ciseaux():
    import random

    s = int(input())
    random.seed(s)
    point = 0

    def affichage_manche(point):
        if point < 0:
            print("Perdu")
        elif point == 0:
            print("Nul")
        else:
            print("Gagné")

    def affichage_bat(result, joueur, ordi, point):
        def rename(name):
            if name == 0:
                name = "Pierre"
            elif name == 1:
                name = "Feuille"
            elif name == 2:
                name = "Ciseaux"
            return name

        joueur = rename(joueur)
        ordi = rename(ordi)

        if result > 0:
            print(ordi, "est battu par", joueur, ":", point)
        elif result == 0:
            print(ordi, "annule", joueur, ":", point)
        else:
            print(ordi, "bat", joueur, ":", point)

    def bat(joueur, ordi):

        PIERRE = 0
        FEUILLE = 1
        CISEAUX = 2

        if joueur == PIERRE and ordi == FEUILLE:
            point = 1
        elif joueur == FEUILLE and ordi == CISEAUX:
            point = 1
        elif joueur == CISEAUX and ordi == PIERRE:
            point = 1
        elif joueur == PIERRE and ordi == CISEAUX:
            point = -1
        elif joueur == FEUILLE and ordi == PIERRE:
            point = -1
        elif joueur == CISEAUX and ordi == FEUILLE:
            point = -1
        else:
            point = 0

        return point

    for i in range(5):
        coup_j = int(input())
        coup_o = random.randint(0, 2)

        result = bat(coup_o, coup_j)
        point += result
        affichage_bat(result, coup_j, coup_o, point)
    affichage_manche(point)


pierre_feuille_ciseaux()
