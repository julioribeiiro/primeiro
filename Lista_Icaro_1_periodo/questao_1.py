arq = open("acidentes2017.csv", "r")
dados = []

for i in arq:
	dados.append(i.split(';'))

print("Arquivo antigo: ", len(dados), "linhas")
var = 0
for i in dados:
	if i[4] == '':
		dados.pop(var)
	var += 1

print("Arquivo novo: ", len(dados), "linhas")

novo = ''
for i in dados:
	novo += ";".join(i)

arq_novo = open("acidentes2017_limpo.csv", "w")


arq_novo.writelines(novo)

print("acidentes2017_limpo.csv criado com sucesso!")