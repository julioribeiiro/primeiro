"""
Sequencia fibonacci

F(n) = 0 if n == 0
F(n) = 1 if n == 1
F(n) = F(n - 1) + F(n - 2)  if n > 1


"""

a = 0
b = 1
aux = 0

n = int(input("Digite o numero da sequencia fibonacci: "))

for i in range(0, n):
	if i == 0:
		print("0", end = ", ")
	elif i == 1:
		print("1", end = ", ")

	else:
		print(a + b, end =", ")
		aux = b
		b = b + a
		a = aux

