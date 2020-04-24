# Auteur: Frédéric CASTEL (Mars/Avril 2020)
"""
Exercices:

Consignes:

"""
# !/usr/bin/python
# -*- coding: utf-8 -*-
# importation des modules

import turtle
import math
from deformation import deformation as Deformation


def la_esfera_deformacion(punto_central_esfera_deformacion, su_radio):
    """
    Funcion auxiliar para visualizar la esfera de deformacion
    Entrada:un punto (x,y) el eje de la esfera y su radio
    """
    turtle.pencolor("green")
    turtle.up()
    turtle.goto(punto_central_esfera_deformacion[0], punto_central_esfera_deformacion[1] - su_radio)
    turtle.down()
    turtle.circle(su_radio)  # Trace un cercle de rayon 120px


def cuadrado(x=0, y=0, tamano=50):
    """
    Dibuja un cuadrado ABCD
    Entrada: La coordenada inferior izq. A y un lado o tamano
    """
    A = (x, y)
    B = (x + tamano, y)
    C = (x + tamano, y + tamano)
    D = (x, y + tamano)

    turtle.goto(A)  # Primer punto del cuadrado ABCD
    turtle.down()
    turtle.goto(B)  # Lado inferior A-B
    turtle.goto(C)  # Lateral derecho B-C
    turtle.goto(D)  # Lado Superior   C-D
    turtle.goto(A)  # Cierra el cuadrado , lado izquierdo  D-A


def cuadradoB(x=0, y=0, tamano=50, color='red'):  # Es una copia del anterior pero lo deformamos ...
    # Todo punto dentro de esta esfera lo deformamos
    # Si intentamos deformar un punto fuera de la esfera no se deforma asi que podemos aplicar siempre esto

    punto_central_esfera_deformacion = 0, 0, 0
    su_radio = 100

    la_esfera_deformacion(punto_central_esfera_deformacion, su_radio)  # Visualizo la esfera deformacion

    A = Deformation((x, y, 0), punto_central_esfera_deformacion, su_radio)[:2]
    B = Deformation((x + tamano, y, 0), punto_central_esfera_deformacion, su_radio)[:2]
    C = Deformation((x + tamano, y + tamano, 0), punto_central_esfera_deformacion, su_radio)[:2]
    D = Deformation((x, y + tamano, 0), punto_central_esfera_deformacion, su_radio)[:2]

    turtle.pencolor(color)
    turtle.up()
    turtle.goto(A)  # Prime punto cuadrado
    turtle.down()
    turtle.goto(B)  # Lado inferior
    turtle.goto(C)  # Lateral derecho
    turtle.goto(D)  # Lado Superior

    turtle.goto(A)  # Cierra el cuadrado , lado izquierdo


cuadrado()  # Cuadrado normal sin funcion deformacion
cuadradoB()  # Cuadrado con funcion deformacion, dentro del area de deformacion ,color rojo
cuadradoB(60, 60, 50,
          'blue')  # Cuadrado con funcion deformacion, con un punto dentro del area de deformacion ,color azul equivalente al anterior tamano 50 pero esta ex 60,60

turtle.done()