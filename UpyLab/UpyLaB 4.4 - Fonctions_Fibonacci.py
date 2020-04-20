def fibo(n):
    if n < 0:
        return None
    temp = 1
    v = 0
    for i in range(n):
        v = v + temp  # ou v += temp
        temp = v - temp  # or à ce stade v = v + temp, il faut donc soustraire temp
    return v


x = int(input())
for i in range(x):
    print(fibo(i))
