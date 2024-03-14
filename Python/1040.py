n1,n2,n3,n4 = map(float,input().split()) 
m = ((n1*2)+(n2*3)+(n3*4)+n4)/10
print("Media: {:.1f}".format(m))
if m >= 7.0:
    print("Aluno aprovado.")
if m >= 5.0 and m <= 6.9:
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame: {}".format(ne))
    mf = (ne+m)/2
    if mf >= 5.0:
        print("Aluno aprovado.\nMedia final: {:.1f}".format(mf))
    if mf <=4.9:
        print("Aluno reprovado.\nMedia final: {:1.f}".format(mf))
if m <= 4.9:
    print("Aluno reprovado.")
