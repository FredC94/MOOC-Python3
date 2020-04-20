def rac_eq_2nd_deg(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return ()
    elif delta == 0:
        return -b / (2 * a),
    else:
        racine = delta ** 0.5
        liste = [((-b - racine) / (2 * a)), ((-b + racine) / (2 * a))]
        return min(liste), max(liste)


print(rac_eq_2nd_deg(-3.5, -2.0, 4.5))
print(rac_eq_2nd_deg(1.0, 1.0, 1.0))
print(rac_eq_2nd_deg(1.0, -4.0, 4.0))
print(rac_eq_2nd_deg(1.0, 1.0, -2.0))
