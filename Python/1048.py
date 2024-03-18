s = float(input())
if s > 0 and s <= 400.00:
    r = (15/100) * s
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(s+r, r, 15))
elif s > 400.00 and s <= 800.00:
    r = (12/100) * s
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(s+r, r, 12))
elif s > 800.00 and s <= 1200.00:
    r = (10/100) * s
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(s+r, r, 10))
elif s > 1200.00 and s <= 2000.00:
    r = (7/100) * s
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(s+r, r, 7))
elif s > 2000.00:
    r = (4/100) * s
    print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(s+r, r, 4))
