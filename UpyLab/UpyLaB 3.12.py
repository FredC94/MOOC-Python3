nbr = int(input())
lettre = "X"
y = 0
z = 0
nbr2 = nbr
print (nbr2 * lettre)
espace = " "
while y != nbr:
#   print ((z * (" ")), nbr2 * lettre)
    print("", nbr2 * lettre, sep=z * espace, end='\n')
    y = y + 1
    z = z + 1
    nbr2 = nbr2 -1


espace = " "
print("", nbr2 * lettre, sep=espace, end='\n')