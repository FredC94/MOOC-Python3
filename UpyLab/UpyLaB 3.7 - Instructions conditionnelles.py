mise = 10 #Somme fixe de 10 euros du joueur
pari = int(input())
numero = int(input())

if  pari == 13 and (numero == 0 or numero == 2 or numero == 4 or numero == 6 or numero == 8 or numero == 11):
    print (2 * mise)
elif pari == 14 and (numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9):
    print(2 * mise)
elif pari == 15 and (numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9):
    print(2 * mise)
elif pari == 16 and (numero == 2 or numero == 4 or numero == 6 or numero == 8 or numero == 11):
    print (2 * mise)
elif pari <= 12 and (pari == numero):
    print(12 * mise)
else:
    print("0")




