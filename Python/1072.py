z, y = 0, 0
a = int(input())
for w in range(a):
    b = int(input())
    if b>=10 and b<=20:
        z += 1
    else:
        y += 1
print("{} in\n{} out".format(z, y))
