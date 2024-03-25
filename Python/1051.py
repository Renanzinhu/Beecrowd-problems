r = float(input())
if r > 0 and r <= 2000.00:
    print("Isento")
elif r >= 2000.01 and r <= 3000.00:
    i = (r-2000) * 0.08
    print("R$ {:.2f}".format(i))
elif r > 3000.00 and r <= 4500.00:
    i = ((r-3000) * 0.18) + (1000 * 0.08)
    print("R$ {:.2f}".format(i))
elif r > 4500.00:
    i = ((r-4500) * 0.28) + (1000 * 0.08) + (1500 * 0.18)
    print("R$ {:.2f}".format(i))
