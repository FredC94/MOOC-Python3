# utiliser des fichiers
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/232431-utilisez-des-fichiers
import os
os.chdir("C:/")
mon_fichier = open("fichier.txt", "r")
contenu = mon_fichier.read()
print(contenu)
mon_fichier.close()