lst = []
num = int(input('How many numbers: '))
if num >=0:
    for n in range(num):
        numbers = int(input('Enter number '))
        lst.append(numbers)
    print("Sum of elements in given list is :", sum(lst))
elif num < 0:
    somme = 0
    numbers = 0
    while numbers != 'F':
        # numbers = int(input('Enter number '))
        numbers = input('Enter number ')
        if numbers == 'F':
            print(int(somme))
        else:
            somme = int(numbers) + somme


#pour upylab
lst = []
num = int(input())
if num >=0:
    for n in range(num):
        numbers = int(input())
        lst.append(numbers)
    print(sum(lst))
elif num < 0:
    somme = 0
    numbers = 0
    while numbers != 'F':
        numbers = input()
        if numbers == 'F':
            print(int(somme))
        else:
            somme = int(numbers) + somme

###partie du corrigé
valeur_suivante = input()
while valeur_suivante != 'F':
      somme += int(valeur_suivante)
      valeur_suivante = input()
