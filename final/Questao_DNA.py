'''
questao DNA
'''

dna = input('digite uma sequencia de DNA: ').upper()

dna = list(dna)

A = 0
C = 0 
G = 0
T = 0

for i in dna:
	if i == 'A':
		A += 1

	elif i == 'C':
		C += 1

	elif i == 'G':
		G += 1

	elif i == 'T':
		T += 1

total = A + C + G + T

A = A / total * 100
C = C / total * 100
G = G / total * 100
T = T / total * 100

print("A: {:.2f}%\nC: {:.2f}%\nG: {:.2f}%\nT: {:.2f}%".format(A, C, G, T))
