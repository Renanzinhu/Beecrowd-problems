a = int(input())
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(a//365, (a-((a//365)*365))//30, (a-((a//365)*365))-(((a-((a//365)*365))//30)*30)))


# beautiful code
#x = int(input())
#a = x//365
#m = (x-a*365)//30
#d = (x-a*365)-(m*30)
#print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(a, m, d)
