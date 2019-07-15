# -*- coding: utf-8 -*-
"""
Uma forma de avaliar se uma pessoa está acima do peso é através do calculo do índice IMC.
 Se o valor do IMC estiver acima de 25, significa que a pessoa está acima do peso.
 A fórmula é: IMC = Peso(Kg) / (Altura(m)*Altura(m)). Com base na altura e peso fornecido
 no console exiba uma mensagem determinando se uma pessoa está acima do peso.


@author: Júlio César Ribeiro de Moraes
"""

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = (peso /(altura*altura))

if imc > 25:
    print("Seu IMC é de: {:.2f}, voce esta acima do peso.".format(imc))
    
else:
    print("Seu IMC é de {:.2f}, voce nao esta com sobrepeso.".format(imc))

