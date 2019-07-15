# -*- coding: utf-8 -*-
"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
 
@author: Júlio César Ribeiro de Moraes
"""

casa = float(input("Digite o valor total da casa: "))
salario = float(input("Digite qual eh o seu salario: "))
anos = int(input("Digite a quantidade de anos que voce vai pagar a casa: "))
anos = float(anos)

prestacao = (casa / (anos*12))

if prestacao > salario*0.3:
    print("A prestacao mensal eh de: {:.2f}, e 30% do seu salario eh: {:.2f}.\nEmprestimo nao pode ser aprovado.".format(prestacao, salario*0.3))
else:
    print("A prestacao mensal eh de: {:.2f}, e 30% do seu salario eh: {:.2f}.\nSeu emprestimo sera aprovado.".format(prestacao, salario*0.3))