'''
QUESTAO matriz
'''
'''
matriz = [['ALUNO A', 4, 123, 5.0, 4.0, 0.5], 
['ALUNO B', 4, 1234, 6.0, 8.0, 0.5],
['ALUNO C', 6, 1235, 3.2, 6.9, 0],
['ALUNO D', 0, 1236, 0.8, 6.9, 0.2],
['ALUNO E', 2, 1237, 0.9, 2.5, 1.0]]
'''

#----LETRA A------

print("--------LETRA A----------\n\n")

qtd_alunos = int(input("Digite a quantidade de alunos: "))

matriz = list() # CRIA UMA VARIAVEL CHAMADA MATRIZ COMO UMA LISTA


#ADICIONA DUAS LISTAS DENTRO DA LISTA MATRIZ 
for i in range(qtd_alunos):
	matriz.append([])


for i in range(qtd_alunos):
	nome = input("Digite o nome do aluno: ")
	matriz[i].append(nome)

	quantidade_faltas = int(input("Digite a quantidade de faltas: "))
	matriz[i].append(quantidade_faltas)

	matricula = int(input("Digite a matricula do aluno: "))
	matriz[i].append(matricula)

	primeira_nota = float(input("Digite a primeira nota do aluno: "))
	matriz[i].append(primeira_nota)

	segunda_nota = float(input("Digite a segunda nota do aluno: "))
	matriz[i].append(segunda_nota)

	extra_nota = float(input("Digite a nota extra do aluno: "))
	matriz[i].append(extra_nota)

	matriz[i].append((primeira_nota + segunda_nota + extra_nota) / 2 ) #PARTE DA LETRA B



print("\n\n---------LETRA B------------\n\n")
print(matriz)

for i in matriz:
	if i[6] >= 5.0 and i[1] <= 10: #VERIFICA CADA LINHA DA MATRIZ
		print("Aluno:", i[0]+": ", "Aprovado")
	else:
		print("Aluno:", i[0]+": ", "Reprovado")


print("\n\n----------LETRA C--------------\n\n")


maior_media = -1

menor_media = 112312

#----VERIFICA A MEDIA DE CADA LINHA-------

for i in matriz:
	if i[6] > maior_media:
		maior_media = i[6]
		maior_media_matricula = i[2]


	if i[6] < menor_media:
		menor_media = i[6]
		menor_media_matricula = i[2]

print("Maior media:", maior_media, "Matricula:", maior_media_matricula, "\nMenor media: ", menor_media, "Matricula:", menor_media_matricula)
















