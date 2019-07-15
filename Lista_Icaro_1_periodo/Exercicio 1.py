# -*- coding: utf-8 -*-
"""
QUESTAO 1:
Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

@author: Júlio César Ribeiro de Moraes / Ciencia da Computação, Cesar School.
43"""

#---------PEGANDO AS VARIAVEIS-----
salario = float(input("Digite o salário do funcionario R$: "))
aumento_p = float(input("Digite quantos % de aumento o salario vai receber: "))

#---------FUNÇAO ERRO, NUMERO INCORRETO----
while aumento_p < 0:
    aumento_p = float(input("Aumento invalido! Digite um aumento maior que 0: "))
    
#-------CALCULOS PEDIDOS---------
aumento = salario*aumento_p/100
novo_salario = salario + aumento

#-------IMPRIMINDO RESULTADOS NA TELA--------
print("O funcionario recebeu um aumento de R$ {0:.2f} assim seu novo salario será de: R$ {1:.2f}".format(aumento, novo_salario))    
