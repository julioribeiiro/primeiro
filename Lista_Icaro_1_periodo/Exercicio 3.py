# -*- coding: utf-8 -*-
"""
QUESTAO 3:
Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento da circunferência.
Solicite que o usuário insira o raio e imprima uma mensagem agradável de volta para o usuário com a resposta.

@author: Júlio César Ribeiro de Moraes / Ciencia da Computação, Cesar School.
"""
#------FUNCAO MATH PARA USAR O PI------
from math import *

#------COLETANDO DADOS-----
raio = float(input("Digite o raio da circunferencia: "))

#------CALCULOS PEDIDOS---------
area = pi*raio**2
comprimento = 2*pi*raio

#-----IMPRESSAO DOS RESULTADOS-------
print("Area = {:.2f} u^2".format(area), "\nComprimento = {:.2f} u".format(comprimento), "\nDiamentro = {:.2f} u".format(raio*2), "\nu = unidade de comprimento qualquer")


