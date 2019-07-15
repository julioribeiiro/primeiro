# -*- coding: utf-8 -*-
"""
QUESTAO 4:
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e # R$ 0,15 por km rodado.

@author: Júlio César Ribeiro de Moraes / Ciencia da Computação, Cesar School.
"""
#----COLETANDO DADOS----
km = float(input("Digite quantos KM voce percorreu com o carro: "))
dias = int(input("Digite quantos dias voce ficou com o carro: "))
dias = float(dias)

#------CALCULO + IMPRESSAO DE RESULTADO---------
print("Preço total: R${:.2f}".format(dias*60 + km*0.15))
