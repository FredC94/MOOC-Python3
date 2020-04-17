"""
Écrivez un code qui lit un nombre entier strictement positif n et affiche sur n lignes
une table de multiplication de taille  n x n, avec, pour i entre 1 et n,
les n premières valeurs multiples de i strictement positives sur la ième ligne.

Ainsi, les n premiers multiples de 1 strictement positifs (0 non compris) sont affichés sur la première ligne,
les n premiers multiples de 2 sur la deuxième, et cætera.

"""
X = 1
Y = 1
Z = int(input())
for X in range(1,Z+1):
 while Y <= Z:
  print((X * Y), end=' ')
  Y+=1
 print()
 Y=1