# -*- coding: utf-8 -*-
"""
Questão 1:
Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.

@author: Júlio César Ribeiro de Moraes
"""
maior = -9999999999999999999
menor = 99999999999999999999


for i in range(5):
    numero = int(input("Digite o {}° numero: ".format(i+1)))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("O maior numero foi: {} e o menor numero foi: {}".format(maior, menor))
    