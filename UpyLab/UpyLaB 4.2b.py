def soleil_leve(lever, coucher, heure):
    cas1 = lever == coucher == 0
    cas2 = lever <= heure < coucher
    cas3 = coucher < lever and (heure < coucher or lever <= heure)
    return cas1 or cas2 or cas3


lE1515 = int(input())  # lever_e1515
cE1515 = int(input())  # coucher_e1515
lE666 = int(input())  # lever_e666
cE666 = int(input())  # coucher_e666

for heure in range(24):
    if soleil_leve(lE1515, cE1515, heure) or soleil_leve(lE666, cE666, heure):
        print(heure)
    else:
        print(heure, '*')
