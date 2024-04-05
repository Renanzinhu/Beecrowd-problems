a, b, c, d = 0, 0, 0, 0 
for z in range(0,5):
    y = int(input())
    if y%2 == 0:
        a += 1
    if y%2 == 1:
        b += 1
    if y>0:
        c += 1
    if y<0:
        d += 1
print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(a,b,c,d))
