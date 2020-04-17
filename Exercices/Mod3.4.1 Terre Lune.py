DISTANCE = 3844.0e5
nombre_pliages = 0
epaisseur = 0.0001
while epaisseur < DISTANCE :
   epaisseur = 2 * epaisseur
   nombre_pliages = nombre_pliages + 1
print('nombre de pliages nécessaire : ', nombre_pliages)