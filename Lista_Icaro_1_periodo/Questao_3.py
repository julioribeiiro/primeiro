"""
QUESTÃO 3
Um robô se move em um plano a partir do ponto original (0,0). O robô pode se mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um passo fornecido. 
O traço do movimento do robô é mostrado da seguinte forma:

CIMA 5
BAIXO 3
ESQUERDA 3
DIREITA 2

Os números após a direção são passos. Escreva um programa para calcular a distância entre a posição atual e o ponto original após uma seqüência de movimentos. 
Se a distância for um float, basta imprimir o inteiro mais próximo.
Exemplo:
Se as seguintes tuplas são dadas como entrada para o programa:

CIMA 5
BAIXO 3
ESQUERDA 3
DIREITA 2

Então, a saída do programa deve ser:
2

Dicas:
As entradas devem ser lidas do console até que um valor vazio seja digitado. A saída deve ser um inteiro que representa a distancia para o ponto original. 
Entradas inválidas devem ser descartadas da contagem.

"""

movimento = 1
x = 0
y = 0
while movimento != [""]:
	movimento = input("Digite o movimento: ")
	movimento = movimento.split(" ")
	if movimento[0] == "CIMA":
		y += int(movimento[1])
	elif movimento[0] == "BAIXO":
		y -= int(movimento[1])
	elif movimento[0] == "ESQUERDA":
		x -= int(movimento[1])
	elif movimento[0] == "DIREITA":
		x += int(movimento[1])
distancia = int((x**2 + y**2)**(1/2))

print(distancia)
