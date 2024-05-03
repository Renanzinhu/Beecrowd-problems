a, i, j = 0, 1, 7
while i <= 9:
    print("I={} J={}".format(i, j))
    j -= 1
    a += 1
    if a == 3:
        a -= 3
        j += 5
        i += 2