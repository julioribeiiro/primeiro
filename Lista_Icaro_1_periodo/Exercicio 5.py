# -*- coding: utf-8 -*-
"""
QUESTÃO 5
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
@author: Júlio César Ribeiro de Moraes / Ciencia da Computação, Cesar School.
"""
#---------COLETANDO DADOS-------
ci_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Digite quantos anos ja fumou: "))

#------CALCULOS PEDIDOS--------
minutos = anos*365*ci_dia*10
dias = minutos/(24*60)

#-------IMPRESSAO DO RESULTADO--------
print("O fumante ja perdeu {0:.2f} dias da sua vida!".format(dias))
