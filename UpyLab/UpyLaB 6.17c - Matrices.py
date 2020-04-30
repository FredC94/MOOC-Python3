def check_regions(matrice):
    somme = 0
    for line in range(3):
        start = 0
        for col in range(start, 9):
            print(matrice[col][line])
            
            #somme += matrice[col][line]

    if somme != 45:
        return False
    else:
        return True


# j = (i // 3) * 3
# k = (i % 3) * 3



print(check_regions([[9, 6, 3, 1, 7, 4, 2, 5, 8], # retourne True
              [1, 7, 8, 3, 2, 5, 6, 4, 9],
              [2, 5, 4, 6, 8, 9, 7, 3, 1],
              [8, 2, 1, 4, 3, 7, 5, 9, 6],
              [4, 9, 6, 8, 5, 2, 3, 1, 7],
              [7, 3, 5, 9, 6, 1, 8, 2, 4],
              [5, 8, 9, 7, 1, 3, 4, 6, 2],
              [3, 1, 7, 2, 4, 6, 9, 8, 5],
              [6, 4, 2, 5, 9, 8, 1, 7, 3]]))