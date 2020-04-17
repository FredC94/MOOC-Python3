"""
La suite de Fibonacci commence ainsi : 0  1  1  2  3  5  8  13  21  34  55  89  144  233  …
Ses deux premiers termes sont 0 et 1, et ensuite, chaque terme successif est la somme des deux termes précédents.
n = int(input('nombre de termes à calculer de la suite de Fibonacci : '))

Nous vous proposons d’écrire deux petits programmes qui calculent
et impriment les premiers termes de la suite de Fibonacci dans 2 cas de figure :"""

# pour les n premiers termes
n = int(input('nombre de termes à calculer de la suite de Fibonacci : '))
prec = 0
succ = 1
print(prec, end=" ")
print(succ, end=" ")
for i in range(n - 2):
    prec, succ = succ, prec + succ
    print(succ, end=" ")
print()

# pour tous les termes inférieurs à une valeur n donnée.
n = int(input('borne supérieur à ne pas dépasser pour calculer la suite de Fibonacci : '))
prec = 0
succ = 1
print(prec, end=" ")
while succ < n:
    print(succ, end=" ")
    prec, succ = succ, prec + succ
print()
