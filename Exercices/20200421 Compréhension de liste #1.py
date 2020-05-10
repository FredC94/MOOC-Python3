ma_liste = []
for i in range(10):
    if i % 2 == 0:
        ma_liste.append(i)

# devient : ma_liste = [i for i in range(10) if i % 2 == 0]