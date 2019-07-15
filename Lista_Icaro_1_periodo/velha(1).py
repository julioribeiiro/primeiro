'''
Questao valendo 0.5
Dupla: 
Julio Cesar Ribeiro de Moraes
Luis Arthur Dornelas
'''

#-------criando tabuleiro--------------
tabuleiro = ([0,0,0],[0,0,0],[0,0,0])

#-----funcao atualiza tabuleiro--------

def tabuleiro_at():
	global tabuleiro
	for i in range(len(tabuleiro)):
		for j in range(len(tabuleiro[i])):
			print(tabuleiro[i][j], end = '  ')
		print('')

def verifica():
	global tabuleiro
	global vitoria
	global contador

#------VERIFICANDO VITORIA POR LINHA---------------

	for i in tabuleiro:
		if i[0] == i[1] and i[0] == i[2]:
			if i[0] == 'X':
				print('Vitoria do jogador 1!')
				vitoria = True
			elif i[0] == 'O':
				print('Vitoria do jogador 2!')
				vitoria = True

#------VERIFICANDO VITORIA POR COLUNA--------------

	for i in range(3):
		if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]:
			if tabuleiro[0][i] == 'X':
				print('Vitoria do jogador 1!')
				vitoria = True
			elif tabuleiro[0][i] == 'O':
				print('Vitoria do jogador 2!')
				vitoria = True
#-------VERIFICANDO DIAGONAL-----------------------

	if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]:
		if tabuleiro[0][0] == 'X':
			print('Vitoria do jogador 1!')
			vitoria = True
		elif tabuleiro[0][0] == 'O':
			print('Vitoria do jogador 2!')
			vitoria = True
	elif contador == 8:
		print('EMPATE!')
		vitoria = True

	elif tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0]:
		if tabuleiro[0][2] == 'X':
			print('Vitoria do jogador 1!')
			vitoria = True
		elif tabuleiro[0][2] == 'O':
			print('Vitoria do jogador 2!')
			vitoria = True
	elif contador == 9:
		print('EMPATE!')
		vitoria = True
	print(contador)


#---------INICIANDO JOGADAS---------
vitoria = False
jogada = 1
contador = 0
tabuleiro_at()
print('As jogadas devem ser digitadas no formato Linha,Coluna')
while vitoria != True:
	while jogada == 1:
		jogador1 = input('Jogador 1 digite sua jogada: ').split(',')
		if tabuleiro[int(jogador1[0])][int(jogador1[1])] == 0:
			tabuleiro[int(jogador1[0])][int(jogador1[1])] = 'X'
			jogada = 2
		else:
			print('Digite uma jogada valida!')
	tabuleiro_at()
	verifica()
	contador += 1
	if vitoria == True:
		break
	while jogada == 2:
		jogador2 = input('Jogador 2 digite sua jogada: ').split(',')
		if tabuleiro[int(jogador2[0])][int(jogador2[1])] == 0:
			tabuleiro[int(jogador2[0])][int(jogador2[1])] = 'O'
			jogada = 1
		else:
			print('Digite uma jogada valida!')
	tabuleiro_at()
	verifica()
	contador += 1




