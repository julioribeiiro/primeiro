# -*- coding: utf-8 -*-
"""
Implementar um programa que calcula o desconto previdenciário de um funcionário.
O programa deve, dado um salário, retornar o valor do desconto proporcional ao mesmo.
O cálculo de desconto segue a regra: o desconto deve 11% do valor do salário, entretanto, o valor máximo de desconto é 318,20.
Sendo assim, ou o programa retorna 11% sobre o salário ou 318,20.

@author: Júlio César Ribeiro de Moraes
"""

salario = float(input("Digite o salario do funcionario: "))
desconto = salario*0.11
if desconto > 318.20:
    print("O desconto que o funcionario recebera eh o desconto maximo, R$318,20")
else:
    print("O desconto que o funcionario recebera eh de: R${:.2f}".format(desconto))
