
def foo(a):
	if a.isdigit():
		print(a)

data1 = "5,10,15"
for item in data1:
	foo(item)

print("----")

data2 = data1.split(',')

for item in data2:
	foo(item)

c = 0

for z in range(2):
	for x in ['a', 'b']:
		for y in ['p', 'q']:
			print(z, x, y, c)
			c += 1
print (c)
