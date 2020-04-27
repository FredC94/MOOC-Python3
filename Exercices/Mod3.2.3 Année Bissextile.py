"""Depuis l’ajustement du calendrier grégorien, l’année sera bissextile :
    si l’année est divisible par 4 et non divisible par 100, ou
    si l’année est divisible par 400.
Sinon, l’année n’est pas bissextile."""

annee = int(input("Donnez l'année à tester :"))
if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    print('bissextile')
else:
    print('non bissextile')