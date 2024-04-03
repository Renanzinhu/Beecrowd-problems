p = 0
y = 0
for z in range(0,6):
    a = float(input())
    if a > 0:
        p += 1
        y += a
print("{} valores positivos\n{:.1f}".format(p, y/p))
