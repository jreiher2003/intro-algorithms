def naive(a,b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
        print x,z
    return z

def time(a):
	return (2 * a) + 3

print time(5)

print naive(63,12)