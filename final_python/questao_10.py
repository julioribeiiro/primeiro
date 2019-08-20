
d = {1: 2, 3: 4, 4: 2, 5: 2, 6:7}


def inva(dic):
	inverso = {}
	for i in dic:
		inverso[dic[i]] = [] #dic[i] sera o valor que cada chave do dicionario possui
							 #e para cada valor eu crio uma lista vazia
							 #para que possamos dar append
	
	for i in dic:
		inverso[dic[i]].append(i) #depois que nos temos o dicionario com as listas vazias
								  #basta dar append nos valores
	print(inverso)

inva(d)
