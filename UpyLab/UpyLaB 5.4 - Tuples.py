"""
Écrire une fonction distance_points() qui reçoit en paramètres deux tuples de deux composantes représentant les coordonnées
de deux points et qui retourne la distance euclidienne séparant ces deux points.
"""
from math import sqrt


def distance_points(x, y):
    # res = sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)
    res = sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    return float(res)


print(distance_points((-4, 3), (3.1, 4.1)))
print(distance_points((-2.0, 2.5), (-1.5, 1.0)))
print(distance_points((1.0, 1.0), (2.0, 1.0)))
print(distance_points((-1.0, 0.5), (2.0, 1.0)))
print(distance_points((-2.5, 1.0), (-1.5, 4.0)))
