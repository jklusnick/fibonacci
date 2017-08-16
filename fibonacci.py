a = 0
b = 1
c = a + b
for i in range(0, 20):
	print(c)
	a = b
	b = c
	c = a + b