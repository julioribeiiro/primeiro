"""
Recebe notas e coloca maior nota como 10

nova = nota*10 / nota
"""

notas = input("Digite as notas: ").split(" ")

notas.sort()

maior = float(notas[-1])

cont = 0
for i in notas:
	print("{}	{}	{:.1f}".format(cont+1, i, ((float(i)*10)/maior)))
	cont += 1