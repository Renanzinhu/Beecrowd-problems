a, b, t, c, r, s = int(input()), [], 0, 0, 0, 0
for z in range(a):
    d = list(input().split())
    b.append(d)
    b[z][0] = int(b[z][0])
    t += b[z][0]
for x in range(a):
    if "C" in b[x][1]: c += b[x][0]
    if "R" in b[x][1]: r += b[x][0]
    if "S" in b[x][1]: s += b[x][0] 
print("Total: {} cobaias".format(t))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))
print("Percentual de coelhos: {:.2f} %".format((c/t)*100))
print("Percentual de ratos: {:.2f} %".format((r/t)*100))
print("Percentual de sapos: {:.2f} %".format((s/t)*100))
