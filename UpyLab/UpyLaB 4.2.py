def soleil_leve(a, b, c):
    if a == 0 and b == 0:
        return True
    elif a == 12 and b == 12:
        return False
    elif c > b and b > a:
        return False
    elif b == c and c != a:
        return False
    elif c < a and a < b:
        return False
    elif c > b and c < a:
        return False
    elif c >= a and c < b:
        return True
    elif a > b and c > a and c > b:
        return True
    elif c < b and b < a:
        return True


print(soleil_leve(12, 12, 23))




