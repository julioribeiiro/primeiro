# -*- coding: utf-8 -*-
"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa primeiramente deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;


@author: Júlio César Ribeiro de Moraes
"""

#--------COLETANDO OS DADOS----------
lados_str = input("Digite os lados do triangulo no formato x, y, z: ")

a,b,c = lados_str.split(",")

a = int(a)
b = int(b)
c = int(c)

#--------VERIFICANDO SE É UM TRIANGULO
if a+b > c and a+c > b and b+c > a:
    print("Esses valores formam um triangulo")
    
    if a == b == c:
        print("Triangulo Equilatero")
    elif a == b or a == c or b == c:
        print("Triangulo Isoceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Nao eh possivel formar um triangulo com esses valores")

