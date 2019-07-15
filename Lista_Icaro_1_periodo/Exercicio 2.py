# -*- coding: utf-8 -*-
"""
QUESTAO 2:
Escreva um programa que converta uma temperatura digitada em °C (graus celsius) # para °F (graus fahrenheit).

@author: Júlio César Ribeiro de Moraes / Ciencia da Computação, Cesar School.
"""

#---------MENU---------------
continuar = 1
menu = 0
while(continuar == 1):
    while menu != 1 and menu != 2:
        print("Digite 1 para transformar graus celsius(°C) em fahrenheit(°F)\nDigite 2 para transformar graus fahrenheit(°F) em celsius(°C):", end ="")
        menu = int(input("Resposta: "))
        
#-------TRANSFORMAÇÕES PEDIDAS + IMPRESSAO DA RESPOSTA------
    if menu == 1:
        celsius = float(input("Digite a temperatura em graus celsius(°C): "))
        print("A temperatura em fahrenheit é de: {:.2f}°F".format((celsius*9/5)+32))
    if menu == 2:
        fah = float(input("Digite a temperatura em graus fahrenheit(°F): "))
        print("A temperatura em graus celsius é de: {:.2f}°C".format((fah - 32)*5/9))
        
#--------FUNÇÃO PARA FAZER OUTRA CONVERSÃO--------
    continuar = int(input("Deseja fazer outra conversão? Digite 1 para sim, 2 para nao: "))
    menu = 0
