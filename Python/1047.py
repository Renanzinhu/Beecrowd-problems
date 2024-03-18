a, b, c, d = list(map(int,input().split()))
hm = ((c * 60) + d) - ((a * 60) + b)
if hm <= 0:
    hm +=24*60
h = hm // 60
m = hm % 60
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))
