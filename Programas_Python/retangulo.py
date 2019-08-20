"""
"""

linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))

print("+"+"-"*linhas+"+")

for i in range(colunas):
	print("|"+" "*linhas+"|")

print("+"+"-"*linhas+"+")