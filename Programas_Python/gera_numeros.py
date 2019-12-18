from random import *

string = ""
array = list()
array.append(0);

numero = 0

#1000 5000 10000 20000 40000

for i in range (1000000):
	numero = 0
	print(str(i)+"/1000000")
	while numero in array:
		numero = randrange(10000000)
	array.append(numero)
	string += str(numero)+","

print(string)
print("\n\n"+str(len(array)))