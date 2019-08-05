seq_1 = [1,1,0]
seq_2 = [1,1,0,1,0,1,0,0,1,1,0,1,0]


contador = 0
vezes = 0


for i in range(len(seq_2) - len(seq_1)):
	if seq_2[i] == seq_1[0]:
		for n in range(1, len(seq_1)):
			if seq_2[i + n] == seq_1[n]:
				contador += 1
			else:
				contador = 0
		if contador == len(seq_1) - 1:
			vezes += 1
		contador = 0
print(vezes)
