n = int(input("Digite o numero: "))
b = 2
p = 0


while abs(n - p**2) > 0.0001:
	print("entrou")
	p = (b+(n/b))/2
	b = p
print("A raiz quadrada de {} eh {:.3f}".format(n, p))