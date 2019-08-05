
d = {1: 2, 3: 4, 4: 2}

def inva(dic):
	inverso = {}
	for i in dic:
		inverso[dic[i]] = []
	for i in dic:
		inverso[dic[i]].append(i)

	print(inverso)

inva(d)
