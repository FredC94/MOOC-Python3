def historique_tempetes(vent_max):
    """affiche pour chaque année la catégorie de vents subis cette année-là
   entrée : vent_max: liste des vents maximums enregistrés en km/h
   chaque année (composante 0 étant pour l'an 2000)"""

    annee = 2000
    for vent in vent_max:
        if vent < 64:
            print("En", annee, ": pas de tempête enregistrée")
        elif vent < 119:
            print("En", annee, ": il y a eu au moins une tempête mais pas de cyclone")
        else:
            print("En", annee, ": le plus gros cyclone enregistré était de catégorie",
                  categorie(vent))
        annee += 1

        def categorie(vent):
            """renvoie la catégorie de cyclone enregistré en fonction du vent"""

            assert vent > 118  # sinon provoque une erreur dans le code

            if vent < 154:
                res = 1
            elif vent < 178:
                res = 2
            elif vent < 210:
                res = 3
            elif vent < 251:
                res = 4
            else:  # catégorie 5
                res = 5
            return res
