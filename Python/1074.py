a = int(input())
for z in range(a):
    b = int(input())
    if b%2 == 0 and b>0: print("EVEN POSITIVE")
    if b%2 == 1 and b>0: print("ODD POSITIVE")
    if b%2 == 0 and b<0: print("EVEN NEGATIVE")
    if b%2 == 1 and b<0: print("ODD NEGATIVE")
    if b == 0: print("NULL")
