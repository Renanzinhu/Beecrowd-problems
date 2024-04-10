a, b, z = int(input()), int(input()), 0
for x in range(b+1, a):
    if x%2 == 1:
        z+= x    
print(z)
