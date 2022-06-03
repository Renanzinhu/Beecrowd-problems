a = int(input())
h = a//3600
print("{}:{}:{}".format(h, (a-h*3600)//60, (a-h*3600)-((a-h*3600)//60)*60))


# beautiful code
#a = int(input())
#h = a//3600
#m = (a-h*3600)//60
#s = (a-h*3600)-(m*60)
#print("{}:{}:{}".format(h, m, s))
