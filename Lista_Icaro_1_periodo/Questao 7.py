# -*- coding: utf-8 -*-
"""
A maioria dos anos tem 365 dias. No entanto, o tempo necessário para a Terra orbitar
o Sol é na verdade um pouco mais que isso. Como resultado, um dia extra, 29 de fevereiro, 
está incluído em alguns anos para corrigir essa diferença. Esses anos são referidos como anos bissextos.
As regras para determinar se um ano é ou não um ano bissexto seguem:
• Qualquer ano que seja divisível por 400 é um ano bissexto.
• Dos anos restantes, qualquer ano que seja divisível por 100 não é um ano bissexto.
• Dos anos restantes, qualquer ano que seja divisível por 4 é um ano bissexto.
• Todos os outros anos não são anos bissextos.
Escreva um programa que leia um ano do usuário e exiba uma mensagem indicando se é ou não um ano bissexto.

@author: Júlio César Ribeiro de Moraes
"""


ano = int(input("Digite o ano: "))

if ano % 400 == 0:
    print("Este eh um ano bissexto.")
    
elif ano % 100 == 0:
    print("Este nao eh um ano bissexto.")
    
elif ano % 4 == 0:
    print("Este eh um ano bissexto.")
    
else:
    print("Este nao eh um ano bissexto.")
    
