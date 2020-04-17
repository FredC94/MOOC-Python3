from math import factorial

x = float(input())
index = 3  # premier entier
exp = 2  # on commence par le signe +
terme = 10
temp = 0

while abs(terme) > 10e-6:
    terme = ((-1) ** exp) * (((x) ** index) / factorial(index))
    temp = terme + temp
    index = index + 2  # incrément de +2 pour changer l'entier dans la boucle
    exp = exp + 1  # incrément de +1 pour changer de signe à chaque tour de boucle
print(x - temp)