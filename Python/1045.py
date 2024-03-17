x = list(map(float,input().split()))
a, b, c = sorted(x)[::-1]
tt = True
if (a >= b+c):
    print("NAO FORMA TRIANGULO")
    tt = False
if (a**2 == (b**2) + (c**2) and tt):
    print("TRIANGULO RETANGULO")
if (a**2 > (b**2) + (c**2) and tt):
    print("TRIANGULO OBTUSANGULO")
if (a**2 < (b**2) + (c**2) and tt):
    print("TRIANGULO ACUTANGULO")
if (a == b and b == c and tt):
    print("TRIANGULO EQUILATERO")
if ((a == b != c) or (b == c != a) or (a == c != b) and tt):
    print("TRIANGULO ISOSCELES")
