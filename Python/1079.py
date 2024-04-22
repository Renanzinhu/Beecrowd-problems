a = int(input())
for z in range(a):
    b, c, d = map(float,input().split())
    m = ((b*2)+(c*3)+(d*5))/10
    print("{:.1f}".format(m))
