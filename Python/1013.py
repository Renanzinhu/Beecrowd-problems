a, b, c = map(int,input().split())
ab = ((a+b)+abs(a-b))//2
print("{} eh o maior".format(((ab+c)+abs(ab-c))//2))
