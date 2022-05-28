c, q, v = input().split()
c2, q2, v2 = input().split()
q, q2, v, v2 = int(q), int(q2), float(v), float(v2)
print("VALOR A PAGAR: R$ {:.2f}".format((q*v)+(q2*v2)))
