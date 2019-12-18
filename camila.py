quantidade = 0
maior = -1
menor = 11
nome_maior = ""
nome_menor = ""

while quantidade < 2:
	nome = input("Qual o nome?\n")
	nota = float(input("Qual a nota?\n"))

	if nota > maior:
		maior = nota
		nome_maior = nome


	if nota < menor:
		menor = nota
		nome_menor = nome 

	quantidade += 1

print("\nA maior nota é",maior,"e o nome do aluno é",nome_maior)
print("\nA menor nota é",menor,"e o nome do aluno é",nome_menor)






