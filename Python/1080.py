t = 0
for x in range(0, 100):
    n = int(input())
    if n > t:
        m = n
        p = x + 1
        t = n
print("{}".format(m))
print("{}".format(p))
