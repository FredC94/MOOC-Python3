a = int(input())
b = int(input())
c = int(input())

def deux_egaux(a, b, c):
    if a==b or b==c or a==c:
        return True
    else:
        return False

print(deux_egaux())

