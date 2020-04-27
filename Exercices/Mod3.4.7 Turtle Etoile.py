"""
Rappelons-nous (module 2 Activité 2.6.3) que pour dessiner un polygone à n côtés (par exemple n = 5),
l’angle intérieur entre deux côtés est de 360^{\circ}/n. Si n vaut 5 cela donne donc 72^{\circ}.

Rappelons-nous également que si l’on veut dessiner des étoiles à n branches et en supposant n impair au moins égal à 5,
l’angle intérieur sera de (n-1)*180^{\circ}/n (par exemple 144^{\circ} pour n valant 5).

import turtle
branche = int(input("Combien de branches: "))
angle = ((branche - 1) * 180 / branche)
print(angle)
for i in range(branche):
   turtle.forward(100)
   turtle.left(50)
 #  turtle.color(blue)
turtle.done()
"""

import turtle
from math import gcd # fonction du module math qui calcule le pgcd de 2 nombres

LONGUEUR = 100 # taille de chaque segment de l'étoile

n = int(input("Combien de branches désirez-vous ? :"))
inc = (n-1) // 2
while gcd(n, inc) > 1:
   inc = inc - 1
if inc == 1 :
   print("Impossible de dessiner une étoile à", n, "branches en un tenant")
else:
   angle =  180 - (n - 2 * inc) * 180 / n
   for i in range(n):
       turtle.forward(LONGUEUR)
       turtle.left(angle)
   turtle.done()