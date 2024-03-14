c, q = map(int,input().split())
t = [4.00, 4.50, 5.00, 2.00, 1.50]
v = (t[c-1])*q
print("Total: R$ {:.2f}".format(v))
