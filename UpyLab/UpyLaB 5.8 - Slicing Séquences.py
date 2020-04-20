def prime_numbers(nb):
    if type(nb) != int or nb < 0:
        liste = None
    else:
        k = 2
        liste = []
        while len(liste) < nb:
            test = True
            for j in range(2, k - 1):
                print(j)
                if k % j == 0:
                    test = False
                    break
            if test:
                liste.append(k)
            k += 1
    return liste


print(prime_numbers(10))
