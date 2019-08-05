'''
alexandre 456123789
anderson 1245698456
antonio 123456456
carlos 91257581
cesar 987458
rosemary 789456125

ACME Inc. Uso do espaço em disco pelos usuários
---------------------------------------------------------------------
--
Nr. Usuário Espaço utilizado % do uso
1 alexandre 434,99 MB 16,85%
2 anderson 1187,99 MB 46,02%
3 antonio 117,73 MB 4,56%
4 carlos 87,03 MB 3,37%
5 cesar 0,94 MB 0,04%
6 rosemary 752,88 MB 29,16%
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

'''
def porcentagem(parte, total):
	porcent = (parte / total) * 100
	return round(porcent, 2)

def mb(byte):
	megabytes = byte/(1024*1024)
	return round(megabytes, 2)


arquivo = open("usuarios.txt")
usuarios = []


espaco_total = 0
for i in arquivo:
	usuarios.append(i.strip().split(" "))

for i in usuarios:
	espaco_total += int(i[1])

espaco_medio = espaco_total / len(usuarios)


relatorio = '''ACME Inc. Uso do espaço em disco pelos usuários
---------------------------------------------------------------------
Nr. 	Usuario 	Espaco utilizado 	%  do uso
'''

contador = 1
for i in usuarios:
	relatorio += "\n"+str(contador)+"\t"+i[0]+"\t"+str(mb(int(i[1])))+" MB"+"\t"+str(porcentagem(int(i[1]), espaco_total))+"%"
	contador += 1
relatorio += "\n"+"Espaco total ocupado: "+str(round(espaco_total,2))+" MB"+"\n"+"Espaco medio ocupado: "+str(round(espaco_medio,2))+" MB"

print(relatorio)
arquivo_relatorio = open("relatorio.txt", "w")
arquivo_relatorio.writelines(relatorio)
print("Arquivo atualizado com sucesso!!")



