import math
x, y = map(float,input().split())
x2, y2 = map(float,input().split())
d = math.sqrt(((x2-x)**2)+((y2-y)**2))
print("{:.4f}".format(d))
