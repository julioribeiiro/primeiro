palavra = input("Digite uma palavra: ")



def mutate(p):
	mutado = []
	alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
	p.lower()

	for i in range(len(p)):
		nova = p[:i]+p[i+1:]
		mutado.append(nova)

	for j in alfabeto:
		for i in range(len(p)):
			nova = p[:i]+j+p[i+1:]
			mutado.append(nova)

	for i in range(len(p) - 1):
		letra = p[i]
		letra2 = p[i+1]
		nova = p[:i] + letra2 + letra + p[i+2:]
		mutado.append(nova)


	print(mutado)

mutate(palavra)


