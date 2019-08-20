"""
JOGO DA FORCA
"""

e = 0
venceu = 0

palavra = input("Digite a palavra secreta: ")

palavra = list(palavra)

resposta = list()

for i in palavra:
	resposta.append("_")

#---------IMPRIME A FORCA DE ACORDO COM OS ERROS--------------------------------

def imprime():
	global palavra
	global e
	global resposta
	if e == 0:
		print("\n----------|\n|         |\n|         |\n|         O\n|        /|\ \n|        /\ \n|\n|\n|\n{}".format(resposta))
	elif e == 1:
		print("----------|\n|         |\n|         |\n|         O\n|        /|\n|        /\n|\n|\n|{}".format(resposta))
	elif e == 2:
		print("----------|\n|         |\n|         |\n|         O\n|        /|\ \n|         \n|\n|\n|\n{}".format(resposta))
	elif e == 3:
		print("\n----------|\n|         |\n|         |\n|         O\n|         |\ \n|        \n|\n|\n|\n{}".format(resposta))
	elif e == 4:
		print("\n----------|\n|         |\n|         |\n|         O\n|         |\n|        \n|\n|\n|\n{}".format(resposta))
	elif e == 5:
		print("\n----------|\n|         |\n|         |\n|         O\n|        \n|        \n|\n|\n|\n{}".format(resposta))
	elif e == 6:
		print("\n----------|\n|         |\n|         |\n|         \n|        \n|        \n|\n|\n|\n{}\nVoce perdeu!!".format(resposta))

#--------------VERIFICA SE HOUVE ERROS OU ACERTOS E VITORIA--------------------------

def verifica():
	global e
	global letra
	global resposta
	global palavra
	global venceu
	erro = 0
	verifica = 0
	for i in range(len(palavra)):
		if letra == palavra[i]:
			resposta[i] = palavra[i]
		else:
			erro += 1
	if erro == len(palavra):
		e += 1
	for i in range(len(palavra)):
		if palavra[i] == resposta[i]:
			verifica += 1
	if verifica == len(palavra):
		print("Voce venceu!")
		venceu = 1
#----------JOGO------------------
imprime()
while e != 6 and venceu == 0:
	letra = input("Digite uma letra: ")
	verifica()
	imprime()





















