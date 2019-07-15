arq = open("atp_matches_2017.csv", "r")


total = []
clay = []
hard = []
grass = []


for i in arq:
	total.append(i.split(','))


for i in total:
	if i[2] == "Clay":
		clay.append(i)
	elif i[2] == "Hard":
		hard.append(i)
	elif i[2] == "Grass":
		grass.append(i)

vencedor_clay = ""
numero_clay = 0
numero_hard = 0
vencedor_hard = ""
numero_grass = 0
vencedor_grass = ""
contador = 0

for i in clay:
	for j in clay:
		if j[10] == i[10]:
			contador += 1
	if contador > numero_clay:
		numero_clay = contador
		vencedor_clay = i[10]
	contador = 0


contador = 0


for i in hard:
	for j in hard:
		if j[10] == i[10]:
			contador += 1
	if contador > numero_hard:
		numero_hard = contador
		vencedor_hard = i[10]
	contador = 0


contador = 0

for i in grass:
	for j in grass:
		if j[10] == i[10]:
			contador += 1
	if contador > numero_grass:
		numero_grass = contador
		vencedor_grass = i[10]
	contador = 0




print("Cimento: {} com um total de {} vitorias!".format(vencedor_hard, numero_hard))
print("Grama: {} com um total de {} vitorias!".format(vencedor_grass, numero_grass))
print("Saibro: {} com um total de {} vitorias!".format(vencedor_clay, numero_clay))
