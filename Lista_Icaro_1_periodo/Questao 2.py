# -*- coding: utf-8 -*-
"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
1 - "Telefonou para a vítima?"
2 - "Esteve no local do crime?"
3 - "Mora perto da vítima?"
4 - "Devia para a vítima?"
5 - "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
 Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
 entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"

@author: Júlio César Ribeiro de Moraes
"""

participacao = 0

#---------SOMANDO A QUANTIDADE DE RESPOSTAS POSITIVAS

print("Digite todas as respostas com sim ou nao")
resposta = input("Telefenou para a vitima? ")
if resposta == 'sim':
    participacao += 1

resposta = input("Esteve no local do crime? ")
if resposta == 'sim':
    participacao += 1
    
resposta = input("Mora perto da vítima? ")
if resposta == 'sim':
    participacao += 1
    
resposta = input("Devia para a vítima? ")
if resposta == 'sim':
    participacao += 1
    
resposta = input("Já trabalhou com a vítima? ")
if resposta == 'sim':
    participacao += 1
    
#--------------CLASSIFICANDO O INDIVIDUO

if participacao == 2:
    classificado = 'Suspeito'
    
elif participacao == 3 or participacao == 4:
    classificado = 'Cumplice'
      
elif participacao == 5:
    classificado = 'Assassino'
    
else:
    classificado = 'Inocente'

#----------IMPRIMINDO RESULTADO
    
print("A pessoa respondeu {} perguntas positivamente, portando sera classificado como {}".format(participacao, classificado))
