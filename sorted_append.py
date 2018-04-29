a = [34, 2, -3, 7, 13]
x = [42, 0, 121, 1, 41]
mi = []
ma = []
b = sorted(a)
b.append(11)

print(a)
print(b)

for x in range(4):
    mi.append(a[x])

for x in range(4, 0, -1):
    ma.append(a[x])

print(mi)
print(ma)
