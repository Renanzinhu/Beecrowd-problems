p = 0
for x in range(5):
    n = int(input())
    np = n%2
    if np == 0:
        p += 1
print("{} valores pares".format(p))
