from math import sqrt


def premier(n):
    """ renvoie vrai si n est un nombre premier"""
    if n == 2:
        return True
    elif n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


x = int(input())
for i in range(x + 1):
    if premier(i):
        print(i)
