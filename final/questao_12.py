'''
PARA UM IP SER VALIDO ELE SO PODE
POSSUIR NUMEROS DE 0 ATE 255

arquivo =
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
192.168.0.256

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4
[Endereços inválidos:]
257.32.4.5
85.345.1.2
192.168.0.256
'''


arquivo = open("ips")

ips = []

for i in arquivo:
	ips.append(i.strip())


validos = []
invalidos = []
lista_auxiliar = []
verifica_invalido = 0


for i in ips:
	lista_auxiliar = i.split('.')
	for j in lista_auxiliar:
		if int(j) > 255:
			verifica_invalido += 1
	if verifica_invalido > 0:
		invalidos.append(i)
	else:
		validos.append(i)
	verifica_invalido = 0

novo_arquivo = ''

novo_arquivo += "[Endereços válidos:]"
for i in validos:
	novo_arquivo+="\n"+i

novo_arquivo += "\n[Endereços inválidos:]"

for i in invalidos:
	novo_arquivo+="\n"+i

escreve_arquivo = open("validos_invalidos.txt", "w")

escreve_arquivo.writelines(novo_arquivo)

print(novo_arquivo)
print("Arquivo atualizado com sucesso!!")


















