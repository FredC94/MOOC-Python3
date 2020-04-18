with  open('mots.txt', encoding = "utf-8") as fichier:
    total = 0
    cnt = 0
    for line in fichier:
        total = total + 1
        if 'e' not in line :
            print(line.strip())
            cnt = cnt + 1

print('Pourcentage de mots sans e:', cnt / total * 100.0, "pourcents")