n = int(input())
print(n)
n100 = n // 100
n = n - n100100
n50 = n // 50
n = n - n5050
n20 = n // 20
n = n - n2020
n10 = n // 10
n = n - n1010
n5 = n // 5
n = n - n55
n2 = n // 2
n = n - n22
n1 = n // 1
n = n - n1*1
print("{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00".format(n100, n50, n20, n10, n5, n2, n1))
