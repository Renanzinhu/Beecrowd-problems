i, j = 1, 7
while i <= 9:
    print("I={} J={}".format(i, j))
    j -= 1
    if j == 4:
        i += 2
        j += 3