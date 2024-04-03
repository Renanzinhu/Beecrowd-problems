t, d = input().split()
d = int(d)
h, m, s, = map(int,input().split(":"))
t2, d2 = input().split()
d2 = int(d2)
h2, m2, s2, = map(int,input().split(":"))
h3 = h2 - h
m3 = m2 - m
s3 = s2 - s
d3 = d2 - d
if s3 < 0:
    s3 += 60
    m3 -= 1
if m3 < 0:
    m3 += 60
    h3 -= 1
if h3 < 0:
    h3 += 24
    d3 -= 1
print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(d3, h3, m3,s3))
