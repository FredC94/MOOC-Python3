from math import sqrt


def NombreFacteur(N):
    count = 2
    racine = sqrt(N)
    I = 2
    while I <= racine:
        if N % I == 0:
            count = count + 1
        I = I + 1
    return count


def premier(N):
    return NombreFacteur(N) == 2


def NombrePremierPlusPetit(N):
    Count = 0
    I = 2
    while I < N:
        if Premier(I):
            Count = Count + 1
        I = I + 1
    return Count


print("Liste des nombres premier avant 1000: ")
I = 2
while I < 1000:
    if Premier(I):
        print(str(I) + " ", end="")
    I = I + 1
print
print("Nombre de nombre premier avant 1000: ", end="")
print(str(NombrePremierPlusPetit(1000)))