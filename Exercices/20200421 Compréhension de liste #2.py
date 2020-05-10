res = []
m = 10
n = 8
for i in range(m):
    res.append([])
    for j in range(n):
        res[i].append(0)

# devient : res = [0 for i in range(m) for j in range(n)]