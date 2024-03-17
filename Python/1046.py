a, b = map(int,input().split())
if a < b:
    c = b - a
else:
    c = (24 - a) + b
print("O JOGO DUROU {} HORA(S)".format(c))
