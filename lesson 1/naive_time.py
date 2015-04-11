def naive(a,b):
	x = a
	y = b
	z = 0
	while x > 0:
		z = z + y
		x = x - 1
	return z

def time(a):
	return 2 * a + 3

print time(5)